---
status: pending
priority: p3
issue_id: "034"
tags: [cleanup, dead-code]
dependencies: []
---

# Remove Dead Code - Unused _apply_filters Method

## Problem Statement

The `_apply_filters` method in forex_opportunity.py is never called - it just wraps `_apply_rating_and_roc_filters` with no additional logic.

## Findings

- **Location:** `tvscreener/lib/screeners/forex_opportunity.py:163-164`
- **Issue:** Method is defined but never called
- **Code:**
  ```python
  def _apply_filters(self, df: pd.DataFrame) -> pd.DataFrame:
      return self._apply_rating_and_roc_filters(df)
  ```

## Proposed Solutions

### Option 1: Remove Method

**Approach:** Delete the unused method.

**Pros:**
- Removes dead code
- Reduces confusion

**Cons:**
- None

**Effort:** 1 minute

**Risk:** None

---

## Recommended Action

[To be filled during triage]

## Technical Details

**Affected files:**
- `tvscreener/lib/screeners/forex_opportunity.py:163-164`

## Acceptance Criteria

- [ ] Dead code removed
- [ ] Tests pass

## Work Log

### 2026-02-25 - Code Review Discovery

**By:** Claude Code (Multiple reviewers)

**Actions:**
- Identified unused method during pattern analysis
