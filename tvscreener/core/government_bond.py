import json
import re

import pandas as pd
import requests

from tvscreener.core.base import Screener, REQUEST_HEADERS, REQUEST_TIMEOUT
from tvscreener.field.government_bond import GovernmentBondField
from tvscreener.util import get_url

DEFAULT_GOVERNMENT_BOND_FIELDS = [
    GovernmentBondField.NAME,
    GovernmentBondField.DESCRIPTION,
    GovernmentBondField.COUNTRY_CODE,
    GovernmentBondField.CLOSE,
    GovernmentBondField.CHANGE,
    GovernmentBondField.CHANGE_ABS,
    GovernmentBondField.DAYS_TO_MATURITY,
    GovernmentBondField.MATURITY_DATE,
]

_TENOR = re.compile(r"(\d+)(M?)Y?$")


class GovernmentBondScreener(Screener):
    """
    Government benchmark bonds by country and tenor (TradingView ``/bonds`` scanner).

    The scanner holds two series per tenor: the yield (typespecs "yield", e.g. TVC:US10Y,
    CLOSE in percent) and the price (e.g. TVC:US10). BondScreener covers individual bonds.

    Example:
        >>> gs = GovernmentBondScreener().yields_only()
        >>> gs.where(GovernmentBondField.COUNTRY_CODE == 'DE')
        >>> df = gs.get()
    """

    _field_type = GovernmentBondField

    def __init__(self):
        super().__init__()
        self.url = get_url("bonds")
        self.specific_fields = DEFAULT_GOVERNMENT_BOND_FIELDS
        self.sort_by(GovernmentBondField.DAYS_TO_MATURITY, True)

    def get(self, print_request=False):
        """
        Get the bonds. The maturity date (YYYYMMDD) is converted to a datetime.

        :param print_request: If True, prints the request URL and payload for debugging.
        :return: ScreenerDataFrame with one row per bond series
        """
        df = super().get(print_request)
        label = GovernmentBondField.MATURITY_DATE.label
        if label in df.columns:
            raw = pd.to_numeric(df[label], errors="coerce").astype("Int64").astype("string")
            df[label] = pd.to_datetime(raw, format="%Y%m%d", errors="coerce")
        return df

    def yields_only(self) -> 'GovernmentBondScreener':
        """Keep the yield series (CLOSE is the yield in percent) and drop the price series."""
        self.where(GovernmentBondField.TYPESPECS.has('yield'))
        return self

    def prices_only(self) -> 'GovernmentBondScreener':
        """Keep the price series and drop the yield series."""
        self.where(GovernmentBondField.TYPESPECS.has_none_of('yield'))
        return self


def _tenor(name):
    """'US10Y' -> '10Y', 'US03MY' -> '3M'."""
    m = _TENOR.search(name)
    if not m:
        return None
    return f"{int(m.group(1))}{'M' if m.group(2) else 'Y'}"


def get_yield_curve(country="US"):
    """
    Government bond yield curve of a country.

    :param country: ISO country code, e.g. "US", "DE", "JP", "GB"
    :return: DataFrame sorted by maturity with columns: symbol, tenor, days_to_maturity,
        maturity_date, yield (percent), change (yield change), description
    """
    columns = ["name", "description", "close", "change_abs", "days_to_maturity", "maturity_date"]
    payload = {
        "columns": columns,
        "filter": [{"left": "typespecs", "operation": "has", "right": "yield"},
                   {"left": "country_code", "operation": "equal", "right": country.upper()}],
        "sort": {"sortBy": "days_to_maturity", "sortOrder": "asc"},
        "range": [0, 200],
    }
    response = requests.post(get_url("bonds"), data=json.dumps(payload), headers=REQUEST_HEADERS, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json().get("data") or []
    raw = pd.DataFrame([d["d"] for d in data], columns=columns)
    return pd.DataFrame({
        "symbol": [d["s"] for d in data],
        "tenor": raw["name"].map(_tenor),
        "days_to_maturity": raw["days_to_maturity"],
        "maturity_date": pd.to_datetime(raw["maturity_date"].astype("Int64").astype("string"), format="%Y%m%d", errors="coerce"),
        "yield": raw["close"],
        "change": raw["change_abs"],
        "description": raw["description"],
    })


_ISO_TENOR = re.compile(r"P(\d+)([MY])$")


def _tenor_months(tenor):
    """'10Y' -> 120, '3M' -> 3."""
    return int(tenor[:-1]) * (12 if tenor.endswith("Y") else 1)


def get_yield_matrix(countries=None, tenors=None):
    """
    Government bond yields of several countries side by side, one column per tenor.

    :param countries: ISO country code or list of them, e.g. ["US", "DE", "JP"]; default every country
    :param tenors: Tenor or list of tenors to keep, e.g. ["3M", "2Y", "10Y", "30Y"]; default all
    :return: DataFrame of yields in percent, one row per country (index), one column per tenor,
        sorted from the shortest tenor. Missing tenors are NaN.
    """
    columns = ["country_code", "close", "term-to-maturity"]
    filters = [{"left": "typespecs", "operation": "has", "right": ["yield"]},
               {"left": "close", "operation": "nempty"}]
    if countries:
        countries = [countries] if isinstance(countries, str) else countries
        filters.append({"left": "country_code", "operation": "in_range", "right": [c.upper() for c in countries]})
    payload = {"columns": columns, "filter": filters, "range": [0, 5000]}
    response = requests.post(get_url("bonds"), data=json.dumps(payload), headers=REQUEST_HEADERS, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    raw = pd.DataFrame([d["d"] for d in response.json().get("data") or []], columns=columns)

    tenor = raw["term-to-maturity"].str.extract(_ISO_TENOR)
    raw["tenor"] = tenor[0].astype("Int64").astype("string") + tenor[1]
    raw = raw.dropna(subset=["tenor"])
    matrix = raw.pivot_table(index="country_code", columns="tenor", values="close", aggfunc="first")
    if tenors:
        wanted = [t.upper() for t in ([tenors] if isinstance(tenors, str) else tenors)]
        ordered = sorted({f"{int(t[:-1])}{t[-1]}" for t in wanted}, key=_tenor_months)
    else:
        ordered = sorted(matrix.columns, key=_tenor_months)
    matrix = matrix.reindex(columns=ordered)
    matrix.index.name = "country"
    matrix.columns.name = "tenor"
    return matrix
