import pandas as pd

from tvscreener.filter import RatingFilter, RocFilter
from tvscreener.lib.screeners.forex_opportunity import (
    ForexOpportunityScreener,
    ForexScreenerConfig,
    ScoringConfig,
)
from tvscreener.lib.screeners.forex_strategy import ForexStrategyScanner, StrategyConfig


class TestScoringConfig:
    def test_default_weights(self):
        config = ScoringConfig()
        assert config.trend_weight == 0.4
        assert config.ma_weight == 0.3
        assert config.osc_weight == 0.2
        assert config.roc_weight == 0.1
        total = config.trend_weight + config.ma_weight + config.osc_weight + config.roc_weight
        assert abs(total - 1.0) < 0.001

    def test_custom_weights(self):
        config = ScoringConfig(trend_weight=0.5, ma_weight=0.2, osc_weight=0.2, roc_weight=0.1)
        assert config.trend_weight == 0.5
        total = config.trend_weight + config.ma_weight + config.osc_weight + config.roc_weight
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
        screener = ForexOpportunityScreener(pairs=["EURUSD", "GBPUSD"], timeframes=["15"])

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


class TestContractTypeFilter:
    def test_cfd_filter_excludes_spot(self):
        config = ForexScreenerConfig(contract_type="cfd")
        screener = ForexOpportunityScreener(pairs=["EURUSD"], config=config)

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD.1.CFJ", "EURUSD.2.DUB"],
                "Symbol": ["EURUSD:ICMARKETS", "EURUSD:OANDA"],
                "Subtype": ["cfd", ""],
                "Recommend All|15": [0.8, 0.5],
                "Recommend All|60": [0.7, 0.4],
                "Recommend All|240": [0.6, 0.3],
                "Roc|15": [1.5, 0.8],
                "Roc|60": [1.2, 0.5],
                "Roc|240": [0.9, 0.2],
                "Average Volume (10 day Calc)": [1000000, 500000],
            }
        )

        result = screener._apply_contract_type_filter(mock_df)
        assert len(result) == 1
        assert result.iloc[0]["Subtype"] == "cfd"

    def test_spot_filter_includes_empty_and_spot(self):
        config = ForexScreenerConfig(contract_type="spot")
        screener = ForexOpportunityScreener(pairs=["EURUSD"], config=config)

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD.1.CFJ", "EURUSD.2.DUB"],
                "Symbol": ["EURUSD:ICMARKETS", "EURUSD:OANDA"],
                "Subtype": ["cfd", ""],
                "Recommend All|15": [0.8, 0.5],
                "Recommend All|60": [0.7, 0.4],
                "Recommend All|240": [0.6, 0.3],
                "Roc|15": [1.5, 0.8],
                "Roc|60": [1.2, 0.5],
                "Roc|240": [0.9, 0.2],
                "Average Volume (10 day Calc)": [1000000, 500000],
            }
        )

        result = screener._apply_contract_type_filter(mock_df)
        assert len(result) == 1
        assert result.iloc[0]["Subtype"] == ""

    def test_all_filter_includes_all(self):
        config = ForexScreenerConfig(contract_type="all")
        screener = ForexOpportunityScreener(pairs=["EURUSD"], config=config)

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD.1.CFJ", "EURUSD.2.DUB"],
                "Symbol": ["EURUSD:ICMARKETS", "EURUSD:OANDA"],
                "Subtype": ["cfd", ""],
                "Recommend All|15": [0.8, 0.5],
                "Recommend All|60": [0.7, 0.4],
                "Recommend All|240": [0.6, 0.3],
                "Roc|15": [1.5, 0.8],
                "Roc|60": [1.2, 0.5],
                "Roc|240": [0.9, 0.2],
                "Average Volume (10 day Calc)": [1000000, 500000],
            }
        )

        result = screener._apply_contract_type_filter(mock_df)
        assert len(result) == 2

    def test_spreadbet_filter(self):
        config = ForexScreenerConfig(contract_type="spreadbet")
        screener = ForexOpportunityScreener(pairs=["EURUSD"], config=config)

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD.1.CFJ", "EURUSD.2.SB"],
                "Symbol": ["EURUSD:ICMARKETS", "EURUSD:SPREADBET"],
                "Subtype": ["cfd", "spreadbet"],
                "Recommend All|15": [0.8, 0.5],
                "Recommend All|60": [0.7, 0.4],
                "Recommend All|240": [0.6, 0.3],
                "Roc|15": [1.5, 0.8],
                "Roc|60": [1.2, 0.5],
                "Roc|240": [0.9, 0.2],
                "Average Volume (10 day Calc)": [1000000, 500000],
            }
        )

        result = screener._apply_contract_type_filter(mock_df)
        assert len(result) == 1
        assert result.iloc[0]["Subtype"] == "spreadbet"


