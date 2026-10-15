from tvscreener.core.base import Screener, default_market, default_sort_stocks
from tvscreener.field import Market, Type, SymbolType
from tvscreener.field.stock import StockField, DEFAULT_STOCK_FIELDS
from tvscreener.filter import FilterOperator, Preset
from tvscreener.util import get_url

# Mapping from SymbolType to Type for efficient lookup
SYMBOL_TYPE_TO_TYPE_MAP = {
    SymbolType.COMMON_STOCK: Type.STOCK,
    SymbolType.DEPOSITORY_RECEIPT: Type.DEPOSITORY_RECEIPT,
    SymbolType.ETF: Type.FUND,
    SymbolType.MUTUAL_FUND: Type.FUND,
    SymbolType.REIT: Type.FUND,
    SymbolType.PREFERRED_STOCK: Type.STOCK,
    SymbolType.ETN: Type.STRUCTURED,
    SymbolType.STRUCTURED: Type.STRUCTURED,
    SymbolType.UIT: Type.FUND,
}


class StockScreener(Screener):
    """Stock screener for querying stocks from TradingView."""

    _field_type = StockField

    def __init__(self):
        super().__init__()
        self.markets = [default_market]
        self.preset = None
        self.url = get_url("global")
        self.specific_fields = DEFAULT_STOCK_FIELDS  # Use default 424 fields (set to StockField for all 3500+)
        self.sort_by(default_sort_stocks, False)

    def _single_market(self):
        """The market scanned when a preset is set and exactly one market is selected."""
        # ipo_calendar only exists on the global scanner
        if self.preset and self.preset != Preset.IPO_CALENDAR.value and len(self.markets) == 1:
            return self.markets[0]
        return None

    def _request_url(self) -> str:
        # Most presets only exist on single-market scanners (/america/scan, /japan/scan...)
        market = self._single_market()
        return get_url(market.value) if market else self.url

    def _build_payload(self, requested_columns_):
        payload = super()._build_payload(requested_columns_)
        if self.markets and not self._single_market():
            payload["markets"] = [market.value for market in self.markets]
        if self.preset:
            payload["preset"] = self.preset
        return payload

    def set_preset(self, preset: Preset | str | None) -> 'StockScreener':
        """
        Use one of TradingView's server-side screens (gainers, losers, most volatile...).

        The preset brings its own filters and sort order. Filters added with where() are
        combined with it. sort_by() after set_preset() replaces the preset's sort.

        With one market selected, the request goes to that market's scanner, where every
        preset exists (except IPO_CALENDAR, which always uses the global scanner). With
        several markets, only Preset.EARNINGS and Preset.IPO_CALENDAR work.

        :param preset: Preset enum or preset name; None removes the preset
        :return: self for method chaining

        Example:
            >>> ss = StockScreener().set_preset(Preset.GAINERS)
            >>> ss.where(StockField.MARKET_CAPITALIZATION > 1e10)
        """
        self.preset = preset.value if isinstance(preset, Preset) else preset
        if self.preset:
            # Let the preset's sort apply; sort_by() can still override it
            self.sort = None
        return self

    def _add_types(self, *types: Type):
        if len(types) > 1:
            operator = FilterOperator.IN_RANGE
        else:
            operator = FilterOperator.EQUAL

        for type_ in types:
            self.add_filter(StockField.TYPE, operator, type_.value)

    def set_symbol_types(self, *symbol_types: SymbolType):
        """
        Set the symbol types to be scanned.

        :param symbol_types: Symbol types to include in the screener results
        :raises ValueError: If an unknown symbol type is provided
        """
        # Validate all symbol types are known
        unknown_types = [st for st in symbol_types if st not in SYMBOL_TYPE_TO_TYPE_MAP]
        if unknown_types:
            raise ValueError(f"Unknown symbol types: {unknown_types}")

        # Collect unique Type values from symbol_types
        types_to_add = {SYMBOL_TYPE_TO_TYPE_MAP[symbol_type] for symbol_type in symbol_types}

        # Add Type filters (use IN_RANGE if multiple types, otherwise EQUAL)
        if types_to_add:
            self._add_types(*types_to_add)

        # Special case: COMMON_STOCK automatically includes DEPOSITORY_RECEIPT
        # This maintains backward compatibility with existing behavior
        symbol_types_list = list(symbol_types)
        if SymbolType.COMMON_STOCK in symbol_types and SymbolType.DEPOSITORY_RECEIPT not in symbol_types:
            symbol_types_list.append(SymbolType.DEPOSITORY_RECEIPT)

        # Add subtype filters
        for symbol_type in symbol_types_list:
            self.add_filter(StockField.SUBTYPE, FilterOperator.IN_RANGE, symbol_type.value.copy())

    def set_markets(self, *markets: Market):
        """
        Set the markets to be scanned
        :param markets: list of markets
        :return: self for method chaining
        """
        if Market.ALL in markets:
            self.markets = [market for market in Market]
        else:
            self.markets = [market for market in markets]
        return self
