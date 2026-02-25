---
title: "feat: expand opportunity mode with full feature parity"
type: feat
date: 2026-02-25
---

# Expand Opportunity Mode with Full Feature Parity

## Overview

Add full feature parity to opportunity scanner by wiring CLI filters, custom scoring, config persistence, and export improvements. The audit found opportunity mode lacks many features available in strategy mode - this plan addresses all gaps.

## Problem Statement

The `run_opportunity_scan()` function (cli.py:60-93) only passes `contract_type` to `ForexScreenerConfig`, ignoring all other filter settings from YAML/CLI. Meanwhile, strategy scanner has full filter support. This creates a feature parity gap.

### Current Gaps

| Gap | Location | Impact |
|-----|----------|--------|
| CLI filters not wired | cli.py:68 | `--min-volume`, `--max-atr`, `--min-ma-rating` ignored |
| Scoring weights not customizable | cli.py:68 | No CLI way to adjust trend/ma/osc/roc weights |
| Timeframe weights hardcoded | constants/forex.py | Cannot adjust 15/60/240 weights |
| Export formats limited | forex_opportunity.py:303-319 | Only CSV/JSON supported |
| No config persistence | cli.py | No save/load config flags |

## Proposed Solution

### Phase 1: Wire Filters to Opportunity Mode

1. **Update `run_opportunity_scan()`** to pass all filter args to `ForexScreenerConfig`:
   - Wire `--min-volume`, `--max-atr`, `--min-ma-rating` to `volume_filter`, `include_atr`, etc.
   - Reuse `filter_utils` helpers for consistency

2. **Add opportunity-specific YAML settings**:
   ```yaml
   opportunity:
     min_volume: null
     max_atr: null
     min_ma_rating: null
     scoring_weights:
       trend: 0.4
       ma: 0.3
       osc: 0.2
       roc: 0.1
   ```

3. **Update `ScreenerSettings`** in config/settings.py to include opportunity section

### Phase 2: Custom Scoring Configuration

1. **Add CLI args for scoring weights**:
   - `--trend-weight`, `--ma-weight`, `--osc-weight`, `--roc-weight`
   - `--timeframe-weights` (e.g., "240:0.5,60:0.3,15:0.2")

2. **Add YAML config support**:
   - Default scoring weights in tvscreener.yaml
   - ENV override support via TVSCREENER_TREND_WEIGHT etc.

3. **Wire to ScoringEngine** via `ScoringConfig`

### Phase 3: Export Improvements

1. **Add new export formats**:
   - `--output file.parquet` → add parquet support
   - `--output file.xml` → add XML support

2. **Include config in exports**:
   - Add metadata header with filter/scoring config used
   - JSON exports include `config` key with settings

### Phase 4: Config Persistence

1. **Add CLI flags**:
   - `--save-config path.yaml` - Save current config to file
   - `--load-config path.yaml` - Load config from file

2. **Support config inheritance**:
   - Load base config, override with CLI args
   - Validate loaded config matches expected schema

## Technical Considerations

### Affected Files

| File | Changes |
|------|---------|
| `tvscreener/cli.py` | Wire filters, add scoring args, add save/load flags |
| `tvscreener/lib/screeners/forex_opportunity.py` | Accept filters in config, pass to engine |
| `tvscreener/config/settings.py` | Add opportunity section |
| `tvscreener/score.py` | Support custom ScoringConfig from CLI |
| `tvscreener.yaml` | Add opportunity section |
| `tvscreener/lib/screeners/export_helpers.py` | Add parquet/XML exporters |

### Backward Compatibility

- All new CLI args should have sensible defaults (current behavior)
- YAML config additions should be optional
- Existing `--output` behavior unchanged

## Acceptance Criteria

### Phase 1 - Filter Wiring
- [x] `--min-volume` filters opportunity results
- [x] `--max-atr` filters by ATR when `include_atr` enabled
- [x] `--min-ma-rating` filters by MA rating
- [x] YAML `opportunity.min_volume` applied when CLI arg not provided

### Phase 2 - Custom Scoring
- [x] `--trend-weight` adjusts trend factor in ensemble score
- [x] `--timeframe-weights` overrides default 240:0.2/60:0.3/15:0.5
- [x] YAML scoring_weights override defaults

### Phase 3 - Export
- [x] `--output file.parquet` exports to Parquet format
- [x] `--output file.xml` exports to XML format
- [x] Exports include config metadata

### Phase 4 - Config Persistence
- [x] `--save-config saved.yaml` writes current config
- [x] `--load-config saved.yaml` loads and applies config
- [x] Loaded config + CLI args merge correctly (CLI wins)

### Quality
- [x] All tests pass: `uv run pytest -q`
- [x] Linting passes: `uvx ruff check`
- [x] CLI help updated with all new args

## Dependencies

- Existing `filter_utils.py` for shared filter functions
- `ScoringEngine` for custom scoring
- `export_helpers` for new export formats

## Risks

- **Complexity**: Adding too many options may confuse users → keep sensible defaults
- **Testing**: Need integration tests for filter + scoring interaction → add tests
- **Performance**: Custom weights may slow scoring → benchmark if needed

## References

- Strategy scanner implementation: `tvscreener/lib/screeners/forex_strategy.py`
- Filter classes: `tvscreener/filter.py:52-72`
- Scoring config: `tvscreener/score.py:9-19`
- Current CLI: `tvscreener/cli.py:60-93`
