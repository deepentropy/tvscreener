"""Tests for risk management utilities."""

from tvscreener.lib.screeners.risk_utils import (
    calculate_position_size,
    calculate_risk_reward_ratio,
    calculate_stop_loss,
    calculate_take_profit,
    calculate_volume_roc,
    check_signal_quality,
    check_volume_spike,
)


class TestStopLoss:
    def test_long_stop_loss(self):
        result = calculate_stop_loss(100.0, "long", 0.5, 2.0)
        assert result == 99.0

    def test_short_stop_loss(self):
        result = calculate_stop_loss(100.0, "short", 0.5, 2.0)
        assert result == 101.0

    def test_none_atr_returns_entry(self):
        result = calculate_stop_loss(100.0, "long", None, 2.0)
        assert result == 100.0


class TestTakeProfit:
    def test_long_take_profit(self):
        result = calculate_take_profit(100.0, 98.0, "long", 2.0)
        assert result == 104.0

    def test_short_take_profit(self):
        result = calculate_take_profit(100.0, 102.0, "short", 2.0)
        assert result == 96.0


class TestPositionSize:
    def test_basic_calculation(self):
        result = calculate_position_size(10000, 0.01, 0.02, 10)
        assert result == 500.0

    def test_zero_stop_distance(self):
        result = calculate_position_size(10000, 0.01, 0, 10)
        assert result == 0.0


class TestRiskRewardRatio:
    def test_risk_reward_calculation(self):
        result = calculate_risk_reward_ratio(100.0, 98.0, 104.0)
        assert result == 2.0


class TestVolumeROC:
    def test_above_average_volume(self):
        result = calculate_volume_roc(1500, 1000)
        assert result == 1.5

    def test_below_average_volume(self):
        result = calculate_volume_roc(500, 1000)
        assert result == 0.5


class TestVolumeSpike:
    def test_spike_detected(self):
        assert check_volume_spike(1.6, 1.5) is True

    def test_no_spike(self):
        assert check_volume_spike(1.2, 1.5) is False


class TestSignalQuality:
    def test_valid_signal(self):
        valid, reason = check_signal_quality(
            confluence_score=4,
            tf_alignment=3,
            roc_aligned=True,
            rvol=1.5,
            min_confluence=3,
            min_tf_alignment=2,
            min_rvol=1.0,
        )
        assert valid is True

    def test_low_confluence(self):
        valid, reason = check_signal_quality(
            confluence_score=2, tf_alignment=3, roc_aligned=True, min_confluence=3
        )
        assert valid is False
        assert "Confluence" in reason

    def test_low_tf_alignment(self):
        valid, reason = check_signal_quality(
            confluence_score=4, tf_alignment=1, roc_aligned=True, min_tf_alignment=2
        )
        assert valid is False
        assert "TF alignment" in reason

    def test_roc_not_aligned(self):
        valid, reason = check_signal_quality(confluence_score=4, tf_alignment=3, roc_aligned=False)
        assert valid is False
        assert "ROC" in reason

    def test_low_volume(self):
        valid, reason = check_signal_quality(
            confluence_score=4, tf_alignment=3, roc_aligned=True, rvol=0.8, min_rvol=1.2
        )
        assert valid is False
        assert "RVOL" in reason
