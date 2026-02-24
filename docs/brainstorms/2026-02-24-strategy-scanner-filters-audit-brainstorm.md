---
date: 2026-02-24
topic: strategy-scanner-filters-audit
---

# Strategy Scanner Filters & Pipeline Audit

## What We're Building

A comprehensive code review and enhancement of the forex strategy scanner filters and selection pipelines. This includes:
- Auditing existing filter logic in `forex_strategy.py` and `forex_opportunity.py`
- Fixing identified bugs and inconsistencies
- Proposing architectural improvements for maintainability

## Why This Approach

The comprehensive approach was chosen to address all 7 identified issues systematically, ensuring the codebase is consistent, correct, and maintainable. The issues range from correctness bugs (ignored CLI filters) to architectural concerns (duplicate filter patterns).

## Key Decisions

### Issues to Fix

| # | Issue | Severity | File(s) |
|---|-------|----------|---------|
| 1 | Unused `merge_with_cli_args()` function | Low | `config/loader.py` |
| 2 | Opportunity scanner ignores CLI filters (`--min-volume`, `--max-atr`, `--min-ma-rating`) | **High** | `cli.py`, `forex_opportunity.py` |
| 3 | Two different filter patterns (dataclass vs method calls) | Medium | Both screeners |
| 4 | Redundant filtering at two levels | Medium | Both screeners |
| 5 | Inconsistent dataclass definitions (`frozen`/`slots`) | Low | Both config classes |
| 6 | Implicit ATR/RSI field inclusion logic | Low | `forex_strategy.py` |
| 7 | No CLI arg validation (can't distinguish "not provided" from default) | Medium | `cli.py` |

### Proposed Fixes

1. **Remove or wire `merge_with_cli_args()`**: Either remove the dead function or integrate it properly into CLI flow
2. **Pass all CLI filter args to opportunity scanner**: Ensure `--min-volume`, `--max-atr`, `--min-ma-rating` work for both scanners
3. **Unify filter patterns**: Choose one approach (dataclass filters or method calls) and standardize
4. **Eliminate redundant filtering**: Apply filters once at appropriate layer
5. **Standardize dataclass definitions**: Both configs should use same mutability/performance settings
6. **Make ATR/RSI inclusion explicit**: Add explicit flags to StrategyConfig rather than implicit derivation
7. **Use sentinel values for CLI args**: Distinguish "not provided" from default using `None` sentinel

## Open Questions

- Should we keep both `ForexOpportunityScreener` and `ForexStrategyScanner` as separate classes, or unify them?
- Should we add unit tests for the CLI integration paths?

## Next Steps

→ `/workflows:plan` for implementation details
