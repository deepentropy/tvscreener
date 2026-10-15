import unittest

from tvscreener import get_symbol, get_enum_values, get_metainfo, StockField
from tvscreener.field import Sector, Industry, Exchange, Country


class TestScannerHelpers(unittest.TestCase):

    def test_get_symbol(self):
        data = get_symbol("NASDAQ:AAPL", StockField.PRICE, StockField.MARKET_CAPITALIZATION)
        self.assertGreater(data["close"], 0)
        self.assertGreater(data["market_cap_basic"], 0)
        self.assertIsNone(get_symbol("NASDAQ:ZZZZZZ", StockField.PRICE))

    def test_enums_are_valid_api_values(self):
        # Every library enum value must still be accepted by TradingView
        values = get_enum_values("sector", "industry", "exchange", "country")
        for enum, key in [(Sector, "sector"), (Industry, "industry"), (Exchange, "exchange"), (Country, "country")]:
            invalid = [m.value for m in enum if m.value != "Any" and m.value not in values[key]]
            self.assertEqual([], invalid, f"{enum.__name__} values unknown to TradingView")

    def test_metainfo(self):
        df = get_metainfo("america")
        self.assertIn("close", df["name"].values)


if __name__ == '__main__':
    unittest.main()
