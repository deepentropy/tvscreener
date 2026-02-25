---
date: 2026-02-25
topic: opportunity-mode-full-feature-expansion
---

# Opportunity Mode Full Feature Expansion

## What We're Building

Expand opportunity scanner with full feature parity to strategy scanner:
- Wire CLI filters (volume, ATR, rating) to opportunity mode
- Add new ranking signals
- Add custom scoring weights
- Add export improvements
- Add save/load configs
- Extend existing YAML config for opportunity mode

## Why This Approach

The audit found opportunity mode lacks many features available in strategy mode. Expanding opportunity mode with full feature parity gives users a more powerful ranking tool while keeping the simpler API for quick scans.

## Key Decisions

- **Config**: Extend existing `tvscreener.yaml` with opportunity-specific settings (not a separate file)
- **Filters**: Wire existing CLI args (`--min-volume`, `--max-atr`, `--min-ma-rating`) to opportunity mode
- **Scoring**: Allow custom weight configuration via YAML + CLI overrides
- **Export**: Add more export formats (XML, parquet) and include config in export
- **Config persistence**: Add `--save-config` and `--load-config` flags

## Open Questions

- Should opportunity mode support the same strategy detection as strategy scanner?
- How to handle config file conflicts when loading saved configs?

## Next Steps

→ `/workflows:plan` for implementation details
