---
title: Enhance strategy screeners with volume, volatility, and MA filters
type: feat
date: 2026-02-23
---

# Enhance Strategy Screeners

## Overview

Add enhanced filtering capabilities to the strategy screeners with CLI-configurable thresholds for volume, volatility, and MA ratings. Also add mean reversion signal detection. Includes layered configuration system with YAML → ENV → CLI priority.

## Problem Statement

Current strategy screeners detect patterns but lack quantitative filters to improve signal quality. Users need configurable filters to:
- Filter illiquid pairs with volume thresholds
- Exclude extreme volatility
- Require strong MA alignment
- Detect mean reversion conditions

## Configuration Architecture

### Layered Settings Priority (Low → High)

```
1. Code Defaults (lowest)
2. YAML config file (tvscreener.yaml)
3. Environment variables (.env or shell)
4. CLI arguments (highest)
```

### Dependencies

```toml
# pyproject.toml
pydantic-settings = "^2.0.0"
pyyaml = "^6.0.0"
python-dotenv = "^1.0.0"
```

### Settings Module (`tvscreener/config/settings.py`)

```python
from pydantic import Field, field_validator, ConfigDict
from pydantic_settings import BaseSettings
from typing import Literal

# Sentinel for CLI args (distinguishes "not provided" from "provided None/0")
_UNSET = object()

class ScreenerSettings(BaseSettings):
    """Layered settings: YAML → ENV → CLI (CLI handled separately)"""
    
    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="TVSCREENER_",
        extra="ignore"
    )
    
    # Strategy settings (with validation)
    min_volume: float | None = Field(default=None, ge=0)
    max_atr: float | None = Field(default=None, ge=0)
    min_ma_rating: float | None = Field(default=None, ge=-2, le=2)
    min_confluence: int = Field(default=1, ge=1)
    trend_threshold: float = Field(default=0.0, ge=-1, le=1)
    mr_threshold: float = Field(default=0.2, ge=0, le=1)
    min_roc: float | None = Field(default=None, ge=0)
    
    # Global defaults
    default_universe: str = Field(default="all")
    default_timeframes: str = Field(default="240,60,15")  # Comma-separated string
    contract_type: Literal["spot", "cfd", "spreadbet", "all"] = Field(default="cfd")
    
    @field_validator("min_ma_rating", "max_atr", "min_volume", "min_roc", mode="before")
    @classmethod
    def empty_string_to_none(cls, v):
        """Convert empty strings to None for CLI compatibility."""
        if v == "" or v == "null" or v == "None":
            return None
        return v
    
    @field_validator("default_timeframes", mode="before")
    @classmethod
    def parse_timeframes(cls, v):
        """Parse comma-separated timeframes from ENV/YAML."""
        if isinstance(v, list):
            return ",".join(str(x) for x in v)
        return v
    
    def get_timeframes_list(self) -> list[str]:
        """Return timeframes as list."""
        return self.default_timeframes.split(",")
    
    @field_validator("default_universe", mode="before")
    @classmethod
    def validate_universe(cls, v):
        """Normalize universe names."""
        if v and isinstance(v, str):
            return v.lower().strip()
        return v
```

### YAML Config (`tvscreener.yaml`)

```yaml
# tvscreener.yaml - committed to repo
# Flat structure (no nesting) for simplicity

# Global defaults
default_universe: "majors"
default_timeframes: "240,60,15"
contract_type: "cfd"

# Strategy settings
min_confluence: 1
trend_threshold: 0.0
mr_threshold: 0.2
min_volume: null
max_atr: null
min_ma_rating: null
min_roc: null
```

### Environment File (`.env.example` - gitignored)

```bash
# .env.example - template for users
# Copy to .env and customize

# Strategy filters
TVSCREENER_MIN_VOLUME=500000
TVSCREENER_MAX_ATR=2.0
TVSCREENER_MIN_MA_RATING=0.5

# Global defaults
TVSCREENER_DEFAULT_UNIVERSE=majors
TVSCREENER_DEFAULT_TIMEFRAMES=240,60,15
TVSCREENER_CONTRACT_TYPE=cfd
```

### CLI Usage Examples

```bash
# Use all defaults from YAML
uv run python -m tvscreener.cli -u majors

# Override with env vars (in .env or shell)
export TVSCREENER_MIN_VOLUME=500000
uv run python -m tvscreener.cli -u majors

# Override with CLI args (highest priority)
uv run python -m tvscreener.cli -u majors --min-volume 1000000
uv run python -m tvscreener.cli -u majors --min-volume 100000 --max-atr 1.5
uv run python -m tvscreener.cli -u minors --strategy trend --min-volume 500000 --min-ma-rating 0.5
```

## Proposed Solution

### 1. Extend StrategyConfig

