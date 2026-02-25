from __future__ import annotations

import json
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
    metadata: dict[str, Any] | None = None,
) -> None:
    df = df_getter()
    with open(path, "w", newline="") as fh:
        if metadata:
            for key, value in metadata.items():
                fh.write(f"# {key}: {value}\n")
        df.to_csv(fh, index=include_index)
    logger.info(f"Saved {len(df)} {label} to {path}")
    if metadata:
        _write_metadata_file(path, metadata, logger, label)


def export_to_json(
    df_getter: Callable[[], pd.DataFrame],
    path: str,
    orient: str,
    *,
    logger: logging.Logger,
    label: str,
    metadata: dict[str, Any] | None = None,
) -> None:
    df = df_getter()
    payload: dict[str, Any] = {"data": df.to_dict(orient=orient)}
    if metadata:
        payload["metadata"] = metadata
    with open(path, "w") as fh:
        json.dump(payload, fh, indent=2)
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


def export_to_parquet(
    df_getter: Callable[[], pd.DataFrame],
    path: str,
    include_index: bool,
    *,
    logger: logging.Logger,
    label: str,
    metadata: dict[str, Any] | None = None,
) -> None:
    df = df_getter()
    df.to_parquet(path, index=include_index)
    logger.info(f"Saved {len(df)} {label} to {path}")
    if metadata:
        _write_metadata_file(path, metadata, logger, label)


def export_to_xml(
    df_getter: Callable[[], pd.DataFrame],
    path: str,
    include_index: bool,
    *,
    logger: logging.Logger,
    label: str,
    metadata: dict[str, Any] | None = None,
) -> None:
    df = df_getter()
    with open(path, "w") as fh:
        if metadata:
            fh.write("<metadata>\n")
            for key, value in metadata.items():
                fh.write(f"  <{key}>{value}</{key}>\n")
            fh.write("</metadata>\n")
        df.to_xml(fh, index=include_index)
    logger.info(f"Saved {len(df)} {label} to {path}")
    if metadata:
        _write_metadata_file(path, metadata, logger, label)


def _write_metadata_file(
    path: str, metadata: dict[str, Any], logger: logging.Logger, label: str
) -> None:
    meta_path = f"{path}.meta.json"
    with open(meta_path, "w") as fh:
        json.dump({"metadata": metadata}, fh, indent=2)
    logger.info(f"Saved metadata for {label} to {meta_path}")
