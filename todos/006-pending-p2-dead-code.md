---
status: pending
priority: p2
issue_id: "006"
tags: [code-review, DRY]
dependencies: []
---

## Problem Statement

The `_get_confluence_level` method in `score.py` is never called - dead code left over from original implementation.

## Findings

1. **Location**: `tvscreener/score.py:227-238`
2. **Issue**: Method exists but is never called after refactoring to vectorized operations
3. **Impact**: 12 lines of dead code

## Proposed Solutions

### Option A: Delete (Recommended)
- Remove the unused method
- **Pros**: Cleaner code
- **Cons**: None
- **Effort**: Small
- **Risk**: Low

## Recommended Action
[To be filled during triage]

## Acceptance Criteria
- [ ] Remove unused `_get_confluence_level` method

## Work Log
- 2026-02-22: Identified during code review
