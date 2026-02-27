import pandas as pd
import pytest

from tvscreener.lib.screeners.forex_strategy import (
    ForexStrategyScanner,
    StrategyConfig,
)


class TestTrendFollowingDetection:
    def test_trend_following_both_bullish(self):
        scanner = ForexStrategyScanner(
            pairs=["EURUSD"],
            timeframes=["240", "60"],
            config=StrategyConfig(trend_threshold=0.0),
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Recommend All|240": [0.8],
                "Recommend All|60": [0.6],
            }
        )

        result = scanner._detect_trend_following(mock_df)

        assert len(result) == 1
        assert result.iloc[0]["STRATEGY"] == "trend_following"
        assert result.iloc[0]["DIRECTION"] == "long"

    def test_trend_following_both_bearish(self):
        scanner = ForexStrategyScanner(
            pairs=["EURUSD"],
            timeframes=["240", "60"],
            config=StrategyConfig(trend_threshold=0.0),
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Recommend All|240": [-0.8],
                "Recommend All|60": [-0.6],
            }
        )

        result = scanner._detect_trend_following(mock_df)

        assert len(result) == 1
        assert result.iloc[0]["DIRECTION"] == "short"

    def test_trend_following_mixed_returns_empty(self):
        scanner = ForexStrategyScanner(
            pairs=["EURUSD"],
            timeframes=["240", "60"],
            config=StrategyConfig(trend_threshold=0.0),
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Recommend All|240": [0.8],
                "Recommend All|60": [-0.6],
            }
        )

        result = scanner._detect_trend_following(mock_df)

        assert len(result) == 0

    def test_trend_following_3tf_all_aligned_long(self):
        scanner = ForexStrategyScanner(
            pairs=["EURUSD"],
            timeframes=["240", "60", "15"],
            config=StrategyConfig(trend_threshold=0.0),
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Recommend All|240": [0.8],
                "Recommend All|60": [0.6],
                "Recommend All|15": [0.4],
            }
        )

        result = scanner._detect_trend_following(mock_df)

        assert len(result) == 1
        assert result.iloc[0]["CONFLUENCE_SCORE"] == 3
        assert result.iloc[0]["DIRECTION"] == "long"

    def test_trend_following_3tf_all_aligned_short(self):
        scanner = ForexStrategyScanner(
            pairs=["EURUSD"],
            timeframes=["240", "60", "15"],
            config=StrategyConfig(trend_threshold=0.0),
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Recommend All|240": [-0.8],
                "Recommend All|60": [-0.6],
                "Recommend All|15": [-0.4],
            }
        )

        result = scanner._detect_trend_following(mock_df)

        assert len(result) == 1
        assert result.iloc[0]["CONFLUENCE_SCORE"] == 3
        assert result.iloc[0]["DIRECTION"] == "short"

    def test_trend_following_3tf_ltf_diverges_filtered(self):
        scanner = ForexStrategyScanner(
            pairs=["EURUSD"],
            timeframes=["240", "60", "15"],
            config=StrategyConfig(trend_threshold=0.0),
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Recommend All|240": [0.8],
                "Recommend All|60": [0.6],
                "Recommend All|15": [-0.4],
            }
        )

        result = scanner._detect_trend_following(mock_df)

        assert len(result) == 0

    def test_trend_following_threshold_filters_weak_signals(self):
        scanner = ForexStrategyScanner(
            pairs=["EURUSD"],
            timeframes=["240", "60", "15"],
            config=StrategyConfig(trend_threshold=0.3),
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Recommend All|240": [0.2],
                "Recommend All|60": [0.1],
                "Recommend All|15": [0.1],
            }
        )

        result = scanner._detect_trend_following(mock_df)

        assert len(result) == 0

    def test_trend_following_missing_15m_fallback(self):
        scanner = ForexStrategyScanner(
            pairs=["EURUSD"],
            timeframes=["240", "60", "15"],
            config=StrategyConfig(trend_threshold=0.0),
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Recommend All|240": [0.8],
                "Recommend All|60": [0.6],
            }
        )

        result = scanner._detect_trend_following(mock_df)

        assert len(result) == 1
        assert result.iloc[0]["CONFLUENCE_SCORE"] == 2


