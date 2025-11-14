import unittest

from tvscreener import StockField
from tvscreener.field import add_historical
from tvscreener.util import format_historical_field


class TestColumns(unittest.TestCase):

    def test_hist_1(self):
        field = format_historical_field(StockField.NEGATIVE_DIRECTIONAL_INDICATOR_14)
        self.assertEqual("ADX-DI[1]", field)

    def test_hist_2(self):
        field = format_historical_field(StockField.NEGATIVE_DIRECTIONAL_INDICATOR_14, 2)
        self.assertEqual("ADX-DI[2]", field)

    def test_add_historical(self):
        field = add_historical(StockField.POSITIVE_DIRECTIONAL_INDICATOR_14.field_name)
        self.assertEqual("ADX+DI[1]", field)

    def test_add_historical_2(self):
        field = add_historical(StockField.POSITIVE_DIRECTIONAL_INDICATOR_14.field_name, 2)
        self.assertEqual("ADX+DI[2]", field)
