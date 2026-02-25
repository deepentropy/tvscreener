---
title: Add Multi-Timeframe and Factor Confluence Metrics
type: feat
date: 2026-02-22
---

# Add Multi-Timeframe and Factor Confluence Metrics

## Enhancement Summary

**Deepened on:** 2026-02-22

### Key Improvements
1. Use vectorized operations instead of `.apply()` for performance
2. Optimize confluence calculation to avoid row-by-row iteration
3. Add helper functions at module level for reusability

---

## Overview

Enhance ForexOpportunityScreener with confluence scoring that counts aligned timeframes and factors. Add direction classification per timeframe and factor for better signal quality assessment.

## Problem Statement

Current implementation uses weighted averages which can mask disagreement between timeframes/factors. Traders need to know:
- How many timeframes agree on direction?
- How many factors are bullish/bearish?
- What's the overall signal quality?

## Proposed Solution

**Performance Note**: Use vectorized pandas operations instead of `.apply(axis=1)` for O(n) → O(1) performance.

Add helper functions at module level:

```python
# Module-level helpers for vectorized operations
def get_direction(series: pd.Series) -> pd.Series:
    """Vectorized direction calculation."""
    return pd.Series(
        np.where(series > 0, "bullish",
                 np.where(series < 0, "bearish", "neutral")),
        index=series.index
    )

def count_bullish(series_list: list[pd.Series]) -> pd.Series:
    """Count bullish signals across multiple series."""
    return sum((s > 0).astype(int) for s in series_list)
```

### 1. Timeframe Direction (Vectorized)

```python
# Per timeframe direction - vectorized
for tf in self.timeframes:
    col = f"Recommend All|{tf}"
    if col in df.columns:
        df[f"TF_{tf}_DIR"] = get_direction(df[col])
```

### 2. Timeframe Confluence Score (Vectorized)

```python
# Count aligned TFs - vectorized approach
tf_cols = [f"Recommend All|{tf}" for tf in self.timeframes if f"Recommend All|{tf}" in df.columns]
if tf_cols:
    tf_values = df[tf_cols].fillna(0)
    df["TF_CONFLUENCE_LONG"] = (tf_values > 0).sum(axis=1)
    df["TF_CONFLUENCE_SHORT"] = (tf_values < 0).sum(axis=1)
```

### 3. Factor Direction & Confluence

```python
# Per factor direction
for factor in ["TREND", "MA", "OSC", "ROC"]:
    col = f"{factor}_SCORE"
    if col in df.columns:
        df[f"{factor}_DIR"] = df[col].apply(get_direction)

# Factor confluence
df["FACTOR_BULLISH_COUNT"] = sum([
    df["TREND_DIR"] == "bullish",
    df["MA_DIR"] == "bullish",
    df["OSC_DIR"] == "bullish",
    df["ROC_DIR"] == "bullish"
])
```

### 4. Confluence Level

```python
def get_confluence_level(row, direction: str) -> str:
    total = row.get(f"TF_CONFLUENCE_{direction}", 0)
    if total >= 3:
        return "strong"
    elif total == 2:
        return "medium"
    elif total == 1:
        return "weak"
    return "none"

df["CONFLUENCE_LEVEL"] = df.apply(
    lambda r: get_confluence_level(r, "long" if r.get("DIRECTION") == "long" else "short"),
    axis=1
)
```

## New Output Columns

| Column | Type | Description |
|--------|------|-------------|
| `TF_240_DIR` | str | bullish/bearish/neutral |
| `TF_60_DIR` | str | bullish/bearish/neutral |
| `TF_15_DIR` | str | bullish/bearish/neutral |
| `TF_CONFLUENCE_LONG` | int | 0-3 TFs bullish |
| `TF_CONFLUENCE_SHORT` | int | 0-3 TFs bearish |
| `TREND_DIR` | str | bullish/bearish/neutral |
| `MA_DIR` | str | bullish/bearish/neutral |
| `OSC_DIR` | str | bullish/bearish/neutral |
| `ROC_DIR` | str | bullish/bearish/neutral |
| `FACTOR_BULLISH_COUNT` | int | 0-4 factors bullish |
| `CONFLUENCE_LEVEL` | str | strong/medium/weak/none |

## Acceptance Criteria

- [ ] Add timeframe direction columns (TF_240_DIR, TF_60_DIR, TF_15_DIR)
- [ ] Calculate TF_CONFLUENCE_LONG and TF_CONFLUENCE_SHORT
- [ ] Add factor direction columns (TREND_DIR, MA_DIR, OSC_DIR, ROC_DIR)
- [ ] Calculate FACTOR_BULLISH_COUNT
- [ ] Add CONFLUENCE_LEVEL classification
- [ ] Update CLI output to show confluence
- [ ] Add tests for confluence calculations

## Files Affected

- `tvscreener/screeners/forex_opportunity.py` - Add confluence logic to _rank_opportunities()
- `tests/unit/test_forex_scoring.py` - Add confluence tests