class TestRatingFilter:
    def test_rating_threshold_includes_above(self):
        screener = ForexOpportunityScreener(pairs=["EURUSD"])

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Recommend All|15": [0.8],
                "Recommend All|60": [0.7],
                "Recommend All|240": [0.6],
                "Roc|15": [1.5],
                "Roc|60": [1.2],
                "Roc|240": [0.9],
                "Average Volume (10 day Calc)": [1000000],
            }
        )

        rf = RatingFilter(rating_type="all", threshold=0.5)
        result = screener._apply_rating_filter(mock_df, rf)
        assert len(result) == 1

    def test_rating_threshold_excludes_below(self):
        screener = ForexOpportunityScreener(pairs=["EURUSD"])

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Recommend All|15": [0.3],
                "Recommend All|60": [0.3],
                "Recommend All|240": [0.3],
                "Roc|15": [1.5],
                "Roc|60": [1.2],
                "Roc|240": [0.9],
                "Average Volume (10 day Calc)": [1000000],
            }
        )

        rf = RatingFilter(rating_type="all", threshold=0.5)
        result = screener._apply_rating_filter(mock_df, rf)
        assert len(result) == 0

    def test_ma_rating_filter(self):
        screener = ForexOpportunityScreener(pairs=["EURUSD"])

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Recommend Ma|15": [0.8],
                "Recommend Ma|60": [0.7],
                "Recommend Ma|240": [0.6],
                "Recommend All|15": [0.3],
                "Recommend All|60": [0.3],
                "Recommend All|240": [0.3],
                "Roc|15": [1.5],
                "Roc|60": [1.2],
                "Roc|240": [0.9],
                "Average Volume (10 day Calc)": [1000000],
            }
        )

        rf = RatingFilter(rating_type="ma", threshold=0.5)
        result = screener._apply_rating_filter(mock_df, rf)
        assert len(result) == 1

    def test_oscillator_rating_filter(self):
        screener = ForexOpportunityScreener(pairs=["EURUSD"])

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Recommend Other|15": [0.8],
                "Recommend Other|60": [0.7],
                "Recommend Other|240": [0.6],
                "Recommend All|15": [0.3],
                "Recommend All|60": [0.3],
                "Recommend All|240": [0.3],
                "Roc|15": [1.5],
                "Roc|60": [1.2],
                "Roc|240": [0.9],
                "Average Volume (10 day Calc)": [1000000],
            }
        )

        rf = RatingFilter(rating_type="oscillator", threshold=0.5)
        result = screener._apply_rating_filter(mock_df, rf)
        assert len(result) == 1


class TestRocFilter:
    def test_roc_min_filter_includes_above(self):
        screener = ForexOpportunityScreener(pairs=["EURUSD"], timeframes=["15"])

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Recommend All|15": [0.8],
                "Recommend Ma|15": [0.6],
                "Recommend Other|15": [0.4],
                "Roc|15": [2.0],
            }
        )

        roc_filter = RocFilter(min_roc=1.0)
        result = screener._apply_roc_filter(mock_df, roc_filter)
        assert len(result) == 1

    def test_roc_min_filter_excludes_below(self):
        screener = ForexOpportunityScreener(pairs=["EURUSD"], timeframes=["15"])

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Recommend All|15": [0.8],
                "Recommend Ma|15": [0.6],
                "Recommend Other|15": [0.4],
                "Roc|15": [0.5],
            }
        )

        roc_filter = RocFilter(min_roc=1.0)
        result = screener._apply_roc_filter(mock_df, roc_filter)
        assert len(result) == 0

    def test_roc_max_filter(self):
        screener = ForexOpportunityScreener(pairs=["EURUSD"], timeframes=["15"])

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Recommend All|15": [0.8],
                "Recommend Ma|15": [0.6],
                "Recommend Other|15": [0.4],
                "Roc|15": [5.0],
            }
        )

        roc_filter = RocFilter(max_roc=3.0)
        result = screener._apply_roc_filter(mock_df, roc_filter)
        assert len(result) == 0

    def test_roc_range_filter(self):
        screener = ForexOpportunityScreener(pairs=["EURUSD"], timeframes=["15"])

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Recommend All|15": [0.8],
                "Recommend Ma|15": [0.6],
                "Recommend Other|15": [0.4],
                "Roc|15": [2.0],
            }
        )

        roc_filter = RocFilter(min_roc=1.0, max_roc=3.0)
        result = screener._apply_roc_filter(mock_df, roc_filter)
        assert len(result) == 1


