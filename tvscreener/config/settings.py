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
