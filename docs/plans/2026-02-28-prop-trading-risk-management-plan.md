---
title: Prop Trading Signal Filters & Risk Management Plan
date: 2026-02-28
status: draft
---

# Prop Trading Signal Filters & Risk Management Plan

## Overview

Add practical trading filters and risk management rules to convert scanner signals into actionable trade executions.

---

## Prop Trading Firm Rules (Common)

### Typical Risk Parameters

| Rule | Standard Value | Description |
|------|---------------|-------------|
| Max Risk per Trade | 1-2% | Maximum account risk per position |
| Max Daily Loss | 3-4% | Daily loss limit before stop trading |
| Max Drawdown | 6-10% | Maximum allowable drawdown |
| Min Risk/Reward | 1.5:1 | Minimum R:R ratio required |
| Min Confluence | Score 3+ | Minimum signal strength |
| Max Open Positions | 5-10 | Concurrent positions limit |

---

## Clean Signal Criteria

### Signal Quality Filters

1. **Confluence Score Filter**
   - Minimum: 3 (medium confluence)
   - Preferred: 4 (strong confluence)
   - Blocks weak signals

2. **TF Alignment Filter**
   - Require: 2+ timeframes aligned
   - HTF must match direction
   - Blocks mixed signals

3. **Momentum Filter**
   - ROC must be positive (for longs)
   - ROC must be negative (for shorts)
   - Blocks choppy/range-bound

4. **Volatility Filter**
   - ATR within acceptable range
   - Not too low (no movement)
   - Not too high (explosive/volatile)

---

## Risk Management Filters

### Position Sizing

```python
@dataclass
class RiskConfig:
    account_balance: float = 10000
    risk_per_trade_pct: float = 0.01  # 1%
    max_daily_loss_pct: float = 0.03  # 3%
    max_drawdown_pct: float = 0.06    # 6%
    min_risk_reward_ratio: float = 1.5
    
def calculate_position_size(
    entry_price: float,
    stop_loss: float,
    account_balance: float,
    risk_pct: float
) -> float:
    risk_amount = account_balance * risk_pct
    pips_at_risk = abs(entry_price - stop_loss)
    position_size = risk_amount / pips_at_risk
    return position_size
```

### Stop Loss Rules

| Signal Type | Stop Loss Method |
|-------------|------------------|
| Trend Following | 2x ATR below entry |
| Mean Reversion | Recent swing low/high |
| Confluence | 1.5x ATR or structure |

### Take Profit Rules

| Target | Ratio |
|--------|-------|
| Minimum | 1.5:1 |
| Preferred | 2:1 |
| Scaling | 1:1, 1.5:1, 2:1 |

---

## Proposed CLI Filters

### New Command Line Options

```bash
# Signal quality filters
--min-confluence SCORE      # Minimum confluence score (default: 2)
--min-tf-alignment COUNT    # Minimum aligned TFs (default: 2)
--require-momentum          # ROC must align with direction

# Risk management
--risk-per-trade PERCENT    # Risk per trade (default: 1%)
--max-daily-loss PERCENT    # Max daily loss (default: 3%)
--min-risk-reward RATIO     # Min R:R (default: 1.5)
--atr-multiplier MULT       # SL ATR multiplier (default: 2)

# Position filters
--max-positions COUNT       # Max concurrent (default: 5)
--min-volume VOLUME         # Minimum volume filter

# Execution output
--show-pips-sl              # Show stop loss in pips
--show-pips-tp              # Show take profit in pips
--show-position-size        # Calculate position size
```

---

## Implementation Phases

### Phase 1: Signal Quality Filters

1. Add `--min-confluence` CLI option
2. Add `--min-tf-alignment` filter
3. Add `--require-momentum` flag
4. Filter output to clean signals only

### Phase 2: Risk Calculations

1. Add ATR-based stop loss calculation
2. Add risk/reward ratio calculation
3. Add position size calculator
4. Output clean entry/stop/target levels

### Phase 3: Trade Management

1. Daily loss tracking
2. Drawdown monitoring
3. Max positions enforcement
4. Session-based filtering

---

## Example Output

### Current Output (Clean Signals)

```
┏━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━┓
┃ Pair   ┃ Direction ┃ Pattern            ┃ Score ┃   MR ┃
┡━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━┩
│ EURJPY │ long      │ trend_continuation │     4 │ 0.18 │
│ GBPCAD │ short     │ trend_mr_entry     │     4 │ 0.27 │
└────────┴───────────┴────────────────────┴───────┴──────┘
```

### Proposed Output (With Risk Levels)

```
┏━━━━━━━━┳━━━━━━━━━┳━━━━━━┳━━━━━━┳━━━━━━━┳━━━━━━━━┳━━━━━━━━━┳━━━━━━━┓
┃ Pair   ┃ Dir    ┃ Ent  ┃  SL  ┃  TP   ┃ R:R    ┃ Risk % ┃ Conf  ┃
┡━━━━━━━━╇━━━━━━━━━╫━━━━━━╫━━━━━━╫━━━━━━━╫━━━━━━━━╇━━━━━━━━━╫━━━━━━━┩
│ EURJPY │ LONG   │ 184  │ 182  │ 188   │ 2.0:1  │ 1.0%   │ 4     │
│ GBPCAD │ SHORT  │ 1.84 │ 1.86 │ 1.80  │ 2.0:1  │ 1.0%   │ 4     │
└────────┴────────┴──────┴──────┴───────┴────────┴─────────┴───────┘
```

---

## Technical Implementation

### Files to Modify

1. `tvscreener/cli.py` - Add new CLI arguments
2. `tvscreener/config/settings.py` - Add risk config
3. `tvscreener/lib/screeners/forex_strategy.py` - Add risk calculations
4. `tvscreener/lib/screeners/risk_utils.py` - New risk calculation module

### New Module: risk_utils.py

```python
def calculate_stop_loss(
    entry: float,
    direction: str,
    atr: float,
    multiplier: float = 2.0
) -> float:
    """Calculate ATR-based stop loss."""
    sl_distance = atr * multiplier
    if direction == "long":
        return entry - sl_distance
    return entry + sl_distance

def calculate_take_profit(
    entry: float,
    stop_loss: float,
    direction: str,
    min_rr: float = 2.0
) -> float:
    """Calculate take profit based on R:R ratio."""
    risk = abs(entry - stop_loss)
    reward = risk * min_rr
    if direction == "long":
        return entry + reward
    return entry - reward

def calculate_position_size(
    account_balance: float,
    risk_per_trade: float,
    entry: float,
    stop_loss: float
) -> float:
    """Calculate position size in lots."""
    risk_amount = account_balance * risk_per_trade
    pips_at_risk = abs(entry - stop_loss)
    return risk_amount / pips_at_risk
```

---

## Acceptance Criteria

- [ ] `--min-confluence` filter works
- [ ] `--min-tf-alignment` filter works
- [ ] ATR-based stop loss calculated
- [ ] Risk/reward ratio shown
- [ ] Position size calculated
- [ ] Tests pass

---

## Next Steps

1. Implement Phase 1: Signal quality filters
2. Add risk calculations
3. Test with live data
4. Refine based on results
