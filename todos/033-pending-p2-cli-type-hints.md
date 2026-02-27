---
status: pending
priority: p2
issue_id: "033"
tags: [type-safety, cli]
dependencies: []
---

# Add Type Hints to CLI Helper Functions

## Problem Statement

CLI helper functions lack type hints on their `args` parameter, reducing code clarity and IDE support.

## Findings

- **Location:** `tvscreener/cli.py`
- **Issue:** Functions without type hints:
  - Line 67: `_build_opportunity_config(args)` 
  - Line 121: `_build_opportunity_metadata(args)`
  - Line 143: `_build_strategy_metadata(args)`
  - Line 176: `_apply_loaded_config(args, config)`
  - Line 190: `_default_scoped_setting(args, settings, ...)`
  - Line 228: `_maybe_save_opportunity_config(args)`
- **Impact:** Poor IDE support, harder to maintain

## Proposed Solutions

### Option 1: Add argparse.Namespace Type Hint

**Approach:** Add `argparse.Namespace` type hint to all helper functions.

**Pros:**
- Simple fix
- Improves IDE support

**Cons:**
- None

**Effort:** 15 minutes

**Risk:** None

---

## Recommended Action

[To be filled during triage]

## Technical Details

**Affected files:**
- `tvscreener/cli.py`

## Acceptance Criteria

- [ ] All CLI helper functions have type hints
- [ ] Tests pass

## Work Log

### 2026-02-25 - Code Review Discovery

**By:** Claude Code (Kieran Python Reviewer)

**Actions:**
- Identified missing type hints in CLI helper functions
