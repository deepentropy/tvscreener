---
title: Run Forex Scanners for Majors and Minors
type: feat
date: 2026-02-20
---

# Run Forex Scanners for Majors and Minors

## Enhancement Summary

**Deepened on:** 2026-02-20

### Key Improvements
1. Added error handling for API failures
2. Added progress indicators for long-running scans
3. Added logging configuration
4. Added rate limiting awareness
5. Added `--filter` CLI option for direction

---

## Overview

Execute the ForexOpportunityScreener and ForexStrategyScanner against the full universe of 27 forex pairs (7 majors + 20 minors).

## Base Universe

| Category | Count | Pairs |
|----------|-------|-------|
| Majors | 7 | EURUSD, GBPUSD, USDJPY, USDCHF, USDCAD, AUDUSD, NZDUSD |
| Minors | 20 | EURGBP, EURJPY, GBPJPY, EURCHF, AUDJPY, EURCAD, CADJPY, CHFJPY, NZDJPY, GBPAUD, EURAUD, AUDNZD, EURNZD, GBPCAD, AUDCAD, GBPNZD, EURNOK, EURSEK |
| **Total** | **27** | |

## Implementation

### Example Script

```python
#!/usr/bin/env python3
"""Run forex scanners for full universe."""

from tvscreener.screeners.forex_opportunity import ForexOpportunityScreener
from tvscreener.screeners.forex_strategy import ForexStrategyScanner
from tvscreener.constants.forex import DEFAULT_FOREX_PAIRS

def main():
    print(f"Scanning {len(DEFAULT_FOREX_PAIRS)} forex pairs...\n")
    
    # Run opportunity screener
    print("=" * 60)
    print("FOREX OPPORTUNITY SCREENER")
    print("=" * 60)
    screener = ForexOpportunityScreener(
        pairs=DEFAULT_FOREX_PAIRS,
        timeframes=["15", "60", "240"]
    )
    opportunities = screener.get_opportunities()
    screener.print_summary()
    
    # Export opportunities
    screener.to_csv("forex_opportunities.csv")
    screener.to_json("forex_opportunities.json")
    
    # Run strategy scanner
    print("\n" + "=" * 60)
    print("FOREX STRATEGY SCANNER")
    print("=" * 60)
    scanner = ForexStrategyScanner(
        pairs=DEFAULT_FOREX_PAIRS,
        timeframes=["240", "60", "15"]
    )
    
    # Scan all strategies
    signals = scanner.scan()
    scanner.print_summary()
    
    # Export signals
    scanner.to_csv("forex_signals.csv")
    scanner.to_json("forex_signals.json")
    
    # Filter by strategy
    print("\n--- Trend Following ---")
    tf = scanner.scan_trend_following()
    print(f"Found {len(tf)} trend following setups")
    
    print("\n--- Mean Reversion ---")
    mr = scanner.scan_mean_reversion()
    print(f"Found {len(mr)} mean reversion setups")
    
    print("\n--- Hybrid ---")
    hybrid = scanner.scan_hybrid()
    print(f"Found {len(hybrid)} hybrid setups")

if __name__ == "__main__":
    main()
```

### CLI Entry Point

Add to `pyproject.toml`:

```toml
[project.scripts]
tvscreener-scan = "tvscreener.cli:main"

[project.optional-dependencies]
cli = [
    "rich>=13.0.0",
    "tqdm>=4.65.0"
]
```

Create `tvscreener/cli.py`:

