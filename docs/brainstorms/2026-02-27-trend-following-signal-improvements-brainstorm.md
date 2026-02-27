---
date: 2026-02-27
topic: trend-following-signal-improvements
---

# Trend Following Signal Improvements

## What We're Building
Improve the trend following signal detection in ForexStrategyScanner to:
1. Use 3-TF alignment (240, 60, 15) instead of just 2-TF
2. Make confluence score meaningful (reflect signal strength, not just alignment)
3. Add configurable trend threshold to filter weak signals
4. Unify DIRECTION calculation across all strategies

## Why This Approach
- Existing 2-TF logic already filters aligned signals, making confluence always = 2
- Adding LTF (15) provides higher quality signals where all 3 TFs agree
- Configurable threshold lets users filter noise (e.g., require 0.3+ instead of 0.0)
- Centralizing DIRECTION reduces maintenance burden and bugs

## Key Decisions
- **3-TF alignment**: Score based on count of aligned TFs (1-3), not binary
- **Magnitude weighting**: Consider signal strength, not just direction
- **Default threshold 0.2**: Balance between sensitivity and noise filtering
- **Unified direction method**: Single `calculate_direction()` for all strategies

## Open Questions
- Should 15m be required or optional for trend following?
- How to handle magnitude weighting - sum of values or count above threshold?
- Backward compatibility for existing users relying on confluence=2?

## Next Steps
→ `/workflows:plan` for implementation details
