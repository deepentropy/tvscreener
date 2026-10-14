import unittest

from tvscreener import OptionScreener, OptionField, get_iv_term_structure


class TestOptionScreener(unittest.TestCase):

    def test_chain(self):
        os_ = OptionScreener("NASDAQ:AAPL")
        df = os_.get()
        self.assertGreater(len(df), 0)
        self.assertTrue((df["Underlying Symbol"] == "NASDAQ:AAPL").all())

    def test_delta_filter(self):
        os_ = OptionScreener("NASDAQ:AAPL")
        os_.where(OptionField.OPTION_TYPE == "call")
        os_.where(OptionField.DELTA.between(0.4, 0.6))
        df = os_.get()
        self.assertGreater(len(df), 0)
        self.assertTrue((df["Option Type"] == "call").all())
        self.assertTrue(df["Delta"].between(0.4, 0.6).all())


class TestIvTermStructure(unittest.TestCase):

    def test_term_structure(self):
        df = get_iv_term_structure("NASDAQ:AAPL")
        self.assertIn("standard", df["kind"].values)
        self.assertIn("listed", df["kind"].values)
        self.assertTrue((df["iv"] > 0).all())


if __name__ == '__main__':
    unittest.main()