```python
from dataclasses import dataclass, field
from typing import Literal

@dataclass(frozen=True, slots=True)
class StrategyConfig:
    # existing fields
    min_confluence: int = 1
    include_strategies: tuple[StrategyType, ...] = ("all",)
    direction: Direction = "all"
    trend_threshold: float = 0.0
    mr_threshold: float = 0.2
    min_roc: float | None = None
    
    # new fields
    min_volume: float | None = None
    max_atr: float | None = None  # ATR as volatility proxy
    min_ma_rating: float | None = None
    mean_reversion_signals: tuple[str, ...] = ()
```

### 2. CLI Arguments

```bash
--min-volume VOLUME          # Minimum average volume (default: from settings)
--max-atr VALUE            # Maximum ATR value as volatility proxy (default: from settings)
--min-ma-rating RATING     # Minimum MA rating -2 to 2 (default: from settings)
--mr-signal SIGNAL         # Mean reversion signal (rsi_oversold, rsi_overbought)
--config FILE              # Custom YAML config path (default: tvscreener.yaml)
```

### 3. Filter Methods

Add to `ForexStrategyScanner`:

```python
def _apply_volume_filter(df, min_volume):
    """Filter by minimum average volume."""
    if min_volume is None:
        return df
    vol_col = "Average Volume (10 day Calc)"
    if vol_col in df.columns:
        return df[df[vol_col] >= min_volume].copy()
    return df

def _apply_atr_filter(df, max_atr):
    """Filter by maximum ATR (volatility proxy)."""
    if max_atr is None:
        return df
    atr_cols = [c for c in df.columns if c.startswith("ATR|")]
    if atr_cols:
        df = df.copy()
        df["_atr_avg"] = df[atr_cols].mean(axis=1)
        result = df[df["_atr_avg"] <= max_atr].copy()
        return result.drop(columns=["_atr_avg"], errors="ignore")
    return df

def _apply_ma_rating_filter(df, min_ma_rating):
    """Filter by minimum MA rating strength."""
    if min_ma_rating is None:
        return df
    ma_cols = [c for c in df.columns if c.startswith("Recommend Ma|")]
    if ma_cols:
        df = df.copy()
        df["_ma_avg"] = df[ma_cols].mean(axis=1)
        result = df[df["_ma_avg"] >= min_ma_rating].copy()
        return result.drop(columns=["_ma_avg"], errors="ignore")
    return df

def _detect_mean_reversion_signals(df, signals):
    """Add mean reversion signal columns.
    
    RSI oversold (<30) = long signal
    RSI overbought (>70) = short signal
    
    Uses vectorized operations for performance.
    """
    rsi_cols = [c for c in df.columns if c.startswith("RSI")]
    if not rsi_cols:
        return df
    
    df = df.copy()
    rsi_data = df[rsi_cols].fillna(50)
    
    if "rsi_oversold" in signals:
        # Vectorized: any timeframe below 30
        df["rsi_oversold"] = (rsi_data < 30).any(axis=1).astype(int)
    
    if "rsi_overbought" in signals:
        # Vectorized: any timeframe above 70
        df["rsi_overbought"] = (rsi_data > 70).any(axis=1).astype(int)
    
    return df
    
    df = df.copy()
    if "rsi_oversold" in signals:
        df["RSI_OVERSOLD"] = df[rsi_cols].fillna(50).apply(
            lambda x: bool((x < 30).any()), axis=1
        ).astype(int)
    
    if "rsi_overbought" in signals:
        df["RSI_OVERBOUGHT"] = df[rsi_cols].fillna(50).apply(
            lambda x: bool((x > 70).any()), axis=1
        ).astype(int)
    
    return df
```

### 4. Settings Loader Utility

```python
# tvscreener/config/loader.py
import argparse
import os
import yaml
from pathlib import Path
from typing import Any

from pydantic import ValidationError

from tvscreener.config.settings import ScreenerSettings

# Sentinel for CLI to distinguish "not provided" from "provided None/0"
_UNSET = argparse.Namespace()

DEFAULT_CONFIG_PATH = "tvscreener.yaml"

def load_yaml_config(config_path: str | None = None) -> dict[str, Any]:
    """Load configuration from YAML file."""
    path = config_path or DEFAULT_CONFIG_PATH
    
    if not Path(path).exists():
        return {}
    
    with open(path) as f:
        return yaml.safe_load(f) or {}

def load_settings(config_path: str | None = None) -> ScreenerSettings:
    """Load settings from YAML, then override with ENV variables."""
    yaml_config = load_yaml_config(config_path)
    
    # Merge YAML config into environment for pydantic-settings to pick up
    for key, value in yaml_config.items():
        if value is not None:
            env_key = f"TVSCREENER_{key.upper()}"
            if env_key not in os.environ:
                os.environ[env_key] = str(value)
    
    try:
        settings = ScreenerSettings()
        return settings
    except ValidationError as e:
        import logging
        logging.warning(f"Settings validation error: {e}. Using defaults.")
        return ScreenerSettings()

def merge_with_cli_args(
    settings: ScreenerSettings, 
    cli_args: argparse.Namespace
) -> dict[str, Any]:
    """Merge settings with CLI args (CLI takes precedence)."""
    config_dict = {}
    
    # All config fields to merge
    config_fields = [
        "min_volume", "max_atr", "min_ma_rating", "min_confluence",
        "trend_threshold", "mr_threshold", "min_roc", "contract_type",
        "default_universe", "default_timeframes"
    ]
    
    for field_name in config_fields:
        cli_value = getattr(cli_args, field_name, _UNSET)
        
        # CLI value provided (even if None or 0) takes precedence
        if cli_value is not _UNSET:
            if cli_value == "None" or cli_value == "null":
                cli_value = None
            config_dict[field_name] = cli_value
        else:
            settings_value = getattr(settings, field_name, None)
            if settings_value is not None:
                config_dict[field_name] = settings_value
    
    return config_dict
```