class TestMeanReversionDetection:
    def test_mean_reversion_oversold(self):
        scanner = ForexStrategyScanner(
            pairs=["EURUSD"],
            timeframes=["240", "60", "15"],
            config=StrategyConfig(mr_threshold=0.2),
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Recommend All|240": [0.5],
                "Recommend Other|15": [-0.5],
            }
        )

        result = scanner._detect_mean_reversion(mock_df)

        assert len(result) == 1
        assert result.iloc[0]["STRATEGY"] == "mean_reversion"
        assert result.iloc[0]["DIRECTION"] == "long"

    def test_mean_reversion_overbought(self):
        scanner = ForexStrategyScanner(
            pairs=["EURUSD"],
            timeframes=["240", "60", "15"],
            config=StrategyConfig(mr_threshold=0.2),
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Recommend All|240": [-0.5],
                "Recommend Other|15": [0.5],
            }
        )

        result = scanner._detect_mean_reversion(mock_df)

        assert len(result) == 1
        assert result.iloc[0]["DIRECTION"] == "short"

    def test_mean_reversion_conflicting_returns_empty(self):
        scanner = ForexStrategyScanner(
            pairs=["EURUSD"],
            timeframes=["240", "60", "15"],
            config=StrategyConfig(mr_threshold=0.2),
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Recommend All|240": [0.5],
                "Recommend Other|15": [0.5],
            }
        )

        result = scanner._detect_mean_reversion(mock_df)

        assert len(result) == 0

    def test_mean_reversion_below_threshold_returns_empty(self):
        scanner = ForexStrategyScanner(
            pairs=["EURUSD"],
            timeframes=["240", "60", "15"],
            config=StrategyConfig(mr_threshold=0.5),
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Recommend All|240": [0.5],
                "Recommend Other|15": [0.2],
            }
        )

        result = scanner._detect_mean_reversion(mock_df)

        assert len(result) == 0


class TestBreakoutDetection:
    def test_breakout_all_positive(self):
        scanner = ForexStrategyScanner(
            pairs=["EURUSD"],
            timeframes=["240", "60", "15"],
            config=StrategyConfig(min_roc=None),
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Roc|240": [1.5],
                "Roc|60": [1.2],
                "Roc|15": [0.8],
            }
        )

        result = scanner._detect_breakout(mock_df)

        assert len(result) == 1
        assert result.iloc[0]["STRATEGY"] == "breakout"
        assert result.iloc[0]["DIRECTION"] == "long"

    def test_breakout_with_min_roc_filter(self):
        scanner = ForexStrategyScanner(
            pairs=["EURUSD"],
            timeframes=["240", "60", "15"],
            config=StrategyConfig(min_roc=1.0),
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Roc|240": [1.5],
                "Roc|60": [0.8],
                "Roc|15": [0.5],
            }
        )

        result = scanner._detect_breakout(mock_df)

        assert len(result) == 0

    def test_breakout_no_roc_columns_returns_empty(self):
        scanner = ForexStrategyScanner(
            pairs=["EURUSD"],
            timeframes=["240", "60", "15"],
            config=StrategyConfig(),
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
            }
        )

        result = scanner._detect_breakout(mock_df)

        assert len(result) == 0


