import pandas as pd
import pytest

from tvscreener.filter import RatingFilter, RocFilter, VolumeFilter
from tvscreener.lib.screeners.forex_opportunity import (
    ForexOpportunityScreener,
    ForexScreenerConfig,
)


class TestVolumeFilter:
    def test_volume_filter_removes_below_threshold(self):
        screener = ForexOpportunityScreener(
            pairs=["EURUSD"],
            timeframes=["15"],
            config=ForexScreenerConfig(volume_filter=VolumeFilter(min_volume=1000000)),
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD", "GBPUSD", "USDJPY"],
                "Symbol": ["EURUSD:OANDA", "GBPUSD:OANDA", "USDJPY:OANDA"],
                "Average Volume (10 day Calc)": [500000, 1500000, 2000000],
            }
        )

        result = screener._apply_volume_filter(mock_df, screener.config.volume_filter)

        assert len(result) == 2
        assert "GBPUSD" in result["Name"].values
        assert "USDJPY" in result["Name"].values

    def test_volume_filter_none_returns_original(self):
        screener = ForexOpportunityScreener(pairs=["EURUSD"], timeframes=["15"])

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Symbol": ["EURUSD:OANDA"],
                "Average Volume (10 day Calc)": [500000],
            }
        )

        result = screener._apply_volume_filter(mock_df, VolumeFilter(min_volume=None))

        assert len(result) == 1

    def test_volume_filter_empty_dataframe(self):
        screener = ForexOpportunityScreener(
            pairs=["EURUSD"],
            timeframes=["15"],
            config=ForexScreenerConfig(volume_filter=VolumeFilter(min_volume=1000000)),
        )

        mock_df = pd.DataFrame()
        result = screener._apply_volume_filter(mock_df, screener.config.volume_filter)

        assert len(result) == 0


class TestRatingFilter:
    def test_rating_filter_keeps_above_threshold(self):
        screener = ForexOpportunityScreener(
            pairs=["EURUSD"],
            timeframes=["15"],
            config=ForexScreenerConfig(
                rating_filters=(RatingFilter(rating_type="all", threshold=0.5),)
            ),
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD", "GBPUSD", "USDJPY"],
                "Symbol": ["EURUSD:OANDA", "GBPUSD:OANDA", "USDJPY:OANDA"],
                "Recommend All|15": [0.8, 0.3, -0.5],
            }
        )

        result = screener._apply_rating_filter(mock_df, screener.config.rating_filters[0])

        assert len(result) == 1
        assert result.iloc[0]["Name"] == "EURUSD"

    def test_rating_filter_empty_dataframe(self):
        screener = ForexOpportunityScreener(
            pairs=["EURUSD"],
            timeframes=["15"],
            config=ForexScreenerConfig(
                rating_filters=(RatingFilter(rating_type="all", threshold=0.5),)
            ),
        )

        mock_df = pd.DataFrame()
        result = screener._apply_rating_filter(mock_df, screener.config.rating_filters[0])

        assert len(result) == 0


class TestRocFilter:
    def test_roc_filter_min_roc(self):
        screener = ForexOpportunityScreener(
            pairs=["EURUSD"],
            timeframes=["15"],
            config=ForexScreenerConfig(roc_filter=RocFilter(min_roc=1.0)),
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD", "GBPUSD", "USDJPY"],
                "Symbol": ["EURUSD:OANDA", "GBPUSD:OANDA", "USDJPY:OANDA"],
                "Roc|15": [1.5, 0.5, -0.5],
            }
        )

        result = screener._apply_roc_filter(mock_df, screener.config.roc_filter)

        assert len(result) == 1
        assert result.iloc[0]["Name"] == "EURUSD"

    def test_roc_filter_max_roc(self):
        screener = ForexOpportunityScreener(
            pairs=["EURUSD"],
            timeframes=["15"],
            config=ForexScreenerConfig(roc_filter=RocFilter(max_roc=1.0)),
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD", "GBPUSD", "USDJPY"],
                "Symbol": ["EURUSD:OANDA", "GBPUSD:OANDA", "USDJPY:OANDA"],
                "Roc|15": [1.5, 0.5, -0.5],
            }
        )

        result = screener._apply_roc_filter(mock_df, screener.config.roc_filter)

        assert len(result) == 2

    def test_roc_filter_empty_dataframe(self):
        screener = ForexOpportunityScreener(
            pairs=["EURUSD"],
            timeframes=["15"],
            config=ForexScreenerConfig(roc_filter=RocFilter(min_roc=1.0)),
        )

        mock_df = pd.DataFrame()
        result = screener._apply_roc_filter(mock_df, screener.config.roc_filter)

        assert len(result) == 0


