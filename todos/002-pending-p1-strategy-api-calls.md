---
status: complete
priority: p1
issue_id: "002"
tags: [code-review, performance, DRY]
dependencies: []
---

## Problem Statement

Each strategy detection method (`scan_trend_following`, `scan_mean_reversion`, `scan_hybrid`, `scan_breakout`) in `ForexStrategyScanner` calls `self._screener.get_opportunities()` separately, resulting in **4-5 duplicate API calls** to fetch the same data.

## Findings

1. **Location**: `tvscreener/screeners/forex_strategy.py`
2. **Lines**: 88, 95, 102, 109 - each method calls API separately
3. **Impact**: Severe performance issue - 4x slower than necessary
4. **Pattern**: The `scan()` method calls individual strategy methods, each of which fetches data again

## Proposed Solutions

### Option A: Fetch once, pass DataFrame (Recommended)
- Fetch data once in `scan()` method
- Pass `raw_data` as parameter to detection methods
- **Pros**: Simple fix, 4x performance improvement
- **Cons**: Changes method signatures
- **Effort**: Small
- **Risk**: Low

### Option B: Cache the result
- Use `@functools.lru_cache` or store in instance variable
- **Pros**: No API changes needed
- **Cons**: More complex state management
- **Effort**: Small
- **Risk**: Low

## Recommended Action
[To be filled during triage]

## Technical Details
- **File**: `tvscreener/screeners/forex_strategy.py`
- **Methods**: `scan()`, `scan_trend_following()`, `scan_mean_reversion()`, `scan_hybrid()`, `scan_breakout()`

## Acceptance Criteria
- [ ] Data fetched only once per scan operation
- [ ] Performance improved by ~4x

## Work Log
- 2026-02-22: Identified during code review

## Resources
- PR branch: `feat/forex-strategy-scanner`
