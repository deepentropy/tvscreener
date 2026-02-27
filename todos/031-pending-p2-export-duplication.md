---
status: pending
priority: p2
issue_id: "031"
tags: [code-quality, duplication, export]
dependencies: []
---

# Consolidate Duplicated Export Methods

## Problem Statement

Export methods (to_csv, to_json, to_parquet, to_xml, print_summary) are duplicated verbatim in both forex_opportunity.py and forex_strategy.py - ~95% identical with only the label parameter differing.

## Findings

- **Location:** 
  - `tvscreener/lib/screeners/forex_opportunity.py:312-374`
  - `tvscreener/lib/screeners/forex_strategy.py:318-380`
- **Issue:** ~80 lines of duplicated code
- **Impact:** Maintenance overhead; code drift over time

## Proposed Solutions

### Option 1: Create BaseScreener Abstract Class

**Approach:** Extract export methods to a base class that both screeners inherit from.

**Pros:**
- Single source of truth
- Easy to add new export formats
- Clear inheritance hierarchy

**Cons:**
- Requires refactoring both classes
- May need to adjust existing tests

**Effort:** 2-3 hours

**Risk:** Low

---

### Option 2: Create ExportMixin

**Approach:** Use a mixin class for export functionality.

**Pros:**
- More flexible than inheritance
- Both classes can use it

**Cons:**
- Still requires changes to both classes

**Effort:** 2 hours

**Risk:** Low

---

## Recommended Action

[To be filled during triage]

## Technical Details

**Affected files:**
- `tvscreener/lib/screeners/forex_opportunity.py`
- `tvscreener/lib/screeners/forex_strategy.py`

## Acceptance Criteria

- [ ] Single source of truth for export methods
- [ ] Both screeners use shared export code
- [ ] Tests pass

## Work Log

### 2026-02-25 - Pattern Review Discovery

**By:** Claude Code (Pattern Recognition Specialist)

**Actions:**
- Identified duplicate export methods across both scanner classes

**Learnings:**
- Same pattern repeated in CLI handling (cli output.py:256-269 vs 335-348)
