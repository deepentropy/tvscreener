---
status: complete
priority: p2
issue_id: "035"
---

# Unify Forex scanner export helpers

## Problem Statement

Opportunity and strategy scanners each implemented four identical export helpers (`to_csv`, `to_json`, `to_parquet`, `to_xml`). Maintaining them separately added duplication and risked errors when exports evolved.

## Findings

- Both scanners already shared the `print_summary` logic but exported through duplicated wrappers around `export_helpers`.  
- CLI code directly called the old helpers, which meant any change needed to touch both scanners and the command layer.  
- A small plan (docs/plans/2026-02-26-forex-scanner-unification-plan.md) recommended a unified `export()` method with a format resolver.

## Proposed Solutions

### Option 1: `export()` + format resolver

**Approach:**  

**Pros:** Consistency, single change point, easier future extensions.  
**Cons:** Slight refactor, CLI needs to supply format args.  
**Effort:** Small (≈1 hour).  
**Risk:** Low (functions already existed).  

### Option 2: Keep duplicate helpers (rejected)

**Approach:** Continue calling `to_csv`/`to_json` etc.  
**Effort:** None.  
**Risk:** High – every change touches two places.

## Recommended Action

Complete the `export()` helper refactor (Option 1).  Both scanners now share one method, CLI uses unified interface, and a helper centralizes format selection.

## Technical Details

- Added `get_export_function` to `tvscreener/lib/screeners/export_helpers.py`.  
- Replaced per-format helpers in both scanners with a single `export()` method.  
- Updated `tvscreener/cli.py` to route through `export()` and pass format-specific args.  

## Acceptance Criteria

- [x] `Export` helper exists on both scanners  
- [x] CLI uses `export()` for csv/json/parquet/xml  
- [x] `get_export_function` centralizes format resolution  
- [x] Existing functionality redelivered (runs still produce CSV/JSON/etc.)

## Work Log

### 2026-02-26

**By:** Claude Code  
**Learnings:** CLI had multiple output branches that now funnel through a single `export()` method; new helper keeps valid formats centralized.
