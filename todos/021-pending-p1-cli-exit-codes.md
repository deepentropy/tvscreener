---
status: complete
priority: p1
issue_id: "021"
tags: [cli, bug]
dependencies: []
---

## Problem Statement

CLI can exit with code 0 even when the scan fails, because errors are mapped to a positive "count".

## Findings

- `tvscreener/cli.py:84-88` and `tvscreener/cli.py:148-152` return `1` on exceptions.
- `tvscreener/cli.py:201` returns `0 if count > 0 else 1`.
- This means an exception path returns `count=1` and exits successfully.

## Proposed Solutions

### Option A: Make runners return `(results_count, ok)`

- Return a tuple and compute exit code from `ok`.

### Option B: Reserve negative values for errors (Recommended)

- Return `-1` (or `None`) on error from `run_*`.
- `main()` exits non-zero when count is negative/None.

## Recommended Action

Option B.

## Acceptance Criteria

- [ ] Any exception results in non-zero exit code
- [ ] Success exit code does not depend on results count
- [ ] "no results" is distinguishable from "error" (via exit code)
