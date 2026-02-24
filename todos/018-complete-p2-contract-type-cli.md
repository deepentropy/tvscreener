---
status: complete
priority: p2
issue_id: "018"
tags: [forex, cli, configuration]
dependencies: []
---

## Problem Statement

The CLI does not expose the `contract_type` configuration option to users. While the default is set to "cfd" in `ForexScreenerConfig`, users cannot change this setting via command-line arguments. Additionally, the "spot" contract type filter may not work correctly as it only checks for empty string.

## Findings

| File | Line | Finding |
|------|------|---------|
| `forex_opportunity.py` | 34 | Default is `"cfd"` in `ForexScreenerConfig` |
| `forex_opportunity.py` | 163-180 | Filter logic checks for empty string for spot: `df[subtype_col] == ""` |
| `cli.py` | 56-88 | `run_opportunity_scan()` doesn't accept or pass contract_type |
| `cli.py` | 150-168 | No `--contract-type` argument in argparse |

The filter for "spot" contracts may have edge cases - TradingView might return "spot" or null instead of empty string for spot contracts.

## Proposed Solutions

### Solution A: Add CLI argument for contract type (Recommended)

Add `--contract-type` argument to CLI and pass through to config.

**Changes:**
1. Add argument to cli.py parser
2. Pass contract_type in ForexScreenerConfig

**Pros:**
- User-facing control
- Backward compatible (default stays "cfd")

**Cons:**
- Minor additional complexity

**Effort:** Small

---

### Solution B: Fix spot filter edge case

Improve the spot contract type detection.

**Changes:**
```python
# In _apply_contract_type_filter():
elif contract_type == "spot":
    return df[df[subtype_col].isin(["", "spot", None])].copy()
```

**Pros:**
- More robust detection

**Effort:** Small

---

## Recommended Action

Implement both Solution A (CLI argument) and Solution B (spot filter fix)

## Acceptance Criteria

- [ ] CLI accepts --contract-type argument
- [ ] Default remains "cfd" for backward compatibility
- [ ] Spot filter handles multiple formats
- [ ] Tests pass

## Work Log

### 2026-02-23 - Initial Investigation

**By:** Claude Code

**Actions:**
- Reviewed cli.py and forex_opportunity.py
- Confirmed contract_type not exposed in CLI

**Learnings:**
- Simple addition to expose existing configuration
