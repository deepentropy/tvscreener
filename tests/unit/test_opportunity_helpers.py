import argparse
import logging

import pandas as pd
import yaml

from tvscreener.cli import (
    _apply_loaded_config,
    _get_opportunity_config_payload,
    _parse_timeframe_weights,
    _save_config_file,
)
from tvscreener.constants.forex import DEFAULT_TIMEFRAME_WEIGHTS
from tvscreener.lib.screeners.export_helpers import export_to_csv, export_to_json


def test_parse_timeframe_weights_valid_string():
    spec = "240:0.5,60:0.3,15:0.2"
    weights = _parse_timeframe_weights(spec)
    assert weights == {"240": 0.5, "60": 0.3, "15": 0.2}


def test_parse_timeframe_weights_defaults_empty():
    weights = _parse_timeframe_weights("")
    assert weights == DEFAULT_TIMEFRAME_WEIGHTS


def test_apply_loaded_config_only_overrides_none():
    namespace = argparse.Namespace(min_volume=None, include_atr=False)
    _apply_loaded_config(namespace, {"min_volume": 1_000_000, "include_atr": True})
    assert namespace.min_volume == 1_000_000
    assert namespace.include_atr is True


def test_get_opportunity_config_payload_has_expected_keys():
    args = argparse.Namespace(
        min_volume=100,
        max_atr=0.01,
        min_ma_rating=0.5,
        include_atr=True,
        include_rsi=False,
        opportunity_trend_weight=0.4,
        opportunity_ma_weight=0.3,
        opportunity_osc_weight=0.2,
        opportunity_roc_weight=0.1,
        opportunity_timeframe_weights="240:0.5,60:0.3,15:0.2",
        contract_type="cfd",
        timeframes="240,60,15",
    )
    payload = _get_opportunity_config_payload(args)
    assert payload["min_volume"] == 100
    assert payload["opportunity_trend_weight"] == 0.4
    assert payload["contract_type"] == "cfd"


def test_save_config_file_creates_yaml(tmp_path):
    path = tmp_path / "cfg" / "config.yaml"
    _save_config_file(str(path), {"key": "value"})
    data = yaml.safe_load(path.read_text())
    assert data == {"key": "value"}


def test_export_helpers_include_metadata(tmp_path):
    df = pd.DataFrame({"a": [1, 2]})
    csv_path = tmp_path / "out.csv"
    metadata = {"foo": "bar"}
    export_to_csv(
        lambda: df,
        str(csv_path),
        include_index=False,
        logger=logging.getLogger("test"),
        label="test",
        metadata=metadata,
    )
    with open(csv_path) as fh:
        first_line = fh.readline().strip()
    assert first_line.startswith("# foo: bar")

    json_path = tmp_path / "out.json"
    export_to_json(
        lambda: df,
        str(json_path),
        orient="records",
        logger=logging.getLogger("test"),
        label="test",
        metadata={"bar": "baz"},
    )
    payload = yaml.safe_load(json_path.read_text())
    assert "metadata" in payload and payload["metadata"]["bar"] == "baz"
