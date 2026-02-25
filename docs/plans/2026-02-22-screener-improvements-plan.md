---
date: 2026-02-22
topic: screener-improvements-plan
status: deepened
---

# Screener Improvements Implementation Plan

## Enhancement Summary

**Deepened on:** 2026-02-22
**Sections enhanced:** 4
**Research agents used:** best-practices-researcher (x2), code-simplicity-reviewer, kieran-python-reviewer

### Key Improvements
1. **Phase 1 removed** - Bugs are NOT real bugs (pandas aligns by index)
2. **Vectorization fixes** - Replace `.apply(lambda)` with `np.where()`
3. **Performance optimizations** - Use pandas vectorized operations
4. **Dataclass improvements** - Add `frozen=True, slots=True`

### New Considerations Discovered
- Exponential timeframe weighting (HTF should weight more)
- Regime-aware thresholds (ADX-based)
- Signal strength classification (strong/moderate/weak)
- Adaptive factor weights

---

## Overview

Fix critical bugs and improve scoring based on three audit reports.

---

## Phase 1: Performance & Vectorization (High Priority)

### Research Insight

The code-simplicity-reviewer found that **Phase 1 bugs are NOT actual bugs**. Pandas Series assignment aligns by index automatically:

```python
htf_trend = result[htf_col].fillna(0)  # Series with original indices
result = result[long_mask | short_mask].copy()  # Filtered, indices preserved
result["HTF_TREND"] = htf_trend  # ✅ pandas aligns by index correctly
```

**Action**: Skip bug fixes, focus on real improvements.

### 1.1 Replace `.apply(lambda)` with `np.where()`

**Location**: `tvscreener/screeners/forex_strategy.py:175-177, 211-213, 250-252`

**Current** (slow):
```python
result["DIRECTION"] = result["LTF_MOMENTUM"].apply(
    lambda x: "long" if x < -self.config.mr_threshold else "short"
)
```

**Fix** (10-100x faster):
```python
result["DIRECTION"] = np.where(
    result["LTF_MOMENTUM"] < -self.config.mr_threshold,
    "long",
    "short"
)
```

### 1.2 Vectorized FACTOR_BEARISH_COUNT

**Location**: `tvscreener/score.py:154-158`

**Current** (slow):
```python
df["FACTOR_BEARISH_COUNT"] = sum(
    (df[c] == "bearish").astype(int) for c in factor_dir_cols
)
```

**Fix** (vectorized):
```python
if factor_dir_cols:
    df["FACTOR_BEARISH_COUNT"] = (df[factor_dir_cols] == "bearish").sum(axis=1)
else:
    df["FACTOR_BEARISH_COUNT"] = 0
```

---

## Phase 2: Confluence Improvements (Medium Priority)

### 2.1 Add FACTOR_BEARISH_COUNT

**Location**: `tvscreener/score.py:154-158`

**Add**:
```python
if factor_dir_cols:
    df["FACTOR_BULLISH_COUNT"] = (df[factor_dir_cols] == "bullish").sum(axis=1)
    df["FACTOR_BEARISH_COUNT"] = (df[factor_dir_cols] == "bearish").sum(axis=1)
else:
    df["FACTOR_BULLISH_COUNT"] = 0
    df["FACTOR_BEARISH_COUNT"] = 0
```

### 2.2 Combined CONFLUENCE_LEVEL

**Location**: `tvscreener/score.py:160-180`

**Research insight**: Industry standard combines TF + Factor confluence

```python
df["TOTAL_CONFLUENCE"] = np.where(
    df["DIRECTION"] == "long",
    df["TF_CONFLUENCE_LONG"] + df["FACTOR_BULLISH_COUNT"],
    df["TF_CONFLUENCE_SHORT"] + df["FACTOR_BEARISH_COUNT"]
)

df["CONFLUENCE_LEVEL"] = np.select(
    [df["TOTAL_CONFLUENCE"] >= 5,
     df["TOTAL_CONFLUENCE"] >= 3,
     df["TOTAL_CONFLUENCE"] >= 1],
    ["strong", "medium", "weak"],
    default="none"
)
```

---

## Phase 3: Mean Reversion Improvements (Medium Priority)

### 3.1 Add MR_STRENGTH ranking

**Location**: `tvscreener/screeners/forex_strategy.py:172-179`

**Research insight**: Rank MR signals by oscillator extremity

**Add**:
```python
result["MR_STRENGTH"] = result["LTF_MOMENTUM"].abs()
result = result.sort_values("MR_STRENGTH", ascending=False)
```

### 3.2 (Deferred) Configurable LTF Timeframe

**YAGNI**: No current use case. Defer until needed.

---

## Phase 4: Dataclass Improvements (Low Priority)

### 4.1 Freeze StrategyConfig

**Location**: `tvscreener/screeners/forex_strategy.py:18-25`

**Current**:
```python
@dataclass
class StrategyConfig:
    ...
```

**Fix**:
```python
@dataclass(frozen=True, slots=True)
class StrategyConfig:
    ...
```

---

## Files to Modify

| File | Changes |
|------|---------|
| `tvscreener/screeners/forex_strategy.py` | Vectorization, MR improvements, dataclass |
| `tvscreener/score.py` | Confluence improvements, vectorization |
| `tvscreener/constants/forex.py` | No changes |

---

## Success Criteria

- [x] `.apply(lambda)` replaced with `np.where()` (4 locations)
- [x] FACTOR_BEARISH_COUNT added (vectorized)
- [x] TOTAL_CONFLUENCE column added
- [x] CONFLUENCE_LEVEL uses combined TF + Factor
- [x] MR_STRENGTH ranking added
- [x] StrategyConfig frozen with slots
- [x] All 129 tests pass

**Completed: 2026-02-22**

---

## Testing

1. Run existing test suite
2. Verify confluence distribution changes
3. Verify MR ranking works
4. Run CLI with various options
5. **New test**: Verify vectorization correctness

```python
def test_trend_following_uses_filtered_data():
    """Regression test for index alignment."""
    scanner = ForexStrategyScanner()
    df = pd.DataFrame({
        "Recommend All|240": [0.5, -0.5, 0.3],
        "Recommend All|60": [0.5, -0.5, 0.1],
    })
    result = scanner._detect_trend_following(df)
    assert result["HTF_TREND"].tolist() == [0.5, -0.5]
```

---

## Estimated Effort

| Phase | Effort |
|-------|--------|
| Phase 1: Vectorization | 30 min |
| Phase 2: Confluence | 45 min |
| Phase 3: MR improvements | 20 min |
| Phase 4: Dataclass | 10 min |
| **Total** | **1.5-2 hours** |

---

## Research References

### Best Practices

- **Timeframe weighting**: HTF should weight more (exponential or hierarchical)
- **Factor confluence**: Independent factors avoid multicollinearity
- **Vectorization**: `np.where()` and pandas native operations 10-100x faster
- **Signal classification**: Strong/Moderate/Weak thresholds improve filtering

### Performance

- Single-pass DataFrame creation with `df.assign(**result_cols)`
- Pre-allocate arrays with NumPy
- Avoid `.apply(lambda)` - use `np.where()` or `np.select()`

### Mean Reversion

- Optimal RSI thresholds: 20/80 for trending, 25/75 for ranging
- Multi-TF confluence improves win rate 10-15%
- Signal ranking by oscillator extremity improves quality
