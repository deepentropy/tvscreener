---
date: 2026-02-22
topic: asset-agnostic-screener-implementation
status: planned
---

# Asset-Agnostic Screener Implementation Plan

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
   - `_calculate_factor_scores()` - weighted scoring across timeframes
   - `_calculate_roc_score()` - momentum scoring
   - `_calculate_ensemble_score()` - combine factors with weights
   - `_calculate_confluence()` - TF confluence levels
   - `_calculate_direction()` - long/short from scores
   - Accept `ScoringConfig` dataclass with weights

2. **Refactor `ForexOpportunityScreener`** to use `ScoringEngine`:
   - Move `_rank_opportunities()` logic to engine
   - Keep pair-specific logic (merge duplicates, exchange priority) in screener

### Validation
- Run existing forex opportunity tests - output unchanged

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

2. **Create filter registry**:
   - `FilterRegistry` class to map filter names to filter classes
   - Allow asset-specific filter extensions

3. **Refactor existing filters** to use new classes

### Validation
- Existing filters work identically

---

## Phase 3: Create AssetUniverse Config Structure (Week 2)

### Goal
Define dataclasses for asset configuration.

### Files Created
- `tvscreener/config/universe.py` (new)

### New Dataclasses

```python
@dataclass
class IndicatorFields:
    recommend_all: str           # "Recommend All|{tf}"
    recommend_ma: str            # "Recommend MA|{tf}"
    recommend_osc: str           # "Recommend Other|{tf}"
    momentum: str                # "Roc|{tf}" or "RSI|{tf}"

@dataclass
class AssetUniverse:
    name: str                    # "forex", "stocks", "commodity", "crypto"
    pairs: list[str]             # market identifiers
    timeframes: list[str]        # ["15", "60", "240", "D"]
    default_tf_weights: dict[str, float]
    fields: IndicatorFields
    exchanges: list[str] | None
    core_class: type             # ForexScreener, StockScreener, etc.
    field_class: type            # ForexField, StockField, etc.
```

### Files Created/Modified
- `tvscreener/constants/forex.py` - refactor to use `AssetUniverse`
- `tvscreener/constants/stocks.py` (new)
- `tvscreener/constants/commodity.py` (new)
- `tvscreener/constants/crypto.py` (new)

### Validation
- `AssetUniverse` instances for all 4 asset types defined

---

## Phase 4: Create Universal BaseOpportunityScreener (Week 2-3)

### Goal
Build base class that handles all asset types via config.

### Files Created
- `tvscreener/screeners/base.py` (new)

### New Classes

```python
class BaseOpportunityScreener(ABC):
    def __init__(self, universe: AssetUniverse, config: ScreenerConfig)
    def get_opportunities(self) -> pd.DataFrame
    def _fetch_data(self) -> pd.DataFrame
    def _apply_filters(self, df) -> pd.DataFrame
    def _rank_opportunities(self, df) -> pd.DataFrame
    def to_csv(), to_json(), print_summary()

@dataclass
class ScreenerConfig:
    rating_filters: list[RatingFilter]
    roc_filter: RocFilter | None
    volume_filter: VolumeFilter | None
    preferred_exchanges: list[str]
    scoring_config: ScoringConfig | None
```

### Key Methods to Implement
1. `_fetch_data()` - uses `universe.core_class` and `universe.field_class`
2. `_build_field_list()` - dynamically builds fields from `universe.fields`
3. `_merge_duplicates()` - asset-specific pair deduplication
4. `_apply_asset_filters()` - override point for asset-specific filtering

### Validation
- `ForexOpportunityScreener` refactored to extend `BaseOpportunityScreener`
- Output identical to current implementation

---

## Phase 5: Add Asset Types (Week 3-4)

### Goal
Implement Stock, Commodity, Crypto configurations.

### Files Created/Modified

1. **Stocks** - `tvscreener/constants/stocks.py`:
   - S&P 500/ETF universe (use existing stock screener logic)
   - Indicators: RSI, VWMA instead of ROC
   - Field mappings for stock-specific fields

2. **Commodities** - `tvscreener/constants/commodity.py`:
   - Gold, Silver, Oil, Natural Gas, etc.
   - Indicators: STOCH
   - Field mappings

3. **Crypto** - `tvscreener/constants/crypto.py`:
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

# New helper
def get_universe(asset_type: str) -> AssetUniverse:
    from tvscreener.constants import FOREX_UNIVERSE, STOCKS_UNIVERSE, ...
    return {
        "forex": FOREX_UNIVERSE,
        "stocks": STOCKS_UNIVERSE,
        "commodity": COMMODITY_UNIVERSE,
        "crypto": CRYPTO_UNIVERSE,
    }[asset_type]

# Updated run functions
def run_opportunity_scan(args):
    universe = get_universe(args.asset_type)
    screener = BaseOpportunityScreener(universe=universe, ...)
```

### Validation
- `python -m tvscreener --asset-type stocks` works
- `python -m tvscreener --asset-type crypto` works

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

| File | Action |
|------|--------|
| `tvscreener/score.py` | Create |
| `tvscreener/filter.py` | Extend |
| `tvscreener/config/universe.py` | Create |
| `tvscreener/constants/forex.py` | Refactor |
| `tvscreener/constants/stocks.py` | Create |
| `tvscreener/constants/commodity.py` | Create |
| `tvscreener/constants/crypto.py` | Create |
| `tvscreener/screeners/base.py` | Create |
| `tvscreener/screeners/forex_opportunity.py` | Refactor |
| `tvscreener/cli.py` | Update |

---

## Success Criteria

- [ ] All 4 asset types run via CLI
- [ ] Forex behavior unchanged (regression)
- [ ] New asset types have parity with forex (scoring, confluence, output)
- [ ] Adding new asset type = new config file only (no code)
- [ ] All existing tests pass
