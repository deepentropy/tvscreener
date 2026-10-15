import datetime as dt

import pandas as pd
import requests

IV_TERM_STRUCTURE_URL = "https://options-charting.tradingview.com/v1/in-time-iv/{symbol}"
VOLATILITY_CHART_URL = "https://options-charting.tradingview.com/v1/volatility-chart/{series}"
REQUEST_TIMEOUT = 30

REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Origin': 'https://www.tradingview.com',
    'Referer': 'https://www.tradingview.com/',
}

# Approximate number of days per span unit, used for the "days" column
_DAYS_PER_UNIT = {"d": 1, "w": 7, "m": 365 / 12, "y": 365}


def get_iv_term_structure(symbol):
    """
    Get the implied volatility term structure of an underlying from TradingView.

    Two kinds of points are returned:

    - ``listed``: one point per listed expiration, at its time to expiration
    - ``standard``: interpolated constant-maturity tenors (1w, 2w, 1m, 2m, 3m, 6m, 9m, 1y)

    Implied volatilities are fractions (0.27 means 27%).

    :param symbol: Exchange-prefixed underlying symbol (e.g. "NASDAQ:AAPL", "SP:SPX")
    :return: DataFrame with columns: kind, tenor, span_value, span_unit, days, iv.
        ``days`` is approximate for the w, m and y units (1m = 365/12 days).
    :raises requests.HTTPError: If the symbol is unknown or has no options
    """
    response = requests.get(
        IV_TERM_STRUCTURE_URL.format(symbol=symbol),
        headers=REQUEST_HEADERS,
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    data = response.json()

    rows = []
    for kind, key in (("listed", "real-ivs"), ("standard", "standard-ivs")):
        for item in data.get(key, []):
            value = item["span"]["value"]
            unit = item["span"]["unit"]
            rows.append({
                "kind": kind,
                "tenor": f"{value}{unit}",
                "span_value": value,
                "span_unit": unit,
                "days": value * _DAYS_PER_UNIT.get(unit, float("nan")),
                "iv": item.get("value"),
            })

    return pd.DataFrame(rows, columns=["kind", "tenor", "span_value", "span_unit", "days", "iv"])


def get_volatility_smile(symbol, expiration, root=None, x="strike"):
    """
    Implied volatility smile of one option expiration, as shown by TradingView's volatility chart.

    :param symbol: Exchange-prefixed underlying symbol, e.g. "NASDAQ:AAPL"
    :param expiration: Expiration date (date, datetime, ISO string or YYYYMMDD int), e.g. "2026-11-13".
        OptionScreener lists the available expirations.
    :param root: Option root when it differs from the ticker (e.g. "SPXW" for SP:SPX weeklies);
        default the ticker
    :param x: "strike" (x is the strike price) or "moneyness" (x is log-moneyness, 0 at the money)
    :return: DataFrame sorted by x with columns: strike or moneyness, iv (fraction, 0.27 = 27%)
    :raises ValueError: If ``x`` is invalid
    :raises requests.HTTPError: If the expiration does not exist (HTTP 404)
    """
    if x not in ("strike", "moneyness"):
        raise ValueError(f"x must be 'strike' or 'moneyness', got {x!r}")
    if isinstance(expiration, (dt.date, dt.datetime)):
        expiration = expiration.strftime("%Y%m%d")
    expiration = str(expiration).replace("-", "")
    root = root or symbol.split(":")[-1]
    response = requests.get(
        VOLATILITY_CHART_URL.format(series=f"{symbol};{root};{expiration}"),
        params={"xaxis": "strikes" if x == "strike" else "moneyness"},
        headers=REQUEST_HEADERS,
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    data = response.json()
    xs = data.get("x-axis", {}).get("x", [])
    plots = data.get("plots") or [{}]
    ys = plots[0].get("plot", {}).get("y", [])
    return pd.DataFrame({x: xs, "iv": ys[:len(xs)]}, columns=[x, "iv"])
