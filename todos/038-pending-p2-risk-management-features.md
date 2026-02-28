---
status: pending
priority: p2
issue_id: "038"
tags: [feature, risk-management, cli]
dependencies: []
---

# Implement Prop Trading Risk Management Features

## Plan Reference

`docs/plans/2026-02-28-prop-trading-risk-management-plan.md`

## Overview

Implement signal quality filters and risk management rules to convert scanner signals into actionable trade executions.

## Implementation Tasks

### Phase 0: Configuration System

- [ ] Add RiskConfig dataclass with layered loading
- [ ] Support config file (YAML)
- [ ] Support environment variables
- [ ] Support CLI args (highest priority)
- [ ] Implement config precedence: CLI > ENV > Config > Defaults

### Phase 1: Signal Quality Filters

- [ ] Add `--min-confluence` CLI option
- [ ] Add `--min-tf-alignment` filter
- [ ] Add `--require-momentum` flag
- [ ] Add `--min-rvol` filter (relative volume threshold)
- [ ] Add `--require-volume-spike` flag (volume > 1.5x average)
- [ ] Calculate Volume ROC for each pair
- [ ] Filter output to clean signals only

### Phase 2: Risk Calculations

- [ ] Create `tvscreener/lib/screeners/risk_utils.py` module
- [ ] Implement ATR-based stop loss calculation
- [ ] Implement risk/reward ratio calculation
- [ ] Implement position size calculator
- [ ] Output clean entry/stop/target levels

### Phase 3: Trade Management

- [ ] Daily loss tracking
- [ ] Drawdown monitoring
- [ ] Max positions enforcement
- [ ] Session-based filtering

## Technical Details

### Files to Modify

1. `tvscreener/cli.py` - Add new CLI arguments
2. `tvscreener/config/settings.py` - Add risk config
3. `tvscreener/lib/screeners/forex_strategy.py` - Add risk calculations
4. `tvscreener/lib/screeners/risk_utils.py` - New module

### Key Formulas

**Position Sizing:**
```
Position Size = (Account Risk Amount) ÷ (ATR × Multiplier × Pip Value)
```

**ATR Stop Loss:**
```
SL = Entry ± (ATR × Multiplier)
```

## Acceptance Criteria

- [ ] CLI args override config file
- [ ] ENV variables override config file
- [ ] Config file loads from tvscreener.yaml
- [ ] `--min-confluence` filter works
- [ ] `--min-tf-alignment` filter works
- [ ] `--require-momentum` blocks conflicting ROC
- [ ] `--min-rvol` filter works
- [ ] `--require-volume-spike` filter works
- [ ] Volume ROC calculated and displayed
- [ ] ATR-based stop loss calculated
- [ ] Risk/reward ratio shown
- [ ] Position size calculated
- [ ] Tests pass

## Work Log

- 2026-02-28: Plan created with relative volume filters
- 2026-02-28: Research added on Volume ROC and relative volume
