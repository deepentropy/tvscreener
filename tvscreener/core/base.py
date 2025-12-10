import json
import time
from typing import Iterator, Callable, Optional, Union, List

import pandas as pd
import requests
from enum import Enum

from tvscreener.exceptions import MalformedRequestException
from tvscreener.field import Field, Market, IndexSymbol
from tvscreener.field.crypto import CryptoField
from tvscreener.field.forex import ForexField
from tvscreener.field.stock import StockField
from tvscreener.filter import FilterOperator, Filter, ExtraFilter
from tvscreener.util import get_columns_to_request, is_status_code_ok

# Configuration constants
DEFAULT_MARKET = Market.AMERICA
DEFAULT_MIN_RANGE = 0
DEFAULT_MAX_RANGE = 150
DEFAULT_SORT_STOCKS = StockField.MARKET_CAPITALIZATION
DEFAULT_SORT_CRYPTO = CryptoField.VOLUME_24H_IN_USD
DEFAULT_SORT_FOREX = ForexField.NAME
REQUEST_TIMEOUT = 30  # seconds
MIN_STREAM_INTERVAL = 1.0  # minimum interval for streaming to avoid rate limiting

# Backward compatibility aliases
default_market = DEFAULT_MARKET
default_min_range = DEFAULT_MIN_RANGE
default_max_range = DEFAULT_MAX_RANGE
default_sort_stocks = DEFAULT_SORT_STOCKS
default_sort_crypto = DEFAULT_SORT_CRYPTO
default_sort_forex = DEFAULT_SORT_FOREX


class ScreenerDataFrame(pd.DataFrame):
    def __init__(self, data, columns: dict, *args, **kwargs):
        # Add the extra received columns
        columns = {"symbol": "Symbol", **columns}
        super().__init__(data, columns=list(columns.values()), *args, **kwargs)

        # Reorder columns - only include first_columns that exist in the request
        first_columns = ['symbol', 'name', 'description']
        ordered_columns = {k: columns.get(k) for k in first_columns if k in columns}
        ordered_columns.update({k: v for k, v in columns.items() if k not in first_columns})
        self.attrs['original_columns'] = ordered_columns
        self._update_inplace(self[ordered_columns.values()])

    def set_technical_columns(self, only: bool = False):
        if only:
            self.columns = pd.Index(self.attrs['original_columns'].keys())
        else:
            self.columns = pd.MultiIndex.from_tuples(self.attrs['original_columns'].items())


