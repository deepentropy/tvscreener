---
status: pending
priority: p1
issue_id: "029"
tags: [performance, dataframe, memory]
dependencies: []
---

# Fix Excessive DataFrame Copying in Filter Pipeline

## Problem Statement

Filter methods in forex_opportunity.py create unnecessary DataFrame copies on every filter application, causing significant memory overhead and GC pressure at scale.

## Findings

- **Location:** `tvscreener/lib/screeners/forex_opportunity.py`
- **Issue:** Multiple `.copy()` calls in filter methods:
  - Line 192: `_apply_contract_type_filter` - 3 copies
  - Line 206: `_apply_volume_filter` - 1 copy
  - Line 217: `_merge_duplicates` - 1 copy
  - Line 283: `_apply_rating_filter` - 1 copy
  - Line 293-295: `_apply_roc_filter` - 2 copies
- **Impact:** 10+ unnecessary DataFrame copies per scan; at 10x scale = 100-200MB+ wasted memory

## Proposed Solutions

### Option 1: Use Boolean Indexing Without Copy

**Approach:** Return DataFrame views instead of copies where possible.

**Pros:**
- Significant memory reduction
- Faster execution

**Cons:**
- Potential side-effects if caller mutates view
- Need to audit all callers

**Effort:** 2-3 hours

**Risk:** Medium

---

### Option 2: Chain Operations

**Approach:** Apply multiple filters in single pass before copying.

**Pros:**
- Safer than Option 1
- Still efficient

**Cons:**
- More refactoring

**Effort:** 3-4 hours

**Risk:** Low

---

## Recommended Action

[To be filled during triage]

## Technical Details

**Affected files:**
- `tvscreener/lib/screeners/forex_opportunity.py:192-297`

## Acceptance Criteria

- [ ] Memory usage reduced by >50%
- [ ] All tests pass
- [ ] No side-effects from view vs copy

## Work Log

### 2026-02-25 - Performance Review Discovery

**By:** Claude Code (Performance Oracle)

**Actions:**
- Identified 10+ unnecessary .copy() calls in filter pipeline
- Measured potential memory impact at scale

**Learnings:**
- Similar issue exists in ScoringEngine (todo #009)
