import json
from unittest.mock import patch, MagicMock

import pandas as pd
import pytest
import requests

from tvscreener import get_economic_calendar, get_forward_curve, get_yield_matrix, search_symbols, get_peers, \
    get_volatility_smile, get_documents, get_document, get_earnings_calls, get_news, get_article
from tvscreener.calendars import ECONOMIC_CALENDAR_LIMIT
from tvscreener.news import _ast_to_text


def _response(payload):
    return MagicMock(json=MagicMock(return_value=payload))


def _event(i, importance=0):
    return {"id": str(i), "date": "2026-10-13T12:30:00.000Z", "country": "US", "title": f"E{i}",
            "importance": importance, "actual": 1.0, "referenceDate": None}


class TestEconomicCalendar:

    @patch('tvscreener.calendars.requests.get')
    def test_params_and_columns(self, mock_get):
        mock_get.return_value = _response({"status": "ok", "result": [_event(1, 1), _event(2, -1)]})
        df = get_economic_calendar("2026-10-13", "2026-10-14", countries=["us", "EU"], importance="medium")
        params = mock_get.call_args.kwargs["params"]
        assert params["countries"] == "US,EU"
        assert params["minImportance"] == 0
        assert params["from"] == "2026-10-13T00:00:00.000Z"
        assert params["to"].startswith("2026-10-14T23:59:59")
        assert df["importance"].tolist() == ["high", "low"]
        assert str(df["date"].dt.tz) == "UTC"

    @patch('tvscreener.calendars.requests.get')
    def test_splits_range_at_server_limit(self, mock_get):
        full = [_event(i) for i in range(ECONOMIC_CALENDAR_LIMIT)]
        mock_get.side_effect = [_response({"result": full}), _response({"result": full[:10]}),
                                _response({"result": full[5:20]})]
        df = get_economic_calendar("2026-01-01", "2026-01-31")
        assert mock_get.call_count == 3
        assert len(df) == 20  # duplicates across halves removed

    def test_rejects_unknown_importance(self):
        with pytest.raises(ValueError):
            get_economic_calendar(importance="critical")


class TestForwardCurve:

    @patch('tvscreener.core.futures.requests.post')
    def test_continuous_symbol_becomes_root(self, mock_post):
        mock_post.return_value = _response({"data": [
            {"s": "NYMEX:CLX2026", "d": ["CLX2026", "Crude Oil", 20261020, 93.9, -1.2, 100, 5000, "USD"]}]})
        df = get_forward_curve("nymex:cl1!")
        payload = json.loads(mock_post.call_args.kwargs["data"])
        assert payload["index_filters"] == [{"name": "root", "values": ["NYMEX:CL"]}]
        assert df["expiration"].iloc[0] == pd.Timestamp("2026-10-20")
        assert df["open_interest"].iloc[0] == 5000

    def test_requires_exchange(self):
        with pytest.raises(ValueError):
            get_forward_curve("CL")


class TestYieldMatrix:

    @patch('tvscreener.core.government_bond.requests.post')
    def test_pivot_sorted_by_tenor(self, mock_post):
        mock_post.return_value = _response({"data": [
            {"s": "TVC:US10Y", "d": ["US", 5.1, "P10Y"]}, {"s": "TVC:US03MY", "d": ["US", 4.2, "P3M"]},
            {"s": "TVC:DE02Y", "d": ["DE", 3.0, "P2Y"]}, {"s": "TVC:XX", "d": ["DE", 1.0, None]}]})
        df = get_yield_matrix(["us", "de"])
        payload = json.loads(mock_post.call_args.kwargs["data"])
        assert {"left": "country_code", "operation": "in_range", "right": ["US", "DE"]} in payload["filter"]
        assert df.columns.tolist() == ["3M", "2Y", "10Y"]
        assert df.loc["US", "10Y"] == 5.1
        assert pd.isna(df.loc["DE", "10Y"])

    @patch('tvscreener.core.government_bond.requests.post')
    def test_tenor_selection(self, mock_post):
        mock_post.return_value = _response({"data": [{"s": "TVC:US10Y", "d": ["US", 5.1, "P10Y"]}]})
        assert get_yield_matrix(tenors=["10y", "03M"]).columns.tolist() == ["3M", "10Y"]


