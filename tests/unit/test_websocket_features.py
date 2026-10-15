import base64
import json
import zlib
from unittest.mock import patch

import pandas as pd
import pytest
from websocket import WebSocketTimeoutException

from tvscreener import get_financials, get_corporate_events, get_seasonals, stream_quotes, TradingViewWebSocketError
from tvscreener import _websocket
from tvscreener._websocket import _parse, get_quote_fields, run_studies, NA


def frame(payload):
    text = payload if isinstance(payload, str) else json.dumps(payload)
    return f"~m~{len(text)}~m~{text}"


class FakeSocket:
    """Returns the scripted raw messages, then times out."""

    def __init__(self, messages):
        self.messages = list(messages)
        self.sent = []

    def recv(self):
        if not self.messages:
            raise WebSocketTimeoutException()
        return self.messages.pop(0)

    def send(self, raw):
        self.sent.append(raw)

    def settimeout(self, _):
        pass

    def close(self):
        pass

    def methods(self):
        return [json.loads(p)["m"] for raw in self.sent for p in _parse(raw) if not p.startswith("~h~")]


def fake(messages):
    sock = FakeSocket(messages)
    return sock, patch.object(_websocket, "create_connection", return_value=sock)


def qsd(symbol, values, status="ok"):
    return frame({"m": "qsd", "p": ["qs", {"n": symbol, "s": status, "v": values}]})


class TestProtocol:

    def test_parse_frames_with_brackets_in_payload(self):
        raw = frame('{"m":"a","p":["~m~"]}') + frame("~h~3")
        assert _parse(raw) == ['{"m":"a","p":["~m~"]}', "~h~3"]

    def test_heartbeat_is_echoed(self):
        sock, p = fake([frame("~h~7") + qsd("X:A", {"lp": 1}), frame({"m": "quote_completed", "p": ["qs", "X:A"]})])
        with p:
            assert get_quote_fields(["X:A"], ["lp"]) == {"X:A": {"lp": 1}}
        assert frame("~h~7") in sock.sent
        assert sock.methods()[:4] == ["set_auth_token", "quote_create_session", "quote_set_fields", "quote_add_symbols"]

    def test_unknown_symbol_is_none(self):
        sock, p = fake([qsd("X:ZZ", {}, status="error")])
        with p:
            assert get_quote_fields(["X:ZZ"], ["lp"]) == {"X:ZZ": None}

    def test_study_rows_deduplicated(self):
        rows = lambda *bars: {"st": [{"i": i, "v": [i, v]} for i, v in bars]}
        sock, p = fake([
            frame({"m": "series_completed", "p": ["cs", "sds_1"]}),
            frame({"m": "du", "p": ["cs", {"st0": rows((1, 10), (2, 20))}]}),
            frame({"m": "du", "p": ["cs", {"st0": rows((2, 21))}]}),
            frame({"m": "study_completed", "p": ["cs", "st0", "s1_st0"]}),
        ])
        with p:
            result = run_studies("X:A", {"k": ("Dividends@tv-basicstudies-279", {})})
        assert result["k"]["rows"] == [[1, 10], [2, 21]]
        assert "create_study" in sock.methods()

    def test_symbol_error_raises(self):
        sock, p = fake([frame({"m": "symbol_error", "p": ["cs", "sym_1", "invalid symbol"]})])
        with p, pytest.raises(TradingViewWebSocketError):
            run_studies("X:ZZ", {"k": ("Splits@tv-basicstudies-279", {})})


CONFIG = pd.DataFrame([
    # industrial layout: revenue > cost of goods > depreciation, then net income
    {"id": "total_revenue_fy", "name": "Total revenue", "category": "Income statements", "period": "FY",
     "view_mode": "industrial", "parent": None, "ordinal": 0, "type": "currency", "hidden": False},
    {"id": "depreciation_fy", "name": "Depreciation", "category": "Income statements", "period": "FY",
     "view_mode": "industrial", "parent": "cost_of_goods_fy", "ordinal": 0, "type": "currency", "hidden": False},
    {"id": "cost_of_goods_fy", "name": "Cost of goods sold", "category": "Income statements", "period": "FY",
     "view_mode": "industrial", "parent": None, "ordinal": 1, "type": "currency", "hidden": False},
    {"id": "net_income_fy", "name": "Net income", "category": "Income statements", "period": "FY",
     "view_mode": "industrial", "parent": None, "ordinal": 2, "type": "currency", "hidden": False},
    {"id": "secret_fy", "name": "Hidden", "category": "Income statements", "period": "FY",
     "view_mode": "industrial", "parent": None, "ordinal": 3, "type": "currency", "hidden": True},
    # banking layout shares net income but its own items are empty for this company
    {"id": "net_income_fy", "name": "Net income", "category": "Income statements", "period": "FY",
     "view_mode": "banking", "parent": None, "ordinal": 0, "type": "currency", "hidden": False},
    {"id": "interest_income_fy", "name": "Interest income", "category": "Income statements", "period": "FY",
     "view_mode": "banking", "parent": None, "ordinal": 1, "type": "currency", "hidden": False},
])


