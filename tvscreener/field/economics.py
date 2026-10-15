from tvscreener.field import Field


class EconomicsField(Field):
    """
    EconomicsField enum generated from /economics2/metainfo by scripts/generate_fields.py (15/10/2026).

    Only fields that returned data on real symbols are included.

    Each field is defined as:
    ENUM_NAME = 'Label', 'api_name', 'format_type', supports_interval, supports_history
    """

    ACTIVE_SYMBOL = 'Active Symbol', 'active_symbol', 'bool', False, False
    BARS_COUNT = 'Bars Count', 'bars_count', 'float', False, False
    CHANGE = 'Change', 'change', 'percent', False, False
    CHANGE_ABS = 'Change Abs', 'change_abs', 'float', False, False
    CHANGE_FROM_OPEN = 'Change From Open', 'change_from_open', 'percent', False, False
    CHANGE_FROM_OPEN_ABS = 'Change From Open Abs', 'change_from_open_abs', 'float', False, False
    CLOSE = 'Close', 'close', 'float', False, False
    COUNTRY_CODE = 'Country Code', 'country_code', 'text', False, False
    CURRENCY = 'Currency', 'currency', 'text', False, False
    CURRENCY_ID = 'Currency ID', 'currency_id', 'text', False, False
    CURRENCY_KIND = 'Currency Kind', 'currency_kind', 'text', False, False
    DESCRIPTION = 'Description', 'description', 'text', False, False
    ECONOMIC_CATEGORY_ID = 'Economic Category ID', 'economic-category-id', 'text', False, False
    EXCHANGE = 'Exchange', 'exchange', 'text', False, False
    GAP = 'Gap', 'gap', 'percent', False, False
    GAP_DOWN = 'Gap Down', 'gap_down', 'percent', False, False
    GAP_DOWN_ABS = 'Gap Down Abs', 'gap_down_abs', 'float', False, False
    GAP_UP = 'Gap Up', 'gap_up', 'percent', False, False
    GAP_UP_ABS = 'Gap Up Abs', 'gap_up_abs', 'float', False, False
    HIGH = 'High', 'high', 'float', False, False
    IS_BLACKLISTED = 'Is Blacklisted', 'is_blacklisted', 'bool', False, False
    IS_PRIMARY = 'Is Primary', 'is_primary', 'bool', False, False
    KIND = 'Kind', 'kind', 'text', False, False
    KIND_DELAY = 'Kind Delay', 'kind-delay', 'float', False, False
    LAST_BAR_UPDATE_TIME = 'Last Bar Update Time', 'last_bar_update_time', 'float', False, False
    LOW = 'Low', 'low', 'float', False, False
    MARKET = 'Market', 'market', 'text', False, False
    MEASURE = 'Measure', 'measure', 'text', False, False
    NAME = 'Name', 'name', 'text', False, False
    OPEN = 'Open', 'open', 'float', False, False
    TIME = 'Time', 'time', 'date', False, False
    TYPE = 'Type', 'type', 'text', False, False
    TYPESPECS = 'Typespecs', 'typespecs', 'text', False, False
    UNIT_ID = 'Unit ID', 'unit-id', 'text', False, False
    UPDATE_MODE = 'Update Mode', 'update_mode', 'text', False, False
    UPDATE_TIME = 'Update Time', 'update_time', 'date', False, False
    VALUE_UNIT_ID = 'Value Unit ID', 'value-unit-id', 'text', False, False
