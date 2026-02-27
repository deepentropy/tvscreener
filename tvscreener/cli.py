#!/usr/bin/env python3
"""CLI for forex scanners."""

import argparse
import logging
import sys
from pathlib import Path
from typing import Any, cast

import yaml
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from tvscreener.config.loader import load_settings
from tvscreener.config.universe import FOREX_UNIVERSE, AssetUniverse, ConfigurationError
from tvscreener.constants.commodity import COMMODITY_UNIVERSE
from tvscreener.constants.crypto import CRYPTO_UNIVERSE
from tvscreener.constants.forex import (
    DEFAULT_FOREX_PAIRS,
    DEFAULT_TIMEFRAME_WEIGHTS,
    FOREX_MAJORS,
    FOREX_MINORS,
)
from tvscreener.constants.stocks import STOCK_UNIVERSE
from tvscreener.filter import RatingFilter, RocFilter, VolumeFilter
from tvscreener.lib.screeners.forex_opportunity import ForexOpportunityScreener, ForexScreenerConfig
from tvscreener.lib.screeners.forex_strategy import (
    ForexStrategyScanner,
    StrategyConfig,
    StrategyType,
)
from tvscreener.score import ScoringConfig

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


def _build_opportunity_config(args) -> ForexScreenerConfig:
    rating_filters = []
    if args.min_ma_rating is not None:
        rating_filters.append(RatingFilter("ma", args.min_ma_rating))

    roc_filter = RocFilter(min_roc=args.min_roc) if args.min_roc is not None else None
    volume_filter = (
        VolumeFilter(min_volume=args.min_volume) if args.min_volume is not None else None
    )

    include_atr = args.include_atr or args.max_atr is not None
    include_rsi = args.include_rsi or bool(args.mr_signal)

    scoring_config = ScoringConfig(
        trend_weight=args.opportunity_trend_weight,
        ma_weight=args.opportunity_ma_weight,
        osc_weight=args.opportunity_osc_weight,
        roc_weight=args.opportunity_roc_weight,
    )

    timeframe_weights = _parse_timeframe_weights(args.opportunity_timeframe_weights)

    return ForexScreenerConfig(
        rating_filters=tuple(rating_filters),
        roc_filter=roc_filter,
        volume_filter=volume_filter,
        contract_type=args.contract_type,
        include_atr=include_atr,
        include_rsi=include_rsi,
        scoring_config=scoring_config,
        timeframe_weights=timeframe_weights,
    )


def _parse_timeframe_weights(spec: str) -> dict[str, float]:
    weights: dict[str, float] = {}
    for entry in spec.split(","):
        if not entry:
            continue
        if ":" not in entry:
            continue
        tf, _, val = entry.partition(":")
        tf = tf.strip()
        if not tf or not val:
            continue
        try:
            weights[tf] = float(val.strip())
        except ValueError:
            continue
    return weights or dict(DEFAULT_TIMEFRAME_WEIGHTS)


def _build_opportunity_metadata(args) -> dict[str, Any]:
    return {
        "scanner": "opportunity",
        "filters": {
            "min_volume": args.min_volume,
            "max_atr": args.max_atr,
            "min_ma_rating": args.min_ma_rating,
            "contract_type": args.contract_type,
            "include_atr": args.include_atr,
            "include_rsi": args.include_rsi,
        },
        "scoring_weights": {
            "trend": args.opportunity_trend_weight,
            "ma": args.opportunity_ma_weight,
            "osc": args.opportunity_osc_weight,
            "roc": args.opportunity_roc_weight,
        },
        "timeframes": args.timeframes,
        "timeframe_weights": _parse_timeframe_weights(args.opportunity_timeframe_weights),
    }


def _build_strategy_metadata(args) -> dict[str, Any]:
    return {
        "scanner": "strategy",
        "strategy": args.strategy,
        "filters": {
            "min_volume": args.min_volume,
            "max_atr": args.max_atr,
            "min_ma_rating": args.min_ma_rating,
            "min_confluence": args.min_confluence,
            "trend_threshold": args.trend_threshold,
            "mr_threshold": args.mr_threshold,
            "min_roc": args.min_roc,
            "filter": args.filter,
        },
        "scoring_weights": {
            "trend": args.opportunity_trend_weight,
            "ma": args.opportunity_ma_weight,
            "osc": args.opportunity_osc_weight,
            "roc": args.opportunity_roc_weight,
        },
        "timeframes": args.timeframes,
    }


