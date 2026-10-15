from unittest.mock import patch, MagicMock

import pandas as pd
import pytest

from tvscreener import (
    EconomicsScreener, EconomicsField, EconomicCategory, IndexScreener, IndexField,
    GovernmentBondScreener, GovernmentBondField, StockField, get_yield_curve,
)
from tvscreener.core.government_bond import _tenor


def _payload(screener):
    return screener._build_payload(["name"])


class TestEconomicsScreener:

    def test_url_and_category_filter(self):
        es = EconomicsScreener()
        es.where(EconomicsField.ECONOMIC_CATEGORY_ID == EconomicCategory.LABOUR)
        assert es.url.endswith("/economics2/scan")
        assert _payload(es)["filter"] == [{"left": "economic-category-id", "operation": "equal", "right": "lbr"}]

    def test_rejects_other_fields(self):
        with pytest.raises(TypeError):
            EconomicsScreener().where(StockField.PRICE > 1)

    @patch('tvscreener.core.base.requests.post')
    def test_time_converted(self, mock_post):
        mock_post.return_value = MagicMock(ok=True, json=MagicMock(return_value={"totalCount": 1, "data": [
            {"s": "ECONOMICS:USUR", "d": ["USUR", 4.2, 1790726400, "streaming"]}]}))
        df = EconomicsScreener().select(EconomicsField.NAME, EconomicsField.CLOSE, EconomicsField.TIME).get()
        assert df["Time"].iloc[0] == pd.Timestamp(1790726400, unit="s", tz="UTC")


class TestIndexScreener:

    @pytest.mark.parametrize("method, tag", [("main_indices", "main"), ("cfds", "cfd"), ("crypto_market_caps", "crypto")])
    def test_typespecs_helpers(self, method, tag):
        s = getattr(IndexScreener(), method)()
        assert s.url.endswith("/cfd/scan")
        assert _payload(s)["filter"] == [{"left": "typespecs", "operation": "has", "right": tag}]


class TestGovernmentBonds:

    def test_yields_only(self):
        gs = GovernmentBondScreener().yields_only()
        assert gs.url.endswith("/bonds/scan")
        assert _payload(gs)["filter"] == [{"left": "typespecs", "operation": "has", "right": "yield"}]
        assert _payload(GovernmentBondScreener().prices_only())["filter"][0]["operation"] == "has_none_of"

    @pytest.mark.parametrize("name, tenor", [("US10Y", "10Y"), ("US03MY", "3M"), ("DE01MY", "1M"), ("JP30Y", "30Y"), ("US10", "10Y")])
    def test_tenor(self, name, tenor):
        assert _tenor(name) == tenor

    @patch('tvscreener.core.government_bond.requests.post')
    def test_yield_curve(self, mock_post):
        mock_post.return_value = MagicMock(json=MagicMock(return_value={"data": [
            {"s": "TVC:US03MY", "d": ["US03MY", "3M", 4.21, 0.01, 91, 20270114]},
            {"s": "TVC:US10Y", "d": ["US10Y", "10Y", 5.11, -0.08, 3592, 20360815]},
        ]}))
        df = get_yield_curve("us")
        assert '"right": "US"' in mock_post.call_args.kwargs["data"]
        assert df["tenor"].tolist() == ["3M", "10Y"]
        assert df["yield"].tolist() == [4.21, 5.11]
        assert df["maturity_date"].iloc[1] == pd.Timestamp(2036, 8, 15)
