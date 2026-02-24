---
status: complete
priority: p2
issue_id: "024"
tags: [forex, strategy, bug]
dependencies: ["022"]
---

## Problem Statement

Strategy enhancement thresholds are guarded by truthy checks, so valid values like `0` are treated as "disabled".

## Findings

- `tvscreener/lib/screeners/forex_strategy.py:97-103` uses `if self.config.min_volume:` / `if self.config.max_atr:` / `if self.config.min_ma_rating:`.
- These conditions skip the filters when the value is `0`.

## Proposed Solutions

### Option A: Use explicit `is not None` checks (Recommended)

- Replace truthy checks with `is not None` to preserve `0` behavior.

## Recommended Action

Option A.

## Acceptance Criteria

- [ ] Setting `min_volume=0` still runs the volume filter path
- [ ] Setting `max_atr=0` still runs the ATR filter path