class TestSymbolSearch:

    @patch('tvscreener.scanner.requests.get')
    def test_tickers_and_paging(self, mock_get):
        page1 = [{"symbol": "AAPL", "exchange": "NASDAQ", "type": "stock"}] * 49 + [
            {"symbol": "BTCUSD", "exchange": "Bitstamp", "prefix": "BITSTAMP", "type": "spot"}]
        page2 = [{"symbol": "ES", "exchange": "CME", "source_id": "CME_MINI", "type": "futures"}]
        mock_get.side_effect = [_response({"symbols": page1, "symbols_remaining": 1}),
                                _response({"symbols": page2, "symbols_remaining": 0})]
        df = search_symbols("x", type="stock", country="de", limit=100)
        assert mock_get.call_args_list[1].kwargs["params"]["start"] == 50
        assert mock_get.call_args.kwargs["params"]["country"] == "DE"
        assert df["symbol"].tolist()[-2:] == ["BITSTAMP:BTCUSD", "CME_MINI:ES"]
        assert df["symbol"].iloc[0] == "NASDAQ:AAPL"

    @patch('tvscreener.scanner.requests.get')
    def test_limit(self, mock_get):
        mock_get.return_value = _response({"symbols": [{"symbol": "A", "exchange": "X"}] * 50, "symbols_remaining": 9})
        assert len(search_symbols("a", limit=3)) == 3
        assert mock_get.call_count == 1


class TestPeers:

    @patch('tvscreener.scanner.requests.post')
    @patch('tvscreener.scanner.requests.get')
    def test_same_industry_excluding_self(self, mock_get, mock_post):
        mock_get.return_value = _response({"industry": "Telecommunications Equipment", "market": "america"})
        row = lambda s: {"s": s, "d": [s, "", "Telecommunications Equipment", "Electronic Technology", 1e9, 1, 0, "USD"]}
        mock_post.return_value = _response({"data": [row("NASDAQ:AAPL"), row("NASDAQ:CSCO"), row("NYSE:MSI")]})
        df = get_peers("NASDAQ:AAPL", n=2)
        payload = json.loads(mock_post.call_args.kwargs["data"])
        assert mock_post.call_args.args[0].endswith("/america/scan")
        assert payload["filter"][0] == {"left": "industry", "operation": "equal", "right": "Telecommunications Equipment"}
        assert df["symbol"].tolist() == ["NASDAQ:CSCO", "NYSE:MSI"]
        assert "market_cap" in df.columns

    @patch('tvscreener.scanner.requests.get')
    def test_unknown_symbol(self, mock_get):
        mock_get.return_value = _response(None)
        with pytest.raises(ValueError):
            get_peers("NASDAQ:ZZZZ")

    def test_invalid_by(self):
        with pytest.raises(ValueError):
            get_peers("NASDAQ:AAPL", by="country")


class TestVolatilitySmile:

    @patch('tvscreener.volatility.requests.get')
    def test_series_url(self, mock_get):
        mock_get.return_value = _response({"x-axis": {"x": [100, 110]}, "plots": [{"plot": {"y": [0.3, 0.25]}}]})
        df = get_volatility_smile("NASDAQ:AAPL", "2026-11-13")
        assert mock_get.call_args.args[0].endswith("/volatility-chart/NASDAQ:AAPL;AAPL;20261113")
        assert mock_get.call_args.kwargs["params"] == {"xaxis": "strikes"}
        assert df.columns.tolist() == ["strike", "iv"]
        get_volatility_smile("SP:SPX", 20261113, root="SPXW", x="moneyness")
        assert mock_get.call_args.args[0].endswith("SP:SPX;SPXW;20261113")
        assert mock_get.call_args.kwargs["params"] == {"xaxis": "moneyness"}

    def test_invalid_axis(self):
        with pytest.raises(ValueError):
            get_volatility_smile("NASDAQ:AAPL", "2026-11-13", x="delta")


