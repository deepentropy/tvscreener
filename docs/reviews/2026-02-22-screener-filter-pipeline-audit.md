---
title: "Audit: Screener Filters & Pipeline Simplification"
type: review
date: 2026-02-22
status: draft
---

# Audit: Screener Filters & Pipeline Simplification

## Executive Summary

Current implementation has **tight coupling** between forex-specific logic and reusable components. The `ForexOpportunityScreener` and `ForexStrategyScanner` are hardcoded for forex pairs, making it difficult to scale to equities, commodities, or bonds without significant code duplication.

---

## Current Architecture Analysis

### Pipeline Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│  FETCH                    FILTER               SCORE              OUTPUT│
│  ─────                    ──────               ─────            ──────  │
│                                                                          │
│  ForexScreener          RatingFilter          Trend Score      DataFrame│
│  .search(pair)          RocFilter              MA Score        with     │
│  .select(fields)       VolumeFilter           Oscillator      scores   │
│  .get()                ContractType            ROC Score                 │
│  (per-pair loop)       Deduplication           Ensemble                   │
│                                               Score                      │
└─────────────────────────────────────────────────────────────────────────┘
```

### Asset-Type Specific vs Reusable

| Component | Reusable? | Notes |
|-----------|-----------|-------|
| `Screener` base class | ✅ YES | All asset types use same pattern |
| `Filter`, `FilterOperator` | ✅ YES | Universal |
| `FieldCondition`, `Field` | ⚠️ PARTIAL | Each asset has own Field enum |
| `ForexOpportunityScreener` | ❌ NO | Forex-specific scoring/filtering |
| `ForexStrategyScanner` | ❌ NO | Strategy detection logic |
| Constants (forex.py) | ❌ NO | Forex-specific pairs/timeframes |

---

## Issues Identified

### 1. Tight Coupling in ForexOpportunityScreener

**Problem:** Hardcoded forex-specific logic throughout

```python
# Hardcoded in _merge_duplicates() - line 239-265
VALID_PAIRS = ["EURUSD", "GBPUSD", ...]  # 27 pairs hardcoded

# Hardcoded timeframe logic
for tf in self.timeframes:
    col = f"Recommend All|{tf}"  # Forex-specific column pattern

# Hardcoded contract type filter
if contract_type == "cfd":
    return df[df[subtype_col] == "cfd"]
```

### 2. Magic Numbers & Strings

- Column names: `"Recommend All|240"`, `"Roc|15"` scattered
- Thresholds: `trend_threshold = 0.0`, `mr_threshold = 1.0`
- Confluence levels: `>= 3 = strong`, `== 2 = medium`
- Scoring weights: 40/30/20/10 hardcoded

### 3. Duplicate Strategy Detection

```python
# ForexStrategyScanner calls ForexOpportunityScreener internally
self._screener = ForexOpportunityScreener(pairs=..., timeframes=...)
# Then applies its own filtering on top
```

### 4. No Abstract Base for High-Level Screeners

- `ForexOpportunityScreener` doesn't extend `Screener` base class
- Can't leverage streaming, pagination, etc.
- Configuration dataclasses are inline (not reusable)

### 5. Filter Configuration is Forex-Specific

```python
@dataclass
class RatingFilter:
    rating_type: Literal["all", "ma", "oscillator"]  # Forex-specific

@dataclass
class RocFilter:  # Generic - good!
    min_roc: float | None = None
    max_roc: float | None = None
```

---

## Proposed Simplified Architecture

### Goal: Asset-Agnostic Pipeline

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         UNIVERSAL PIPELINE                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  BaseScreener              FilterPipeline          ScoringEngine        │
│  (fetch raw data)    →    (apply filters)    →    (compute scores)      │
│                                                                          │
│  ┌──────────────┐         ┌──────────────┐        ┌──────────────┐      │
│  │ ForexScreener│         │ RatingFilter │        │ ScoreConfig  │      │
│  │ StockScreener│         │ VolumeFilter │        │ (weights)    │      │
│  │ CryptoScreener│        │ RocFilter    │        │              │      │
│  │ BondScreener │         │ ...          │        │              │      │
│  └──────────────┘         └──────────────┘        └──────────────┘      │
│                                                                          │
│  Output: DataFrame + optional strategy signals                           │
└─────────────────────────────────────────────────────────────────────────┘
```

### Key Principles

1. **Separate Concerns:** Fetch ≠ Filter ≠ Score ≠ Strategy
2. **Composition over Inheritance:** Reusable pipeline components
3. **Configuration-Driven:** Weights, thresholds in config, not code
4. **Asset-Agnostic Core:** Base classes work for any asset type

---

## Proposed Changes

### 1. Extract Universal Scoring Engine

```python
# tvscreener/scoring/base.py
@dataclass
class ScoreConfig:
    """Asset-agnostic scoring configuration."""
    factor_weights: dict[str, float]  # e.g., {"trend": 0.4, "ma": 0.3}
    min_score: float = -10.0
    max_score: float = 10.0


class ScoringEngine:
    """Universal scoring engine for any asset type."""
    
    def __init__(self, config: ScoreConfig):
        self.config = config
    
    def compute_scores(
        self, 
        df: pd.DataFrame, 
        factor_columns: dict[str, list[str]]
    ) -> pd.DataFrame:
        """Compute ensemble score from factor columns."""
        # ... vectorized scoring logic
```

### 2. Extract Universal Filter Pipeline

```python
# tvscreener/filters/pipeline.py
class FilterPipeline:
    """Reusable filter chain."""
    
    def __init__(self, filters: list[Filter]):
        self.filters = filters
    
    def apply(self, df: pd.DataFrame) -> pd.DataFrame:
        for filter_ in self.filters:
            df = filter_.apply(df)
        return df


# Universal filter base class
class DataFrameFilter:
    """Filter that operates on pandas DataFrame (post-fetch)."""
    
    def apply(self, df: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError
```