class TestExportMethod:
    def test_export_csv_format(self, tmp_path):
        screener = ForexOpportunityScreener(pairs=["EURUSD"], timeframes=["15"])

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Price": [1.0850],
                "RATING_SCORE": [0.5],
                "ROC_AVG": [0.25],
            }
        )

        screener._cached_data = mock_df

        output_path = tmp_path / "test_export.csv"
        screener.export(str(output_path), "csv", include_index=False)

        assert output_path.exists()
        content = output_path.read_text()
        assert "EURUSD" in content

    def test_export_json_format(self, tmp_path):
        screener = ForexOpportunityScreener(pairs=["EURUSD"], timeframes=["15"])

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Price": [1.0850],
            }
        )

        screener._cached_data = mock_df

        output_path = tmp_path / "test_export.json"
        screener.export(str(output_path), "json", orient="records")

        assert output_path.exists()

    def test_export_invalid_format_raises(self, tmp_path):
        screener = ForexOpportunityScreener(pairs=["EURUSD"], timeframes=["15"])

        mock_df = pd.DataFrame({"Name": ["EURUSD"]})
        screener._cached_data = mock_df

        output_path = tmp_path / "test_export.xyz"

        with pytest.raises(ValueError, match="Unknown export format"):
            screener.export(str(output_path), "xyz")

    def test_export_with_metadata(self, tmp_path):
        screener = ForexOpportunityScreener(pairs=["EURUSD"], timeframes=["15"])

        mock_df = pd.DataFrame({"Name": ["EURUSD"], "Price": [1.0850]})
        screener._cached_data = mock_df

        output_path = tmp_path / "test_export.csv"
        metadata = {"pairs": ["EURUSD"], "timeframes": ["15"]}
        screener.export(str(output_path), "csv", include_index=False, metadata=metadata)

        assert output_path.exists()
        content = output_path.read_text()
        assert "# pairs" in content


class TestContractTypeFilter:
    def test_contract_type_cfd_only(self):
        screener = ForexOpportunityScreener(
            pairs=["EURUSD"],
            timeframes=["15"],
            config=ForexScreenerConfig(contract_type="cfd"),
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD", "GBPUSD"],
                "Subtype": ["cfd", "spot"],
            }
        )

        result = screener._apply_contract_type_filter(mock_df)

        assert len(result) == 1
        assert result.iloc[0]["Name"] == "EURUSD"

    def test_contract_type_all_returns_all(self):
        screener = ForexOpportunityScreener(
            pairs=["EURUSD"],
            timeframes=["15"],
            config=ForexScreenerConfig(contract_type="all"),
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD", "GBPUSD"],
                "Subtype": ["cfd", "spot"],
            }
        )

        result = screener._apply_contract_type_filter(mock_df)

        assert len(result) == 2


class TestEdgeCases:
    def test_empty_dataframe_operations(self):
        screener = ForexOpportunityScreener(pairs=["EURUSD"], timeframes=["15"])

        mock_df = pd.DataFrame()

        result = screener._apply_rating_and_roc_filters(mock_df)

        assert len(result) == 0

    def test_missing_volume_column(self):
        screener = ForexOpportunityScreener(pairs=["EURUSD"], timeframes=["15"])

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Symbol": ["EURUSD:OANDA"],
            }
        )

        result = screener._apply_volume_filter(mock_df, VolumeFilter(min_volume=1000000))

        assert len(result) == 1

    def test_null_rating_values_treated_as_neutral(self):
        screener = ForexOpportunityScreener(
            pairs=["EURUSD"],
            timeframes=["15"],
            config=ForexScreenerConfig(
                rating_filters=(RatingFilter(rating_type="all", threshold=0.5),)
            ),
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Symbol": ["EURUSD:OANDA"],
                "Recommend All|15": [None],
            }
        )

        result = screener._apply_rating_filter(mock_df, screener.config.rating_filters[0])

        assert len(result) == 0
