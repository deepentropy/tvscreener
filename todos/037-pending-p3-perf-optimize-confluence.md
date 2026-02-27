---
status: pending
priority: p3
issue_id: '037'
tags: [code-review, performance, optimization]
dependencies: []
---

# Optimize _detect_confluence performance

## Problem Statement

The `_detect_confluence` method has performance optimization opportunities around memory allocation and redundant computations.

## Findings

From performance-oracle review:
1. **pd.concat().max() inefficiency** (line ~383) - creates temporary DataFrame
2. **Double boolean evaluation** - np.select evaluates conditions twice
3. **ROC calculation** - could use numpy arrays directly

## Proposed Solutions

### Option A: Optimize mr_extremity calculation
Replace `pd.concat([...]).max(axis=1)` with numpy:

```python
mr_extremity = pd.Series(
    np.max([osc_htf.abs().values, osc_stf.abs().values, osc_ltf.abs().values], axis=0),
    index=df.index
)
```

### Option B: Keep as-is (current scale is fine)
The current implementation handles 20-50 pairs efficiently. Optimizations matter at 500+ pairs.

- **Effort:** Medium
- **Risk:** Low
- **Priority:** Low (current scale works fine)

## Recommended Action

Skip optimization at current scale. The code is performant for typical forex pair counts.

## Technical Details

- **File:** `tvscreener/lib/screeners/forex_strategy.py`
- **Method:** `_detect_confluence`

## Acceptance Criteria

- [ ] Performance acceptable at current scale (20-50 pairs)

## Work Log

- 2026-02-28: Identified in code review

## Resources

- Related: performance-oracle feedback
