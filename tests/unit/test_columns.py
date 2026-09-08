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

    def test_add_historical_before_interval(self):
        """The offset goes on the base field, before the |interval suffix."""
        self.assertEqual("RSI[1]|1W", add_historical("RSI|1W"))
        self.assertEqual("RSI[2]|60", add_historical("RSI|60", 2))

    def test_add_historical_stacks_on_existing_offset(self):
        """Pre-baked fields already carrying an offset get a second one."""
        self.assertEqual("ADX+DI[1][1]|1", add_historical("ADX+DI[1]|1"))
