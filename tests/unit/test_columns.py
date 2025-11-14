import unittest

from tvscreener import StockField
from tvscreener.field import add_time_interval, add_historical
from tvscreener.util import format_historical_field


class TestColumns(unittest.TestCase):

    def test_hist_1(self):
        field = format_historical_field(StockField.NEGATIVE_DIRECTIONAL_INDICATOR_14, "1D")
        self.assertEqual("ADX-DI[1]", field)

    def test_hist_2(self):
        field = format_historical_field(StockField.NEGATIVE_DIRECTIONAL_INDICATOR_14, "1D", 2)
        self.assertEqual("ADX-DI[2]", field)

    def test_hist_update_mode(self):
        field = format_historical_field(StockField.NEGATIVE_DIRECTIONAL_INDICATOR_14, "1W", 1)
        self.assertEqual("ADX-DI[1]|1W", field)

    def test_add_time_interval(self):
        field = add_time_interval("change", "1D")
        self.assertEqual("change|1D", field)

    def test_add_historical(self):
        field = add_historical(StockField.POSITIVE_DIRECTIONAL_INDICATOR_14.field_name)
        self.assertEqual("ADX+DI[1]", field)

    def test_add_historical_2(self):
        field = add_historical(StockField.POSITIVE_DIRECTIONAL_INDICATOR_14.field_name, 2)
        self.assertEqual("ADX+DI[2]", field)
