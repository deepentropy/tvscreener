import datetime as dt
from unittest.mock import patch, MagicMock

import pandas as pd
import pytest

from tvscreener import StockScreener, StockField, Preset, Market, get_earnings_calendar, get_dividends_calendar, \
    get_ipo_calendar
from tvscreener.calendars import _range, _markets

T0, T1 = _range("2026-10-12", "2026-10-18")


class TestPreset:

    def test_preset_routes_to_single_market_and_clears_sort(self):
        ss = StockScreener().set_preset(Preset.GAINERS)
        payload = ss._build_payload(["name"])
        assert payload["preset"] == "gainers"
        assert payload["sort"] is None
        assert "markets" not in payload
        assert ss._request_url().endswith("/america/scan")

    def test_preset_with_several_markets_uses_global(self):
        ss = StockScreener().set_markets(Market.AMERICA, Market.JAPAN).set_preset(Preset.EARNINGS)
        assert ss._request_url().endswith("/global/scan")
        assert ss._build_payload(["name"])["markets"] == ["america", "japan"]

    def test_ipo_calendar_always_global(self):
        ss = StockScreener().set_preset(Preset.IPO_CALENDAR)
        assert ss._request_url().endswith("/global/scan")
        assert ss._build_payload(["name"])["markets"] == ["america"]

    def test_sort_by_after_preset_overrides(self):
        ss = StockScreener().set_preset("gainers").sort_by(StockField.MARKET_CAPITALIZATION, False)
        assert ss._build_payload(["name"])["sort"] == {"sortBy": "market_cap_basic", "sortOrder": "desc"}

    def test_no_preset_unchanged(self):
        ss = StockScreener()
        assert ss._request_url().endswith("/global/scan")
        assert "preset" not in ss._build_payload(["name"])

    def test_remove_preset(self):
        ss = StockScreener().set_preset(Preset.GAINERS).set_preset(None)
        assert "preset" not in ss._build_payload(["name"])


class TestCalendarHelpers:

    def test_range_is_inclusive_utc_days(self):
        assert T0 == dt.datetime(2026, 10, 12, tzinfo=dt.timezone.utc).timestamp()
        assert T1 == pytest.approx(dt.datetime(2026, 10, 19, tzinfo=dt.timezone.utc).timestamp() - 0.001)

    def test_range_rejects_reversed(self):
        with pytest.raises(ValueError):
            _range("2026-10-18", "2026-10-12")

    def test_markets(self):
        assert _markets(None) == ["america"]
        assert _markets(Market.JAPAN) == ["japan"]
        assert _markets([Market.AMERICA, "germany"]) == ["america", "germany"]
        assert "ALL" not in _markets(Market.ALL) and len(_markets(Market.ALL)) == len(Market) - 1


def _response(rows, symbols, total=None):
    return MagicMock(json=MagicMock(return_value={
        "totalCount": len(rows) if total is None else total,
        "data": [{"s": s, "d": r} for s, r in zip(symbols, rows)],
    }))


class TestEarningsCalendar:

    @patch('tvscreener.calendars.requests.post')
    def test_reported_and_upcoming_rows(self, mock_post):
        inside, before, after = T0 + 3600, T0 - 86400 * 90, T1 + 86400 * 90
        reported = ["JPM", "JPMorgan", "america", inside, after, -1, -1, 5.57, 5.93, 6.1, -0.36, -6.03,
                    4.6e10, 4.5e10, 4.7e10, 1e9, 2.2, 8e11, "USD"]
        upcoming = ["NFLX", "Netflix", "america", before, inside, 1, 1, 7.0, 6.9, 7.5, 0.1, 1.4,
                    1.1e10, 1.0e10, 1.2e10, 1e8, 1.0, 5e11, "USD"]
        mock_post.return_value = _response([reported, upcoming], ["NYSE:JPM", "NASDAQ:NFLX"])
        df = get_earnings_calendar("2026-10-12", "2026-10-18")

        jpm = df.set_index("symbol").loc["NYSE:JPM"]
        assert jpm["reported"] and jpm["time"] == "before_open"
        assert jpm["eps_actual"] == 5.57 and jpm["eps_estimate"] == 5.93

        nflx = df.set_index("symbol").loc["NASDAQ:NFLX"]
        assert not nflx["reported"] and nflx["time"] == "after_close"
        assert nflx["eps_estimate"] == 7.5            # forecast of the next quarter
        assert pd.isna(nflx["eps_actual"])            # previous quarter's actual is not shown
        assert nflx["date"] == pd.Timestamp(inside, unit="s", tz="UTC")

        payload = mock_post.call_args.kwargs["data"]
        assert '"earnings_release_date,earnings_release_next_date"' in payload

    @patch('tvscreener.calendars.requests.post')
    def test_pagination(self, mock_post):
        row = ["A", "A", "america", T0 + 1, None, -1, None] + [1.0] * 10 + [1e9, "USD"]
        mock_post.side_effect = [_response([row], ["X:A"], total=7000), _response([row], ["X:B"], total=7000)]
        df = get_earnings_calendar("2026-10-12")
        assert mock_post.call_count == 2
        assert len(df) == 2


class TestDividendsAndIpo:

    @patch('tvscreener.calendars.requests.post')
    def test_dividends_pick_event_in_range(self, mock_post):
        recent = ["A", "A Inc", "america", T0 + 10, T1 + 1e6, T0 + 20, T1 + 2e6, 0.5, 0.6, 3.1, "USD"]
        upcoming = ["B", "B Inc", "america", T0 - 1e6, T0 + 10, T0 - 5e5, T0 + 50, 0.2, 0.25, 2.0, "USD"]
        mock_post.return_value = _response([recent, upcoming], ["X:A", "X:B"])
        df = get_dividends_calendar("2026-10-12", "2026-10-18").set_index("symbol")
        assert df.loc["X:A", "amount"] == 0.5
        assert df.loc["X:B", "amount"] == 0.25

    @patch('tvscreener.calendars.requests.post')
    def test_ipo_uses_preset(self, mock_post):
        mock_post.return_value = _response([["IAM", "Iambic", "NASDAQ", "america", T0 + 5, "pending",
                                             None, "15.00 - 17.00", 9375000, 1.6e8, None]], ["NASDAQ:IAM"])
        df = get_ipo_calendar("2026-10-12", "2026-10-18")
        assert '"preset": "ipo_calendar"' in mock_post.call_args.kwargs["data"]
        assert df.loc[0, "status"] == "pending"
