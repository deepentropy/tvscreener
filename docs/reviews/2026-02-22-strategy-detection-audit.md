---
title: "Strategy Detection Audit"
type: review
date: 2026-02-22
status: completed
---

# Strategy Detection Audit

## Summary

Audited the strategy detection logic in `tvscreener/screeners/forex_strategy.py`.

## Findings

### Critical Bugs

| Issue | Location | Description |
|-------|----------|-------------|
| #1 | Lines 146-147 | `_detect_trend_following()` uses wrong variable for HTF_TREND/STF_TREND after filter |
| #2 | Lines 208-209 | `_detect_hybrid()` same bug - uses pre-filter data |

### Medium Issues

| Issue | Location | Description |
|-------|----------|-------------|
| #3 | Line 24 | `mr_threshold=0.2` too permissive |
| #4 | Line 23 | `trend_threshold=0.0` too permissive |

### Low Issues

| Issue | Location | Description |
|-------|----------|-------------|
| #5 | Lines 250-252 | Breakout direction uses only first ROC column |
| #6 | Lines 268, 212 | Direction uses 0 instead of configured threshold |
| #7 | Lines 86-118 | Code duplication in scan methods |

## Verified Working

- Mean reversion direction logic is correct
- Empty result handling is correct
- Filter application order is correct

## Current Thresholds

| Parameter | Current | Recommended |
|-----------|---------|-------------|
| `trend_threshold` | 0.0 | 0.3-0.5 |
| `mr_threshold` | 0.2 | 0.5-1.0 |
| `min_confluence` | 1 | 1-2 |

## Strategy Signals (Current Run)

| Strategy | Long | Short | Total |
|----------|------|-------|-------|
| Trend Following | 9 | 9 | 18 |
| Mean Reversion | 5 | 0 | 5 |
| Hybrid | 1 | 0 | 1 |
| Breakout | 4 | 8 | 12 |
| **Total** | **19** | **17** | **36** |
