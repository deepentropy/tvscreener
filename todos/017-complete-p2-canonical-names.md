---
status: complete
priority: p2
issue_id: "017"
tags: [forex, display, quality]
dependencies: []
---

## Problem Statement

CLI output displays full TradingView symbol names with exchange/subtype suffixes (e.g., "AUDUSD.1.CFJ", "USDJPY.100.MINI", "EURUSD.10.DUB") instead of canonical base/quote currency pair names (e.g., "AUDUSD", "USDJPY", "EURUSD").

Users want clean, readable output showing only the canonical forex pair names without exchange metadata.

## Findings

**Root Cause:** The `_base_pair` column is computed in `_merge_duplicates()` method at `forex_opportunity.py:222` for deduplication purposes, but it is explicitly **dropped** before the data is returned to the caller.

| File | Line | Finding |
|------|------|---------|
| `forex_opportunity.py` | 222 | `_base_pair` is created via `df["_base_pair"] = df["Name"].apply(get_base_pair)` |
| `forex_opportunity.py` | 237 | Used for deduplication: `df = df.drop_duplicates(subset=["_base_pair"], keep="first")` |
| `forex_opportunity.py` | 246-250 | **DROPPED** before returning: `_base_pair` is in the drop list |
| `forex_opportunity.py` | 329 | Display uses original `Name`: `name = row.get("Name", "N/A")` which contains full TV symbol |

The `get_base_pair()` function at lines 204-218 correctly extracts canonical names (e.g., "AUDUSD" from "AUDUSD.1.CFJ"), but the result is discarded.

## Proposed Solutions

### Solution A: Preserve `_base_pair` column (Recommended)

Keep `_base_pair` in the DataFrame and use it for display.

**Changes:**
1. In `_merge_duplicates()`, modify drop columns to preserve `_base_pair`
2. In `print_summary()`, use `_base_pair` for display name

**Pros:**
- Minimal code changes
- Leverages existing `get_base_pair()` logic
- Single source of truth for canonical name

**Cons:**
- Adds column to all output DataFrames

**Effort:** Small

---

### Solution B: Extract canonical name on display

Add a helper function and extract canonical name in `print_summary()` without preserving column.

**Changes:**
1. Add `_get_canonical_name()` helper method
2. Update `print_summary()` in both screeners to use helper

**Pros:**
- No extra column in output DataFrames
- Cleaner API output

**Cons:**
- Duplicates extraction logic
- More changes across multiple methods

**Effort:** Medium

## Recommended Action

Solution A - Preserve `_base_pair` column

## Acceptance Criteria

- [ ] CLI output shows canonical names (e.g., "AUDUSD" not "AUDUSD.1.CFJ")
- [ ] Both opportunity and strategy scanners display canonical names
- [ ] Existing tests pass
- [ ] No regression in CSV/JSON export output

## Work Log

### 2026-02-23 - Initial Investigation

**By:** Claude Code

**Actions:**
- Reviewed forex_opportunity.py and forex_strategy.py
- Identified root cause: _base_pair computed but dropped
- Confirmed get_base_pair() function works correctly

**Learnings:**
- The canonical name extraction logic already exists
- Just needs to be preserved for display
