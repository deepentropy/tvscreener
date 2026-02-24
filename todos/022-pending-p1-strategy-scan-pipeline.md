---
status: complete
priority: p1
issue_id: "022"
tags: [forex, strategy, bug]
dependencies: []
---

## Problem Statement

Strategy-specific CLI paths bypass the unified scan pipeline, so config filters (direction/min_confluence/min_volume/max_atr/min_ma_rating/mr_signals) are inconsistently applied.

## Findings

- `tvscreener/cli.py:120-131` calls `scanner.scan_trend_following()` / `scanner.scan_mean_reversion()` / etc when `--strategy` is not `all`.
- These methods return only `_detect_*` results (see `tvscreener/lib/screeners/forex_strategy.py:119-146`) and do not run the post-processing done by `scan()`.
- `scan()` is the only place that applies `_apply_filters()` and the enhanced filters/signals (`tvscreener/lib/screeners/forex_strategy.py:95-107`).

## Proposed Solutions

### Option A: Route all CLI strategy choices through `scan()` (Recommended)

- Treat CLI `--strategy` as a config input (`include_strategies`) and always call `scanner.scan()`.

### Option B: Make `scan_*` call a shared internal method

- Move the post-processing/filter pipeline into a helper that `scan()` and `scan_*` both call.

## Recommended Action

Option A.

## Acceptance Criteria

- [ ] Strategy results are identical whether selected via `--strategy all` or directly via `--strategy trend` etc
- [ ] Direction/min_confluence and enhanced filters apply for every strategy
