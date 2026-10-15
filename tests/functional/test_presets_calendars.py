import datetime as dt
import unittest

import pandas as pd

from tvscreener import StockScreener, StockField, Preset, Market, get_earnings_calendar, get_dividends_calendar, \
    get_ipo_calendar


class TestPresets(unittest.TestCase):

    def test_gainers_sorted_by_change(self):
        ss = StockScreener().set_preset(Preset.GAINERS).select(StockField.NAME, StockField.CHANGE_PERCENT)
        df = ss.get()
        self.assertGreater(len(df), 0)
        self.assertTrue((df["Change %"] > 0).all())
        self.assertTrue(df["Change %"].is_monotonic_decreasing)

    def test_preset_on_another_market(self):
        df = StockScreener().set_markets(Market.GERMANY).set_preset(Preset.LOSERS).get()
        self.assertGreater(len(df), 0)


class TestCalendars(unittest.TestCase):

    def setUp(self):
        self.start = dt.date.today() - dt.timedelta(days=7)
        self.end = dt.date.today() + dt.timedelta(days=7)
        self.lo = pd.Timestamp(self.start, tz="UTC")
        self.hi = pd.Timestamp(self.end + dt.timedelta(days=1), tz="UTC")

    def test_earnings(self):
        df = get_earnings_calendar(self.start, self.end, markets=Market.ALL)
        self.assertGreater(len(df), 0)
        self.assertTrue(df["date"].between(self.lo, self.hi).all())
        self.assertTrue(df.loc[~df["reported"], "eps_actual"].isna().all())

    def test_dividends(self):
        df = get_dividends_calendar(self.start, self.end)
        self.assertGreater(len(df), 0)
        self.assertTrue(df["ex_date"].between(self.lo, self.hi).all())

    def test_ipo(self):
        start = dt.date.today() - dt.timedelta(days=30)
        df = get_ipo_calendar(start, self.end, markets=Market.ALL)
        self.assertGreater(len(df), 0)
        self.assertTrue(df["date"].between(pd.Timestamp(start, tz="UTC"), self.hi).all())


if __name__ == '__main__':
    unittest.main()
