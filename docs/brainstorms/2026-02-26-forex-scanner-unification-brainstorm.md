---
date: 2026-02-26
topic: forex-scanner-unification
---

# Forex Scanner Unification

## What We're Building

Unify the ForexOpportunityScreener and ForexStrategyScanner by:
1. Creating shared base class/mixin for exports
2. Eliminating duplicate code (exports, helpers)
3. Maintaining separation but ensuring consistent interfaces

## Current Architecture

| Component | ForexOpportunityScreener | ForexStrategyScanner |
|-----------|--------------------------|----------------------|
| **Config** | ForexScreenerConfig (36-48) | StrategyConfig (32-46) |
| **Data Fetch** | Own implementation (129-161) | Delegates to OpportunityScreener (76) |
| **Filtering** | Rating, ROC, Volume filters (166-297) | Strategy filters + filter_utils (300-321) |
| **Ranking/Scoring** | ScoringEngine.rank_opportunities (299-305) | Strategy detection (162-283) |
| **Exports** | to_csv, to_json, to_parquet, to_xml (312-404) | Identical methods (318-407) |

## Key Decisions

### 1. Export Methods (~95% duplicate)
Both classes have identical export methods differing only in `label` parameter ("opportunities" vs "signals"). 

**Solution:** Create `ExportMixin` class with generic export methods that accept label as parameter.

### 2. Config Dataclasses
- `ForexScreenerConfig`: rating_filters, roc_filter, volume_filter, contract_type, scoring_config
- `StrategyConfig`: min_confluence, include_strategies, direction, min_volume, max_atr

**Solution:** Keep separate configs (different concerns), but extract common fields to shared base or use composition.

### 3. Data Fetching Pipeline
ForexStrategyScanner creates ForexOpportunityScreener internally (line 60-68) to fetch data.

**Solution:** Create abstract base class `BaseForexScanner` with data fetching, let each scanner implement strategy-specific detection.

### 4. CLI Entry Points
Currently separate: `run_opportunity_scan()` and `run_strategy_scan()` in cli.py.

**Solution:** Keep separate CLI commands but unify underlying scanner instantiation via factory.

## Proposed Approaches

### Approach A: ExportMixin + Shared Config (Recommended)

Create mixin for exports, extract common config fields, keep scanners separate.

**Pros:**
- Minimal refactoring
- Maintains separation of concerns
- Quick win on export duplication

**Cons:**
- Doesn't fully unify architecture

**Best when:** Gradual improvement, low risk

### Approach B: Abstract Base Class

Create `BaseForexScanner` abstract class with data fetching, scoring, and export. Subclass for opportunity/strategy.

**Pros:**
- True shared architecture
- Enforces consistent interface
- Single source of truth for common logic

**Cons:**
- Larger refactoring
- May force unwanted coupling

**Best when:** Long-term maintainability is priority

### Approach C: Strategy as Filter

Treat strategy detection as another filter layer on top of opportunity scoring.

**Pros:**
- Unified pipeline
- Flexible composition

**Cons:**
- Significant redesign
- May lose strategy-specific nuances

**Best when:** Strategy detection needs to be optional/composable

## Open Questions

- Should StrategyScanner inherit from OpportunityScreener or compose it?
- How to handle different output columns between scanners in unified exports?
- Should CLI maintain separate commands or unified with mode flag?

## Next Steps

→ `/workflows:plan` for implementation details
