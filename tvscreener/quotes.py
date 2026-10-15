"""Real-time quotes pushed by TradingView's data websocket."""
import time
from datetime import datetime, timezone

from tvscreener._websocket import Connection, session_id

# Readable name -> TradingView quote field
QUOTE_FIELDS = {
    "price": "lp",
    "change": "ch",
    "change_percent": "chp",
    "volume": "volume",
    "bid": "bid",
    "ask": "ask",
    "bid_size": "bid_size",
    "ask_size": "ask_size",
    "open": "open_price",
    "high": "high_price",
    "low": "low_price",
    "prev_close": "prev_close_price",
    "time": "lp_time",
    "extended_price": "rtc",
    "extended_change": "rch",
    "extended_change_percent": "rchp",
    "extended_time": "rtc_time",
    "session": "current_session",
    "update_mode": "update_mode",
    "description": "description",
    "currency": "currency_code",
    "exchange": "exchange",
    "type": "type",
}
DEFAULT_QUOTE_FIELDS = ["price", "change", "change_percent", "volume", "bid", "ask", "time", "extended_price",
                        "extended_change_percent", "session", "update_mode"]
_TIME_FIELDS = {"lp_time", "rtc_time"}
_NAMES = {api: name for name, api in QUOTE_FIELDS.items()}


def stream_quotes(symbols, fields=None, on_update=None, max_updates=None, duration=None):
    """
    Stream real-time quotes: TradingView pushes each change, no polling.

    Logged out, most US stocks and crypto are real time; some exchanges are delayed
    (``update_mode`` is then e.g. "delayed_streaming_900", 15 minutes).

    :param symbols: Exchange-prefixed symbol or list of them, e.g. ["NASDAQ:AAPL", "BINANCE:BTCUSDT"]
    :param fields: Fields to receive; readable names from ``QUOTE_FIELDS`` ("price", "bid", "volume"...)
        or raw TradingView quote fields. Default ``DEFAULT_QUOTE_FIELDS``.
    :param on_update: Optional callback called with each update
    :param max_updates: Stop after this many updates (None = no limit)
    :param duration: Stop after this many seconds (None = no limit)
    :yield: Dict with "symbol", "updated" (names of the fields that changed) and the latest value of
        every field received so far. Times are UTC datetimes.
        Unknown symbols yield one update with "error" set.

    Example:
        >>> for quote in stream_quotes(["NASDAQ:AAPL", "NASDAQ:MSFT"], duration=60):
        ...     print(quote["symbol"], quote["price"], quote["updated"])
    """
    symbols = [symbols] if isinstance(symbols, str) else list(symbols)
    names = fields or DEFAULT_QUOTE_FIELDS
    api_fields = [QUOTE_FIELDS.get(name, name) for name in names]
    state = {s: {"symbol": s} for s in symbols}
    deadline = time.monotonic() + duration if duration is not None else None
    count = 0

    with Connection() as conn:
        qs = session_id("qs_")
        conn.send("quote_create_session", qs)
        conn.send("quote_set_fields", qs, *api_fields)
        conn.send("quote_add_symbols", qs, *symbols)
        for message in conn.messages(deadline):
            if message["m"] != "qsd":
                continue
            data = message["p"][1]
            quote = state.setdefault(data.get("n"), {"symbol": data.get("n")})
            if data.get("s") == "error":
                quote["error"] = data.get("errmsg") or "unknown symbol"
                updated = []
            else:
                changes = {k: v for k, v in (data.get("v") or {}).items() if k in api_fields}
                if not changes:
                    continue
                for key, value in changes.items():
                    if key in _TIME_FIELDS and value is not None:
                        value = datetime.fromtimestamp(value, tz=timezone.utc)
                    quote[_NAMES.get(key, key)] = value
                updated = [_NAMES.get(k, k) for k in changes]
            update = {**quote, "updated": updated}
            if on_update:
                on_update(update)
            yield update
            count += 1
            if max_updates is not None and count >= max_updates:
                return
