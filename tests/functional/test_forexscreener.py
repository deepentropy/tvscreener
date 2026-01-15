import unittest

from tvscreener import ForexScreener, ForexField, FilterOperator
from tvscreener.field import Region


class TestForexScreener(unittest.TestCase):

    def test_len(self):
        fs = ForexScreener()
        df = fs.get()
        self.assertEqual(150, len(df))

    def test_region(self):
        fs = ForexScreener()
        fs.add_filter(ForexField.REGION, FilterOperator.EQUAL, Region.AFRICA)
        df = fs.get()
        # Count can change over time, just verify we got results
        self.assertGreater(len(df), 30)
        self.assertLess(len(df), 150)

        # Verify structure, not specific symbol (order is not guaranteed by TV)
        self.assertIsInstance(df.loc[0, "Symbol"], str)
        self.assertIsInstance(df.loc[0, "Name"], str)