def _load_yaml_config_file(path: str) -> dict[str, Any]:
    try:
        with open(path) as fh:
            return yaml.safe_load(fh) or {}
    except FileNotFoundError:
        logger.warning(f"Config file not found: {path}")
        return {}


def _apply_loaded_config(args, config: dict[str, Any]) -> None:
    for key, value in config.items():
        if value is None:
            continue
        if not hasattr(args, key):
            continue
        current = getattr(args, key)
        if isinstance(current, bool):
            if not current:
                setattr(args, key, value)
        elif current is None:
            setattr(args, key, value)


def _default_scoped_setting(args, settings, attr: str, opportunity_attr: str) -> None:
    current = getattr(args, attr)
    if current is not None:
        return
    value = None
    if args.scanner == "opportunity":
        value = getattr(settings, opportunity_attr, None)
    if value is None:
        value = getattr(settings, attr)
    setattr(args, attr, value)


def _get_opportunity_config_payload(args) -> dict[str, Any]:
    return {
        "min_volume": args.min_volume,
        "max_atr": args.max_atr,
        "min_ma_rating": args.min_ma_rating,
        "include_atr": args.include_atr,
        "include_rsi": args.include_rsi,
        "opportunity_trend_weight": args.opportunity_trend_weight,
        "opportunity_ma_weight": args.opportunity_ma_weight,
        "opportunity_osc_weight": args.opportunity_osc_weight,
        "opportunity_roc_weight": args.opportunity_roc_weight,
        "opportunity_timeframe_weights": args.opportunity_timeframe_weights,
        "contract_type": args.contract_type,
        "timeframes": args.timeframes,
    }


def _save_config_file(path: str, payload: dict[str, Any]) -> None:
    directory = Path(path).parent
    if directory and not directory.exists():
        directory.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as fh:
        yaml.safe_dump(payload, fh)
    logger.info(f"Saved opportunity config to {path}")


def _maybe_save_opportunity_config(path: str, args) -> None:
    payload = _get_opportunity_config_payload(args)
    _save_config_file(path, payload)


