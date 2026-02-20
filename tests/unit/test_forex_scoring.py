import pytest
import pandas as pd
from tvscreener.screeners.forex_opportunity import (
    ForexOpportunityScreener,
    ScoringConfig,
    DEFAULT_SCORING_CONFIG,
)


class TestScoringConfig:
    def test_default_weights(self):
        config = ScoringConfig()
        assert config.trend_weight == 0.4
        assert config.ma_weight == 0.3
        assert config.osc_weight == 0.2
        assert config.roc_weight == 0.1
        total = (
            config.trend_weight
            + config.ma_weight
            + config.osc_weight
            + config.roc_weight
        )
        assert abs(total - 1.0) < 0.001

    def test_custom_weights(self):
        config = ScoringConfig(
            trend_weight=0.5, ma_weight=0.2, osc_weight=0.2, roc_weight=0.1
        )
        assert config.trend_weight == 0.5
        total = (
            config.trend_weight
            + config.ma_weight
            + config.osc_weight
            + config.roc_weight
        )
        assert abs(total - 1.0) < 0.001


class TestEnsembleScoring:
    def test_factor_score_columns_present(self):
        screener = ForexOpportunityScreener(
            pairs=["EURUSD"],
            timeframes=["15"],
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Symbol": ["EURUSD:OANDA"],
                "Recommend All|15": [0.8],
                "Recommend Ma|15": [0.6],
                "Recommend Other|15": [0.4],
                "Roc|15": [1.5],
            }
        )

        result = screener._rank_opportunities(mock_df)

        assert "TREND_SCORE" in result.columns
        assert "MA_SCORE" in result.columns
        assert "OSC_SCORE" in result.columns
        assert "ROC_SCORE" in result.columns
        assert "ENSEMBLE_SCORE" in result.columns
        assert "DIRECTION" in result.columns

    def test_ensemble_score_calculation(self):
        screener = ForexOpportunityScreener(
            pairs=["EURUSD"],
            timeframes=["15"],
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Symbol": ["EURUSD:OANDA"],
                "Recommend All|15": [1.0],
                "Recommend Ma|15": [1.0],
                "Recommend Other|15": [1.0],
                "Roc|15": [1.0],
            }
        )

        result = screener._rank_opportunities(mock_df)

        expected_ensemble = (1.0 * 0.4) + (1.0 * 0.3) + (1.0 * 0.2) + (1.0 * 0.1)
        assert abs(result.iloc[0]["ENSEMBLE_SCORE"] - expected_ensemble) < 0.1

    def test_direction_long(self):
        screener = ForexOpportunityScreener(pairs=["EURUSD"], timeframes=["15"])

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Symbol": ["EURUSD:OANDA"],
                "Recommend All|15": [1.0],
                "Recommend Ma|15": [1.0],
                "Recommend Other|15": [1.0],
                "Roc|15": [1.0],
            }
        )

        result = screener._rank_opportunities(mock_df)

        assert result.iloc[0]["DIRECTION"] == "long"

    def test_direction_short(self):
        screener = ForexOpportunityScreener(pairs=["EURUSD"], timeframes=["15"])

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Symbol": ["EURUSD:OANDA"],
                "Recommend All|15": [-1.0],
                "Recommend Ma|15": [-1.0],
                "Recommend Other|15": [-1.0],
                "Roc|15": [-1.0],
            }
        )

        result = screener._rank_opportunities(mock_df)

        assert result.iloc[0]["DIRECTION"] == "short"

    def test_sorted_by_ensemble_score(self):
        screener = ForexOpportunityScreener(
            pairs=["EURUSD", "GBPUSD"], timeframes=["15"]
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD", "GBPUSD"],
                "Symbol": ["EURUSD:OANDA", "GBPUSD:OANDA"],
                "Recommend All|15": [0.5, 1.0],
                "Recommend Ma|15": [0.5, 1.0],
                "Recommend Other|15": [0.5, 1.0],
                "Roc|15": [0.5, 1.0],
            }
        )

        result = screener._rank_opportunities(mock_df)

        assert result.iloc[0]["Name"] == "GBPUSD"
        assert result.iloc[1]["Name"] == "EURUSD"
