#!/usr/bin/env python3
"""CLI for forex scanners."""

import argparse
import logging
import sys

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from tvscreener.config.loader import load_settings
from tvscreener.config.universe import FOREX_UNIVERSE, AssetUniverse, ConfigurationError
from tvscreener.constants.commodity import COMMODITY_UNIVERSE
from tvscreener.constants.crypto import CRYPTO_UNIVERSE
from tvscreener.constants.forex import DEFAULT_FOREX_PAIRS, FOREX_MAJORS, FOREX_MINORS
from tvscreener.constants.stocks import STOCK_UNIVERSE
from tvscreener.lib.screeners.forex_opportunity import ForexOpportunityScreener, ForexScreenerConfig
from tvscreener.lib.screeners.forex_strategy import ForexStrategyScanner, StrategyConfig

console = Console()
logger = logging.getLogger(__name__)

UNIVERSE_MAP: dict[str, AssetUniverse] = {}

UNIVERSE_MAP["forex"] = FOREX_UNIVERSE
UNIVERSE_MAP["stocks"] = STOCK_UNIVERSE
UNIVERSE_MAP["commodity"] = COMMODITY_UNIVERSE
UNIVERSE_MAP["crypto"] = CRYPTO_UNIVERSE


def get_universe(asset_type: str) -> AssetUniverse:
    """Get universe config by asset type with validation."""
    if asset_type not in UNIVERSE_MAP:
        raise ConfigurationError(
            f"Unknown asset type: {asset_type}. Valid options: {', '.join(UNIVERSE_MAP.keys())}"
        )
    return UNIVERSE_MAP[asset_type]


def setup_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


def get_pairs(universe: str | None, specific: list[str] | None) -> list[str]:
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

    console.print(f"[cyan]Scanning {len(pairs)} {args.asset_type} pairs...[/cyan]")

    try:
        config = ForexScreenerConfig(contract_type=args.contract_type)
        screener = ForexOpportunityScreener(pairs=pairs, timeframes=timeframes, config=config)

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
        return -1


def run_strategy_scan(args) -> int:
    """Run strategy scanner."""
    pairs = get_pairs(args.universe, args.pairs)
    timeframes = args.timeframes.split(",") if args.timeframes else ["15", "60", "240"]

    console.print(
        f"[cyan]Scanning {len(pairs)} {args.asset_type} pairs for {args.strategy} signals...[/cyan]"
    )

    try:
        strategy_map = {
            "trend": "trend_following",
            "mean_reversion": "mean_reversion",
            "hybrid": "hybrid",
            "breakout": "breakout",
            "all": "all",
        }
        strategy_name = strategy_map[args.strategy]
        strategy_tuple = (strategy_name,) if strategy_name != "all" else ("all",)
        mr_signals = tuple(args.mr_signal) if args.mr_signal else ()

        config = StrategyConfig(
            include_strategies=strategy_tuple,
            direction=args.filter or "all",
            min_confluence=args.min_confluence,
            trend_threshold=args.trend_threshold,
            mr_threshold=args.mr_threshold,
            min_roc=args.min_roc,
            min_volume=args.min_volume,
            max_atr=args.max_atr,
            min_ma_rating=args.min_ma_rating,
            mean_reversion_signals=mr_signals,
            contract_type=args.contract_type,
        )
        scanner = ForexStrategyScanner(pairs=pairs, timeframes=timeframes, config=config)

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            progress.add_task("Fetching data...", total=None)
            results = scanner.scan()

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
        return -1


def main():
    parser = argparse.ArgumentParser(
        description="Run forex scanners",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--config",
        default=None,
        help="Path to YAML config (default: tvscreener.yaml)",
    )

    parser.add_argument("--scanner", "-s", choices=["opportunity", "strategy"], default="strategy")
    parser.add_argument(
        "--asset-type",
        choices=["forex", "stocks", "commodity", "crypto"],
        default="forex",
    )
    parser.add_argument("--universe", "-u", choices=["majors", "minors", "all"], default=None)
    parser.add_argument("--pairs", nargs="+", help="Specific pairs to scan")
    parser.add_argument("--timeframes", "-t", default=None, help="Comma-separated timeframes")
    parser.add_argument(
        "--contract-type",
        choices=["spot", "cfd", "spreadbet", "all"],
        default=None,
        help="Contract type to filter (default: cfd)",
    )
    parser.add_argument("--output", "-o", help="Output file (csv/json)")
    parser.add_argument(
        "--strategy",
        choices=["all", "trend", "mean_reversion", "hybrid", "breakout"],
        default="all",
    )
    parser.add_argument("--filter", choices=["long", "short"], help="Filter by direction")
    parser.add_argument("--min-volume", type=float, help="Minimum average volume")
    parser.add_argument("--max-atr", type=float, help="Maximum ATR (volatility proxy)")
    parser.add_argument("--min-ma-rating", type=float, help="Minimum MA rating (-2 to 2)")
    parser.add_argument(
        "--mr-signal",
        choices=["rsi_oversold", "rsi_overbought"],
        action="append",
        help="Mean reversion signal (can be specified multiple times)",
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")

    args = parser.parse_args()
    setup_logging(args.verbose)

    settings = load_settings(args.config)

    if args.universe is None:
        args.universe = settings.default_universe
    if args.timeframes is None:
        args.timeframes = settings.default_timeframes
    if args.contract_type is None:
        args.contract_type = settings.contract_type

    if args.min_volume is None:
        args.min_volume = settings.min_volume
    if args.max_atr is None:
        args.max_atr = settings.max_atr
    if args.min_ma_rating is None:
        args.min_ma_rating = settings.min_ma_rating

    args.min_confluence = settings.min_confluence
    args.trend_threshold = settings.trend_threshold
    args.mr_threshold = settings.mr_threshold
    args.min_roc = settings.min_roc

    count = run_opportunity_scan(args) if args.scanner == "opportunity" else run_strategy_scan(args)

    if count < 0:
        console.print("\n[bold red]Scan failed[/bold red]")
        return 2

    console.print(f"\n[bold]Total: {count} results[/bold]")
    return 0 if count > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
