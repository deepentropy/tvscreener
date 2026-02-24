import unittest

import tvscreener.ta as ta
from tvscreener.field import Rating


class TestTechnicalAnalysis(unittest.TestCase):
    def test_adx_buy(self):
        # +DI crosses above -DI with ADX > 20
        result = ta.adx(adx_value=25, dminus=10, dplus=15, dminus_old=12, dplus_old=8)
        self.assertEqual(Rating.BUY, result)

    def test_adx_sell(self):
        # -DI crosses above +DI with ADX > 20
        result = ta.adx(adx_value=25, dminus=15, dplus=10, dminus_old=8, dplus_old=12)
        self.assertEqual(Rating.SELL, result)

    def test_adx_neutral_low_adx(self):
        # ADX <= 20 should return neutral
        result = ta.adx(adx_value=18, dminus=10, dplus=15, dminus_old=12, dplus_old=8)
        self.assertEqual(Rating.NEUTRAL, result)

    def test_adx_neutral_no_cross(self):
        # No cross, should return neutral
        result = ta.adx(adx_value=25, dminus=10, dplus=15, dminus_old=10, dplus_old=15)
        self.assertEqual(Rating.NEUTRAL, result)

    def test_ao_bullish_cross(self):
        # AO crosses above zero
        result = ta.ao(ao_value=5, ao_old_1=-2, ao_old_2=-5)
        self.assertEqual(Rating.BUY, result)

    def test_ao_bearish_cross(self):
        # AO crosses below zero
        result = ta.ao(ao_value=-5, ao_old_1=2, ao_old_2=5)
        self.assertEqual(Rating.SELL, result)

    def test_ao_bullish_saucer(self):
        # Bullish saucer: AO > 0, green bar after red bars
        result = ta.ao(ao_value=10, ao_old_1=5, ao_old_2=8)
        self.assertEqual(Rating.BUY, result)

    def test_ao_bearish_saucer(self):
        # Bearish saucer: AO < 0, red bar after green bars
        result = ta.ao(ao_value=-10, ao_old_1=-5, ao_old_2=-8)
        self.assertEqual(Rating.SELL, result)

    def test_ao_neutral(self):
        # No pattern detected
        result = ta.ao(ao_value=5, ao_old_1=6, ao_old_2=7)
        self.assertEqual(Rating.NEUTRAL, result)

    def test_bb_lower_buy(self):
        # Close below lower band = buy signal
        result = ta.bb_lower(low_limit=100, close=95)
        self.assertEqual(Rating.BUY, result)

    def test_bb_lower_neutral(self):
        # Close above lower band = neutral
        result = ta.bb_lower(low_limit=100, close=105)
        self.assertEqual(Rating.NEUTRAL, result)

    def test_bb_upper_sell(self):
        # Close above upper band = sell signal
        result = ta.bb_upper(up_limit=100, close=105)
        self.assertEqual(Rating.SELL, result)

    def test_bb_upper_neutral(self):
        # Close below upper band = neutral
        result = ta.bb_upper(up_limit=100, close=95)
        self.assertEqual(Rating.NEUTRAL, result)


if __name__ == "__main__":
    unittest.main()
