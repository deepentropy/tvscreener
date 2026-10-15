import unittest

from tvscreener import StockScreener, StockField, Market


class TestCurrency(unittest.TestCase):

    def _get(self, currency=None):
        ss = StockScreener().set_markets(Market.JAPAN, Market.GERMANY)
        if currency:
            ss.set_currency(currency)
        ss.select(StockField.PRICE, StockField.MARKET_CAPITALIZATION, StockField.FUNDAMENTAL_CURRENCY_CODE)
        ss.where(StockField.MARKET_CAPITALIZATION > 1e9)
        ss.set_range(0, 50)
        return ss.get()

    def test_fundamentals_converted_prices_not(self):
        usd = self._get()
        eur = self._get("eur")
        self.assertTrue((usd["Fundamental Currency Code"] == "USD").all())
        self.assertTrue((eur["Fundamental Currency Code"] == "EUR").all())
        both = usd.merge(eur, on="Symbol", suffixes=("_usd", "_eur"))
        self.assertGreater(len(both), 0)
        # Market caps differ by the exchange rate, prices are untouched
        ratio = both["Market Capitalization_eur"] / both["Market Capitalization_usd"]
        self.assertLess(ratio.max() - ratio.min(), 0.01)
        self.assertNotAlmostEqual(ratio.mean(), 1.0, places=3)
        # Quotes can tick between the two requests; a conversion would move them by the FX rate
        price_ratio = both["Price_eur"] / both["Price_usd"]
        self.assertLess((price_ratio - 1).abs().max(), 0.02)


if __name__ == '__main__':
    unittest.main()
