---
status: pending
priority: p2
issue_id: "005"
tags: [code-review, DRY, duplicate]
dependencies: []
---

## Problem Statement

VALID_PAIRS is hardcoded in `forex_opportunity.py` (lines 190-216) but duplicates `DEFAULT_FOREX_PAIRS` from `tvscreener/constants/forex.py`.

## Findings

1. **Location**: `tvscreener/screeners/forex_opportunity.py:190-216`
2. **Issue**: 27 hardcoded pairs that already exist as DEFAULT_FOREX_PAIRS
3. **Impact**: Maintenance burden, potential inconsistency

## Proposed Solutions

### Option A: Use constant (Recommended)
```python
from tvscreener.constants.forex import DEFAULT_FOREX_PAIRS
VALID_PAIRS = DEFAULT_FOREX_PAIRS
```
- **Pros**: Single source of truth
- **Cons**: None
- **Effort**: Small
- **Risk**: Low

## Recommended Action
[To be filled during triage]

## Acceptance Criteria
- [ ] Remove hardcoded VALID_PAIRS, use constant from forex.py

## Work Log
- 2026-02-22: Identified during code review
