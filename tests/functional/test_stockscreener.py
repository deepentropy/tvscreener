import io
import unittest
from unittest.mock import patch

import pandas as pd

from tvscreener import StockScreener, MalformedRequestException, \
    ExtraFilter, FilterOperator, StockField
from tvscreener.field import SymbolType, Market, SubMarket, Country, Exchange


class TestScreener(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_stdout(self, mock_stdout):
        ss = StockScreener()
        ss.get(print_request=True)
        self.assertIn("filter", mock_stdout.getvalue())

    def test_malformed_request(self):
        ss = StockScreener()
        ss.add_filter(StockField.TYPE, FilterOperator.ABOVE_OR_EQUAL, "test")
        with self.assertRaises(MalformedRequestException):
            ss.get()

    def test_range(self):
        ss = StockScreener()
        df = ss.get()
        self.assertEqual(150, len(df))

    def test_search(self):
        ss = StockScreener()
        ss.set_symbol_types(SymbolType.COMMON_STOCK)
        ss.search('AA')
        df = ss.get()
        self.assertGreater(len(df), 80)

        # Verify structure, not specific symbol (order is not guaranteed by TV)
        self.assertTrue(df.loc[0, "Symbol"].startswith(("NASDAQ:", "NYSE:", "AMEX:", "OTC:")))
        self.assertIsInstance(df.loc[0, "Name"], str)

    def test_column_order(self):
        ss = StockScreener()
        df = ss.get()

        self.assertEqual(df.columns[0], "Symbol")
        self.assertEqual(df.columns[1], "Name")
        self.assertEqual(df.columns[2], "Description")

        # Verify structure, not specific symbol (order is not guaranteed by TV)
        self.assertIsInstance(df.loc[0, "Symbol"], str)
        self.assertIsInstance(df.loc[0, "Name"], str)

    def test_not_multiindex(self):
        ss = StockScreener()
        df = ss.get()
        self.assertIsInstance(df.index, pd.Index)

        self.assertEqual("Symbol", df.columns[0])
        self.assertEqual("Name", df.columns[1])
        self.assertEqual("Description", df.columns[2])

        # Verify structure, not specific symbol (order is not guaranteed by TV)
        self.assertIsInstance(df.loc[0, "Symbol"], str)
        self.assertIsInstance(df.loc[0, "Name"], str)

    def test_primary_filter(self):
        ss = StockScreener()
        ss.add_filter(ExtraFilter.PRIMARY, FilterOperator.EQUAL, True)
        df = ss.get()
        self.assertEqual(150, len(df))

        # Verify structure, not specific symbol (order is not guaranteed by TV)
        self.assertIsInstance(df.loc[0, "Symbol"], str)
        self.assertIsInstance(df.loc[0, "Name"], str)

    def test_market(self):
        ss = StockScreener()
        ss.set_markets(Market.ARGENTINA)
        df = ss.get()
        self.assertEqual(150, len(df))

        # Verify all results are from Argentina market (BCBA exchange)
        self.assertTrue(df.loc[0, "Symbol"].startswith("BCBA:"))

    def test_submarket(self):
        ss = StockScreener()
        ss.add_filter(StockField.SUBMARKET, FilterOperator.EQUAL, SubMarket.OTCQB)
        df = ss.get()
        self.assertEqual(150, len(df))

        # Verify all results are from OTC market
        self.assertTrue(df.loc[0, "Symbol"].startswith("OTC:"))

    def test_submarket_pink(self):
        ss = StockScreener()
        ss.add_filter(StockField.SUBMARKET, FilterOperator.EQUAL, SubMarket.PINK)
        df = ss.get()
        self.assertEqual(150, len(df))

        # Verify all results are from OTC market
        self.assertTrue(df.loc[0, "Symbol"].startswith("OTC:"))

    def test_country(self):
        ss = StockScreener()
        ss.add_filter(StockField.COUNTRY, FilterOperator.EQUAL, Country.ARGENTINA)
        df = ss.get()
        # Count can change over time, just verify we got results
        self.assertGreater(len(df), 10)
        self.assertLess(len(df), 50)

        # Verify structure
        self.assertIsInstance(df.loc[0, "Symbol"], str)
        self.assertIsInstance(df.loc[0, "Name"], str)

    def test_countries(self):
        ss = StockScreener()
        ss.add_filter(StockField.COUNTRY, FilterOperator.EQUAL, Country.ARGENTINA)
        ss.add_filter(StockField.COUNTRY, FilterOperator.EQUAL, Country.BERMUDA)
        df = ss.get()
        # Count can change over time, just verify we got results
        self.assertGreater(len(df), 50)
        self.assertLess(len(df), 200)

    def test_exchange(self):
        ss = StockScreener()
        ss.add_filter(StockField.EXCHANGE, FilterOperator.EQUAL, Exchange.NYSE_ARCA)
        df = ss.get()
        self.assertEqual(150, len(df))

        # Verify all results are from AMEX exchange
        self.assertTrue(df.loc[0, "Symbol"].startswith("AMEX:"))

    def test_current_trading_day(self):
        ss = StockScreener()
        ss.add_filter(ExtraFilter.CURRENT_TRADING_DAY, FilterOperator.EQUAL, True)
        df = ss.get()
        self.assertEqual(150, len(df))

        # Verify structure, not specific symbol (order is not guaranteed by TV)
        self.assertIsInstance(df.loc[0, "Symbol"], str)
        self.assertIsInstance(df.loc[0, "Name"], str)
