"""Risk management utilities for forex trading."""

from dataclasses import dataclass
from typing import Literal

Direction = Literal["long", "short"]


@dataclass(frozen=True)
class RiskConfig:
    """Risk management configuration."""

    account_balance: float = 10000.0
    risk_per_trade_pct: float = 1.0
    max_daily_loss_pct: float = 3.0
    max_drawdown_pct: float = 6.0
    min_risk_reward_ratio: float = 1.5
    atr_multiplier: float = 2.0
    default_pip_value: float = 10.0


def calculate_stop_loss(
    entry: float, direction: Direction, atr: float, multiplier: float = 2.0
) -> float:
    """Calculate ATR-based stop loss.

    Args:
        entry: Entry price
        direction: Trade direction (long/short)
        atr: Average True Range value
        multiplier: ATR multiplier for stop distance

    Returns:
        Stop loss price level
    """
    if atr is None or atr <= 0:
        return entry
    sl_distance = atr * multiplier
    if direction == "long":
        return entry - sl_distance
    return entry + sl_distance


def calculate_take_profit(
    entry: float, stop_loss: float, direction: Direction, min_rr: float = 2.0
) -> float:
    """Calculate take profit based on R:R ratio.

    Args:
        entry: Entry price
        stop_loss: Stop loss price
        direction: Trade direction (long/short)
        min_rr: Minimum risk:reward ratio

    Returns:
        Take profit price level
    """
    if stop_loss is None or entry is None:
        return entry
    risk = abs(entry - stop_loss)
    reward = risk * min_rr
    if direction == "long":
        return entry + reward
    return entry - reward


def calculate_position_size(
    account_balance: float, risk_per_trade: float, stop_distance: float, pip_value: float = 10.0
) -> float:
    """Calculate position size in lots.

    Args:
        account_balance: Account balance in currency units
        risk_per_trade: Risk per trade as decimal (e.g., 0.01 for 1%)
        stop_distance: Stop loss distance in price terms
        pip_value: Value per pip/lot (default 10 for standard lots)

    Returns:
        Position size in lots
    """
    if stop_distance <= 0:
        return 0.0
    risk_amount = account_balance * risk_per_trade
    return risk_amount / (stop_distance * pip_value)


def calculate_risk_reward_ratio(entry: float, stop_loss: float, take_profit: float) -> float:
    """Calculate risk:reward ratio.

    Args:
        entry: Entry price
        stop_loss: Stop loss price
        take_profit: Take profit price

    Returns:
        Risk:reward ratio
    """
    if stop_loss is None or take_profit is None or entry is None:
        return 0.0
    risk = abs(entry - stop_loss)
    reward = abs(take_profit - entry)
    if risk <= 0:
        return 0.0
    return reward / risk


def calculate_volume_roc(current_volume: float, average_volume: float) -> float:
    """Calculate volume rate of change.

    Args:
        current_volume: Current period volume
        average_volume: Historical average volume

    Returns:
        Volume ROC as multiplier (e.g., 1.5 = 50% above average)
    """
    if average_volume is None or average_volume <= 0:
        return 1.0
    return current_volume / average_volume


def check_volume_spike(rvol: float, threshold: float = 1.5) -> bool:
    """Check if volume is above spike threshold.

    Args:
        rvol: Relative volume (1.0 = average)
        threshold: Minimum threshold for spike (default 1.5)

    Returns:
        True if volume is a spike
    """
    return rvol is not None and rvol >= threshold


def check_signal_quality(
    confluence_score: int,
    tf_alignment: int,
    roc_aligned: bool,
    rvol: float | None = None,
    min_confluence: int = 3,
    min_tf_alignment: int = 2,
    min_rvol: float = 1.0,
) -> tuple[bool, str]:
    """Validate if signal meets quality thresholds.

    Args:
        confluence_score: Current confluence score
        tf_alignment: Number of aligned timeframes
        roc_aligned: Whether ROC aligns with direction
        rvol: Relative volume
        min_confluence: Minimum required confluence
        min_tf_alignment: Minimum required TF alignment
        min_rvol: Minimum required RVOL

    Returns:
        Tuple of (is_valid, reason)
    """
    if confluence_score < min_confluence:
        return False, f"Confluence {confluence_score} < {min_confluence}"

    if tf_alignment < min_tf_alignment:
        return False, f"TF alignment {tf_alignment} < {min_tf_alignment}"

    if not roc_aligned:
        return False, "ROC opposes direction"

    if rvol is not None and rvol < min_rvol:
        return False, f"RVOL {rvol:.2f} < {min_rvol}"

    return True, "Signal valid"
