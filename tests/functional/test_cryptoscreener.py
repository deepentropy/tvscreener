import unittest

from tvscreener import CryptoScreener


class TestScreener(unittest.TestCase):

    def test_range(self):
        ss = CryptoScreener()
        df = ss.get()
        self.assertEqual(150, len(df))

    def test_update_mode(self):
        ss = CryptoScreener()
        df = ss.get(update_mode="240")
        self.assertEqual(150, len(df))
