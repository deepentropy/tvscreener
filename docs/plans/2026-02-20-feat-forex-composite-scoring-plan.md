---
title: Add Composite Scoring to ForexOpportunityScreener
type: feat
date: 2026-02-20
---

# Add Composite Scoring to ForexOpportunityScreener

## Enhancement Summary

**Deepened on:** 2026-02-20
**Revised on:** 2026-02-20 (incorporating SOLID, KISS, DRY, YAGNI)

### Principles Applied

- **KISS**: Simple per-timeframe weighted average → ensemble score
- **DRY**: Reuse existing `_rank_opportunities()` logic, add direction column
- **YAGNI**: No separate methods for long/short; add direction column to existing output
- **SOLID**: Single responsibility (scoring), open for extension (configurable weights)

### Key Simplifications
1. Add direction column to existing DataFrame output (not separate methods)
2. Use existing `_rank_opportunities()` pattern, extend for factor breakdown
3. ScoringConfig optional - defaults work out of box
4. Remove duplicate standalone `calculate_opportunity_score()` function

---

## Overview

Enhance the ForexOpportunityScreener with a composite scoring system that produces individual factor scores and separate long/short candidate universes based on weighted ensemble scoring.

## Problem Statement

Currently the screener ranks opportunities by a simple weighted average of ratings. Users need:
- Individual factor scores (Trend, MA, OSC, ROC) for transparency
- Configurable weights to customize the scoring algorithm
- Separate long/short candidate lists for directional trading

## Proposed Solution

**YAGNI**: Keep it simple - add direction column to existing output, no new methods needed.

### API Design (KISS)

```python
# Simple: Add direction column to existing get_opportunities() output
# No new methods required

# Optional: Separate config if user wants custom weights
@dataclass
class ScoringConfig:
    trend_weight: float = 0.4
    ma_weight: float = 0.3
    osc_weight: float = 0.2
    roc_weight: float = 0.1
```

### Score Calculation

1. **Per-factor score** (weighted by timeframe, existing pattern):
   ```
   Trend = sum(Recommend.All|{tf} * tf_weight) / sum(weights_used)
   MA = sum(Recommend.MA|{tf} * tf_weight) / sum(weights_used)
   OSC = sum(Recommend.Other|{tf} * tf_weight) / sum(weights_used)
   ROC = avg(ROC|{tf})
   ```

2. **Ensemble score** (weighted sum):
   ```
   Ensemble = Trend * 0.4 + MA * 0.3 + OSC * 0.2 + ROC * 0.1
   ```

3. **Direction** (YAGNI - simple threshold):
   ```
   Direction = "long" if Ensemble > 0 else "short"
   ```

### Output

Add columns to existing DataFrame:
- `TREND_SCORE`, `MA_SCORE`, `OSC_SCORE`, `ROC_SCORE` (factor breakdown)
- `ENSEMBLE_SCORE` (weighted total)
- `DIRECTION` ("long" | "short")

## Technical Considerations

### Column Mapping

| Factor | TradingView Column |
|--------|-------------------|
| Trend | `Recommend.All|{tf}` |
| MA | `Recommend.MA|{tf}` |
| OSC | `Recommend.Other|{tf}` |
| ROC | `Roc|{tf}` |

### Implementation (KISS - Follow Existing Pattern)

Reuse existing `_rank_opportunities()` at forex_opportunity.py:500-526:

```python
def _calculate_factor_scores(self, df: pd.DataFrame) -> pd.DataFrame:
    """Calculate individual factor scores (DRY - extend existing pattern)."""
    tf_weights = DEFAULT_TIMEFRAME_WEIGHTS
    
    for factor, col_pattern in [("TREND", "Recommend.All|"), 
                                  ("MA", "Recommend.MA|"),
                                  ("OSC", "Recommend.Other|")]:
        cols = [c for c in df.columns if col_pattern in c]
        if cols:
            weights = np.array([tf_weights.get(c.split("|")[-1], 0.33) for c in cols])
            values = df[cols].fillna(0).values
            df[f"{factor}_SCORE"] = (values * weights).sum(axis=1) / weights.sum()
    
    # ROC: simple average (YAGNI - no normalization needed)
    roc_cols = [c for c in df.columns if c.startswith("Roc|")]
    if roc_cols:
        df["ROC_SCORE"] = df[roc_cols].mean(axis=1)
    
    return df
```

### Validation (Minimal)

- Weights default to 1.0 sum (no validation needed for defaults)
- If custom weights: validate sum to 1.0 with ±0.01 tolerance

### Edge Cases (KISS)

- Missing factor → weight redistributed to valid factors
- All weights zero → use equal weights
- Empty DataFrame → return as-is

### Dead Code Cleanup (DRY)

Remove duplicate standalone function:
```python
# DELETE: calculate_opportunity_score() at line 578-602
# It duplicates _rank_opportunities() logic
```

## Acceptance Criteria

- [x] Add optional `ScoringConfig` dataclass (KISS - defaults work out of box)
- [x] Extend `_rank_opportunities()` with factor score calculation (DRY)
- [x] Add factor columns: `TREND_SCORE`, `MA_SCORE`, `OSC_SCORE`, `ROC_SCORE`
- [x] Add `ENSEMBLE_SCORE` (weighted combination)
- [x] Add `DIRECTION` column ("long" | "short" based on ensemble sign)
- [x] Remove duplicate `calculate_opportunity_score()` function (DRY)
- [x] Add basic test for scoring calculation

## Dependencies & Risks

- **Risk**: Low - self-contained, follows existing patterns
- **Benefit**: Removes dead code (`calculate_opportunity_score()`)
- **Breaking**: None - adds columns to existing output

## References

- Existing scoring: `tvscreener/screeners/forex_opportunity.py:500-526`
- Existing config patterns: `tvscreener/screeners/forex_opportunity.py:31-61`
- Timeframe weights: `tvscreener/constants/forex.py:42`
