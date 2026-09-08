import unittest

from tvscreener import ForexField, StockField
from tvscreener.core.base import ScreenerDataFrame, _uniquify
from tvscreener.util import get_columns_to_request


class TestUniquify(unittest.TestCase):

    def test_no_duplicates_unchanged(self):
        self.assertEqual(["a", "b", "c"], _uniquify(["a", "b", "c"]))

    def test_duplicate_gets_suffix(self):
        self.assertEqual(["a", "a.1", "b"], _uniquify(["a", "a", "b"]))

    def test_triple_duplicate(self):
        self.assertEqual(["a", "a.1", "a.2"], _uniquify(["a", "a", "a"]))

    def test_length_is_preserved(self):
        names = ["a", "a", "b", "a", "b"]
        self.assertEqual(len(names), len(_uniquify(names)))

    def test_suffix_does_not_collide_with_real_name(self):
        # 'a.1' already exists, so the duplicate 'a' must skip to 'a.2'
        self.assertEqual(["a", "a.1", "a.2"], _uniquify(["a", "a.1", "a"]))


class TestScreenerDataFrame(unittest.TestCase):

    def test_symbol_column_is_added(self):
        columns = {"name": "Name", "close": "Price"}
        df = ScreenerDataFrame([["NASDAQ:AAPL", "AAPL", 100.0]], columns)
        self.assertEqual(["Symbol", "Name", "Price"], list(df.columns))
        self.assertEqual("NASDAQ:AAPL", df.loc[0, "Symbol"])

    def test_field_named_symbol_does_not_shadow_ticker(self):
        """Forex/Crypto/Bond/Futures/Coin define a 'symbol' field of their own."""
        columns = {"name": "Name", "symbol": "Symbol"}
        df = ScreenerDataFrame([["FX_IDC:AEDAUD", "AEDAUD", None]], columns)
        self.assertEqual(3, len(df.columns))
        self.assertEqual("FX_IDC:AEDAUD", df.loc[0, "Symbol"])
        self.assertEqual("AEDAUD", df.loc[0, "Name"])
        self.assertIn("Symbol.1", df.columns)

    def test_duplicate_labels_are_disambiguated(self):
        """'High.All' and 'all_time_high' share the label 'All Time High'."""
        columns = {"name": "Name", "High.All": "All Time High", "all_time_high": "All Time High"}
        df = ScreenerDataFrame([["FX:EURUSD", "EURUSD", 1.2, 1.2]], columns)
        self.assertEqual(4, len(df.columns))
        self.assertIn("All Time High", df.columns)
        self.assertIn("All Time High.1", df.columns)
        self.assertFalse(df.columns.duplicated().any())

    def test_original_columns_keys_stay_unique(self):
        columns = {"name": "Name", "symbol": "Symbol"}
        df = ScreenerDataFrame([["FX_IDC:AEDAUD", "AEDAUD", None]], columns)
        keys = list(df.attrs["original_columns"].keys())
        self.assertEqual(len(keys), len(set(keys)))
        self.assertEqual(["symbol", "name", "symbol.1"], keys)

    def test_select_all_columns_have_no_collision(self):
        """Every field enum must yield one unique name per returned value."""
        for field_type in (StockField, ForexField):
            with self.subTest(field_type=field_type.__name__):
                columns = get_columns_to_request(field_type)
                row = ["EXCHANGE:TICKER"] + [None] * len(columns)
                df = ScreenerDataFrame([row], columns)
                self.assertEqual(len(columns) + 1, len(df.columns))
                self.assertFalse(df.columns.duplicated().any())