class TestFinancials:

    @patch("tvscreener.fundamentals.get_fundamentals_config", return_value=CONFIG)
    @patch("tvscreener.fundamentals.get_quote_fields")
    def test_layout_order_and_periods(self, mock_quotes, _):
        mock_quotes.return_value = {"X:A": {
            "fiscal_period_fy_h": [2025, 2024], "fiscal_period_end_fy_h": [1759190400, 1727654400],
            "fundamental_currency_code": "USD",
            "total_revenue_fy_h": [400, 300], "cost_of_goods_fy_h": [-200, -150], "depreciation_fy_h": [-10, NA],
            "net_income_fy_h": [100, 90], "interest_income_fy_h": None,
        }}
        df = get_financials("X:A")
        requested = mock_quotes.call_args.args[1]
        assert "secret_fy_h" not in requested
        assert df.index.tolist() == ["2024", "2025"]
        assert df.columns.tolist() == ["period_end", "Total revenue", "Cost of goods sold", "Depreciation", "Net income"]
        assert df.loc["2025", "Total revenue"] == 400
        assert pd.isna(df.loc["2024", "Depreciation"])
        assert df.attrs["currency"] == "USD"
        assert df["period_end"].iloc[-1] == pd.Timestamp("2025-09-30", tz="UTC")

    @patch("tvscreener.fundamentals.get_fundamentals_config", return_value=CONFIG)
    @patch("tvscreener.fundamentals.get_quote_fields")
    def test_field_ids(self, mock_quotes, _):
        mock_quotes.return_value = {"X:A": {"fiscal_period_fy_h": [2025], "total_revenue_fy_h": [1]}}
        assert get_financials("X:A", labels=False).columns.tolist() == ["period_end", "total_revenue"]

    @patch("tvscreener.fundamentals.get_fundamentals_config", return_value=CONFIG)
    @patch("tvscreener.fundamentals.get_quote_fields", return_value={"X:ZZ": None})
    def test_unknown_symbol(self, *_):
        with pytest.raises(ValueError):
            get_financials("X:ZZ")

    @pytest.mark.parametrize("kwargs", [{"statement": "pnl"}, {"period": "monthly"}])
    def test_invalid_arguments(self, kwargs):
        with pytest.raises(ValueError):
            get_financials("X:A", **kwargs)


class TestCorporateEvents:

    @patch("tvscreener.fundamentals.run_studies")
    def test_decoding(self, mock_studies):
        mock_studies.return_value = {
            "dividends": {"rows": [[1786368600, 0.27, 1786320000000, NA, 1786579200000]], "graphics": None},
            "earnings": {"rows": [[1785369600, 2.0244, 1.89, 1782777600, 1785369600000, 2.02, 109038.9, 109417.0, 22],
                                  [1793577600, NA, 1.98, 1790726400, 1793577600000, NA, 113380.0, NA, 12]],
                         "graphics": None},
            "splits": {"rows": [[1718026200, 1.0, 10.0, 1717977600000]], "graphics": None},
        }
        events = get_corporate_events("X:A")
        div = events["dividends"].iloc[0]
        assert div["amount"] == 0.27 and pd.isna(div["net_amount"])
        assert div["ex_date"] == pd.Timestamp("2026-08-10", tz="UTC")
        earnings = events["earnings"]
        assert earnings["reported"].tolist() == [True, False]
        assert earnings["eps_reported"].iloc[0] == 2.02 and earnings["eps_diluted"].iloc[0] == 2.0244
        assert earnings["revenue_actual"].iloc[0] == 109417.0 * 1e6
        assert events["splits"]["ratio"].iloc[0] == 10.0

    def test_unknown_kind(self):
        with pytest.raises(ValueError):
            get_corporate_events("X:A", kinds=["buybacks"])


class TestSeasonals:

    @patch("tvscreener.fundamentals.run_studies")
    def test_compressed_payload(self, mock_studies):
        data = {"performance": {"2025": {"months": [[1.0, 10.0]] * 12}, "2026": {"months": [[2.0, 20.0]] * 3}}}
        packed = base64.b64encode(zlib.compress(json.dumps(data).encode())).decode().rstrip("=")
        mock_studies.return_value = {"seasonals": {"rows": [], "graphics": json.dumps({"dataCompressed": packed})}}
        df = get_seasonals("X:A", 2025, 2026)
        config = json.loads(mock_studies.call_args.args[1]["seasonals"][1]["config"])
        assert config == {"ticker": "X:A", "years": {"start": 2025, "end": 2026}}
        assert df.index.tolist() == [2025, 2026]
        assert df.loc[2026, "Mar"] == 20.0 and pd.isna(df.loc[2026, "Apr"])
        assert get_seasonals("X:A", 2025, 2026, absolute=True).loc[2025, "Jan"] == 1.0

    @patch("tvscreener.fundamentals.run_studies")
    def test_plain_payload(self, mock_studies):
        data = {"data": {"performance": {"2024": {"months": [[1.0, 5.0]]}}}}
        mock_studies.return_value = {"seasonals": {"rows": [], "graphics": json.dumps(data)}}
        assert get_seasonals("X:A", 2024, 2024).loc[2024, "Jan"] == 5.0


class TestStreamQuotes:

    def test_merged_updates(self):
        sock, p = fake([
            qsd("X:A", {"lp": 10.0, "lp_time": 1792051559, "pro_name": "X:A"}),
            qsd("X:ZZ", {}, status="error"),
            qsd("X:A", {"bid": 9.9}),
            qsd("X:A", {"lp": 10.5}),
        ])
        seen = []
        with p:
            updates = list(stream_quotes(["X:A", "X:ZZ"], fields=["price", "time", "bid"], on_update=seen.append,
                                         max_updates=3))
        assert sock.methods()[2:4] == ["quote_set_fields", "quote_add_symbols"]
        assert updates[0]["price"] == 10.0 and updates[0]["time"].year == 2026
        assert "pro_name" not in updates[0]
        assert updates[1]["error"]
        assert updates[2] == {"symbol": "X:A", "price": 10.0, "time": updates[0]["time"], "bid": 9.9,
                              "updated": ["bid"]}
        assert len(seen) == 3

    def test_stops_after_duration(self):
        sock, p = fake([qsd("X:A", {"lp": 1.0})])
        with p:
            assert len(list(stream_quotes("X:A", duration=0.3))) == 1