### 5. Update CLI

```python
from tvscreener.config.settings import ScreenerSettings
from tvscreener.config.loader import load_settings, merge_with_cli_args

def run_strategy_scan(args) -> int:
    # Load settings from YAML/ENV
    settings = load_settings(args.config)
    
    # Merge CLI args (highest priority)
    config_dict = merge_with_cli_args(settings, args)
    
    config = StrategyConfig(
        min_confluence=config_dict.get("min_confluence", 1),
        min_volume=config_dict.get("min_volume"),
        max_atr=config_dict.get("max_atr"),
        min_ma_rating=config_dict.get("min_ma_rating"),
        # ... other config
    )
    scanner = ForexStrategyScanner(pairs=pairs, timeframes=timeframes, config=config)
```

### 6. Update scan() Pipeline

```python
def scan(self) -> pd.DataFrame:
    raw_data = self._screener.get_opportunities()
    # ... existing strategy detection ...
    
    # Add new filters
    if self.config.min_volume:
        combined = self._apply_volume_filter(combined, self.config.min_volume)
    if self.config.max_atr:
        combined = self._apply_atr_filter(combined, self.config.max_atr)
    if self.config.min_ma_rating:
        combined = self._apply_ma_rating_filter(combined, self.config.min_ma_rating)
    if self.config.mean_reversion_signals:
        combined = self._detect_mean_reversion_signals(combined, self.config.mean_reversion_signals)
    
    return self._apply_filters(combined)
```

## Files to Create/Modify

| File | Action | Description |
|------|--------|-------------|
| `pyproject.toml` | Modify | Add pydantic-settings, pyyaml, python-dotenv |
| `tvscreener/config/__init__.py` | Create | Config package init |
| `tvscreener/config/settings.py` | Create | Pydantic settings with YAML/ENV/DOTENV support |
| `tvscreener/config/loader.py` | Create | Settings loader utility |
| `tvscreener.yaml` | Create | Default configuration |
| `.env.example` | Create | Environment template |
| `tvscreener/lib/screeners/forex_strategy.py` | Modify | Add new filter methods |
| `tvscreener/cli.py` | Modify | Add CLI args and settings integration |
| `tests/` | Modify | Add tests for new filters |

## Acceptance Criteria

### Configuration
- [ ] pydantic-settings, pyyaml, python-dotenv added to dependencies
- [ ] Settings load from YAML file
- [ ] Settings load from .env file (dotenv)
- [ ] Environment variables override YAML
- [ ] CLI arguments override everything
- [ ] Settings validation works (min/max constraints)

### Filters
- [ ] CLI accepts --min-volume, --max-atr, --min-ma-rating, --mr-signal arguments
- [ ] Volume filter correctly filters pairs below threshold
- [ ] ATR filter excludes high-volatility pairs (using ATR as proxy)
- [ ] MA rating filter requires minimum MA alignment
- [ ] Mean reversion signals detected (RSI oversold/overbought)
- [ ] All filters work in combination

### Quality
- [ ] Existing tests still pass
- [ ] New tests added for filter methods
- [ ] Settings validation tested

## Technical Considerations

- **Volatility**: Use ATR (Average True Range) instead of "volatility" - ForexField has ATR columns (ATR|15, ATR|60, ATR|240)
- **RSI**: Available in ForexField as RSI14, RSI14|15, RSI14|60, etc.
- **Bollinger Bands**: Available as "Bollinger Lower Band (20)", "Bollinger Upper Band (20)"
- **Volume field**: "Average Volume (10 day Calc)" - used for volume filtering
- Filters should be optional (None = no filter)
- All filters must handle missing columns gracefully

### Error Handling
- Missing YAML config: Fall back to defaults
- Missing .env file: Continue without error
- Invalid env vars: Use defaults with warning
- Invalid CLI args: Show error with usage

## Dependencies

- pydantic-settings - Settings management with YAML/ENV support
- pyyaml - YAML configuration parsing
- python-dotenv - .env file support
