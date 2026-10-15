import re
import unittest

import requests

from tvscreener import StockScreener, StockField
from tvscreener.core.base import REQUEST_HEADERS


class TestFilterGroups(unittest.TestCase):

    def test_or_group(self):
        ss = StockScreener().select(StockField.NAME, StockField.SECTOR, StockField.MARKET_CAPITALIZATION)
        ss.where(StockField.MARKET_CAPITALIZATION > 1e11)
        ss.where((StockField.SECTOR == 'Finance') | (StockField.SECTOR == 'Utilities'))
        df = ss.get()
        self.assertGreater(len(df), 0)
        self.assertTrue(df["Sector"].isin(['Finance', 'Utilities']).all())
        self.assertTrue((df["Market Capitalization"] > 1e11).all())


class TestNewOperations(unittest.TestCase):

    def test_above_pct(self):
        sma50 = StockField.SIMPLE_MOVING_AVERAGE_50
        ss = StockScreener().select(StockField.PRICE, sma50)
        ss.where(StockField.PRICE.above_pct(sma50, 5))
        df = ss.get()
        self.assertGreater(len(df), 0)
        self.assertTrue((df["Price"] > 1.05 * df[sma50.label]).all())

    def test_has_etf(self):
        ss = StockScreener().select(StockField.TYPESPECS)
        ss.where(StockField.TYPESPECS.has('etf'))
        df = ss.get()
        self.assertGreater(len(df), 0)
        self.assertTrue(df["Typespecs"].apply(lambda t: 'etf' in t).all())

    def test_not_empty(self):
        ss = StockScreener().select(StockField.DIVIDENDS_YIELD)
        ss.where(StockField.DIVIDENDS_YIELD.not_empty())
        df = ss.get()
        self.assertGreater(len(df), 0)
        self.assertTrue(df[StockField.DIVIDENDS_YIELD.label].notna().all())


class TestHistoryFlags(unittest.TestCase):

    def test_metainfo_history_fields_are_historical(self):
        # Every 'X[n]' listed by TradingView must be reachable with X.with_history(n) (#65)
        response = requests.post("https://scanner.tradingview.com/america/metainfo",
                                 headers=REQUEST_HEADERS, data="{}", timeout=30)
        response.raise_for_status()
        bases = {re.sub(r"\[\d+\]$", "", f["n"]) for f in response.json()["fields"] if re.search(r"\[\d+\]$", f["n"])}
        by_name = {f.field_name: f for f in StockField}
        not_historical = sorted(b for b in bases if b in by_name and not by_name[b].historical)
        self.assertEqual([], not_historical)


if __name__ == '__main__':
    unittest.main()
