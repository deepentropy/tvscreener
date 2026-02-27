---
status: pending
priority: p2
issue_id: '036'
tags: [code-review, quality, dead-code]
dependencies: []
---

# Remove unused _add_confluence_and_direction method

## Problem Statement

The `_add_confluence_and_direction` method in `forex_strategy.py` (lines ~415-428) is defined but never called anywhere in the codebase. This is dead code that should be removed.

## Findings

From kieran-python-reviewer:
- Method at lines 415-428 in `tvscreener/lib/screeners/forex_strategy.py`
- Method is defined but never imported or called
- Creates maintenance confusion

## Proposed Solutions

### Option A: Remove Method (Recommended)
Delete the unused `_add_confluence_and_direction` method entirely.

- **Pros:** Clean codebase, removes confusion
- **Cons:** Lose the code if needed later (but git history preserves it)
- **Effort:** Small
- **Risk:** Low

### Option B: Document and Keep
Add docstring explaining it's kept for potential future use.

- **Pros:** Preserves code for reference
- **Cons:** Adds to codebase bloat
- **Effort:** Small
- **Risk:** Low

## Recommended Action

Remove the unused method.

## Technical Details

- **File:** `tvscreener/lib/screeners/forex_strategy.py`
- **Lines:** ~415-428

## Acceptance Criteria

- [ ] Unused method removed from codebase
- [ ] Tests pass after removal

## Work Log

- 2026-02-28: Identified in code review

## Resources

- Related: kieran-python-reviewer feedback
