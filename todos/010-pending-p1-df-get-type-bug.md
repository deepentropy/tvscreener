---
status: pending
priority: p1
issue_id: "010"
tags: [type-safety, score, edge-case]
dependencies: []
---

## Problem Statement

`df.get("ENSEMBLE_SCORE", 0)` returns either a `pd.Series` or scalar `int`. When it returns a scalar, `np.where` produces a scalar result that broadcasts incorrectly, causing all rows to get the same DIRECTION value when `calculate_confluence` is called independently.

## Findings

- **Location:** `score.py:160` - `df.get("ENSEMBLE_SCORE", 0) > 0`
- **Impact:** If calculate_confluence called without calculate_ensemble_score, all rows get identical DIRECTION
- **Evidence:** 
```python
df["DIRECTION"] = np.where(df.get("ENSEMBLE_SCORE", 0) > 0, "long", "short")
# df.get() can return scalar 0, not a Series!
```

## Proposed Solutions

### Option A: Explicit Column Check (Recommended)
```python
if "ENSEMBLE_SCORE" not in df.columns:
    df["ENSEMBLE_SCORE"] = 0.0
df["DIRECTION"] = np.where(df["ENSEMBLE_SCORE"] > 0, "long", "short")
```
- **Pros:** Clear intent, fails fast if column missing
- **Cons:** Adds 2 lines
- **Effort:** Low
- **Risk:** Low

### Option B: Use .get with Series Default
```python
df["DIRECTION"] = np.where(
    df["ENSEMBLE_SCORE"].fillna(0) > 0, "long", "short"
)
```
- **Pros:** Concise
- **Cons:** Assumes column exists
- **Effort:** Low
- **Risk:** Low

## Recommended Action

<!-- To be filled during triage -->

## Acceptance Criteria

- [ ] DIRECTION computed correctly when calculate_confluence called standalone
- [ ] Tests pass for edge case

## Work Log

### 2026-02-22 - Initial Review

**By:** performance-oracle agent

**Actions:**
- Flagged type inconsistency in calculate_confluence

**Learnings:**
- df.get() behavior differs between Series and scalar defaults
