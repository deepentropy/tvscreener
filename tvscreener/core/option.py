from datetime import date, datetime

import pandas as pd

from tvscreener.core.base import Screener
from tvscreener.field.option import OptionField, DEFAULT_OPTION_FIELDS
from tvscreener.util import get_url


def _to_yyyymmdd(value):
    """Convert a date, datetime or ISO date string to the YYYYMMDD integer the API expects."""
    if isinstance(value, (date, datetime)):
        return int(value.strftime("%Y%m%d"))
    if isinstance(value, str) and "-" in value:
        return int(date.fromisoformat(value).strftime("%Y%m%d"))
    return value


class OptionScreener(Screener):
    """
    Option screener for querying option chains from TradingView.

    The API requires at least one underlying symbol, with its exchange prefix
    (e.g. "NASDAQ:AAPL", "AMEX:SPY", "SP:SPX", "NSE:NIFTY").

    Example:
        >>> os_ = OptionScreener("NASDAQ:AAPL")
        >>> os_.where(OptionField.OPTION_TYPE == "call")
        >>> os_.where(OptionField.DELTA.between(0.4, 0.6))
        >>> df = os_.get()
    """

    _field_type = OptionField

    def __init__(self, *underlyings: str):
        super().__init__()
        self.url = get_url("options")
        self.specific_fields = DEFAULT_OPTION_FIELDS
        self.underlyings = []
        self.set_underlying(*underlyings)
        self.sort_by(OptionField.EXPIRATION, True)

    def set_underlying(self, *symbols: str) -> 'OptionScreener':
        """
        Set the underlying symbol(s) whose options are returned.

        :param symbols: Exchange-prefixed symbols (e.g. "NASDAQ:AAPL")
        :return: self for method chaining
        """
        self.underlyings = list(symbols)
        return self

    def add_filter(self, filter_type, operation, values):
        # Expiration is stored as a YYYYMMDD integer; accept dates as well
        if filter_type is OptionField.EXPIRATION:
            if isinstance(values, (list, tuple)):
                values = [_to_yyyymmdd(v) for v in values]
            else:
                values = _to_yyyymmdd(values)
        super().add_filter(filter_type, operation, values)

    def _build_payload(self, requested_columns_):
        if not self.underlyings:
            raise ValueError(
                "OptionScreener requires an underlying symbol, "
                "e.g. OptionScreener('NASDAQ:AAPL') or set_underlying('NASDAQ:AAPL')"
            )
        payload = super()._build_payload(requested_columns_)
        payload["index_filters"] = [{"name": "underlying_symbol", "values": self.underlyings}]
        return payload

    def get(self, print_request=False):
        """
        Get the option chain from TradingView.

        The expiration column is converted from YYYYMMDD integers to datetimes.

        :param print_request: If True, prints the request URL and payload for debugging.
        :return: ScreenerDataFrame containing the option contracts
        """
        df = super().get(print_request)
        label = OptionField.EXPIRATION.label
        if label in df.columns:
            raw = pd.to_numeric(df[label], errors="coerce").astype("Int64").astype("string")
            df[label] = pd.to_datetime(raw, format="%Y%m%d", errors="coerce")
        return df
