from __future__ import annotations

from dataclasses import dataclass

from tvscreener.constants.forex import (
    DEFAULT_FOREX_PAIRS,
    DEFAULT_TIMEFRAME_WEIGHTS,
    DEFAULT_TIMEFRAMES,
    LIQUID_EXCHANGES,
)


@dataclass(frozen=True, slots=True)
class IndicatorFields:
    """Field patterns for indicators - uses {tf} placeholder."""

    recommend_all: str = "Recommend All|{tf}"
    recommend_ma: str = "Recommend Ma|{tf}"
    recommend_osc: str = "Recommend Other|{tf}"
    momentum: str = "Roc|{tf}"


class ConfigurationError(Exception):
    """Raised when asset configuration is invalid."""

    pass


@dataclass(frozen=True, slots=True)
class AssetUniverse:
    """Asset configuration - immutable and memory-efficient.

    Use this class to configure an asset type for the universal screener.
    """

    name: str
    pairs: list[str]
    timeframes: list[str]
    default_tf_weights: dict[str, float]
    fields: IndicatorFields
    exchanges: list[str] | None = None
    core_class_name: str = "ForexScreener"
    field_class_name: str = "ForexField"

    def validate(self) -> None:
        """Validate configuration at instantiation."""
        if not self.pairs:
            raise ConfigurationError("pairs cannot be empty")
        if not self.timeframes:
            raise ConfigurationError("timeframes cannot be empty")
        total_weight = sum(self.default_tf_weights.values())
        if not 0.99 <= total_weight <= 1.01:
            raise ConfigurationError(f"timeframe weights must sum to 1.0, got {total_weight}")


FOREX_UNIVERSE = AssetUniverse(
    name="forex",
    pairs=DEFAULT_FOREX_PAIRS,
    timeframes=DEFAULT_TIMEFRAMES,
    default_tf_weights=DEFAULT_TIMEFRAME_WEIGHTS,
    fields=IndicatorFields(),
    exchanges=LIQUID_EXCHANGES,
    core_class_name="ForexScreener",
    field_class_name="ForexField",
)
FOREX_UNIVERSE.validate()
