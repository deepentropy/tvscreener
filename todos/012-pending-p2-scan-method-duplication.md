---
status: complete
priority: p2
issue_id: "012"
tags: [architecture, forex-strategy, code-smell]
dependencies: []
---

## Problem Statement

Four scan methods (`scan_trend_following`, `scan_mean_reversion`, `scan_hybrid`, `scan_breakout`) have identical boilerplate code for handling raw_data parameter and empty checks.

## Findings

- **Location:** `forex_strategy.py:90-120`
- **Evidence:**
```python
def scan_trend_following(self, raw_data: pd.DataFrame | None = None) -> pd.DataFrame:
    if raw_data is None:
        raw_data = self._screener.get_opportunities()
    if raw_data.empty:
        return pd.DataFrame()
    return self._detect_trend_following(raw_data)

# Identical pattern repeated 3 more times
```

## Proposed Solutions

### Option A: Template Method / Decorator
```python
def _scan_with_data(self, raw_data, detector):
    if raw_data is None:
        raw_data = self._screener.get_opportunities()
    if raw_data.empty:
        return pd.DataFrame()
    return detector(raw_data)

def scan_trend_following(self, raw_data=None):
    return self._scan_with_data(raw_data, self._detect_trend_following)
```
- **Pros:** Eliminates duplication, easy to test
- **Cons:** Slightly more complex flow
- **Effort:** Low
- **Risk:** Low

### Option B: Simple Refactor
Keep as-is but document the pattern is intentional for API clarity.

- **Pros:** No code change
- **Cons:** Code duplication remains
- **Effort:** None
- **Risk:** None

## Recommended Action

<!-- To be filled during triage -->

## Acceptance Criteria

- [ ] Reduced code duplication OR documented why pattern is intentional

## Work Log

### 2026-02-22 - Initial Review

**By:** pattern-recognition-specialist agent

**Actions:**
- Identified 4x repeated pattern in scan methods
