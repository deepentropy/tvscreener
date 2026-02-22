---
status: complete
priority: p1
issue_id: "008"
tags: [code-review, bug]
dependencies: []
---

## Problem Statement

The `--universe` flag (majors/minors/all) is not working in the CLI. It always scans all pairs from the universe regardless of the flag.

## Findings

1. **Location**: `tvscreener/cli.py:63` and `cli.py:99`
2. **Bug**: Uses `universe.pairs` directly instead of calling `get_pairs(args.universe, args.pairs)`
3. **Impact**: `--universe majors` and `--universe minors` don't filter pairs

## Proposed Solutions

### Option A: Use get_pairs function (Recommended)
```python
# Line 63: change from
pairs = args.pairs if args.pairs else universe.pairs

# To:
pairs = get_pairs(args.universe, args.pairs)
```
- **Pros**: Fixes bug, reuses existing function
- **Effort**: Small
- **Risk**: Low

## Recommended Action
[To be filled during triage]

## Acceptance Criteria
- [ ] --universe majors filters to 7 pairs
- [ ] --universe minors filters to 18 pairs
- [ ] --universe all scans all 25 pairs

## Work Log
- 2026-02-22: Identified during CLI testing

## Resources
- Bug found when testing CLI with uv run
