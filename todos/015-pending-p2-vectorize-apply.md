---
status: complete
priority: p2
issue_id: "015"
tags: [performance, row-wise]
dependencies: []
---

## Problem Statement

Row-wise `.apply()` operations in `_merge_duplicates` create O(n×m) complexity. With 1000 rows × 30 pairs = 30,000 iterations.

## Findings

- **Location:** `forex_opportunity.py:221-222`
```python
df["_base_pair"] = df["Name"].apply(get_base_pair)
df["_priority"] = df.apply(get_priority, axis=1)
```

## Proposed Solutions

### Option A: Vectorized String Methods
```python
df["_base_pair"] = df["Name"].str[:6].str.upper()
```
- **Pros:** O(n) instead of O(n×m)
- **Effort:** Low
- **Risk:** Low

## Recommended Action

<!-- To be filled during triage -->

## Acceptance Criteria

- [x] No row-wise apply in hot path

## Work Log

### 2026-02-24

- Replaced row-wise `.apply()` in `_merge_duplicates` with vectorized `str.extract` (base pair) and `str.split` (exchange).
- Added unit tests covering embedded-pair extraction and exchange-priority selection.
