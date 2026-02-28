from typing import Literal

from pydantic import ConfigDict, Field, field_validator
from pydantic_settings import BaseSettings


class ScreenerSettings(BaseSettings):
    """Layered settings: YAML → ENV → CLI (CLI handled separately)"""

    model_config = ConfigDict(
        env_file=".env", env_file_encoding="utf-8", env_prefix="TVSCREENER_", extra="ignore"
    )

    min_volume: float | None = Field(default=None, ge=0)
    max_atr: float | None = Field(default=None, ge=0)
    min_ma_rating: float | None = Field(default=None, ge=-2, le=2)
    min_confluence: int = Field(default=1, ge=1)
    trend_threshold: float = Field(default=0.2, ge=-1, le=1)
    mr_threshold: float = Field(default=0.2, ge=0, le=1)
    min_roc: float | None = Field(default=None, ge=0)

    default_universe: str = Field(default="all")
    default_timeframes: str = Field(default="240,60,15")
    contract_type: Literal["spot", "cfd", "spreadbet", "all"] = Field(default="cfd")

    opportunity_min_volume: float | None = Field(default=None, ge=0)
    opportunity_max_atr: float | None = Field(default=None, ge=0)
    opportunity_min_ma_rating: float | None = Field(default=None, ge=-2, le=2)
    opportunity_trend_weight: float = Field(default=0.4, ge=0, le=1)
    opportunity_ma_weight: float = Field(default=0.3, ge=0, le=1)
    opportunity_osc_weight: float = Field(default=0.2, ge=0, le=1)
    opportunity_roc_weight: float = Field(default=0.1, ge=0, le=1)
    opportunity_timeframe_weights: str = Field(default="240:0.2,60:0.3,15:0.5")

    @field_validator("min_ma_rating", "max_atr", "min_volume", "min_roc", mode="before")
    @classmethod
    def empty_string_to_none(cls, v):
        if v == "" or v == "null" or v == "None":
            return None
        return v

    @field_validator("default_timeframes", mode="before")
    @classmethod
    def parse_timeframes(cls, v):
        if isinstance(v, list):
            return ",".join(str(x) for x in v)
        return v

    def get_timeframes_list(self) -> list[str]:
        return self.default_timeframes.split(",")

    def get_opportunity_timeframe_weights(self) -> dict[str, float]:
        entries = self.opportunity_timeframe_weights.split(",")
        weights: dict[str, float] = {}
        for entry in entries:
            if not entry:
                continue
            key, sep, value = entry.partition(":")
            if sep and value:
                try:
                    weights[key.strip()] = float(value)
                except ValueError:
                    continue
        return weights

    @field_validator("default_universe", mode="before")
    @classmethod
    def validate_universe(cls, v):
        if v and isinstance(v, str):
            return v.lower().strip()
        return v

    @field_validator("opportunity_timeframe_weights", mode="before")
    @classmethod
    def validate_opportunity_timeframes(cls, v):
        if isinstance(v, list):
            return ",".join(str(x) for x in v)
        return v

    # Risk Management Settings
    min_tf_alignment: int = Field(default=2, ge=1, le=3)
    require_momentum: bool = Field(default=False)
    min_rvol: float = Field(default=1.0, ge=0.0)
    require_volume_spike: bool = Field(default=False)
    volume_spike_threshold: float = Field(default=1.5, ge=1.0)

    risk_per_trade: float = Field(default=1.0, ge=0.1, le=10.0)
    max_daily_loss: float = Field(default=3.0, ge=0.1, le=20.0)
    max_drawdown: float = Field(default=6.0, ge=0.1, le=30.0)
    min_risk_reward: float = Field(default=1.5, ge=0.5, le=5.0)
    atr_multiplier: float = Field(default=2.0, ge=0.5, le=5.0)

    account_balance: float = Field(default=10000.0, ge=100)
    pip_value: float = Field(default=10.0, ge=0.01)

    @field_validator("require_momentum", "require_volume_spike", mode="before")
    @classmethod
    def parse_bool(cls, v):
        if isinstance(v, bool):
            return v
        if isinstance(v, str):
            return v.lower() in ("true", "1", "yes")
        return bool(v)
