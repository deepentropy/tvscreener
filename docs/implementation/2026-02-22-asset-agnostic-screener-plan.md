---
date: 2026-02-22
topic: asset-agnostic-screener-implementation
status: planned
---

# Asset-Agnostic Screener Implementation Plan

## Enhancement Summary

**Deepened on:** 2026-02-22
**Sections enhanced:** All phases
**Research agents used:** code-simplicity-reviewer, kieran-python-reviewer, best-practices-researcher

### Key Improvements
1. **Removed FilterRegistry** - unnecessary indirection, violate YAGNI
2. **Removed `core_class` and `field_class`** from AssetUniverse - tight coupling, use string names instead
3. **Added frozen dataclasses** with `slots=True` for memory efficiency
4. **Added type bounds** to type hints (e.g., `type[BaseScreener]`)
5. **Added `@abstractmethod`** for base class template methods
6. **Simplified Phase 5** - create asset configs on demand, not preemptively
7. **Added custom exceptions** for configuration validation
8. **Improved CLI dispatch** with proper error handling

### New Considerations Discovered
- Strategy Pattern for swappable scoring algorithms (weighted, percentile, etc.)
- YAML-driven screener configs for user-defined screeners
- Protocol-based interface for screener classes
- Start with only Forex + one more asset type (not all 4)

---

## Overview

Implement a configuration-driven screener framework supporting Forex, Stocks/ETFs, Commodities, and Crypto with shared filtering, scoring, and strategy detection logic.

---

## Phase 1: Extract ScoringEngine (Week 1)

### Goal
Isolate scoring logic from `ForexOpportunityScreener` into a reusable `ScoringEngine`.

### Files Modified
- `tvscreener/screeners/forex_opportunity.py` (refactor)
- `tvscreener/score.py` (new)

### Changes

1. **Create `ScoringEngine` class** in `tvscreener/score.py`:
   - Use public methods (not underscore-prefixed) for API:
     - `calculate_factor_scores()` - weighted scoring across timeframes
     - `calculate_roc_score()` - momentum scoring
     - `calculate_ensemble_score()` - combine factors with weights
     - `calculate_confluence()` - TF confluence levels
     - `calculate_direction()` - long/short from scores
   - Accept `ScoringConfig` dataclass with weights
   - Add `__slots__` for memory efficiency

2. **Refactor `ForexOpportunityScreener`** to use `ScoringEngine`:
   - Move `_rank_opportunities()` logic to engine
   - Keep pair-specific logic (merge duplicates, exchange priority) in screener

### Validation
- Run existing forex opportunity tests - output unchanged

### Research Insights
- Use Strategy Pattern for swappable scoring algorithms
- Consider adding `ScoringStrategyRegistry` for config-driven strategy selection
- Keep underscore-prefixed methods only if truly private implementation details

---

## Phase 2: Generalize Filters with DataFrameFilter Base (Week 1-2)

### Goal
Create base filter classes that work across all asset types.

### Files Modified
- `tvscreener/filter.py` (extend)
- `tvscreener/screeners/forex_opportunity.py` (refactor)

### Changes

1. **Extend `Filter` classes** in `tvscreener/filter.py`:
   - Add `RatingFilter` (from forex_opportunity.py)
   - Add `RocFilter`
   - Add `VolumeFilter`
   - Add `DataFrameFilter` base class for post-fetch filters

2. **Add custom exceptions** for filter errors:
   ```python
   class FilterError(Exception): pass
   class FilterValidationError(FilterError): pass
   ```

3. **Refactor existing filters** to use new classes

### Validation
- Existing filters work identically

### Simplification Note (from review)
- **DELETE**: FilterRegistry - unnecessary indirection, violates YAGNI
- Filters can be imported and used directly where needed

---

## Phase 3: Create AssetUniverse Config Structure (Week 2)

### Goal
Define dataclasses for asset configuration.

### Files Created
- `tvscreener/config/universe.py` (new)

### New Dataclasses

