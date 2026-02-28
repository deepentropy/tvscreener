---
title: Prettify Scanner Outputs with Strength Symbols
type: feat
date: 2026-02-28
---

# Prettify Scanner Outputs with Strength Symbols

## Overview

Update the CLI output of the Forex scanners (opportunity and strategy) to be clean, clear, and intuitive. All views (detailed, matrix, and summary) use unified, math-based multi-sign directional/strength indicator systems (`++`, `+`, `=`, `-`, `--`).

## Problem Statement / Motivation

The current output formats had several readability issues:
1. **Detailed View:** Emojis were distracting and didn't convey the *strength* of the signal.
2. **Matrix View:** Letters (L/N/S) or multi-emojis caused alignment issues and required mental parsing.
3. **Summary Views:** Just saying "LONG" or "SHORT" didn't tell the user how strong the overall signal was.

A clean, symbol-based system (like `++` for strong long, `-` for weak short) is standard in professional trading terminals and provides a much higher signal-to-noise ratio.

## Proposed Solution

Implemented a shared visual sign system that maps raw scores (-1.0 to 1.0) to clear visual signs representing both direction and strength simultaneously.

### Visual Sign System Design

| Condition | Text Symbol Format | Meaning |
|-----------|--------------------|---------|
| Score >= 0.5 | `[bold green]++[/bold green]` | Strong Bullish |
| 0.1 <= Score < 0.5 | `[green]+ [/green]` | Bullish |
| -0.1 < Score < 0.1 | `[dim white]= [/dim white]` | Neutral |
| -0.5 < Score <= -0.1 | `[red]- [/red]` | Bearish |
| Score <= -0.5 | `[bold red]--[/bold red]` | Strong Bearish |

*Note: For the ROC factor, which is a percentage (often < 0.5), thresholds are scaled: >= 0.15 for strong bullish (`++`), <= -0.15 for strong bearish (`--`).*

## Technical Approach

### Phase 1: Core Helper Functions

- [x] Add `_get_strength_sign(value: float, is_roc: bool = False, pad: bool = True) -> str` to `ForexOpportunityScreener`.
- [x] Use padding to ensure perfect monospace alignment in tables.

### Phase 2: Opportunity Scanner Updates

- [x] Update `_render_detailed` to use `_get_strength_sign`.
- [x] Update `_render_matrix` to use `_get_strength_sign` with pipe separators for a clean grid.
- [x] Update default `_render` (clean summary) to append the ensemble strength sign to the direction string.

### Phase 3: Strategy Scanner Updates

- [x] Add `_get_strength_sign(score: float, direction: str) -> str` to `ForexStrategyScanner`.
- [x] Colorize the `Direction` column and append strength signs based on `CONFLUENCE_SCORE`.
- [x] Base signs on `CONFLUENCE_SCORE` (1-3) to avoid oxymorons like `LONG =`.

## Acceptance Criteria

- [x] Detailed view displays `+`, `++`, `=`, `-`, `--` next to raw scores.
- [x] Matrix view displays pipe-separated symbols with perfect vertical alignment.
- [x] Opportunity default summary includes text strength symbols next to LONG/SHORT.
- [x] Strategy summary is color-coded with strength symbols.
- [x] ROC thresholds are scaled properly so strong signals are achievable.
- [x] Tests pass and output is visually audited.

## References & Research

- Final implementation: `tvscreener/lib/screeners/forex_opportunity.py`
- Final implementation: `tvscreener/lib/screeners/forex_strategy.py`
