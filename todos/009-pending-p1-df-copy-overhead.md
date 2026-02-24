---
status: complete
priority: p1
issue_id: "009"
tags: [performance, dataframe, score]
dependencies: []
---

## Problem Statement

Each method in ScoringEngine creates a full copy of the DataFrame. In `rank_opportunities`, this results in **5 separate copies** being created through the pipeline chain, causing memory bloat and performance degradation at scale.

## Findings

- **Location:** `score.py:57, 82, 101, 124` - every method calls `df = df.copy()`
- **Impact:** With 10K rows × 100 columns: ~200MB wasted memory, ~200ms overhead
- **Evidence:** `rank_opportunities` chains 6 methods, each copying the full DataFrame

## Proposed Solutions

### Option A: Single Copy at Pipeline Entry (Recommended)
```python
def rank_opportunities(self, df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    df = df.copy()  # Single copy here
    # All methods operate in-place
    self._calculate_factor_scores_inplace(df, "TREND", "Recommend All|")
    ...
```
- **Pros:** Minimal code change, clear data flow
- **Cons:** Requires converting methods to in-place
- **Effort:** Medium
- **Risk:** Low

### Option B: Remove All Copies
```python
def calculate_factor_scores(self, df, ...):
    # No copy - operate directly
    df[f"{factor_name}_SCORE"] = ...
    return df
```
- **Pros:** Maximum performance
- **Cons:** Caller must not reuse DataFrame, more risky
- **Effort:** High
- **Risk:** Medium

### Option C: Add Copy Parameter
```python
def calculate_factor_scores(self, df, ..., copy=True):
    if copy:
        df = df.copy()
    ...
```
- **Pros:** Backward compatible
- **Cons:** Adds complexity, easy to misuse
- **Effort:** Low
- **Risk:** Low

## Recommended Action

<!-- To be filled during triage -->

## Acceptance Criteria

- [ ] Single DataFrame copy in rank_opportunities pipeline
- [ ] Memory usage reduced by ~80% for scoring pipeline
- [ ] All existing tests pass

## Work Log

### 2026-02-22 - Initial Review

**By:** Code Review Agents

**Actions:**
- Identified 5+ df.copy() calls in scoring pipeline
- performance-oracle flagged as P1 issue

**Learnings:**
- Vectorization is correct, but copy overhead is significant