class TestHybridDetection:
    def test_hybrid_bullish_trend_with_oversold_oscillator(self):
        scanner = ForexStrategyScanner(
            pairs=["EURUSD"],
            timeframes=["240", "15"],
            config=StrategyConfig(trend_threshold=0.0, mr_threshold=0.2),
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Recommend All|240": [0.8],
                "Recommend Other|15": [-0.5],
            }
        )

        result = scanner._detect_hybrid(mock_df)

        assert len(result) == 1
        assert result.iloc[0]["STRATEGY"] == "hybrid"
        assert result.iloc[0]["DIRECTION"] == "long"
        assert result.iloc[0]["CONFLUENCE_SCORE"] == 2


class TestConfluenceScoring:
    def test_confluence_score_calculation(self):
        scanner = ForexStrategyScanner(
            pairs=["EURUSD"],
            timeframes=["240", "60"],
            config=StrategyConfig(),
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Recommend All|240": [0.8],
                "Recommend All|60": [0.6],
            }
        )

        result = scanner._detect_trend_following(mock_df)

        assert "CONFLUENCE_SCORE" in result.columns
        assert result.iloc[0]["CONFLUENCE_SCORE"] >= 1


class TestDirectionFilter:
    def test_direction_filter_long_only(self):
        scanner = ForexStrategyScanner(
            pairs=["EURUSD", "GBPUSD"],
            timeframes=["240", "60"],
            config=StrategyConfig(direction="long"),
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD", "GBPUSD"],
                "Recommend All|240": [0.8, -0.8],
                "Recommend All|60": [0.6, -0.6],
                "STRATEGY": ["trend_following", "trend_following"],
                "HTF_TREND": [0.8, -0.8],
                "STF_TREND": [0.6, -0.6],
                "CONFLUENCE_SCORE": [2, 2],
                "DIRECTION": ["long", "short"],
            }
        )

        result = scanner._apply_filters(mock_df)

        assert len(result) == 1
        assert result.iloc[0]["Name"] == "EURUSD"


class TestExportMethod:
    def test_export_csv(self, tmp_path):
        scanner = ForexStrategyScanner(pairs=["EURUSD"], timeframes=["240"])

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "STRATEGY": ["trend_following"],
                "DIRECTION": ["long"],
                "CONFLUENCE_SCORE": [2],
            }
        )

        scanner._cached_results = mock_df

        output_path = tmp_path / "test_export.csv"
        scanner.export(str(output_path), "csv", include_index=False)

        assert output_path.exists()
        content = output_path.read_text()
        assert "EURUSD" in content

    def test_export_json(self, tmp_path):
        scanner = ForexStrategyScanner(pairs=["EURUSD"], timeframes=["240"])

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "STRATEGY": ["trend_following"],
            }
        )

        scanner._cached_results = mock_df

        output_path = tmp_path / "test_export.json"
        scanner.export(str(output_path), "json", orient="records")

        assert output_path.exists()

    def test_export_invalid_format_raises(self, tmp_path):
        scanner = ForexStrategyScanner(pairs=["EURUSD"], timeframes=["240"])

        mock_df = pd.DataFrame({"Name": ["EURUSD"]})
        scanner._cached_results = mock_df

        output_path = tmp_path / "test.xyz"

        with pytest.raises(ValueError, match="Unknown export format"):
            scanner.export(str(output_path), "xyz")


class TestEdgeCases:
    def test_no_signals_returns_empty(self):
        scanner = ForexStrategyScanner(
            pairs=["EURUSD"],
            timeframes=["240", "60"],
            config=StrategyConfig(trend_threshold=10.0),
        )

        mock_df = pd.DataFrame(
            {
                "Name": ["EURUSD"],
                "Recommend All|240": [0.1],
                "Recommend All|60": [0.1],
            }
        )

        result = scanner._detect_trend_following(mock_df)

        assert len(result) == 0

    def test_empty_dataframe_returns_empty(self):
        scanner = ForexStrategyScanner(
            pairs=["EURUSD"],
            timeframes=["240", "60"],
            config=StrategyConfig(),
        )

        mock_df = pd.DataFrame()

        result = scanner._detect_trend_following(mock_df)

        assert len(result) == 0
