import unittest

from tvscreener import (
    EconomicsScreener, EconomicsField, EconomicCategory, IndexScreener, IndexField,
    GovernmentBondScreener, GovernmentBondField, get_yield_curve,
)


class TestEconomicsScreener(unittest.TestCase):

    def test_us_labour(self):
        es = EconomicsScreener()
        es.where(EconomicsField.COUNTRY_CODE == 'US')
        es.where(EconomicsField.ECONOMIC_CATEGORY_ID == EconomicCategory.LABOUR)
        df = es.get()
        self.assertGreater(len(df), 0)
        self.assertTrue((df["Country Code"] == "US").all())
        self.assertTrue((df["Economic Category ID"] == "lbr").all())
        self.assertTrue(df["Time"].notna().all())


class TestIndexScreener(unittest.TestCase):

    def test_groups(self):
        for screener, tag in [(IndexScreener().main_indices(), "main"), (IndexScreener().cfds(), "cfd")]:
            df = screener.select(IndexField.NAME, IndexField.TYPESPECS).get()
            self.assertGreater(len(df), 0)
            self.assertTrue(df["Typespecs"].apply(lambda t: tag in t).all())


class TestGovernmentBonds(unittest.TestCase):

    def test_screener_yields(self):
        gs = GovernmentBondScreener().yields_only()
        gs.where(GovernmentBondField.COUNTRY_CODE == 'DE')
        df = gs.get()
        self.assertGreater(len(df), 0)
        self.assertTrue(df["Name"].str.startswith("DE").all())
        self.assertTrue(df["Days To Maturity"].is_monotonic_increasing)

    def test_yield_curve(self):
        df = get_yield_curve("US")
        self.assertIn("10Y", df["tenor"].values)
        self.assertTrue(df["days_to_maturity"].is_monotonic_increasing)
        self.assertTrue(df["yield"].between(-5, 30).all())


if __name__ == '__main__':
    unittest.main()
