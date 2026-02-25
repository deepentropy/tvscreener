---
title: "Run Forex Screener CLI with uv"
type: plan
date: 2026-02-22
status: planned
---

# Run Forex Screener CLI with uv

## Goal

Run the forex screener CLI for majors and minors using uv run commands (no pip, uv pip, or global python).

## CLI Options

| Argument | Description | Values |
|----------|-------------|---------|
| `--scanner` | Scanner type | `opportunity`, `strategy` |
| `--asset-type` | Asset class | `forex`, `stocks`, `commodity`, `crypto` |
| `--universe` | Forex subset | `majors`, `minors`, `all` |
| `--pairs` | Specific pairs | list |
| `--timeframes` | Timeframes | comma-separated (default: 240,60,15) |
| `--strategy` | Strategy filter | `all`, `trend`, `mean_reversion`, `hybrid`, `breakout` |
| `--filter` | Direction filter | `long`, `short` |
| `--output` | Output file | csv/json path |

## Commands to Run

### 1. Opportunity Screener - All Pairs

```bash
uv run python -m tvscreener.cli --scanner opportunity --universe all
```

### 2. Strategy Scanner - All Pairs (default)

```bash
uv run python -m tvscreener.cli --scanner strategy --universe all
```

### 3. Strategy Scanner - Majors Only

```bash
uv run python -m tvscreener.cli --scanner strategy --universe majors
```

### 4. Strategy Scanner - Minors Only

```bash
uv run python -m tvscreener.cli --scanner strategy --universe minors
```

### 5. Strategy Scanner - Specific Strategy

```bash
# Trend following only
uv run python -m tvscreener.cli --scanner strategy --universe all --strategy trend

# Mean reversion only
uv run python -m tvscreener.cli --scanner strategy --universe all --strategy mean_reversion

# Breakout only
uv run python -m tvscreener.cli --scanner strategy --universe all --strategy breakout

# Hybrid only
uv run python -m tvscreener.cli --scanner strategy --universe all --strategy hybrid
```

### 6. Filter by Direction

```bash
# Long signals only
uv run python -m tvscreener.cli --scanner strategy --universe all --filter long

# Short signals only
uv run python -m tvscreener.cli --scanner strategy --universe all --filter short
```

### 7. Output to File

```bash
# Save to CSV
uv run python -m tvscreener.cli --scanner strategy --universe all -o results.csv

# Save to JSON
uv run python -m tvscreener.cli --scanner strategy --universe all -o results.json
```

### 8. Custom Timeframes

```bash
# 4H and 1H only
uv run python -m tvscreener.cli --scanner strategy --universe all --timeframes 240,60

# All three
uv run python -m tvscreener.cli --scanner strategy --universe all --timeframes 240,60,15
```

## Expected Output

The CLI should output:
- Progress indicator during data fetch
- Summary table with top opportunities
- Total count of results
- (Optional) CSV/JSON file if --output specified

## Verification

After each run, verify:
1. Results count matches expected pairs
2. Strategy breakdown is reasonable
3. Confluence levels are populated
4. Output file is created if specified
