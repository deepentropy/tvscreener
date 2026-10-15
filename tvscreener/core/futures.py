import json
import re

import pandas as pd
import requests

from tvscreener.core.base import Screener, REQUEST_HEADERS, REQUEST_TIMEOUT
from tvscreener.field.futures import FuturesField, DEFAULT_FUTURES_FIELDS
from tvscreener.util import get_url

_CONTINUOUS = re.compile(r"\d+!$")


class FuturesScreener(Screener):
    """Futures screener for querying futures from TradingView."""

    _field_type = FuturesField

    def __init__(self):
        super().__init__()
        self.url = get_url("futures")
        self.specific_fields = DEFAULT_FUTURES_FIELDS
        self.sort_by(FuturesField.VOLUME, False)


def get_forward_curve(root):
    """
    Futures forward curve: every listed contract month of a futures root, by expiration.

    :param root: Exchange-prefixed root, e.g. "CME_MINI:ES", "NYMEX:CL", "COMEX:GC".
        A continuous symbol such as "NYMEX:CL1!" is accepted too.
    :return: DataFrame sorted by expiration with columns: symbol, name, description,
        expiration (datetime), close, change (%), volume, open_interest, currency.
        Empty when the root is unknown.
    :raises ValueError: If ``root`` has no exchange prefix
    """
    if ":" not in root:
        raise ValueError(f"root needs an exchange prefix, e.g. 'NYMEX:CL', got {root!r}")
    root = _CONTINUOUS.sub("", root.upper())
    columns = ["name", "description", "expiration", "close", "change", "volume", "open_interest", "currency"]
    payload = {
        "columns": columns,
        "filter": [{"left": "expiration", "operation": "nempty"}],
        "index_filters": [{"name": "root", "values": [root]}],
        "sort": {"sortBy": "expiration", "sortOrder": "asc"},
        "range": [0, 500],
    }
    response = requests.post(get_url("futures"), data=json.dumps(payload), headers=REQUEST_HEADERS,
                             timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json().get("data") or []
    raw = pd.DataFrame([d["d"] for d in data], columns=columns)
    return pd.DataFrame({
        "symbol": [d["s"] for d in data],
        "name": raw["name"],
        "description": raw["description"],
        "expiration": pd.to_datetime(raw["expiration"].astype("Int64").astype("string"), format="%Y%m%d",
                                     errors="coerce"),
        "close": raw["close"],
        "change": raw["change"],
        "volume": raw["volume"],
        "open_interest": raw["open_interest"],
        "currency": raw["currency"],
    })