```python
from dataclasses import dataclass, field
from typing import Literal

@dataclass(frozen=True, slots=True)
class IndicatorFields:
    """Field patterns for indicators - uses {tf} placeholder."""
    recommend_all: str           # "Recommend All|{tf}"
    recommend_ma: str           # "Recommend MA|{tf}"
    recommend_osc: str          # "Recommend Other|{tf}"
    momentum: str                # "Roc|{tf}" or "RSI|{tf}"


@dataclass(frozen=True, slots=True)
class AssetUniverse:
    """Asset configuration - immutable and memory-efficient."""
    name: str                                           # "forex", "stocks", "commodity", "crypto"
    pairs: list[str]                                    # market identifiers
    timeframes: list[str]                               # ["15", "60", "240", "D"]
    default_tf_weights: dict[str, float]
    fields: IndicatorFields
    exchanges: list[str] | None
    core_class_name: str                               # "ForexScreener" - string for decoupling
    field_class_name: str                              # "ForexField" - string for decoupling
    
    def validate(self) -> None:
        """Validate configuration at instantiation."""
        if not self.pairs:
            raise ConfigurationError("pairs cannot be empty")
        if not self.timeframes:
            raise ConfigurationError("timeframes cannot be empty")
        total_weight = sum(self.default_tf_weights.values())
        if not 0.99 <= total_weight <= 1.01:  # Allow float tolerance
            raise ConfigurationError(
                f"timeframe weights must sum to 1.0, got {total_weight}"
            )
```

### Files Created/Modified
- `tvscreener/constants/forex.py` - refactor to use `AssetUniverse`
- `tvscreener/constants/stocks.py` (create on demand in Phase 5)
- `tvscreener/constants/commodity.py` (create on demand)
- `tvscreener/constants/crypto.py` (create on demand)

### Validation
- `AssetUniverse` instances for all 4 asset types defined
- Config validation catches errors at startup

### Simplification Note (from review)
- **REMOVED**: `core_class: type` and `field_class: type` - tight coupling
- **NOW**: Use string names (`core_class_name`, `field_class_name`) + factory instantiation
- Create asset constants on demand, not preemptively

---

## Phase 4: Create Universal BaseOpportunityScreener (Week 2-3)

### Goal
Build base class that handles all asset types via config.

### Files Created
- `tvscreener/screeners/base.py` (new)

### New Classes

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
import pandas as pd

@dataclass
class ScreenerConfig:
    """Universal screener configuration."""
    rating_filters: list[RatingFilter] = field(default_factory=list)
    roc_filter: RocFilter | None = None
    volume_filter: VolumeFilter | None = None
    preferred_exchanges: list[str] = field(default_factory=list)
    scoring_config: ScoringConfig | None = None


class BaseOpportunityScreener(ABC):
    """Abstract base for asset-agnostic screening."""
    
    def __init__(self, universe: AssetUniverse, config: ScreenerConfig):
        self.universe = universe
        self.config = config
        self._screener = None  # Lazy init
    
    def get_opportunities(self) -> pd.DataFrame:
        df = self._fetch_data()
        df = self._apply_filters(df)
        df = self._rank_opportunities(df)
        return df
    
    @abstractmethod
    def fetch_data(self) -> pd.DataFrame:
        """Fetch market data. Must be implemented by subclasses."""
        ...
    
    def apply_filters(self, df: pd.DataFrame) -> pd.DataFrame:
        """Apply configured filters. Can be overridden."""
        ...
    
    def rank_opportunities(self, df: pd.DataFrame) -> pd.DataFrame:
        """Rank opportunities by score. Can be overridden."""
        ...
    
    # Internal methods (can be overridden)
    def _build_field_list(self) -> list[str]:
        """Build field list from universe config."""
        ...
    
    def _merge_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        """Asset-specific pair deduplication."""
        ...
    
    def to_csv(self, path: str, include_index: bool = False): ...
    def to_json(self, path: str, orient: str = "records"): ...
    def print_summary(self): ...
