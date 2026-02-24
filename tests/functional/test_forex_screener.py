import pytest

from tvscreener.lib.screeners.forex_opportunity import ForexOpportunityScreener, ForexScreenerConfig


class TestIntegrationFilters:
    @pytest.mark.slow
    def test_cfd_filter_integration(self):
        config = ForexScreenerConfig(contract_type="cfd")
        screener = ForexOpportunityScreener(pairs=["EURUSD"], config=config)
        results = screener.get_opportunities()
        assert len(results) > 0

    @pytest.mark.slow
    def test_all_filter_integration(self):
        config = ForexScreenerConfig(contract_type="all")
        screener = ForexOpportunityScreener(pairs=["EURUSD"], config=config)
        results = screener.get_opportunities()
        assert len(results) > 0


class TestIntegrationRanking:
    @pytest.mark.slow
    def test_ranking_order_integration(self):
        screener = ForexOpportunityScreener(pairs=["EURUSD", "GBPUSD", "USDJPY"])
        results = screener.get_opportunities()
        assert len(results) > 0
        assert "ENSEMBLE_SCORE" in results.columns
        assert "DIRECTION" in results.columns

    @pytest.mark.slow
    def test_canonical_names_integration(self):
        screener = ForexOpportunityScreener(pairs=["EURUSD"])
        results = screener.get_opportunities()
        assert len(results) > 0
        assert "_base_pair" in results.columns
        assert results.iloc[0]["_base_pair"] == "EURUSD"