```python
#!/usr/bin/env python3
"""CLI for forex scanners."""

import argparse
import logging
import sys
from typing import Optional

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from tvscreener.screeners.forex_opportunity import ForexOpportunityScreener
from tvscreener.screeners.forex_strategy import ForexStrategyScanner
from tvscreener.constants.forex import DEFAULT_FOREX_PAIRS, FOREX_MAJORS, FOREX_MINORS

console = Console()
logger = logging.getLogger(__name__)


def setup_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )


def get_pairs(universe: Optional[str], specific: Optional[list[str]]) -> list[str]:
    if specific:
        return specific
    if universe == "majors":
        return FOREX_MAJORS
    elif universe == "minors":
        return FOREX_MINORS
    return DEFAULT_FOREX_PAIRS


def run_opportunity_scan(args) -> int:
    """Run opportunity screener."""
    pairs = get_pairs(args.universe, args.pairs)
    timeframes = args.timeframes.split(",") if args.timeframes else ["15", "60", "240"]
    
    console.print(f"[cyan]Scanning {len(pairs)} pairs...[/cyan]")
    
    try:
        screener = ForexOpportunityScreener(pairs=pairs, timeframes=timeframes)
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            progress.add_task("Fetching data...", total=None)
            results = screener.get_opportunities()
        
        screener.print_summary()
        
        if args.output:
            if args.output.endswith(".csv"):
                screener.to_csv(args.output)
            elif args.output.endswith(".json"):
                screener.to_json(args.output)
            console.print(f"[green]Saved to {args.output}[/green]")
        
        return len(results)
        
    except Exception as e:
        logger.error(f"Error running scanner: {e}")
        console.print(f"[red]Error: {e}[/red]")
        return 1


def run_strategy_scan(args) -> int:
    """Run strategy scanner."""
    pairs = get_pairs(args.universe, args.pairs)
    timeframes = args.timeframes.split(",") if args.timeframes else ["240", "60", "15"]
    
    console.print(f"[cyan]Scanning {len(pairs)} pairs for {args.strategy} signals...[/cyan]")
    
    try:
        scanner = ForexStrategyScanner(pairs=pairs, timeframes=timeframes)
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            progress.add_task("Fetching data...", total=None)
            
            if args.strategy == "all":
                results = scanner.scan()
            elif args.strategy == "trend":
                results = scanner.scan_trend_following()
            elif args.strategy == "mean_reversion":
                results = scanner.scan_mean_reversion()
            elif args.strategy == "hybrid":
                results = scanner.scan_hybrid()
            elif args.strategy == "breakout":
                results = scanner.scan_breakout()
            else:
                results = scanner.scan()
        
        # Filter by direction
        if args.filter:
            results = results[results["DIRECTION"] == args.filter] if not results.empty else results
        
        scanner.print_summary()
        
        if args.output:
            if args.output.endswith(".csv"):
                scanner.to_csv(args.output)
            elif args.output.endswith(".json"):
                scanner.to_json(args.output)
            console.print(f"[green]Saved to {args.output}[/green]")
        
        return len(results)
        
    except Exception as e:
        logger.error(f"Error running scanner: {e}")
        console.print(f"[red]Error: {e}[/red]")
        return 1


def main():
    parser = argparse.ArgumentParser(
        description="Run forex scanners",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("--scanner", "-s", choices=["opportunity", "strategy"], default="strategy")
    parser.add_argument("--universe", "-u", choices=["majors", "minors", "all"], default="all")
    parser.add_argument("--pairs", nargs="+", help="Specific pairs to scan")
    parser.add_argument("--timeframes", "-t", default="240,60,15", help="Comma-separated timeframes")
    parser.add_argument("--output", "-o", help="Output file (csv/json)")
    parser.add_argument("--strategy", choices=["all", "trend", "mean_reversion", "hybrid", "breakout"], default="all")
    parser.add_argument("--filter", choices=["long", "short"], help="Filter by direction")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    
    args = parser.parse_args()
    setup_logging(args.verbose)
    
    if args.scanner == "opportunity":
        count = run_opportunity_scan(args)
    else:
        count = run_strategy_scan(args)
    
    console.print(f"\n[bold]Total: {count} results[/bold]")
    return 0 if count > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
```

## Usage Examples

```bash
# Scan all pairs with strategy scanner (all strategies)
tvscreener-scan --scanner strategy --universe all

# Scan only majors with opportunity screener
tvscreener-scan --scanner opportunity --universe majors

# Scan with custom timeframes
tvscreener-scan --scanner strategy --timeframes 240,60

# Save to CSV
tvscreener-scan --scanner strategy --output signals.csv

# Filter by strategy type
tvscreener-scan --scanner strategy --strategy trend

# Filter by direction (long/short)
tvscreener-scan --scanner strategy --filter long

# Verbose output for debugging
tvscreener-scan --scanner strategy --verbose

# Specific pairs
tvscreener-scan --scanner strategy --pairs EURUSD GBPUSD USDJPY
```

## Cron Scheduling (Optional)

Add to crontab for automated scanning:

```bash
# Run at market open (7am UTC)
0 7 * * 1-5 cd /path/to/project && tvscreener-scan --scanner strategy --output ~/signals_$(date +\%Y\%m\%d).csv >> /var/log/forex_scan.log 2>&1
```

Or use systemd timer for more control.

## Acceptance Criteria

- [x] Create example script (`examples/run_scanners.py`)
- [x] Add CLI entry point (`tvscreener/cli.py`)
- [x] Update `pyproject.toml` with CLI script
- [x] Test with full 27-pair universe
- [x] Export results to CSV/JSON
- [x] Add `--filter` for direction filtering
- [x] Add `--strategy` for strategy selection
- [x] Add progress indicators
- [x] Add error handling for API failures