### 3. Create Universal Opportunity Screener

```python
# tvscreener/screeners/base.py
@dataclass
class ScreenerConfig:
    """Asset-agnostic screener configuration."""
    pairs: list[str]
    timeframes: list[str]
    exchanges: list[str] | None = None
    scoring: ScoreConfig | None = None
    filters: list[DataFrameFilter] = field(default_factory=list)


class BaseOpportunityScreener:
    """Universal opportunity screener for any asset type."""
    
    def __init__(self, config: ScreenerConfig):
        self.config = config
        self._screener = None  # Lazy init
    
    def get_opportunities(self) -> pd.DataFrame:
        df = self._fetch()
        df = self._filter(df)
        df = self._score(df)
        return df
    
    def _fetch(self) -> pd.DataFrame:
        raise NotImplementedError  # Asset-specific
    
    def _filter(self, df: pd.DataFrame) -> pd.DataFrame:
        for filter_ in self.config.filters:
            df = filter_.apply(df)
        return df
    
    def _score(self, df: pd.DataFrame) -> pd.DataFrame:
        if self.config.scoring:
            engine = ScoringEngine(self.config.scoring)
            return engine.compute(df)
        return df
```

### 4. Move Constants to Configurable Assets

```python
# tvscreener/constants/assets.py
@dataclass
class AssetUniverse:
    name: str
    pairs: list[str]
    timeframes: list[str]
    default_weights: dict[str, float]
    fields: dict[str, str]  # indicator field mappings


FOREX_UNIVERSE = AssetUniverse(
    name="forex",
    pairs=["EURUSD", "GBPUSD", ...],
    timeframes=["15", "60", "240"],
    default_weights={"15": 0.5, "60": 0.3, "240": 0.2},
    fields={
        "recommend_all": "Recommend All|{tf}",
        "recommend_ma": "Recommend Ma|{tf}",
        "roc": "Roc|{tf}",
    }
)

STOCK_UNIVERSE = AssetUniverse(
    name="stocks",
    pairs=[],  # Dynamic from screener
    timeframes=["60", "240", "D"],
    default_weights={"60": 0.3, "240": 0.4, "D": 0.3},
    fields={
        "recommend_all": "Recommend.All|{tf}",  # Different pattern!
        "recommend_ma": "Recommend.MA|{tf}",
        "rsia": "RSI|{tf}",
    }
)
```

---

## Migration Path

### Phase 1: Extract & Abstract (Low Risk)

1. Create `ScoringEngine` class in new `scoring/` module
2. Move scoring logic from `ForexOpportunityScreener` to engine
3. Keep existing forex screener, delegate to engine
4. **No breaking changes**

### Phase 2: Generalize Filters (Medium Risk)

1. Create `DataFrameFilter` base class
2. Extract forex-specific filters to use base class
3. Add stock/commodity example filters

### Phase 3: Create Universal Screener (Medium Risk)

1. Create `BaseOpportunityScreener` abstract class
2. Refactor `ForexOpportunityScreener` to extend it
3. Add `StockOpportunityScreener` as example

### Phase 4: Add Asset Universes (New Feature)

1. Create `AssetUniverse` config for each type
2. Build screeners that consume universe config
3. CLI automatically handles different asset types

---

## Acceptance Criteria

- [ ] Extract `ScoringEngine` class (Phase 1)
- [ ] ScoringEngine supports custom weights via config (Phase 1)
- [ ] Create `DataFrameFilter` base class (Phase 2)
- [ ] Move existing filters to use base class (Phase 2)
- [ ] Create `BaseOpportunityScreener` abstract class (Phase 3)
- [ ] Refactor ForexOpportunityScreener to extend base (Phase 3)
- [ ] Add StockOpportunityScreener example (Phase 3)
- [ ] Create AssetUniverse config for forex/stocks (Phase 4)
- [ ] CLI supports --asset-type flag (Phase 4)

---

## Files to Modify/Create

### New Files

```
tvscreener/
├── scoring/
│   ├── __init__.py
│   ├── base.py          # ScoreConfig, ScoringEngine
│   └── filters.py       # DataFrameFilter classes
├── screeners/
│   └── base.py          # BaseOpportunityScreener
└── constants/
    └── assets.py        # AssetUniverse configs
```

### Modified Files

```
tvscreener/
├── screeners/
│   └── forex_opportunity.py  # Use ScoringEngine
├── screeners/
│   └── forex_strategy.py     # Use BaseScreener
└── cli.py                    # Add --asset-type
```

---

## Complexity Assessment

| Phase | Risk | Effort |
|-------|------|--------|
| Phase 1: Extract Scoring | Low | 2 hours |
| Phase 2: Generalize Filters | Medium | 3 hours |
| Phase 3: Universal Screener | Medium | 4 hours |
| Phase 4: Asset Universes | Low | 3 hours |

**Total Estimated Effort:** ~12 hours

---

## Appendix: Field Patterns by Asset Type

| Asset | Recommend Field | Timeframe Pattern | Unique Fields |
|-------|---------------|-------------------|---------------|
| Forex | `Recommend.All\|{tf}` | 15, 60, 240 | `Roc\|{tf}` |
| Stocks | `Recommend.All\|{tf}` | 60, 240, D | `RSI\|{tf}`, `VWMA\|{tf}` |
| Crypto | `Recommend.All\|{tf}` | 15, 60, 240, D | `STOCH\|{tf}` |
| Bonds | `Recommend.All\|{tf}` | 60, 240, W | `MACD\|{tf}` |

**Note:** Field patterns are similar but not identical across asset types. Use configurable field mappings.