class TestDeduplication:
    def test_canonical_pair_selection(self):
        screener = ForexOpportunityScreener(pairs=["EURUSD", "GBPUSD"])

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD.1.CFJ", "EURUSD.10.DUB", "GBPUSD.1.OANDA"],
                "Symbol": ["EURUSD:ICMARKETS", "EURUSD:OANDA", "GBPUSD:OANDA"],
                "Subtype": ["cfd", "cfd", "cfd"],
                "Recommend All|15": [0.8, 0.9, 0.7],
                "Recommend All|60": [0.7, 0.8, 0.6],
                "Recommend All|240": [0.6, 0.7, 0.5],
                "Roc|15": [1.5, 1.6, 1.4],
                "Roc|60": [1.2, 1.3, 1.1],
                "Roc|240": [0.9, 1.0, 0.8],
                "Average Volume (10 day Calc)": [1000000, 2000000, 800000],
            }
        )

        result = screener._merge_duplicates(mock_df)
        assert len(result) == 2
        assert "_base_pair" in result.columns
        assert "EURUSD" in result["_base_pair"].values
        assert "GBPUSD" in result["_base_pair"].values

    def test_base_pair_extraction_from_embedded_pair(self):
        screener = ForexOpportunityScreener(pairs=["EURUSD", "GBPUSD"])

        mock_df = pd.DataFrame(
            {
                "Name": ["X_EURUSD.1.CFJ", "X_GBPUSD.1.OANDA"],
                "Symbol": ["EURUSD:ICMARKETS", "GBPUSD:OANDA"],
                "Subtype": ["cfd", "cfd"],
                "Recommend All|15": [0.8, 0.7],
                "Recommend All|60": [0.7, 0.6],
                "Recommend All|240": [0.6, 0.5],
                "Roc|15": [1.5, 1.4],
                "Roc|60": [1.2, 1.1],
                "Roc|240": [0.9, 0.8],
                "Average Volume (10 day Calc)": [1000000, 800000],
            }
        )

        result = screener._merge_duplicates(mock_df)
        assert set(result["_base_pair"].tolist()) == {"EURUSD", "GBPUSD"}

    def test_volume_priority_selection(self):
        screener = ForexOpportunityScreener(pairs=["EURUSD"])

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD.1.CFJ", "EURUSD.10.DUB"],
                "Symbol": ["EURUSD:ICMARKETS", "EURUSD:OANDA"],
                "Subtype": ["cfd", "cfd"],
                "Recommend All|15": [0.8, 0.9],
                "Recommend All|60": [0.7, 0.8],
                "Recommend All|240": [0.6, 0.7],
                "Roc|15": [1.5, 1.6],
                "Roc|60": [1.2, 1.3],
                "Roc|240": [0.9, 1.0],
                "Average Volume (10 day Calc)": [1000000, 5000000],
            }
        )

        result = screener._merge_duplicates(mock_df)
        assert len(result) == 1
        assert result.iloc[0]["Symbol"] == "EURUSD:OANDA"

    def test_exchange_priority_selection(self):
        screener = ForexOpportunityScreener(pairs=["EURUSD"])

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD.1.OANDA", "EURUSD.1.CFJ"],
                "Symbol": ["OANDA:EURUSD", "ICMARKETS:EURUSD"],
                "Subtype": ["cfd", "cfd"],
                "Recommend All|15": [0.8, 0.8],
                "Recommend All|60": [0.7, 0.7],
                "Recommend All|240": [0.6, 0.6],
                "Roc|15": [1.5, 1.5],
                "Roc|60": [1.2, 1.2],
                "Roc|240": [0.9, 0.9],
                "Average Volume (10 day Calc)": [1000000, 1000000],
            }
        )

        result = screener._merge_duplicates(mock_df)
        assert len(result) == 1
        assert result.iloc[0]["Symbol"] == "OANDA:EURUSD"

    def test_empty_dataframe(self):
        screener = ForexOpportunityScreener(pairs=["EURUSD"])

        mock_df = pd.DataFrame()
        result = screener._merge_duplicates(mock_df)
        assert len(result) == 0


class TestStrategyRequestedIndicatorFields:
    def test_enables_atr_request_when_max_atr_set(self):
        scanner = ForexStrategyScanner(
            pairs=["EURUSD"],
            timeframes=["15"],
            config=StrategyConfig(max_atr=1.0),
        )

        assert scanner._screener.config.include_atr is True
        assert scanner._screener.config.include_rsi is False

    def test_enables_rsi_request_when_mr_signals_set(self):
        scanner = ForexStrategyScanner(
            pairs=["EURUSD"],
            timeframes=["15"],
            config=StrategyConfig(mean_reversion_signals=("rsi_oversold",)),
        )

        assert scanner._screener.config.include_atr is False
        assert scanner._screener.config.include_rsi is True

    def test_defaults_do_not_request_extra_fields(self):
        scanner = ForexStrategyScanner(
            pairs=["EURUSD"],
            timeframes=["15"],
            config=StrategyConfig(),
        )

        assert scanner._screener.config.include_atr is False
        assert scanner._screener.config.include_rsi is False
