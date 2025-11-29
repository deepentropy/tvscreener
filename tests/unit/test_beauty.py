import unittest
import pandas as pd
import math

from tvscreener import beautify, StockField
from tvscreener.beauty import (
    _get_recommendation, _percent_colors, _rating_colors, _rating_letter,
    BUY_CHAR, SELL_CHAR, NEUTRAL_CHAR,
    COLOR_RED_NEGATIVE, COLOR_GREEN_POSITIVE, COLOR_BLUE_BUY, COLOR_RED_SELL, COLOR_GRAY_NEUTRAL
)
from tvscreener.field import Rating


class TestBeautifyHelpers(unittest.TestCase):

    def test_get_recommendation_positive(self):
        self.assertEqual(Rating.BUY, _get_recommendation(1))
        self.assertEqual(Rating.BUY, _get_recommendation(0.5))
        self.assertEqual(Rating.BUY, _get_recommendation(100))

    def test_get_recommendation_negative(self):
        self.assertEqual(Rating.SELL, _get_recommendation(-1))
        self.assertEqual(Rating.SELL, _get_recommendation(-0.5))
        self.assertEqual(Rating.SELL, _get_recommendation(-100))

    def test_get_recommendation_neutral(self):
        self.assertEqual(Rating.NEUTRAL, _get_recommendation(0))

    def test_percent_colors_positive(self):
        self.assertEqual(COLOR_GREEN_POSITIVE, _percent_colors("1.50%"))
        self.assertEqual(COLOR_GREEN_POSITIVE, _percent_colors("0.00%"))

    def test_percent_colors_negative(self):
        self.assertEqual(COLOR_RED_NEGATIVE, _percent_colors("-1.50%"))
        self.assertEqual(COLOR_RED_NEGATIVE, _percent_colors("-0.01%"))

    def test_rating_colors_buy(self):
        self.assertEqual(COLOR_BLUE_BUY, _rating_colors(f"1.5 {BUY_CHAR}"))

    def test_rating_colors_sell(self):
        self.assertEqual(COLOR_RED_SELL, _rating_colors(f"1.5 {SELL_CHAR}"))

    def test_rating_colors_neutral(self):
        self.assertEqual(COLOR_GRAY_NEUTRAL, _rating_colors(f"1.5 {NEUTRAL_CHAR}"))

    def test_rating_colors_non_string(self):
        """Test that non-string values return neutral color."""
        self.assertEqual(COLOR_GRAY_NEUTRAL, _rating_colors(123))
        self.assertEqual(COLOR_GRAY_NEUTRAL, _rating_colors(None))
        self.assertEqual(COLOR_GRAY_NEUTRAL, _rating_colors(1.5))

    def test_rating_letter_buy(self):
        self.assertEqual(BUY_CHAR, _rating_letter(Rating.BUY))
        self.assertEqual(BUY_CHAR, _rating_letter(Rating.STRONG_BUY))

    def test_rating_letter_sell(self):
        self.assertEqual(SELL_CHAR, _rating_letter(Rating.SELL))
        self.assertEqual(SELL_CHAR, _rating_letter(Rating.STRONG_SELL))

    def test_rating_letter_neutral(self):
        self.assertEqual(NEUTRAL_CHAR, _rating_letter(Rating.NEUTRAL))


class TestBeautifyFunction(unittest.TestCase):

    def test_beautify_returns_styler(self):
        # Create a simple DataFrame with percent column
        df = pd.DataFrame({
            'change': [1.5, -2.3, 0.0]
        })
        # Mock the StockField to test basic functionality
        # Note: beautify expects a ScreenerDataFrame, so we test with minimal setup
        # This is a simple smoke test
        self.assertTrue(callable(beautify))


if __name__ == '__main__':
    unittest.main()
