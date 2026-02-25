---
title: Enhance strategy screeners with volume, volatility, and MA filters
date: 2026-02-23
status: brainstorm
tags: [forex, strategy, filters, enhancement]
---

# Enhance Strategy Screeners

## What We're Building

Enhance the existing strategy screeners with additional filtering capabilities:
- Volume threshold filter (min volume to filter illiquid pairs)
- Volatility filter (exclude extreme volatility)
- MA rating filter (require strong MA alignment)
- Mean reversion signals (RSI, MACD, Bollinger positions)

All configurable via CLI arguments.

## Why This Approach

The existing strategy screeners (`ForexStrategyScanner`) detect patterns but lack quantitative filters. Adding these filters will:
- Improve signal quality by filtering weak signals
- Allow users to customize based on their risk tolerance
- Provide more actionable trading signals

## Key Decisions

### Filter Architecture

```
StrategyConfig (existing)
├── min_confluence: int
├── include_strategies: tuple
├── direction: Direction
├── trend_threshold: float
├── mr_threshold: float
└── min_roc: float | None

NEW FIELDS TO ADD:
├── min_volume: float | None      # Minimum average volume
├── max_volatility: float | None  # Maximum volatility %
├── min_ma_rating: float | None  # Minimum MA rating (-2 to 2)
└── mean_reversion_signals: list  # RSI, MACD, BB positions
```

### CLI Arguments to Add

```bash
--min-volume VOLUME          # Minimum average volume
--max-volatility VOLATILITY  # Maximum volatility %
--min-ma-rating RATING       # Minimum MA rating
--mean-reversion SIGNAL      # Add mean reversion signals (rsi_oversold/rsi_overbought)
```

### Strategy-Specific Filters

| Strategy | Filters |
|----------|---------|
| Trend Following | min_volume, min_ma_rating |
| Mean Reversion | max_volatility, mean_reversion_signals |
| Hybrid | min_volume, min_ma_rating, max_volatility |
| Breakout | min_volume, max_volatility |

## Open Questions

1. **Default values?** - Need sensible defaults for each filter
2. **Volatility field availability?** - Need to verify ForexField has volatility data
3. **Integration with existing filters?** - How to combine with existing confluence filters

## Next Steps

1. Run `/workflows:plan` to create implementation plan
2. Implement CLI arguments
3. Add filter methods to StrategyConfig
4. Add validation tests for new filters
