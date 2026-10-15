import unittest

from tvscreener import ETFScreener, StockField


class TestETFScreener(unittest.TestCase):

    def test_default(self):
        df = ETFScreener().get()
        self.assertGreater(len(df), 100)
        self.assertTrue(df["Aum"].dropna().is_monotonic_decreasing)
        self.assertIn("VOO", df["Name"].values)

    def test_filters_on_readable_names(self):
        es = ETFScreener()
        es.where(StockField.EXPENSE_RATIO < 0.1)
        es.where(StockField.ASSET_CLASS_NAME == 'Equity')
        df = es.get()
        self.assertGreater(len(df), 0)
        self.assertTrue((df["Asset Class Name"] == "Equity").all())
        self.assertTrue((df["Expense Ratio"] < 0.1).all())


if __name__ == '__main__':
    unittest.main()
