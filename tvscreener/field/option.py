from tvscreener.field import Field


class OptionField(Field):
    """
    OptionField enum with the option contract fields returned by the
    TradingView options scanner (scanner.tradingview.com/options/scan).

    Greeks and implied volatilities are per contract. Implied volatilities are
    fractions (0.27 means 27%). Values close to expiration can be extreme.

    The options scanner does not return last price, volume or open interest.

    Each field is defined as:
    ENUM_NAME = 'Label', 'api_name', 'format_type', is_technical, is_oscillator
    """

    NAME = 'Name', 'name', 'text', False, False
    DESCRIPTION = 'Description', 'description', 'text', False, False
    ROOT = 'Root', 'root', 'text', False, False
    UNDERLYING_SYMBOL = 'Underlying Symbol', 'underlying_symbol', 'text', False, False
    OPTION_TYPE = 'Option Type', 'option-type', 'text', False, False
    STRIKE = 'Strike', 'strike', 'float', False, False
    EXPIRATION = 'Expiration', 'expiration', 'date', False, False
    BID = 'Bid', 'bid', 'float', False, False
    ASK = 'Ask', 'ask', 'float', False, False
    BID_ASK_SPREAD_PCT = 'Bid Ask Spread Pct', 'bid_ask_spread_pct', 'percent', False, False
    THEORETICAL_PRICE = 'Theoretical Price', 'theoPrice', 'float', False, False
    IMPLIED_VOLATILITY = 'Implied Volatility', 'iv', 'float', False, False
    BID_IMPLIED_VOLATILITY = 'Bid Implied Volatility', 'bid_iv', 'float', False, False
    ASK_IMPLIED_VOLATILITY = 'Ask Implied Volatility', 'ask_iv', 'float', False, False
    DELTA = 'Delta', 'delta', 'float', False, False
    GAMMA = 'Gamma', 'gamma', 'float', False, False
    THETA = 'Theta', 'theta', 'float', False, False
    VEGA = 'Vega', 'vega', 'float', False, False
    RHO = 'Rho', 'rho', 'float', False, False
    CURRENCY = 'Currency', 'currency', 'text', False, False
    EXCHANGE = 'Exchange', 'exchange', 'text', False, False
    TYPE = 'Type', 'type', 'text', False, False
    MARKET = 'Market', 'market', 'text', False, False
    PRICE_SCALE = 'Price Scale', 'pricescale', 'float', False, False
    MIN_MOVE = 'Min Move', 'minmov', 'float', False, False
    DATA_DELAY = 'Data Delay', 'kind-delay', 'float', False, False
    IS_PRIMARY = 'Is Primary', 'is_primary', 'bool', False, False
    UPDATE_TIME = 'Update Time', 'update-time', 'float', False, False


DEFAULT_OPTION_FIELDS = [
    OptionField.UNDERLYING_SYMBOL,
    OptionField.OPTION_TYPE,
    OptionField.STRIKE,
    OptionField.EXPIRATION,
    OptionField.BID,
    OptionField.ASK,
    OptionField.THEORETICAL_PRICE,
    OptionField.IMPLIED_VOLATILITY,
    OptionField.BID_IMPLIED_VOLATILITY,
    OptionField.ASK_IMPLIED_VOLATILITY,
    OptionField.DELTA,
    OptionField.GAMMA,
    OptionField.THETA,
    OptionField.VEGA,
    OptionField.RHO,
]
