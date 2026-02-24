---
status: complete
priority: p1
issue_id: "014"
tags: [performance, redundant-api]
dependencies: []
---

## Problem Statement

`to_csv()`, `to_json()`, and `print_summary()` each call `get_opportunities()` or `scan()` again, triggering redundant API calls. A user calling `get_opportunities()` then `to_csv()` makes 2 API calls instead of 1.

## Findings

- **Location:** 
  - `forex_opportunity.py:264-272, 280, 310`
  - `forex_strategy.py:277-285, 293, 319`

## Proposed Solutions

### Option A: Accept Optional DataFrame Parameter
```python
def to_csv(self, path: str, df: pd.DataFrame | None = None, include_index: bool = False) -> None:
    df = df or self.get_opportunities()
    df.to_csv(path, index=include_index)
```
- **Pros:** Backward compatible, clear intent
- **Cons:** Callers must pass df if they have it
- **Effort:** Low
- **Risk:** Low

## Recommended Action

<!-- To be filled during triage -->

## Acceptance Criteria

- [ ] No redundant API calls when data already fetched

## Work Log

### 2026-02-23 - Code Review

**By:** Review agents
