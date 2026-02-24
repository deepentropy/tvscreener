from __future__ import annotations

import logging
from collections.abc import Callable
from typing import Any

import pandas as pd


def export_to_csv(
    df_getter: Callable[[], pd.DataFrame],
    path: str,
    include_index: bool,
    *,
    logger: logging.Logger,
    label: str,
) -> None:
    df = df_getter()
    df.to_csv(path, index=include_index)
    logger.info(f"Saved {len(df)} {label} to {path}")


def export_to_json(
    df_getter: Callable[[], pd.DataFrame],
    path: str,
    orient: str,
    *,
    logger: logging.Logger,
    label: str,
) -> None:
    df = df_getter()
    df.to_json(path, orient=orient, indent=2)
    logger.info(f"Saved {len(df)} {label} to {path}")


def print_summary(
    df_getter: Callable[[], pd.DataFrame],
    *,
    empty_rich_message: str,
    render_rich: Callable[[pd.DataFrame, Any, Any], None],
) -> None:
    try:
        from rich.console import Console
        from rich.table import Table
    except ImportError:
        df = df_getter()
        print(df.to_string())
        return

    console = Console()
    df = df_getter()

    if df.empty:
        console.print(f"[yellow]{empty_rich_message}[/yellow]")
        return

    render_rich(df, console, Table)
