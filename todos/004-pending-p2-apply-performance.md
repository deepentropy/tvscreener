---
status: pending
priority: p2
issue_id: "004"
tags: [code-review, performance]
dependencies: []
---

## Problem Statement

The `ScoringEngine` uses inefficient `.apply()` with lambdas instead of vectorized numpy operations. This is a performance issue when processing many opportunities.

## Findings

1. **Location**: `tvscreener/score.py`
   - Line 110-112: `df["DIRECTION"] = df["ENSEMBLE_SCORE"].apply(lambda x: "long" if x > 0 else "short")`
   - Line 162-165: `df.apply(lambda r: self._get_confluence_level(r, ...), axis=1)`
   
2. **Impact**: Slow for large datasets - row-wise operations vs vectorized

## Proposed Solutions

### Option A: Use np.where (Recommended)
- Replace `.apply(lambda)` with `np.where()`
- **Pros**: 10-100x faster for large datasets
- **Cons**: None
- **Effort**: Small
- **Risk**: Low

```python
# Before:
df["DIRECTION"] = df["ENSEMBLE_SCORE"].apply(lambda x: "long" if x > 0 else "short")

# After:
df["DIRECTION"] = np.where(df["ENSEMBLE_SCORE"] > 0, "long", "short")
```

## Recommended Action
[To be filled during triage]

## Technical Details
- **File**: `tvscreener/score.py`
- **Methods**: `calculate_ensemble_score()`, `calculate_confluence()`

## Acceptance Criteria
- [ ] No `.apply(lambda)` in scoring code
- [ ] Use vectorized numpy operations throughout

## Work Log
- 2026-02-22: Identified during code review

## Resources
- PR branch: `feat/forex-strategy-scanner`
