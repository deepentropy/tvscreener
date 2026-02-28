---
title: Prettify Scanner Outputs with Strength Symbols
type: feat
date: 2026-02-28
---

# Prettify Scanner Outputs with Strength Symbols

## Overview

Update the CLI output of the Forex scanners (opportunity and strategy) to be clean, clear, and intuitive. Replace the current mix of single emojis (🟢/🔴/⚪) and letters (L/S/N) with unified, math-based multi-sign directional/strength indicator systems. The detailed and summary views will use symbols (`++`, `+`, `=`, `-`, `--`), while the matrix view will use multi-emojis (`🟢🟢`, `🟢`, `⚪`, `🔴`, `🔴🔴`).

## Problem Statement / Motivation

The current output formats have several readability issues:
1. **Detailed View:** Single emojis don't convey the *strength* of the signal (a +0.9 gets the same emoji as a +0.15).
2. **Matrix View:** Letters (L/N/S) require mental parsing and also lack strength indication.
3. **Summary Views:** Just saying "LONG" or "SHORT" doesn't tell the user how strong the overall ensemble or strategy signal is without looking at the raw decimals.

A strength-based symbol system provides a much higher signal-to-noise ratio and allows for quick visual scanning of signal quality.

## Proposed Solution

Implement a shared visual sign system that maps raw scores (-1.0 to 1.0) to clear visual signs representing both direction and strength simultaneously.

### Visual Sign System Design

| Condition | Text Symbol Format | Matrix Emoji Format | Meaning |
|-----------|--------------------|---------------------|---------|
| Score >= 0.5 | `[bold green]++[/bold green]` | `🟢🟢` | Strong Bullish |
| 0.1 <= Score < 0.5 | `[green]+[/green]` | `🟢` | Bullish |
| -0.1 < Score < 0.1 | `[dim white]=[/dim white]` | `⚪` | Neutral |
| -0.5 < Score <= -0.1 | `[red]-[/red]` | `🔴` | Bearish |
| Score <= -0.5 | `[bold red]--[/bold red]` | `🔴🔴` | Strong Bearish |

*Note: For the ROC factor, which is a percentage (often < 0.5), we will scale the thresholds: >= 0.15 for strong bullish (`++`/`🟢🟢`), <= -0.15 for strong bearish (`--`/`🔴🔴`).*

## Technical Approach

### Phase 1: Core Helper Functions

- [x] Add `_get_strength_sign(value: float, is_roc: bool = False) -> str` to `ForexOpportunityScreener` for `+`/`-` text symbols.
- [x] Add `_get_strength_emoji(value: float, is_roc: bool = False) -> str` to `ForexOpportunityScreener` for `🟢🟢`/`🔴🔴` emoji symbols.
- [x] Remove existing `_get_direction_indicator` and `_get_direction_letter` from `ForexOpportunityScreener`.

### Phase 2: Opportunity Scanner Updates

- [x] Update `_render_detailed` to use `_get_strength_sign` instead of single emojis.
  - *Example: `+0.49 + ` instead of `+0.49 🟢`*
- [x] Update `_render_matrix` to use `_get_strength_emoji` instead of letters.
  - *Example: `🟢🟢|🟢|⚪` instead of `L|L|N`*
  - Update the legend text to match the new emojis.
- [x] Update default `_render` (clean summary) to append the ensemble strength sign to the direction string.
  - *Example: `[bold green]LONG ++[/bold green]` based on ENSEMBLE_SCORE.*

### Phase 3: Strategy Scanner Updates

- [x] Add strength indicator logic to `ForexStrategyScanner.print_summary()`.
- [x] Colorize the `Direction` column (`[bold green]LONG[/bold green]`).
- [x] Append a text strength sign (`++`, `+`, etc.) based on the `CONFLUENCE_SCORE` or `HTF_TREND`.
  - For confluence strategy: 3 = `++`, 2 = `+`, 1 = `=`
  - For others: map from the raw SCORE.

## Acceptance Criteria

- [x] Detailed view displays `+`, `++`, `=`, `-`, `--` next to raw scores.
- [x] Matrix view displays pipe-separated multi-emojis (e.g., `🟢🟢|🟢|⚪`).
- [x] Opportunity default summary includes text strength symbols next to LONG/SHORT.
- [x] Strategy summary is color-coded with text strength symbols.
- [x] ROC thresholds are scaled properly so strong signals are achievable.
- [x] Tests pass (including any updates needed for modified methods).

## References & Research

- Existing implementation: `tvscreener/lib/screeners/forex_opportunity.py:417` (matrix rendering)
- Existing implementation: `tvscreener/lib/screeners/forex_opportunity.py:366` (detailed rendering)
- Existing implementation: `tvscreener/lib/screeners/forex_strategy.py:477` (strategy rendering)
