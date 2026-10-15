from tvscreener.core.stock import StockScreener
from tvscreener.field.stock import StockField

# Same universe as TradingView's ETF screener: ETFs and exchange-traded notes (structured)
ETF_UNIVERSE = StockField.TYPESPECS.has(['etf']) | (StockField.TYPE == 'structured')

DEFAULT_ETF_FIELDS = [
    StockField.NAME,
    StockField.DESCRIPTION,
    StockField.PRICE,
    StockField.CHANGE_PERCENT,
    StockField.VOLUMEXPRICE,
    StockField.RELATIVE_VOLUME,
    StockField.AUM,
    StockField.NAV_TOTAL_RETURN_3Y,
    StockField.ETF_HOLDINGS_COUNT,
    StockField.EXPENSE_RATIO,
    StockField.ASSET_CLASS_NAME,
    StockField.FOCUS_NAME,
    StockField.ISSUER,
    StockField.INDEX_TRACKED,
]


class ETFScreener(StockScreener):
    """
    ETF screener: ETFs and exchange-traded notes, sorted by assets under management.

    Uses StockField, so every stock field works, plus the ETF fields (AUM, EXPENSE_RATIO,
    FUND_FLOWS_*, NAV_TOTAL_RETURN_*, ISSUER, INDEX_TRACKED...). Fields such as ASSET_CLASS
    or FOCUS hold TradingView codes; their *_NAME variants hold the readable names.

    Example:
        >>> es = ETFScreener()
        >>> es.where(StockField.EXPENSE_RATIO < 0.1)
        >>> es.where(StockField.ASSET_CLASS_NAME == 'Equity')
        >>> df = es.get()
    """

    def __init__(self):
        super().__init__()
        self.specific_fields = DEFAULT_ETF_FIELDS
        self.sort_by(StockField.AUM, False)
        self.filter_groups.append(ETF_UNIVERSE)
