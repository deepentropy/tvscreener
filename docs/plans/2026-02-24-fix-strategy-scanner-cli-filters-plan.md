---
title: fix: strategy scanner CLI filters ignored and filter pipeline inconsistencies
type: fix+refactor
date: 2026-02-24
---

# Fix Strategy Scanner CLI Filters and Filter Pipeline Inconsistencies

## Overview

Fix critical bugs and architectural inconsistencies in the forex strategy scanner filters and CLI integration. The CLI ignores user-provided filter arguments, and the codebase uses two different filter application patterns that create maintenance overhead.

## Problem Statement

### Bug: CLI Filter Args Ignored

When users provide filter arguments via CLI (e.g., `--min-confluence 2`), the values are overwritten by settings defaults. This makes the CLI ineffective for controlling filter behavior.

**Location:** `tvscreener/cli.py:216-219`

```python
# BUG: Unconditionally overwrites CLI args!
args.min_confluence = settings.min_confluence     # Line 216
args.trend_threshold = settings.trend_threshold   # Line 217
args.mr_threshold = settings.mr_threshold         # Line 218
args.min_roc = settings.min_roc                  # Line 219
```

### Dead Code

The function `merge_with_cli_args()` in `config/loader.py` was meant to handle this but was never integrated into the CLI flow.

### Inconsistent Filter Patterns

Two different approaches exist:
1. **Dataclass filters**: `RatingFilter`, `RocFilter`, `VolumeFilter` in `ForexScreenerConfig`
2. **Method calls**: `_apply_volume_filter()`, `_apply_atr_filter()`, etc. in `ForexStrategyScanner`

This duplication increases maintenance burden and creates confusion.

## Proposed Solution

### Fix 1: CLI Arg Precedence (Critical)

Apply the same pattern as lines 209-214 to lines 216-219:

```python
# Should be:
if args.min_confluence is None:
    args.min_confluence = settings.min_confluence
if args.trend_threshold is None:
    args.trend_threshold = settings.trend_threshold
# ... etc
```

### Fix 2: Remove Dead Code

`merge_with_cli_args()` has been removed from `config/loader.py` to keep the configuration path focused on `load_settings()`.

### Fix 3: Unify Filter Patterns

Choose one approach (recommended: method calls) and standardize across both scanners.

### Fix 4: Consistent Config Dataclasses

Make `ForexScreenerConfig` use same mutability as `StrategyConfig`.

### Fix 5: Explicit ATR/RSI Flags

Add explicit flags to `StrategyConfig` rather than implicit derivation.

### Fix 6: Sentinel Values for CLI Args

Ensure CLI arguments only override settings when explicitly provided, otherwise fall back to defaults.

## Technical Considerations

- **Backward compatibility**: Must ensure existing behavior is preserved for users not using CLI
- **Testing**: Add integration tests for CLI arg precedence
- **Config flow**: Consider if settings should only apply when CLI args are absent
- **Performance**: Add `slots=True` to frozen dataclasses for better performance (see best practices)

## Best Practices Research

### CLI Config Precedence

Standard precedence order: `CLI args > environment variables > config file (YAML) > hardcoded defaults`

Use pydantic-settings `model_fields_set` to only override fields explicitly set in env/CLI.

**External Docs:**
- https://docs.pydantic.dev/latest/concepts/pydantic_settings/ - Official pydantic-settings docs

### Dataclass Performance

- `frozen=True` adds ~2.4x overhead for instantiation
- Add `slots=True` for memory efficiency and slight speed improvement
- Keep `frozen=True` for filter configs (used as dict keys, need immutability)

**External Docs:**
- https://docs.python.org/3/library/dataclasses.html - Official dataclass docs

### Filter Design Patterns

Consider adopting a pipeline pattern for composable filter chains:

```python
class FilterPipeline:
    def __init__(self):
        self.filters: list[DataFrameFilter] = []
    
    def add_filter(self, filter_: DataFrameFilter) -> 'FilterPipeline':
        self.filters.append(filter_)
        return self  # Enable chaining
    
    def apply(self, df: pd.DataFrame) -> pd.DataFrame:
        for filter_ in self.filters:
            df = filter_.apply(df)
        return df
```

## Acceptance Criteria

- [x] CLI args `--min-confluence`, `--trend-threshold`, `--mr-threshold`, `--min-roc` take precedence over settings
- [x] `merge_with_cli_args()` removed to simplify config loading
- [x] Filter patterns are unified via shared helpers
- [x] Both config dataclasses use `frozen` + `slots`
- [x] ATR/RSI inclusion is explicit in `StrategyConfig`
- [x] All CLI arg handling uses sentinel pattern consistently
- [x] Tests pass: `uv run pytest -q`

## Dependencies & Risks

- **Risks**: Changing filter behavior could affect existing users
- **Mitigation**: Add tests before making changes; verify with existing CLI runs

## Implementation Phases

### Phase 1: Critical Bug Fix

1. Fix CLI arg precedence in `cli.py:216-219`
2. Add test to verify CLI args take precedence

### Phase 2: Cleanup

3. Remove or integrate `merge_with_cli_args()`
4. Standardize config dataclass definitions

### Phase 3: Refactor

5. Unify filter application patterns
6. Make ATR/RSI inclusion explicit

## References

### Internal References

- Related brainstorm: `docs/brainstorms/2026-02-24-strategy-scanner-filters-audit-brainstorm.md`
- CLI code: `tvscreener/cli.py:200-219`
- Config loader: `tvscreener/config/loader.py:53-81`
- Strategy scanner: `tvscreener/lib/screeners/forex_strategy.py`
- Opportunity scanner: `tvscreener/lib/screeners/forex_opportunity.py`

### External References

- pydantic-settings: https://docs.pydantic.dev/latest/concepts/pydantic_settings/
- Python dataclasses: https://docs.python.org/3/library/dataclasses.html
- jsonargparse (alternative): https://jsonargparse.readthedocs.io/
- Hydra config composition: https://hydra.cc/docs/tutorials/basic/your_first_app/
