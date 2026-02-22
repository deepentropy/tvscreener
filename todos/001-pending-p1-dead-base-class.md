---
status: complete
priority: p1
issue_id: "001"
tags: [code-review, architecture, duplicate]
dependencies: []
---

## Problem Statement

The `BaseOpportunityScreener` abstract base class in `tvscreener/screeners/base.py` (189 LOC) is **never used**. `ForexOpportunityScreener` in `forex_opportunity.py` does NOT inherit from it - it has its own standalone implementation.

## Findings

1. **Dead Abstract Base**: `BaseOpportunityScreener` at `tvscreener/screeners/base.py:25-189` - Never inherited
2. **Unused Code**: 189 lines of dead code that adds maintenance burden
3. **Confusion**: Creates false impression of extensibility that doesn't exist

## Proposed Solutions

### Option A: Delete the dead code (Recommended)
- Delete `tvscreener/screeners/base.py` entirely
- Keep `ForexOpportunityScreener` as standalone
- **Pros**: Removes dead code, reduces confusion
- **Cons**: Loses the abstraction for future use
- **Effort**: Small
- **Risk**: Low

### Option B: Implement the abstraction properly
- Make `ForexOpportunityScreener` inherit from `BaseOpportunityScreener`
- Use `AssetUniverse` throughout
- **Pros**: True asset-agnostic design
- **Cons**: Significant refactoring needed
- **Effort**: Large
- **Risk**: Medium

## Recommended Action
[To be filled during triage]

## Technical Details
- **File**: `tvscreener/screeners/base.py`
- **Lines**: 189 (entire file)
- **Pattern**: Abstract base class never used

## Acceptance Criteria
- [ ] Dead code removed or abstraction properly implemented
- [ ] No confusion about extensibility

## Work Log
- 2026-02-22: Identified during code review

## Resources
- PR branch: `feat/forex-strategy-scanner`