class Screener:
    """Base screener class for querying TradingView screeners."""

    # Subclasses should override this to enable field type validation
    _field_type: type = None

    def __init__(self):
        self.sort = None
        self.url = None
        self.filters = []
        self.options = {}
        self.symbols = None
        self.misc = {}
        self.specific_fields = None

        self.range = None
        self.set_range()
        self.add_option("lang", "en")

    # def add_prebuilt_filter(self, filter_: Filter):
    #    self.filters.append(filter_.to_dict())

    # def add_filter(self, filter_: Filter, operation: FilterOperator = None, values=None):
    #    filter_val = {"left": filter_, "operation": operation.value, "right": values}
    #    self.filters.append(filter_val)

    def search(self, value: str):
        self.add_filter(ExtraFilter.SEARCH, FilterOperator.MATCH, value)

    def _get_filter(self, filter_type: Field | ExtraFilter) -> Filter:
        for filter_ in self.filters:
            if filter_.field == filter_type:
                return filter_

    def remove_filter(self, filter_type: ExtraFilter | Field):
        filter_ = self._get_filter(filter_type)
        if filter_:
            self.filters.remove(filter_)

    @staticmethod
    def _merge_filters(current_filter: Filter, new_filter: Filter):
        if not set(new_filter.values).issubset(set(current_filter.values)):
            # Set the operation is IN_RANGE with multiple values
            current_filter.operation = FilterOperator.IN_RANGE
            current_filter.values.extend(new_filter.values)
        return current_filter

    def _add_new_filter(self, filter_: Filter):
        # Case where the filter does not exist
        # If the filter contains values array with only one value, we can use EQUAL instead of IN_RANGE
        if len(filter_.values) == 1 and filter_.operation == FilterOperator.IN_RANGE:
            filter_.operation = FilterOperator.EQUAL
        self.filters.append(filter_)

    def _validate_field_type(self, field: Field | ExtraFilter):
        """Validate that the field type matches the screener's expected field type."""
        from tvscreener.field import FieldWithInterval, FieldWithHistory

        # Skip validation for ExtraFilter (search, etc.)
        if isinstance(field, ExtraFilter):
            return
        # Skip validation if no field type is set
        if self._field_type is None:
            return
        # Handle FieldWithInterval and FieldWithHistory - check their underlying field
        if isinstance(field, (FieldWithInterval, FieldWithHistory)):
            underlying_field = field.field
            if not isinstance(underlying_field, self._field_type):
                raise TypeError(
                    f"Invalid field type: expected {self._field_type.__name__}, "
                    f"got {type(underlying_field).__name__}. "
                    f"Use {self._field_type.__name__} fields with {type(self).__name__}."
                )
            return
        # Validate field type
        if not isinstance(field, self._field_type):
            raise TypeError(
                f"Invalid field type: expected {self._field_type.__name__}, "
                f"got {type(field).__name__}. "
                f"Use {self._field_type.__name__} fields with {type(self).__name__}."
            )

    def add_filter(self, filter_type: Field | ExtraFilter, operation: FilterOperator, values: Enum or str):
        self._validate_field_type(filter_type)
        filter_ = Filter(filter_type, operation, values)
        # Case where the filter already exists, and we want to add more values
        existing_filter = self._get_filter(filter_.field)
        if existing_filter:
            self._merge_filters(existing_filter, filter_)
        else:
            self._add_new_filter(filter_)

    def where(self, condition_or_field, operation: FilterOperator = None, value=None) -> 'Screener':
        """
        Add a filter condition (fluent method).

        Supports two syntaxes:

        1. **New Pythonic syntax** (recommended):
            >>> ss.where(StockField.PRICE > 100)
            >>> ss.where(StockField.VOLUME >= 1_000_000)
            >>> ss.where(StockField.MARKET_CAPITALIZATION.between(1e9, 10e9))

        2. **Legacy syntax** (still supported):
            >>> ss.where(StockField.PRICE, FilterOperator.ABOVE, 100)

        :param condition_or_field: Either a FieldCondition (from comparison) or a Field
        :param operation: Filter operation (only for legacy syntax)
        :param value: Value to compare against (only for legacy syntax)
        :return: self for method chaining

        Example:
            >>> ss = StockScreener()
            >>> # New syntax
            >>> ss.where(StockField.PRICE > 100).where(StockField.VOLUME > 1e6)
            >>> # Legacy syntax
            >>> ss.where(StockField.PRICE, FilterOperator.ABOVE, 100)
        """
        from tvscreener.filter import FieldCondition

        if isinstance(condition_or_field, FieldCondition):
            # New Pythonic syntax: ss.where(StockField.PRICE > 100)
            self.add_filter(condition_or_field.field, condition_or_field.operation, condition_or_field.value)
        else:
            # Legacy syntax: ss.where(field, operator, value)
            self.add_filter(condition_or_field, operation, value)
        return self

    def select(self, *fields: Field) -> 'Screener':
        """
        Set fields to retrieve (fluent method).

        :param fields: Fields to include in results
        :return: self for method chaining

        Example:
            >>> ss = StockScreener()
            >>> ss.select(StockField.NAME, StockField.PRICE, StockField.VOLUME)
        """
        self.specific_fields = list(fields)
        return self

    def select_all(self) -> 'Screener':
        """
        Select all available fields for this screener type.

        :return: self for method chaining

        Example:
            >>> ss = StockScreener()
            >>> ss.select_all()
            >>> df = ss.get()  # Returns all ~3000+ stock fields
        """
        if self._field_type is None:
            raise ValueError("Cannot select all fields: screener has no field type defined")
        self.specific_fields = list(self._field_type)
        return self

    def add_option(self, key, value):
        self.options[key] = value

    def add_misc(self, key, value):
        self.misc[key] = value

    def set_range(self, from_range: int = default_min_range, to_range: int = default_max_range) -> 'Screener':
        self.range = [from_range, to_range]
        return self

    def sort_by(self, sort_by: Field, ascending=True):
        self.sort = {"sortBy": sort_by.field_name, "sortOrder": "asc" if ascending else "desc"}

    def set_index(self, *indices: IndexSymbol) -> 'Screener':
        """
        Filter screener results to only include constituents of the specified index(es).

        :param indices: One or more IndexSymbol enum values
        :return: self for method chaining

        Example:
            >>> ss = StockScreener()
            >>> ss.set_index(IndexSymbol.SP500)
            >>> df = ss.get()  # Returns only S&P 500 constituents

            >>> # Multiple indices
            >>> ss.set_index(IndexSymbol.SP500, IndexSymbol.NASDAQ_100)
        """
        if not indices:
            return self

        symbolset = [idx.symbolset_value for idx in indices]

        if self.symbols is None:
            self.symbols = {"symbolset": symbolset}
        else:
            # Merge with existing symbols configuration
            self.symbols["symbolset"] = symbolset

        return self

    def _build_payload(self, requested_columns_):
        payload = {
            "filter": [f.to_dict() for f in self.filters],
            "options": self.options,
            "symbols": self.symbols if self.symbols else {"query": {"types": []}, "tickers": []},
            "sort": self.sort,
            "range": self.range,
            "columns": requested_columns_,
            **self.misc
        }
        return payload

    def get(self, print_request=False):
        """
        Get the screener data from TradingView.

        :param print_request: If True, prints the request URL and payload for debugging.
        :return: ScreenerDataFrame containing the screener results
        :raises MalformedRequestException: If the API request fails
        :raises requests.RequestException: If there's a network error
        """
        # Build columns
        columns = get_columns_to_request(self.specific_fields)

        payload = self._build_payload(list(columns.keys()))
        payload_json = json.dumps(payload, indent=4)

        if print_request:
            print(f"Request: {self.url}")
            print("Payload:")
            print(payload_json)

        try:
            # Fixed: Add timeout to prevent hanging indefinitely
            response = requests.post(
                self.url,
                data=payload_json,
                timeout=REQUEST_TIMEOUT,
                headers={'Content-Type': 'application/json'}
            )

            if is_status_code_ok(response):
                data = [[d["s"]] + d["d"] for d in response.json()['data']]
                return ScreenerDataFrame(data, columns)
            else:
                raise MalformedRequestException(
                    response.status_code,
                    response.text,
                    self.url,
                    payload_json
                )

        except requests.Timeout:
            raise MalformedRequestException(
                408,  # Request Timeout
                f"Request timed out after {REQUEST_TIMEOUT} seconds",
                self.url,
                payload_json
            )
        except requests.RequestException as e:
            raise MalformedRequestException(
                0,  # Unknown status code
                str(e),
                self.url,
                payload_json
            )

    def stream(
        self,
        interval: float = 5.0,
        max_iterations: Optional[int] = None,
        on_update: Optional[Callable[['ScreenerDataFrame'], None]] = None
    ) -> Iterator['ScreenerDataFrame']:
        """
        Stream screener data at regular intervals.

        :param interval: Refresh interval in seconds (minimum 1.0 to avoid rate limiting)
        :param max_iterations: Maximum number of refreshes (None = infinite)
        :param on_update: Optional callback function called with each DataFrame
        :yield: ScreenerDataFrame on each refresh, or None if an error occurs

        Example:
            >>> ss = StockScreener()
            >>> for df in ss.stream(interval=10, max_iterations=5):
            ...     print(f"Updated: {len(df)} rows")
        """
        # Enforce minimum interval to be respectful of TradingView's API
        interval = max(interval, MIN_STREAM_INTERVAL)

        iteration = 0
        while max_iterations is None or iteration < max_iterations:
            try:
                df = self.get()
                if on_update:
                    on_update(df)
                yield df
            except Exception as e:
                # Log error but continue streaming
                print(f"Error fetching data: {e}")
                yield None

            iteration += 1
            if max_iterations is None or iteration < max_iterations:
                time.sleep(interval)
