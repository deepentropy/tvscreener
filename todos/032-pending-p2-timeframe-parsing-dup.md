---
status: pending
priority: p2
issue_id: "032"
tags: [code-quality, duplication, cli]
dependencies: []
---

# Remove Duplicate Timeframe Weight Parsing

## Problem Statement

Timeframe weight parsing logic is duplicated in two places: settings.py and cli.py. This violates DRY and creates maintenance overhead.

## Findings

- **Locations:**
  - `tvscreener/config/settings.py:52-64` - `get_opportunity_timeframe_weights()` method
  - `tvscreener/cli.py:103-118` - `_parse_timeframe_weights()` function
- **Issue:** Nearly identical parsing logic exists in two places
- **Impact:** If parsing changes, must update in two places

## Proposed Solutions

### Option 1: Use Settings Method in CLI

**Approach:** Import and use `ScreenerSettings.get_opportunity_timeframe_weights()` in CLI.

**Pros:**
- Single source of truth
- Settings validation available

**Cons:**
- Requires importing settings in CLI

**Effort:** 30 minutes

**Risk:** Low

---

### Option 2: Extract to Shared Utility

**Approach:** Create `tvscreener/utils/timeframe.py` with parsing function.

**Pros:**
- Explicit dependency
- Easy to test

**Cons:**
- New file to maintain

**Effort:** 30 minutes

**Risk:** Low

---

## Recommended Action

[To be filled during triage]

## Technical Details

**Affected files:**
- `tvscreener/config/settings.py`
- `tvscreener/cli.py`

## Acceptance Criteria

- [ ] Single source of truth for timeframe weight parsing
- [ ] Tests pass

## Work Log

### 2026-02-25 - Code Review Discovery

**By:** Claude Code (Multiple reviewers)

**Actions:**
- Identified duplicate parsing logic
