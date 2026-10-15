import unittest
from unittest.mock import patch, MagicMock

from tvscreener import get_symbol, get_enum_values, get_metainfo, StockField, CryptoScreener


def _response(payload):
    return MagicMock(json=MagicMock(return_value=payload))


class TestGetSymbol(unittest.TestCase):

    @patch('tvscreener.scanner.requests.get')
    def test_fields_are_joined(self, mock_get):
        mock_get.return_value = _response({"close": 1.0})
        result = get_symbol("NASDAQ:AAPL", StockField.PRICE, StockField.RSI2.with_history(1), "earnings_fq_h")
        params = mock_get.call_args.kwargs["params"]
        self.assertEqual("NASDAQ:AAPL", params["symbol"])
        self.assertEqual("close,RSI2[1],earnings_fq_h", params["fields"])
        self.assertEqual("true", params["no_404"])
        self.assertEqual({"close": 1.0}, result)

    @patch('tvscreener.scanner.requests.get')
    def test_unknown_symbol_returns_none(self, mock_get):
        mock_get.return_value = _response(None)
        self.assertIsNone(get_symbol("NASDAQ:ZZZZZ", StockField.PRICE))

    def test_requires_fields(self):
        with self.assertRaises(ValueError):
            get_symbol("NASDAQ:AAPL")


class TestGetEnumValues(unittest.TestCase):

    @patch('tvscreener.scanner.requests.get')
    def test_maps_id_to_name(self, mock_get):
        mock_get.return_value = _response({"sector": [
            {"id": "Basic Materials", "name": "Basic materials", "options": {}},
            {"id": "Capital Goods", "name": "Capital goods", "options": {}},
        ]})
        result = get_enum_values("sector", "zzz")
        self.assertEqual("sector,zzz", mock_get.call_args.kwargs["params"]["id"])
        self.assertEqual({"sector": {"Basic Materials": "Basic materials", "Capital Goods": "Capital goods"}}, result)

    def test_requires_ids(self):
        with self.assertRaises(ValueError):
            get_enum_values()


class TestMetainfo(unittest.TestCase):

    @patch('tvscreener.scanner.requests.post')
    def test_dataframe(self, mock_post):
        mock_post.return_value = _response({"fields": [{"n": "close", "t": "price", "r": None},
                                                       {"n": "type", "t": "text", "r": ["spot"]}]})
        df = get_metainfo("crypto")
        self.assertTrue(mock_post.call_args.args[0].endswith("/crypto/metainfo"))
        self.assertEqual(["close", "type"], df["name"].tolist())
        self.assertEqual(["spot"], df["values"].iloc[1])

    @patch('tvscreener.scanner.requests.post')
    def test_screener_uses_its_market(self, mock_post):
        mock_post.return_value = _response({"fields": []})
        CryptoScreener().metainfo()
        self.assertTrue(mock_post.call_args.args[0].endswith("/crypto/metainfo"))


if __name__ == '__main__':
    unittest.main()
