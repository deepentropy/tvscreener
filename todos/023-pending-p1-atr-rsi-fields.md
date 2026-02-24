---
status: complete
priority: p1
issue_id: "023"
tags: [forex, strategy, indicators, bug]
dependencies: ["022"]
---

## Problem Statement

ATR/RSI-based filters and mean-reversion signals are effectively no-ops because the underlying opportunity fetch does not request ATR/RSI columns.

## Findings

- `tvscreener/lib/screeners/forex_opportunity.py:120-132` selects Name/Price/Volume/Subtype + Recommend*/ROC fields only.
- `tvscreener/lib/screeners/forex_strategy.py:361-367` expects columns starting with `ATR|`.
- `tvscreener/lib/screeners/forex_strategy.py:392-404` expects columns starting with `RSI`.
- With current `select_fields`, those columns will never exist, so the filters/signals silently do nothing.

## Proposed Solutions

### Option A: Request ATR/RSI fields when needed (Recommended)

- Extend opportunity fetch to include `ForexField.ATR_*` and `ForexField.RSI_*` for the active timeframes.
- Only request them if the strategy config enables `max_atr` and/or `mean_reversion_signals`.

### Option B: Fail fast when fields are missing

- If `max_atr` or RSI signals are enabled but no matching columns exist, raise a configuration error.

## Recommended Action

Option A.

## Acceptance Criteria

- [ ] Enabling `--max-atr` changes results
- [ ] Enabling `--mr-signal rsi_oversold|rsi_overbought` adds corresponding signal columns
- [ ] Tests cover the "fields present" and "fields missing" cases