```

### Key Methods to Implement
1. `fetch_data()` - abstract method, uses universe config to route to correct screener
2. `_build_field_list()` - dynamically builds fields from `universe.fields`
3. `_merge_duplicates()` - asset-specific pair deduplication
4. Filter application via `config` settings

### Validation
- `ForexOpportunityScreener` refactored to extend `BaseOpportunityScreener`
- Output identical to current implementation

### Simplification Note (from review)
- Use `@abstractmethod` for methods subclasses MUST implement
- Avoid extensive override hooks - if base needs overrides, consider composition instead

---

## Phase 5: Add Asset Types (Week 3-4)

### Goal
Implement Stock, Commodity, Crypto configurations - **on demand, not preemptively**.

### Approach
Start with Forex + ONE more asset type (whichever is most needed).
Create additional configs only when required.

### Files Created/Modified

1. **Stocks** - `tvscreener/constants/stocks.py` (on demand):
   - S&P 500/ETF universe (use existing stock screener logic)
   - Indicators: RSI, VWMA instead of ROC
   - Field mappings for stock-specific fields

2. **Commodities** - `tvscreener/constants/commodity.py` (on demand):
   - Gold, Silver, Oil, Natural Gas, etc.
   - Indicators: STOCH
   - Field mappings

3. **Crypto** - `tvscreener/constants/crypto.py` (on demand):
   - BTC, ETH, major alts
   - Indicators: MACD
   - Field mappings

### Configuration Details

| Asset | Core Class | Field Class | Unique Indicators |
|-------|-----------|-------------|-------------------|
| Forex | ForexScreener | ForexField | ROC |
| Stocks | StockScreener | StockField | RSI, VWMA |
| Commodity | FuturesScreener | FuturesField | STOCH |
| Crypto | CryptoScreener | CryptoField | MACD |

### Validation
- Each asset type runs successfully via CLI
- Results contain expected fields per asset

### Simplification Note (from review)
- Don't create all 4 constants files upfront
- Create on demand when actually needed
- Avoid dead code

---

## Phase 6: CLI Updates for --asset-type Flag (Week 4)

### Goal
Add asset-type selection to CLI.

### Files Modified
- `tvscreener/cli.py`

### CLI Changes

```python
# New arguments
parser.add_argument(
    "--asset-type", 
    choices=["forex", "stocks", "commodity", "crypto"],
    default="forex"
)

# With error handling
UNIVERSE_MAP: dict[str, AssetUniverse] = {}

def get_universe(asset_type: str) -> AssetUniverse:
    """Get universe config by asset type with validation."""
    if asset_type not in UNIVERSE_MAP:
        raise ValueError(
            f"Unknown asset type: {asset_type}. "
            f"Valid options: {', '.join(UNIVERSE_MAP.keys())}"
        )
    return UNIVERSE_MAP[asset_type]

# Updated run functions
def run_opportunity_scan(args):
    universe = get_universe(args.asset_type)
    screener = BaseOpportunityScreener(universe=universe, ...)
```

### Validation
- `python -m tvscreener --asset-type stocks` works
- `python -m tvscreener --asset-type crypto` works
- Invalid asset type shows clear error message

---

## Dependencies & Ordering

```
Phase 1 ──┬──> Phase 2 ──┬──> Phase 3 ──> Phase 4 ──> Phase 5 ──> Phase 6
          │              │
          └──────────────┘ (ScoringEngine used by filters)
```

---

## Testing Strategy

1. **Unit tests** for each new class (ScoringEngine, filters, config)
2. **Integration tests** for each asset type
3. **CLI tests** for --asset-type flag
4. **Regression tests** - forex output unchanged

---

## Files to Create/Modify Summary

| File | Action | Notes |
|------|--------|-------|
| `tvscreener/score.py` | Create | ScoringEngine with Strategy Pattern |
| `tvscreener/filter.py` | Extend | Add DataFrameFilter, exceptions |
| `tvscreener/config/universe.py` | Create | AssetUniverse with validation |
| `tvscreener/constants/forex.py` | Refactor | Use AssetUniverse |
| `tvscreener/constants/stocks.py` | Create | On demand only |
| `tvscreener/constants/commodity.py` | Create | On demand only |
| `tvscreener/constants/crypto.py` | Create | On demand only |
| `tvscreener/screeners/base.py` | Create | Abstract base with @abstractmethod |
| `tvscreener/screeners/forex_opportunity.py` | Refactor | Extend base class |
| `tvscreener/cli.py` | Update | --asset-type with error handling |

**NOT creating (YAGNI):**
- FilterRegistry - unnecessary indirection

---

## Success Criteria

- [ ] ScoringEngine extracted and working (Phase 1)
- [ ] ForexOpportunityScreener uses ScoringEngine (Phase 1)
- [ ] Filters generalized and use frozen dataclasses (Phase 2)
- [ ] AssetUniverse config with validation works (Phase 3)
- [ ] BaseOpportunityScreener with @abstractmethod (Phase 4)
- [ ] Forex extends BaseOpportunityScreener (Phase 4)
- [ ] At least ONE additional asset type works (Phase 5)
- [ ] CLI --asset-type flag with error handling (Phase 6)
- [ ] All existing tests pass (regression)
- [ ] Adding new asset type = new config file only (no code)
