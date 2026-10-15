"""Minimal client for TradingView's data websocket (the protocol behind the website's charts and quotes).

Private module: it backs get_financials(), stream_quotes(), get_corporate_events() and get_seasonals().
"""
import json
import random
import re
import string
import time

from websocket import create_connection, WebSocketTimeoutException

WEBSOCKET_URL = "wss://data.tradingview.com/socket.io/websocket"
ORIGIN = "https://www.tradingview.com"
CONNECT_TIMEOUT = 15
# Frames are "~m~<length>~m~<payload>"; heartbeats are "~h~<n>" payloads that must be echoed back
_FRAME = re.compile(r"~m~(\d+)~m~")
# Studies return this value for "no data"
NA = 1e100


class TradingViewWebSocketError(Exception):
    """The websocket returned an error for a symbol, series or study."""


def session_id(prefix):
    return prefix + "".join(random.choices(string.ascii_lowercase, k=12))


def _parse(raw):
    """Split a raw websocket message into its payloads."""
    payloads, pos = [], 0
    while True:
        match = _FRAME.match(raw, pos)
        if not match:
            return payloads
        start = match.end()
        end = start + int(match.group(1))
        payloads.append(raw[start:end])
        pos = end


class Connection:
    """One websocket connection, used as a context manager."""

    def __init__(self, timeout=CONNECT_TIMEOUT):
        self.timeout = timeout
        self._ws = None

    def __enter__(self):
        self._ws = create_connection(WEBSOCKET_URL, header=[f"Origin: {ORIGIN}"], timeout=self.timeout)
        self.send("set_auth_token", "unauthorized_user_token")
        return self

    def __exit__(self, *exc):
        self.close()

    def close(self):
        if self._ws is not None:
            try:
                self._ws.close()
            finally:
                self._ws = None

    def send(self, method, *params):
        payload = json.dumps({"m": method, "p": list(params)}, separators=(",", ":"))
        self._ws.send(f"~m~{len(payload)}~m~{payload}")

    def messages(self, deadline=None):
        """
        Yield decoded messages ({"m": method, "p": params}) until ``deadline`` (time.monotonic()).
        Heartbeats are answered here.
        """
        while deadline is None or time.monotonic() < deadline:
            if deadline is not None:
                self._ws.settimeout(max(0.1, min(self.timeout, deadline - time.monotonic())))
            try:
                raw = self._ws.recv()
            except WebSocketTimeoutException:
                continue
            for payload in _parse(raw):
                if payload.startswith("~h~"):
                    self._ws.send(f"~m~{len(payload)}~m~{payload}")
                    continue
                try:
                    message = json.loads(payload)
                except json.JSONDecodeError:
                    continue
                if "m" in message:
                    yield message


def get_quote_fields(symbols, fields, timeout=30):
    """
    One snapshot of quote fields for several symbols.

    :return: Dict of symbol to {field: value} with the fields the server sent, or None for unknown symbols
    """
    values = {s: {} for s in symbols}
    pending = set(symbols)
    with Connection() as conn:
        qs = session_id("qs_")
        conn.send("quote_create_session", qs)
        conn.send("quote_set_fields", qs, *fields)
        conn.send("quote_add_symbols", qs, *symbols)
        for message in conn.messages(time.monotonic() + timeout):
            if message["m"] == "qsd":
                data = message["p"][1]
                if data.get("s") == "error":
                    values[data.get("n")] = None
                    pending.discard(data.get("n"))
                elif values.get(data.get("n"), {}) is not None:
                    values.setdefault(data.get("n"), {}).update(data.get("v") or {})
            elif message["m"] == "quote_completed":
                pending.discard(message["p"][1])
            if not pending:
                break
    return values


def run_studies(symbol, studies, bars=300, timeframe="D", timeout=60):
    """
    Run built-in studies on a symbol's chart.

    :param studies: Dict of key to (study id, inputs), e.g. {"dividends": ("Dividends@tv-basicstudies-279", {...})}
    :return: Dict of key to {"rows": [[time, plot values...]], "graphics": raw non-series output or None}
    :raises TradingViewWebSocketError: If the symbol cannot be resolved or a study fails
    """
    results = {key: {"rows": {}, "graphics": None} for key in studies}
    ids = {f"st{i}": key for i, key in enumerate(studies)}
    pending = set(ids)
    with Connection() as conn:
        cs = session_id("cs_")
        conn.send("chart_create_session", cs, "")
        conn.send("resolve_symbol", cs, "sym_1", "=" + json.dumps({"adjustment": "splits", "symbol": symbol}))
        conn.send("create_series", cs, "sds_1", "s1", "sym_1", timeframe, bars, "")
        started = False
        for message in conn.messages(time.monotonic() + timeout):
            method, params = message["m"], message["p"]
            if method in ("symbol_error", "series_error", "critical_error", "protocol_error"):
                raise TradingViewWebSocketError(f"{symbol}: {method} {params[1:]}")
            if method == "series_completed" and not started:
                started = True
                for sid, key in ids.items():
                    study_id, inputs = studies[key]
                    conn.send("create_study", cs, sid, "st1", "sds_1", study_id, inputs)
            elif method in ("du", "timescale_update"):
                for sid, data in params[1].items():
                    if sid in ids and isinstance(data, dict):
                        result = results[ids[sid]]
                        # Updates resend the last bars: keep one row per bar index
                        result["rows"].update((row["i"], row["v"]) for row in data.get("st", []))
                        graphics = (data.get("ns") or {}).get("d")
                        if graphics:
                            result["graphics"] = graphics
            elif method == "study_error":
                raise TradingViewWebSocketError(f"{symbol}: {ids.get(params[1], params[1])} failed: {params[3:]}")
            elif method == "study_completed":
                pending.discard(params[1])
                if not pending:
                    break
    if pending:
        raise TradingViewWebSocketError(f"{symbol}: no answer within {timeout}s")
    for result in results.values():
        result["rows"] = [result["rows"][i] for i in sorted(result["rows"])]
    return results
