---
status: complete
priority: p2
issue_id: "003"
tags: [code-review, DRY, duplicate]
dependencies: []
---

## Problem Statement

Filter dataclasses (`RatingFilter`, `RocFilter`, `VolumeFilter`, `ScreenerConfig`) are defined in THREE different locations:
1. `tvscreener/filter.py` (lines 52-73)
2. `tvscreener/screeners/base.py` (lines 14-22)
3. `tvscreener/screeners/forex_opportunity.py` (lines 33-57)

## Findings

1. **Duplicate Code**: Same dataclasses with identical fields in 3 places
2. **Maintenance Burden**: Changes must be made in 3 locations
3. **Inconsistency Risk**: Could lead to different behavior
4. **Effort to Fix**: Low - just consolidate imports

## Proposed Solutions

### Option A: Single source of truth (Recommended)
- Keep filter classes in `tvscreener/filter.py`
- Remove from `forex_opportunity.py` - import from filter
- Delete `base.py` entirely (or remove ScreenerConfig)
- **Pros**: Single source of truth, easy maintenance
- **Cons**: Requires updating imports
- **Effort**: Small
- **Risk**: Low

### Option B: Keep separate for now
- Document the duplication
- Add tests to ensure consistency
- **Pros**: Less refactoring now
- **Cons**: Technical debt accumulates
- **Effort**: N/A
- **Risk**: Medium

## Recommended Action
[To be filled during triage]

## Technical Details
- **Files**: 
  - `tvscreener/filter.py` (RatingFilter, RocFilter, VolumeFilter)
  - `tvscreener/screeners/base.py` (ScreenerConfig)
  - `tvscreener/screeners/forex_opportunity.py` (RatingFilter, RocFilter, VolumeFilter, ForexScreenerConfig)

## Acceptance Criteria
- [ ] Filter classes defined in only one location
- [ ] All imports updated to use single source

## Work Log
- 2026-02-22: Identified during code review

## Resources
- PR branch: `feat/forex-strategy-scanner`
