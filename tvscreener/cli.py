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
from tvscreener.config.universe import AssetUniverse, ConfigurationError
from tvscreener.constants.stocks import STOCK_UNIVERSE
from tvscreener.constants.commodity import COMMODITY_UNIVERSE
from tvscreener.constants.crypto import CRYPTO_UNIVERSE

console = Console()
logger = logging.getLogger(__name__)

UNIVERSE_MAP: dict[str, AssetUniverse] = {}

from tvscreener.config.universe import FOREX_UNIVERSE

UNIVERSE_MAP["forex"] = FOREX_UNIVERSE
UNIVERSE_MAP["stocks"] = STOCK_UNIVERSE
UNIVERSE_MAP["commodity"] = COMMODITY_UNIVERSE
UNIVERSE_MAP["crypto"] = CRYPTO_UNIVERSE


def get_universe(asset_type: str) -> AssetUniverse:
    """Get universe config by asset type with validation."""
    if asset_type not in UNIVERSE_MAP:
        raise ConfigurationError(
            f"Unknown asset type: {asset_type}. "
            f"Valid options: {', '.join(UNIVERSE_MAP.keys())}"
        )
    return UNIVERSE_MAP[asset_type]


def setup_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
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
    universe = get_universe(args.asset_type)
    pairs = args.pairs if args.pairs else universe.pairs
    timeframes = args.timeframes.split(",") if args.timeframes else universe.timeframes

    console.print(f"[cyan]Scanning {len(pairs)} {args.asset_type} pairs...[/cyan]")

    try:
        screener = ForexOpportunityScreener(pairs=pairs, timeframes=timeframes)

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
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
    universe = get_universe(args.asset_type)
    pairs = args.pairs if args.pairs else universe.pairs
    timeframes = args.timeframes.split(",") if args.timeframes else universe.timeframes

    console.print(
        f"[cyan]Scanning {len(pairs)} {args.asset_type} pairs for {args.strategy} signals...[/cyan]"
    )

    try:
        scanner = ForexStrategyScanner(pairs=pairs, timeframes=timeframes)

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
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
            results = (
                results[results["DIRECTION"] == args.filter]
                if not results.empty
                else results
            )

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
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--scanner", "-s", choices=["opportunity", "strategy"], default="strategy"
    )
    parser.add_argument(
        "--asset-type",
        choices=["forex", "stocks", "commodity", "crypto"],
        default="forex",
    )
    parser.add_argument(
        "--universe", "-u", choices=["majors", "minors", "all"], default="all"
    )
    parser.add_argument("--pairs", nargs="+", help="Specific pairs to scan")
    parser.add_argument(
        "--timeframes", "-t", default="240,60,15", help="Comma-separated timeframes"
    )
    parser.add_argument("--output", "-o", help="Output file (csv/json)")
    parser.add_argument(
        "--strategy",
        choices=["all", "trend", "mean_reversion", "hybrid", "breakout"],
        default="all",
    )
    parser.add_argument(
        "--filter", choices=["long", "short"], help="Filter by direction"
    )
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
