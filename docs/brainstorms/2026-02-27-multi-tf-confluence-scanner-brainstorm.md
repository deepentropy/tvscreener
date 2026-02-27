---
date: 2026-02-27
topic: multi-tf-confluence-scanner
---

# Multi-Timeframe Confluence Scanner

## What We're Building
Enhance the forex strategy scanner to detect sophisticated market conditions using multi-timeframe and multi-factor confluence. The scanner will:

1. **Auto-detect all signal types** with unified confluence scoring
2. **Prioritize mean reversion entries** in LTF/STF when aligned with HTF trend
3. **Ranking system** to score and sort all pairs by confluence strength

## Confluence Combos to Support

| Combo | HTF (240) | STF (60) | LTF (15) | Description |
|-------|------------|----------|----------|-------------|
| Trend Continuation | Trend | Trend | Trend | Classic trend following |
| Trend + MR Entry | Trend | MR | MR | Trend with pullback entry |
| MR Reversal | MR | MR | MR | Multi-TF mean reversion |
| Trend Pullback | Trend | Trend | MR | Shallow pullback |
| Deep Pullback | Trend | MR | MR | Strong pullback, wait for confirmation |

## Why This Approach

Current scanner has separate detection methods (trend_following, mean_reversion, hybrid, breakout) that run independently. This misses opportunities where:
- HTF is trending but LTF is oversold (excellent entry)
- Multiple TFs show mean reversion signals (high probability reversal)

The new approach treats all signals as "confluence patterns" and scores them by:
1. Direction alignment across TFs
2. Signal type alignment (trend vs mean reversion)
3. Magnitude of LTF/STF extremity

## Key Decisions

- **Unified scoring**: Single CONFLUENCE_SCORE reflects overall signal strength
- **MR priority**: When LTF/STF show oversold/overbought, boost score
- **Ranking**: All pairs ranked by confluence, not filtered
- **Backward compatible**: Keep existing strategies, add new combo detection

## Signal Types

| Signal | Logic | Entry Quality |
|--------|-------|---------------|
| Trend Continuation | HTF+STF+LTF all trending same direction | Standard |
| MR Entry | HTF trending + LTF/STF at extremes | **High** |
| Pullback | HTF trend + LTF reversal | Medium |
| Reversal | All TFs at extremes opposite to prior trend | High |

## Open Questions

- Should breakout be included in confluence scoring?
- How to weight MR vs Trend signals in the same direction?
- Minimum threshold for "extremity" in LTF/STF?

## Next Steps
→ `/workflows:plan` for implementation details
