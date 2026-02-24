import argparse
from pathlib import Path
from typing import Any

import yaml
from pydantic import ValidationError

from tvscreener.config.settings import ScreenerSettings

_UNSET = object()

DEFAULT_CONFIG_PATH = "tvscreener.yaml"


def load_yaml_config(config_path: str | None = None) -> dict[str, Any]:
    """Load configuration from YAML file."""
    path = config_path or DEFAULT_CONFIG_PATH

    if not Path(path).exists():
        return {}

    with open(path) as f:
        return yaml.safe_load(f) or {}


def load_settings(config_path: str | None = None) -> ScreenerSettings:
    """Load settings from YAML, then override with ENV and .env."""
    yaml_config = load_yaml_config(config_path) or {}
    yaml_config = {k: v for k, v in yaml_config.items() if v is not None}

    try:
        env_settings = ScreenerSettings()
    except ValidationError as e:
        import logging

        logging.warning(f"Settings validation error: {e}. Using defaults.")
        env_settings = ScreenerSettings()

    merged: dict[str, Any] = dict(yaml_config)

    for field_name in env_settings.model_fields_set:
        merged[field_name] = getattr(env_settings, field_name)

    try:
        return ScreenerSettings(**merged)
    except ValidationError as e:
        import logging

        logging.warning(f"Settings validation error: {e}. Using defaults.")
        return ScreenerSettings()


def merge_with_cli_args(settings: ScreenerSettings, cli_args: argparse.Namespace) -> dict[str, Any]:
    """Merge settings with CLI args (CLI takes precedence)."""
    config_dict = {}

    config_fields = [
        "min_volume",
        "max_atr",
        "min_ma_rating",
        "min_confluence",
        "trend_threshold",
        "mr_threshold",
        "min_roc",
        "contract_type",
        "default_universe",
        "default_timeframes",
    ]

    for field_name in config_fields:
        cli_value = getattr(cli_args, field_name, _UNSET)

        if cli_value is not _UNSET and cli_value is not None:
            if cli_value == "None" or cli_value == "null":
                cli_value = None
            config_dict[field_name] = cli_value
        else:
            settings_value = getattr(settings, field_name, None)
            if settings_value is not None:
                config_dict[field_name] = settings_value

    return config_dict
