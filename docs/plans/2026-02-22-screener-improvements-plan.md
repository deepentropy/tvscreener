---
date: 2026-02-22
topic: screener-improvements-plan
status: planned
---

# Screener Improvements Implementation Plan

Based on audits: Strategy Detection, Mean Reversion, Confluence Score

## Overview

Fix critical bugs and improve scoring based on three audit reports.

## Phase 1: Critical Bug Fixes (High Priority)

### Bug #1: _detect_trend_following wrong column assignment

**Location**: `tvscreener/screeners/forex_strategy.py:146-147`

**Problem**: Uses pre-filter data for HTF_TREND/STF_TREND columns

**Current**:
```python
htf_trend = result[htf_col].fillna(0)  # Pre-filter
stf_trend = result[stf_col].fillna(0)  # Pre-filter
result = result[long_mask | short_mask].copy()  # Filter
result["HTF_TREND"] = htf_trend  # WRONG: uses pre-filter data
result["STF_TREND"] = stf_trend  # WRONG
```

**Fix**:
```python
result = result[long_mask | short_mask].copy()
result["HTF_TREND"] = result[htf_col].fillna(0)
result["STF_TREND"] = result[stf_col].fillna(0)
```

### Bug #2: _detect_hybrid same issue

**Location**: `tvscreener/screeners/forex_strategy.py:208-209`

**Fix**: Same pattern as Bug #1

---

## Phase 2: Confluence Improvements (Medium Priority)

### 2.1 Add FACTOR_BEARISH_COUNT

**Location**: `tvscreener/score.py:154-158`

**Current**: Only FACTOR_BULLISH_COUNT

**Add**:
```python
df["FACTOR_BEARISH_COUNT"] = sum(
    (df[c] == "bearish").astype(int) for c in factor_dir_cols
)
```

### 2.2 Combined CONFLUENCE_LEVEL

**Location**: `tvscreener/score.py:160-180`

**Current**: Only uses TF_CONFLUENCE

**Improve**: Include factor confluence

```python
# Combine TF + Factor confluence
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

### 3.1 Configurable LTF Timeframe

**Location**: `tvscreener/screeners/forex_strategy.py:19-25`, `157`

**Current**: Hardcoded to 15m

**Add to StrategyConfig**:
```python
ltf_timeframe: str = "15"  # For mean reversion
```

**Update _detect_mean_reversion**:
```python
ltf_col = f"Recommend Other|{self.config.ltf_timeframe}"
```

### 3.2 Add MR Strength ranking

**Location**: `tvscreener/screeners/forex_strategy.py:172-179`

**Add**:
```python
result["MR_STRENGTH"] = result["LTF_MOMENTUM"].abs()
result = result.sort_values("MR_STRENGTH", ascending=False)
```

---

## Phase 4: Threshold Adjustments (Low Priority)

### Current vs Recommended

| Parameter | Current | Recommended |
|-----------|---------|-------------|
| `trend_threshold` | 0.0 | 0.3 |
| `mr_threshold` | 0.2 | 0.2 (keep) |
| `min_confluence` | 1 | 1 (keep) |

**Decision**: Keep current thresholds, make them configurable

---

## Files to Modify

| File | Changes |
|------|---------|
| `tvscreener/screeners/forex_strategy.py` | Bug fixes, MR improvements |
| `tvscreener/score.py` | Confluence improvements |
| `tvscreener/constants/forex.py` | No changes |

---

## Success Criteria

- [ ] Bug #1 fixed: HTF_TREND uses filtered data
- [ ] Bug #2 fixed: Hybrid uses filtered data
- [ ] FACTOR_BEARISH_COUNT added
- [ ] CONFLUENCE_LEVEL includes factor confluence
- [ ] MR LTF timeframe configurable
- [ ] MR_STRENGTH ranking added
- [ ] All 129 tests pass

---

## Testing

1. Run existing test suite
2. Verify confluence distribution changes
3. Verify MR ranking works
4. Run CLI with various options

---

## Estimated Effort

| Phase | Effort |
|-------|--------|
| Phase 1: Bug fixes | 30 min |
| Phase 2: Confluence | 1 hour |
| Phase 3: MR improvements | 30 min |
| Phase 4: Thresholds | 15 min |
| **Total** | **2-2.5 hours** |
