import datetime as dt
import unittest
from unittest.mock import patch, MagicMock

import pandas as pd

from tvscreener import OptionScreener, OptionField, StockField, get_iv_term_structure


def _response(payload):
    response = MagicMock()
    response.ok = True
    response.json.return_value = payload
    return response


class TestOptionScreener(unittest.TestCase):

    def test_url(self):
        self.assertEqual("https://scanner.tradingview.com/options/scan", OptionScreener().url)

    def test_payload_has_index_filters(self):
        os_ = OptionScreener("NASDAQ:AAPL", "AMEX:SPY")
        payload = os_._build_payload(["iv"])
        self.assertEqual(
            [{"name": "underlying_symbol", "values": ["NASDAQ:AAPL", "AMEX:SPY"]}],
            payload["index_filters"]
        )

    def test_set_underlying_replaces(self):
        os_ = OptionScreener("NASDAQ:AAPL").set_underlying("NASDAQ:MSFT")
        self.assertEqual(["NASDAQ:MSFT"], os_.underlyings)

    def test_missing_underlying_raises(self):
        with self.assertRaises(ValueError):
            OptionScreener()._build_payload(["iv"])

    def test_default_sort_by_expiration(self):
        self.assertEqual({"sortBy": "expiration", "sortOrder": "asc"}, OptionScreener("NASDAQ:AAPL").sort)

    def test_rejects_other_field_types(self):
        with self.assertRaises(TypeError):
            OptionScreener("NASDAQ:AAPL").where(StockField.PRICE > 10)

    def test_expiration_filter_accepts_dates(self):
        os_ = OptionScreener("NASDAQ:AAPL")
        os_.where(OptionField.EXPIRATION == dt.date(2026, 11, 20))
        self.assertEqual([20261120], os_.filters[0].values)

    def test_expiration_filter_accepts_iso_strings_and_ints(self):
        os_ = OptionScreener("NASDAQ:AAPL")
        os_.where(OptionField.EXPIRATION.between("2026-11-01", 20261231))
        self.assertEqual([20261101, 20261231], os_.filters[0].values)

    @patch('tvscreener.core.base.requests.post')
    def test_get_parses_expiration(self, mock_post):
        mock_post.return_value = _response({"totalCount": 2, "data": [
            {"s": "OPRA:AAPL261120C250.0", "d": [250, 20261120, 0.42, "delayed_streaming_900"]},
            {"s": "OPRA:AAPL261218P250.0", "d": [250, None, 0.40, "delayed_streaming_900"]},
        ]})
        os_ = OptionScreener("NASDAQ:AAPL").select(
            OptionField.STRIKE, OptionField.EXPIRATION, OptionField.IMPLIED_VOLATILITY
        )
        df = os_.get()
        self.assertEqual(pd.Timestamp(2026, 11, 20), df["Expiration"].iloc[0])
        self.assertTrue(pd.isna(df["Expiration"].iloc[1]))
        self.assertAlmostEqual(0.42, df["Implied Volatility"].iloc[0])


class TestIvTermStructure(unittest.TestCase):

    @patch('tvscreener.volatility.requests.get')
    def test_parses_listed_and_standard(self, mock_get):
        mock_get.return_value = MagicMock(json=MagicMock(return_value={
            "symbol": "NASDAQ:AAPL",
            "real-ivs": [{"span": {"value": 4, "unit": "d"}, "value": 0.21}],
            "standard-ivs": [
                {"span": {"value": 1, "unit": "w"}, "value": 0.22},
                {"span": {"value": 1, "unit": "y"}, "value": 0.27},
            ],
        }))
        df = get_iv_term_structure("NASDAQ:AAPL")

        self.assertIn("NASDAQ:AAPL", mock_get.call_args[0][0])
        self.assertEqual(["listed", "standard", "standard"], df["kind"].tolist())
        self.assertEqual(["4d", "1w", "1y"], df["tenor"].tolist())
        self.assertEqual([4, 7, 365], df["days"].tolist())
        self.assertEqual([0.21, 0.22, 0.27], df["iv"].tolist())

    @patch('tvscreener.volatility.requests.get')
    def test_empty_response(self, mock_get):
        mock_get.return_value = MagicMock(json=MagicMock(return_value={"symbol": "X:Y"}))
        df = get_iv_term_structure("X:Y")
        self.assertTrue(df.empty)
        self.assertEqual(["kind", "tenor", "span_value", "span_unit", "days", "iv"], list(df.columns))


if __name__ == '__main__':
    unittest.main()
