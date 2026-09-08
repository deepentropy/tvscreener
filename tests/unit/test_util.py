import unittest
import math

from tvscreener import StockField, get_columns_to_request, get_recommendation, millify
from tvscreener.util import _is_nan


class TestUtil(unittest.TestCase):

    def test_get_columns_type(self):
        columns = get_columns_to_request(StockField)
        self.assertIsInstance(columns, dict)
        # StockField has 3509 fields after expanding technical indicators with intervals
        self.assertGreater(len(columns), 3000)

    def test_get_columns_len(self):
        columns = get_columns_to_request(StockField)
        self.assertIsInstance(columns, dict)

    def test_get_columns_with_interval_field(self):
        rsi_1h = StockField.RELATIVE_STRENGTH_INDEX_14.with_interval('60')
        columns = get_columns_to_request([StockField.NAME, rsi_1h])
        self.assertIsInstance(columns, dict)
        self.assertIn("RSI|60", columns)

    def test_get_columns_with_history_field(self):
        rsi_hist = StockField.RELATIVE_STRENGTH_INDEX_14.with_history(3)
        columns = get_columns_to_request([StockField.NAME, rsi_hist])
        self.assertIsInstance(columns, dict)
        self.assertIn("RSI[3]", columns)

    def test_get_columns_with_history_no_stacked_offset(self):
        """An explicit offset must not get a second offset stacked on it."""
        rsi_hist = StockField.RELATIVE_STRENGTH_INDEX_14.with_history(1)
        columns = get_columns_to_request([StockField.NAME, rsi_hist])
        self.assertIn("RSI[1]", columns)
        self.assertNotIn("RSI[1][1]", columns)

    def test_get_columns_interval_offset_before_interval(self):
        """TradingView needs RSI[1]|1W, not RSI|1W[1], for the Prev. column."""
        rsi_1w = StockField.RELATIVE_STRENGTH_INDEX_14.with_interval('1W')
        columns = get_columns_to_request([StockField.NAME, rsi_1w])
        self.assertIn("RSI|1W", columns)
        self.assertIn("RSI[1]|1W", columns)
        self.assertNotIn("RSI|1W[1]", columns)

    def test_get_recommendation(self):
        self.assertEqual("S", get_recommendation(-1))
        self.assertEqual("N", get_recommendation(0))
        self.assertEqual("B", get_recommendation(1))

    def test_millify(self):
        self.assertEqual("1.000M", millify(10 ** 6))
        self.assertEqual("10.000M", millify(10 ** 7))
        self.assertEqual("1.000B", millify(10 ** 9))

    def test_millify_thousands(self):
        self.assertEqual("1.000K", millify(10 ** 3))
        self.assertEqual("10.000K", millify(10 ** 4))
        self.assertEqual("100.000K", millify(10 ** 5))

    def test_millify_negative(self):
        self.assertEqual("-1.000M", millify(-10 ** 6))
        self.assertEqual("-1.000K", millify(-10 ** 3))
        self.assertEqual("-1.000B", millify(-10 ** 9))

    def test_millify_small(self):
        self.assertEqual("100.000", millify(100))
        self.assertEqual("1.000", millify(1))

    def test_is_nan_with_nan(self):
        self.assertTrue(_is_nan(float('nan')))
        self.assertTrue(_is_nan(math.nan))

    def test_is_nan_with_number(self):
        self.assertFalse(_is_nan(1))
        self.assertFalse(_is_nan(0))
        self.assertFalse(_is_nan(-1))
        self.assertFalse(_is_nan(1.5))

    def test_is_nan_with_string(self):
        self.assertFalse(_is_nan("hello"))
        self.assertFalse(_is_nan(""))

    def test_is_nan_with_none(self):
        self.assertFalse(_is_nan(None))