def run_opportunity_scan(args) -> int:
    """Run opportunity screener."""
    pairs = get_pairs(args.universe, args.pairs)
    timeframes = args.timeframes.split(",") if args.timeframes else ["15", "60", "240"]

    console.print(f"[cyan]Scanning {len(pairs)} {args.asset_type} pairs...[/cyan]")

    try:
        config = _build_opportunity_config(args)
        screener = ForexOpportunityScreener(pairs=pairs, timeframes=timeframes, config=config)

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            progress.add_task("Fetching data...", total=None)
            results = screener.get_opportunities()

        screener.print_summary()

        metadata = _build_opportunity_metadata(args)

        if args.output:
            output_path = args.output
            output_lower = output_path.lower()
            if output_lower.endswith(".csv"):
                screener.export(output_path, "csv", include_index=False, metadata=metadata)
            elif output_lower.endswith(".json"):
                screener.export(output_path, "json", orient="records", metadata=metadata)
            elif output_lower.endswith(".parquet"):
                screener.export(output_path, "parquet", include_index=False, metadata=metadata)
            elif output_lower.endswith(".xml"):
                screener.export(output_path, "xml", include_index=False, metadata=metadata)
            else:
                console.print(f"[yellow]Unknown output format: {args.output}[/yellow]")
                return -1
            console.print(f"[green]Saved to {args.output}[/green]")

        if args.save_config:
            _maybe_save_opportunity_config(args.save_config, args)

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
        if strategy_name == "all":
            strategy_tuple = cast(tuple[StrategyType, ...], ("all",))
        else:
            strategy_tuple = (cast(StrategyType, strategy_name),)
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
            include_atr_fields=args.include_atr or args.max_atr is not None,
            include_rsi_fields=args.include_rsi or bool(args.mr_signal),
        )
        scanner = ForexStrategyScanner(pairs=pairs, timeframes=timeframes, config=config)

        metadata = _build_strategy_metadata(args)

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            progress.add_task("Fetching data...", total=None)
            results = scanner.scan()

        scanner.print_summary()

        if args.output:
            output_path = args.output
            output_lower = output_path.lower()
            if output_lower.endswith(".csv"):
                scanner.export(output_path, "csv", include_index=False, metadata=metadata)
            elif output_lower.endswith(".json"):
                scanner.export(output_path, "json", orient="records", metadata=metadata)
            elif output_lower.endswith(".parquet"):
                scanner.export(output_path, "parquet", include_index=False, metadata=metadata)
            elif output_lower.endswith(".xml"):
                scanner.export(output_path, "xml", include_index=False, metadata=metadata)
            else:
                console.print(f"[yellow]Unknown output format: {args.output}[/yellow]")
                return -1
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
    parser.add_argument("--output", "-o", help="Output file (csv/json/parquet/xml)")
    parser.add_argument("--save-config", help="Save opportunity config to YAML")
    parser.add_argument("--load-config", help="Load opportunity config from YAML")
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
        "--min-confluence",
        type=int,
        help="Minimum confluence score (strategy scanner)",
    )
    parser.add_argument(
        "--trend-threshold",
        type=float,
        help="Trend score threshold (strategy scanner)",
    )
    parser.add_argument(
        "--mr-threshold",
        type=float,
        help="Mean-reversion score threshold (strategy scanner)",
    )
    parser.add_argument(
        "--min-roc",
        type=float,
        help="Minimum ROC value for breakout filter",
    )
    parser.add_argument(
        "--opportunity-trend-weight",
        type=float,
        help="Trend weight for opportunity scoring",
    )
    parser.add_argument(
        "--opportunity-ma-weight",
        type=float,
        help="MA weight for opportunity scoring",
    )
    parser.add_argument(
        "--opportunity-osc-weight",
        type=float,
        help="Oscillator weight for opportunity scoring",
    )
    parser.add_argument(
        "--opportunity-roc-weight",
        type=float,
        help="ROC weight for opportunity scoring",
    )
    parser.add_argument(
        "--opportunity-timeframe-weights",
        help="Timeframe weights for opportunity scoring (format 240:0.2,60:0.3,15:0.5)",
    )
    parser.add_argument(
        "--include-atr",
        action="store_true",
        help="Request ATR fields when running strategy scan",
    )
    parser.add_argument(
        "--include-rsi",
        action="store_true",
        help="Request RSI fields when running strategy scan",
    )
    parser.add_argument(
        "--mr-signal",
        choices=["rsi_oversold", "rsi_overbought"],
        action="append",
        help="Mean reversion signal (can be specified multiple times)",
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")

    args = parser.parse_args()
    if args.load_config:
        _apply_loaded_config(args, _load_yaml_config_file(args.load_config))
    setup_logging(args.verbose)

    settings = load_settings(args.config)

    if args.universe is None:
        args.universe = settings.default_universe
    if args.timeframes is None:
        args.timeframes = settings.default_timeframes
    if args.contract_type is None:
        args.contract_type = settings.contract_type

    _default_scoped_setting(args, settings, "min_volume", "opportunity_min_volume")
    _default_scoped_setting(args, settings, "max_atr", "opportunity_max_atr")
    _default_scoped_setting(args, settings, "min_ma_rating", "opportunity_min_ma_rating")

    if args.min_confluence is None:
        args.min_confluence = settings.min_confluence
    if args.trend_threshold is None:
        args.trend_threshold = settings.trend_threshold
    if args.mr_threshold is None:
        args.mr_threshold = settings.mr_threshold
    if args.min_roc is None:
        args.min_roc = settings.min_roc
    if args.opportunity_trend_weight is None:
        args.opportunity_trend_weight = settings.opportunity_trend_weight
    if args.opportunity_ma_weight is None:
        args.opportunity_ma_weight = settings.opportunity_ma_weight
    if args.opportunity_osc_weight is None:
        args.opportunity_osc_weight = settings.opportunity_osc_weight
    if args.opportunity_roc_weight is None:
        args.opportunity_roc_weight = settings.opportunity_roc_weight
    if args.opportunity_timeframe_weights is None:
        args.opportunity_timeframe_weights = settings.opportunity_timeframe_weights

    count = run_opportunity_scan(args) if args.scanner == "opportunity" else run_strategy_scan(args)

    if count < 0:
        console.print("\n[bold red]Scan failed[/bold red]")
        return 2

    console.print(f"\n[bold]Total: {count} results[/bold]")
    return 0 if count > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