class TestDocuments:

    @patch('tvscreener.documents.requests.get')
    def test_documents(self, mock_get):
        mock_get.return_value = _response({"items": [
            {"id": "a", "reported": 1785445200, "title": "Q3 2026", "category": {"id": "quarterly_report"},
             "event": "earning", "fiscal_year": 2026, "fiscal_period": "Q3", "form": {"title": "10-Q"},
             "views": [{"id": "pdf1", "type": "pdf"}], "provider": {"name": "Quartr"}},
            {"id": "b", "reported": 1785445300, "title": "Q3 2026", "category": {"id": "call_transcript"},
             "views": [{"id": "t1", "type": "transcript"}, {"id": "s1", "type": "summary"}]}]})
        df = get_documents("NASDAQ:AAPL", category="call_transcript", start="2026-01-01")
        params = mock_get.call_args.kwargs["params"]
        filters = [v for k, v in params if k == "filter"]
        assert filters == sorted(filters)
        assert ("start_date", "2026-01-01T00:00:00.000Z") in params
        assert df["id"].tolist() == ["b"]
        assert df[["transcript_id", "summary_id"]].iloc[0].tolist() == ["t1", "s1"]

    def test_unknown_category(self):
        with pytest.raises(ValueError):
            get_documents("NASDAQ:AAPL", category="10-K")

    @patch('tvscreener.documents.requests.get')
    def test_document_text(self, mock_get):
        mock_get.return_value = _response({"astDescription": {"type": "root", "children": [
            {"type": "p", "children": [{"type": "b", "children": ["CEO"]}, ": Hello."]},
            {"type": "p", "children": ["Bye."]}]}})
        assert get_document("urn:t") == "CEO: Hello.\n\nBye."

    @patch('tvscreener.documents.requests.get')
    def test_earnings_calls_windows(self, mock_get):
        call = {"event": {"id": 1, "date": "2025-01-30T22:00:00.000Z", "title": "Q1 2025", "fiscalYear": 2025,
                          "fiscalPeriod": "Q1", "state": "completed"},
                "liveTranscript": {"transcript": "https://t"}, "audio": {"fileUrl": "https://a",
                                                                         "audioMetadata": {"duration": 3000.0}}}
        mock_get.return_value = _response({"items": [call]})
        df = get_earnings_calls("NASDAQ:AAPL", start="2025-01-01", end="2026-12-31")
        assert mock_get.call_count == 2  # 365-day windows
        for c in mock_get.call_args_list:
            params = dict(c.kwargs["params"][2:])
            assert (pd.Timestamp(params["end_date"]) - pd.Timestamp(params["start_date"])).days < 365
        assert len(df) == 1  # same event in every window
        assert df[["transcript_url", "audio_url", "audio_duration"]].iloc[0].tolist() == ["https://t", "https://a", 3000.0]


class TestNews:

    @patch('tvscreener.news.requests.get')
    def test_filters_sorted(self, mock_get):
        mock_get.return_value = _response({"items": [{"id": "x:1:0", "title": "t", "published": 1792049277,
                                                      "provider": {"name": "Reuters"}, "storyPath": "/news/x"}]})
        df = get_news("NASDAQ:AAPL", provider="reuters", corp_activity="insider_trading", country="us")
        assert mock_get.call_args.kwargs["params"]["filter"] == [
            "corp_activity:insider_trading", "lang:en", "market_country:US", "provider:reuters", "symbol:NASDAQ:AAPL"]
        assert df["id"].tolist() == ["x:1:0"]

    @patch('tvscreener.news.requests.get')
    def test_article_by_id_uses_api(self, mock_get):
        mock_get.return_value = _response({"ast_description": {"type": "root", "children": [
            {"type": "p", "children": ["Apple ", {"type": "symbol", "params": {"symbol": "NASDAQ:AAPL",
                                                                               "text": "NASDAQ:AAPL"}}, " rose."]},
            {"type": "list", "children": [{"type": "*", "children": ["one"]}, {"type": "*", "children": ["two"]}]}]}})
        text = get_article("DJN_1:0")
        assert mock_get.call_args.kwargs["params"]["id"] == "DJN_1:0"
        assert text == "Apple NASDAQ:AAPL rose.\n\none\n\ntwo"

    @patch('tvscreener.news.requests.get')
    def test_article_by_path_uses_page(self, mock_get):
        mock_get.return_value = MagicMock(text='<div class="body-x">\n<p>A</p><p>B</p></div>')
        assert get_article("/news/x:1:0-slug/") == "A\n\nB"
        assert mock_get.call_args.args[0] == "https://www.tradingview.com/news/x:1:0-slug/"

    def test_ast_links(self):
        node = {"type": "p", "children": ["See ", {"type": "url", "params": {"url": "https://u", "linkText": "here"}}]}
        assert _ast_to_text(node) == "See here"
