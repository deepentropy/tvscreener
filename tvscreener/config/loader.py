from pathlib import Path
from typing import Any

import yaml
from pydantic import ValidationError

from tvscreener.config.settings import ScreenerSettings

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
