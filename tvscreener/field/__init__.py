import math
from enum import Enum


def add_time_interval(field_name, update_mode):
    return f"{field_name}|{update_mode}"


def add_historical(field_name, historical=1):
    return f"{field_name}[{historical}]"


def add_historical_to_label(field_name, historical=1):
    return f"Prev. {field_name}"


def add_rec(field_name):
    return f"Rec.{field_name}"


def add_rec_to_label(label):
    return f"Reco. {label}"


class Field(Enum):

    def __init__(self, label, field_name, format_=None, interval=False, historical=False):
        self.label = label
        self.field_name = field_name
        self.format = format_
        self.interval = interval
        self.historical = historical

    def has_recommendation(self):
        return self.format == 'recommendation'

    def get_rec_label(self):
        if self.has_recommendation():
            return add_rec_to_label(self.label)
        return None

    def get_rec_field(self):
        if self.has_recommendation():
            return add_rec(self.field_name)
        return None

    @classmethod
    def get_by_label(cls, specific_fields, label):
        for specific_field in specific_fields:
            if specific_field.label == label:
                return specific_field
        return None

    @classmethod
    def search(cls, query: str) -> list:
        """
        Search fields by name or label.

        :param query: Search query (case-insensitive)
        :return: List of matching Field enum members

        Example:
            >>> StockField.search("market cap")
            [<StockField.MARKET_CAPITALIZATION: ...>, <StockField.MARKET_CAP_BASIC: ...>, ...]
        """
        query = query.lower()
        return [f for f in cls if query in f.name.lower() or query in f.label.lower()]

    @classmethod
    def by_format(cls, format_type: str) -> list:
        """
        Get fields by format type.

        :param format_type: Format type (e.g., 'percent', 'float', 'text', 'recommendation')
        :return: List of fields with matching format

        Example:
            >>> StockField.by_format('recommendation')
            [<StockField.RSI: ...>, <StockField.MACD: ...>, ...]
        """
        return [f for f in cls if f.format == format_type]

    @classmethod
    def technicals(cls) -> list:
        """
        Get all technical indicator fields (fields with interval=True).

        :return: List of technical indicator fields

        Example:
            >>> StockField.technicals()
            [<StockField.RSI: ...>, <StockField.MACD: ...>, ...]
        """
        return [f for f in cls if f.interval]

    @classmethod
    def with_history(cls) -> list:
        """
        Get all fields that support historical lookback.

        :return: List of fields with historical=True

        Example:
            >>> StockField.with_history()
            [<StockField.RSI: ...>, <StockField.VOLUME: ...>, ...]
        """
        return [f for f in cls if f.historical]

    @classmethod
    def recommendations(cls) -> list:
        """
        Get all recommendation fields.

        :return: List of fields with format='recommendation'

        Example:
            >>> StockField.recommendations()
            [<StockField.RSI: ...>, <StockField.STOCH_K: ...>, ...]
        """
        return [f for f in cls if f.format == 'recommendation']

    def with_interval(self, interval: str) -> 'FieldWithInterval':
        """
        Return a field wrapper with time interval modifier.

        Supported intervals: '1', '5', '15', '30', '60', '120', '240', '1D', '1W', '1M'

        :param interval: Time interval string
        :return: FieldWithInterval wrapper
        :raises ValueError: If field does not support intervals

        Example:
            >>> StockField.RSI.with_interval('1H')
            FieldWithInterval(RSI, interval='1H')
        """
        if not self.interval:
            raise ValueError(f"{self.name} does not support time intervals")
        return FieldWithInterval(self, interval)

    def with_history(self, periods: int = 1) -> 'FieldWithHistory':
        """
        Return a field wrapper with historical lookback.

        :param periods: Number of periods to look back (default 1)
        :return: FieldWithHistory wrapper
        :raises ValueError: If field does not support historical lookback

        Example:
            >>> StockField.VOLUME.with_history(1)  # Previous period volume
            FieldWithHistory(VOLUME, periods=1)
        """
        if not self.historical:
            raise ValueError(f"{self.name} does not support historical lookback")
        return FieldWithHistory(self, periods)

    # Comparison operators for Pythonic filtering syntax
    def __gt__(self, other) -> 'FieldCondition':
        """
        Greater than comparison.

        Example:
            >>> StockField.PRICE > 100
        """
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.ABOVE, other)

    def __ge__(self, other) -> 'FieldCondition':
        """
        Greater than or equal comparison.

        Example:
            >>> StockField.PRICE >= 100
        """
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.ABOVE_OR_EQUAL, other)

    def __lt__(self, other) -> 'FieldCondition':
        """
        Less than comparison.

        Example:
            >>> StockField.PRICE < 100
        """
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.BELOW, other)

    def __le__(self, other) -> 'FieldCondition':
        """
        Less than or equal comparison.

        Example:
            >>> StockField.PRICE <= 100
        """
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.BELOW_OR_EQUAL, other)

    def __eq__(self, other) -> 'FieldCondition':
        """
        Equality comparison. Returns FieldCondition for value comparisons,
        or standard enum equality for Field-to-Field comparisons.

        Example:
            >>> StockField.SECTOR == 'Technology'
        """
        # For enum-to-enum comparison, use standard Enum equality
        if isinstance(other, Field):
            return self.value == other.value
        # For Field vs FieldWithInterval/FieldWithHistory, compare field_name
        if hasattr(other, 'field_name'):
            return self.field_name == other.field_name
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.EQUAL, other)

    def __ne__(self, other) -> 'FieldCondition':
        """
        Not equal comparison. Returns FieldCondition for value comparisons,
        or standard enum inequality for Field-to-Field comparisons.

        Example:
            >>> StockField.SECTOR != 'Technology'
        """
        # For enum-to-enum comparison, use standard Enum inequality
        if isinstance(other, Field):
            return self.value != other.value
        # For Field vs FieldWithInterval/FieldWithHistory, compare field_name
        if hasattr(other, 'field_name'):
            return self.field_name != other.field_name
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.NOT_EQUAL, other)

    def __hash__(self):
        """Required for Enum when __eq__ is overridden."""
        return hash(self.value)

    def between(self, min_val, max_val) -> 'FieldCondition':
        """
        Check if field value is within a range (inclusive).

        Example:
            >>> StockField.PRICE.between(50, 100)
            >>> StockField.MARKET_CAPITALIZATION.between(1e9, 10e9)
        """
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.IN_RANGE, [min_val, max_val])

    def not_between(self, min_val, max_val) -> 'FieldCondition':
        """
        Check if field value is outside a range.

        Example:
            >>> StockField.PRICE.not_between(50, 100)
        """
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.NOT_IN_RANGE, [min_val, max_val])

    def isin(self, values: list) -> 'FieldCondition':
        """
        Check if field value is in a list of values.

        Example:
            >>> StockField.SECTOR.isin(['Technology', 'Healthcare'])
            >>> StockField.EXCHANGE.isin([Exchange.NASDAQ, Exchange.NYSE])
        """
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.IN_RANGE, values)

    def not_in(self, values: list) -> 'FieldCondition':
        """
        Check if field value is not in a list of values.

        Example:
            >>> StockField.SECTOR.not_in(['Finance', 'Utilities'])
        """
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.NOT_IN_RANGE, values)


class FieldCondition:
    """Forward declaration for type hints - actual implementation is in filter.py"""
    pass


class FieldWithInterval:
    """
    Wrapper for a Field with a time interval modifier.

    This allows specifying different timeframes for technical indicators.
    """

    def __init__(self, field: Field, interval: str):
        """
        Initialize a field with interval wrapper.

        :param field: The base Field enum member
        :param interval: Time interval (e.g., '1', '5', '15', '1H', '1D', '1W', '1M')
        """
        self.field = field
        self._interval = interval
        self.field_name = f"{field.field_name}|{interval}"
        self.label = f"{field.label} ({interval})"
        self.format = field.format
        self.interval = True
        self.historical = field.historical
        self.name = f"{field.name}_{interval}"  # For repr in FieldCondition

    def __repr__(self):
        return f"FieldWithInterval({self.field.name}, interval='{self._interval}')"

    # Comparison operators
    def __gt__(self, other):
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.ABOVE, other)

    def __ge__(self, other):
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.ABOVE_OR_EQUAL, other)

    def __lt__(self, other):
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.BELOW, other)

    def __le__(self, other):
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.BELOW_OR_EQUAL, other)

    def __eq__(self, other):
        # For comparison with Field or FieldWithInterval, compare field_name
        if isinstance(other, Field) or hasattr(other, 'field_name'):
            return self.field_name == other.field_name
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.EQUAL, other)

    def __ne__(self, other):
        # For comparison with Field or FieldWithInterval, compare field_name
        if isinstance(other, Field) or hasattr(other, 'field_name'):
            return self.field_name != other.field_name
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.NOT_EQUAL, other)

    def __hash__(self):
        """Required when __eq__ is overridden."""
        return hash(self.field_name)

    def between(self, min_val, max_val):
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.IN_RANGE, [min_val, max_val])

    def not_between(self, min_val, max_val):
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.NOT_IN_RANGE, [min_val, max_val])

    def isin(self, values: list):
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.IN_RANGE, values)

    def not_in(self, values: list):
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.NOT_IN_RANGE, values)


class FieldWithHistory:
    """
    Wrapper for a Field with historical lookback.

    This allows getting previous period values for indicators.
    """

    def __init__(self, field: Field, periods: int = 1):
        """
        Initialize a field with historical lookback.

        :param field: The base Field enum member
        :param periods: Number of periods to look back
        """
        self.field = field
        self.periods = periods
        self.field_name = f"{field.field_name}[{periods}]"
        self.label = f"Prev. {field.label}" if periods == 1 else f"{field.label} [{periods}]"
        self.format = field.format
        self.interval = field.interval
        self.historical = True
        self.name = f"{field.name}_history_{periods}"  # For repr in FieldCondition

    def __repr__(self):
        return f"FieldWithHistory({self.field.name}, periods={self.periods})"

    # Comparison operators
    def __gt__(self, other):
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.ABOVE, other)

    def __ge__(self, other):
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.ABOVE_OR_EQUAL, other)

    def __lt__(self, other):
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.BELOW, other)

    def __le__(self, other):
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.BELOW_OR_EQUAL, other)

    def __eq__(self, other):
        # For comparison with Field or FieldWithHistory, compare field_name
        if isinstance(other, Field) or hasattr(other, 'field_name'):
            return self.field_name == other.field_name
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.EQUAL, other)

    def __ne__(self, other):
        # For comparison with Field or FieldWithHistory, compare field_name
        if isinstance(other, Field) or hasattr(other, 'field_name'):
            return self.field_name != other.field_name
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.NOT_EQUAL, other)

    def __hash__(self):
        """Required when __eq__ is overridden."""
        return hash(self.field_name)

    def between(self, min_val, max_val):
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.IN_RANGE, [min_val, max_val])

    def not_between(self, min_val, max_val):
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.NOT_IN_RANGE, [min_val, max_val])

    def isin(self, values: list):
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.IN_RANGE, values)

    def not_in(self, values: list):
        from tvscreener.filter import FieldCondition, FilterOperator
        return FieldCondition(self, FilterOperator.NOT_IN_RANGE, values)


class Type(Enum):
    STOCK = "stock"
    DEPOSITORY_RECEIPT = "dr"
    FUND = "fund"
    STRUCTURED = "structured"


class Rating(Enum):
    STRONG_BUY = 0.5, 1, "Strong Buy"
    BUY = 0.1, 0.5, "Buy"
    NEUTRAL = -0.1, 0.1, "Neutral"
    SELL = -0.5, -0.1, "Sell"
    STRONG_SELL = -1, -0.5, "Strong Sell"
    UNKNOWN = math.nan, math.nan, "Unknown"

    def __init__(self, min_, max_, label):
        self.min = min_
        self.max = max_
        self.label = label

    def __contains__(self, item):
        return self.min <= item <= self.max

    def range(self):
        return [self.min, self.max]

    @classmethod
    def find(cls, value: float):
        if value is not None:
            for rating in Rating:
                if value in rating:
                    return rating
        return Rating.UNKNOWN

    @classmethod
    def names(cls):
        return list(map(lambda c: c.name, cls))

    @classmethod
    def values(cls):
        return list(map(lambda c: c.value, cls))


class Country(Enum):
    ALBANIA = 'Albania'
    ARGENTINA = 'Argentina'
    AUSTRALIA = 'Australia'
    AUSTRIA = 'Austria'
    AZERBAIJAN = 'Azerbaijan'
    BAHAMAS = 'Bahamas'
    BARBADOS = 'Barbados'
    BELGIUM = 'Belgium'
    BERMUDA = 'Bermuda'
    BRAZIL = 'Brazil'
    BRITISH_VIRGIN_ISLANDS = 'British Virgin Islands'
    CAMBODIA = 'Cambodia'
    CANADA = 'Canada'
    CAYMAN_ISLANDS = 'Cayman Islands'
    CHILE = 'Chile'
    CHINA = 'China'
    COLOMBIA = 'Colombia'
    COSTA_RICA = 'Costa Rica'
    CYPRUS = 'Cyprus'
    CZECH_REPUBLIC = 'Czech Republic'
    DENMARK = 'Denmark'
    DOMINICAN_REPUBLIC = 'Dominican Republic'
    EGYPT = 'Egypt'
    FAROE_ISLANDS = 'Faroe Islands'
    FINLAND = 'Finland'
    FRANCE = 'France'
    GERMANY = 'Germany'
    GIBRALTAR = 'Gibraltar'
    GREECE = 'Greece'
    HONG_KONG = 'Hong Kong'
    HUNGARY = 'Hungary'
    ICELAND = 'Iceland'
    INDIA = 'India'
    INDONESIA = 'Indonesia'
    IRELAND = 'Ireland'
    ISRAEL = 'Israel'
    ITALY = 'Italy'
    JAMAICA = 'Jamaica'
    JAPAN = 'Japan'
    JORDAN = 'Jordan'
    KAZAKHSTAN = 'Kazakhstan'
    LUXEMBOURG = 'Luxembourg'
    MACAU = 'Macau'
    MACEDONIA = 'Macedonia'
    MALAYSIA = 'Malaysia'
    MALTA = 'Malta'
    MAURITIUS = 'Mauritius'
    MEXICO = 'Mexico'
    MONACO = 'Monaco'
    MONGOLIA = 'Mongolia'
    MONTENEGRO = 'Montenegro'
    NETHERLANDS = 'Netherlands'
    NEW_ZEALAND = 'New Zealand'
    NORWAY = 'Norway'
    PANAMA = 'Panama'
    PERU = 'Peru'
    PHILIPPINES = 'Philippines'
    POLAND = 'Poland'
    PORTUGAL = 'Portugal'
    PUERTO_RICO = 'Puerto Rico'
    ROMANIA = 'Romania'
    RUSSIAN_FEDERATION = 'Russian Federation'
    SINGAPORE = 'Singapore'
    SOUTH_AFRICA = 'South Africa'
    SOUTH_KOREA = 'South Korea'
    SPAIN = 'Spain'
    SWEDEN = 'Sweden'
    SWITZERLAND = 'Switzerland'
    TAIWAN = 'Taiwan'
    TANZANIA = 'Tanzania'
    THAILAND = 'Thailand'
    TURKEY = 'Turkey'
    U_S__VIRGIN_ISLANDS = 'U.S. Virgin Islands'
    UNITED_ARAB_EMIRATES = 'United Arab Emirates'
    UNITED_KINGDOM = 'United Kingdom'
    UNITED_STATES = 'United States'
    URUGUAY = 'Uruguay'
    VIETNAM = 'Vietnam'


class Exchange(Enum):
    OTC = "OTC"
    NYSE_ARCA = "AMEX"
    NASDAQ = "NASDAQ"
    NYSE = "NYSE"


class Index(Enum):
    DOW_JONES_COMPOSITE_AVERAGE = 'Dow Jones Composite Average'
    DOW_JONES_INDUSTRIAL_AVERAGE = 'Dow Jones Industrial Average'
    DOW_JONES_TRANSPORTATION_AVERAGE = 'Dow Jones Transportation Average'
    DOW_JONES_UTILITY_AVERAGE = 'Dow Jones Utility Average'
    KBW_NASDAQ_BANK_INDEX = 'KBW NASDAQ BANK INDEX'
    MINI_RUSSELL_2000_INDEX = 'MINI RUSSELL 2000 INDEX'
    NASDAQ_100 = 'NASDAQ 100'
    NASDAQ_100_TECHNOLOGY_SECTOR = 'NASDAQ 100 TECHNOLOGY SECTOR'
    NASDAQ_BANK = 'NASDAQ BANK'
    NASDAQ_BIOTECHNOLOGY = 'NASDAQ BIOTECHNOLOGY'
    NASDAQ_COMPOSITE = 'NASDAQ COMPOSITE'
    NASDAQ_COMPUTER = 'NASDAQ COMPUTER'
    NASDAQ_GOLDEN_DRAGON_CHINA_INDEX = 'NASDAQ GOLDEN DRAGON CHINA INDEX'
    NASDAQ_INDUSTRIAL = 'NASDAQ INDUSTRIAL'
    NASDAQ_INSURANCE = 'NASDAQ INSURANCE'
    NASDAQ_OTHER_FINANCE = 'NASDAQ OTHER FINANCE'
    NASDAQ_TELECOMMUNICATIONS = 'NASDAQ TELECOMMUNICATIONS'
    NASDAQ_TRANSPORTATION = 'NASDAQ TRANSPORTATION'
    NASDAQ_US_BENCHMARK_FOOD_PRODUCERS_INDEX = 'NASDAQ US BENCHMARK FOOD PRODUCERS INDEX'
    NYSE_ARCA_MAJOR_MARKET = 'NYSE ARCA MAJOR MARKET'
    PHLX_GOLD_AND_SILVER_SECTOR_INDEX = 'PHLX GOLD AND SILVER SECTOR INDEX'
    PHLX_HOUSING_SECTOR = 'PHLX HOUSING SECTOR'
    PHLX_OIL_SERVICE_SECTOR = 'PHLX OIL SERVICE SECTOR'
    PHLX_SEMICONDUCTOR = 'PHLX SEMICONDUCTOR'
    PHLX_UTILITY_SECTOR = 'PHLX UTILITY SECTOR'
    RUSSELL_1000 = 'RUSSELL 1000'
    RUSSELL_2000 = 'RUSSELL 2000'
    RUSSELL_3000 = 'RUSSELL 3000'
    SANDP_100 = 'S&P 100'
    SANDP_400 = 'S&P 400'
    SANDP_500 = 'S&P 500'
    SANDP_500_COMMUNICATION_SERVICES = 'S&P 500 Communication Services'
    SANDP_500_CONSUMER_DISCRETIONARY = 'S&P 500 Consumer Discretionary'
    SANDP_500_CONSUMER_STAPLES = 'S&P 500 Consumer Staples'
    SANDP_500_ESG_INDEX = 'S&P 500 ESG INDEX'
    SANDP_500_ENERGY = 'S&P 500 Energy'
    SANDP_500_FINANCIALS = 'S&P 500 Financials'
    SANDP_500_HEALTH_CARE = 'S&P 500 Health Care'
    SANDP_500_INDUSTRIALS = 'S&P 500 Industrials'
    SANDP_500_INFORMATION_TECHNOLOGY = 'S&P 500 Information Technology'
    SANDP_500_MATERIALS = 'S&P 500 Materials'
    SANDP_500_REAL_ESTATE = 'S&P 500 Real Estate'
    SANDP_500_UTILITIES = 'S&P 500 Utilities'


class Industry(Enum):
    ADVERTISINGMARKETING_SERVICES = 'Advertising/Marketing Services'
    AEROSPACE_AND_DEFENSE = 'Aerospace & Defense'
    AGRICULTURAL_COMMODITIESMILLING = 'Agricultural Commodities/Milling'
    AIR_FREIGHTCOURIERS = 'Air Freight/Couriers'
    AIRLINES = 'Airlines'
    ALTERNATIVE_POWER_GENERATION = 'Alternative Power Generation'
    ALUMINUM = 'Aluminum'
    APPARELFOOTWEAR = 'Apparel/Footwear'
    APPARELFOOTWEAR_RETAIL = 'Apparel/Footwear Retail'
    AUTO_PARTS_OEM = 'Auto Parts: OEM'
    AUTOMOTIVE_AFTERMARKET = 'Automotive Aftermarket'
    BEVERAGES_ALCOHOLIC = 'Beverages: Alcoholic'
    BEVERAGES_NONALCOHOLIC = 'Beverages: Non-Alcoholic'
    BIOTECHNOLOGY = 'Biotechnology'
    BROADCASTING = 'Broadcasting'
    BUILDING_PRODUCTS = 'Building Products'
    CABLESATELLITE_TV = 'Cable/Satellite TV'
    CASINOSGAMING = 'Casinos/Gaming'
    CATALOGSPECIALTY_DISTRIBUTION = 'Catalog/Specialty Distribution'
    CHEMICALS_AGRICULTURAL = 'Chemicals: Agricultural'
    CHEMICALS_MAJOR_DIVERSIFIED = 'Chemicals: Major Diversified'
    CHEMICALS_SPECIALTY = 'Chemicals: Specialty'
    COAL = 'Coal'
    COMMERCIAL_PRINTINGFORMS = 'Commercial Printing/Forms'
    COMPUTER_COMMUNICATIONS = 'Computer Communications'
    COMPUTER_PERIPHERALS = 'Computer Peripherals'
    COMPUTER_PROCESSING_HARDWARE = 'Computer Processing Hardware'
    CONSTRUCTION_MATERIALS = 'Construction Materials'
    CONSUMER_SUNDRIES = 'Consumer Sundries'
    CONTAINERSPACKAGING = 'Containers/Packaging'
    CONTRACT_DRILLING = 'Contract Drilling'
    DATA_PROCESSING_SERVICES = 'Data Processing Services'
    DEPARTMENT_STORES = 'Department Stores'
    DISCOUNT_STORES = 'Discount Stores'
    DRUGSTORE_CHAINS = 'Drugstore Chains'
    ELECTRIC_UTILITIES = 'Electric Utilities'
    ELECTRICAL_PRODUCTS = 'Electrical Products'
    ELECTRONIC_COMPONENTS = 'Electronic Components'
    ELECTRONIC_EQUIPMENTINSTRUMENTS = 'Electronic Equipment/Instruments'
    ELECTRONIC_PRODUCTION_EQUIPMENT = 'Electronic Production Equipment'
    ELECTRONICS_DISTRIBUTORS = 'Electronics Distributors'
    ELECTRONICSAPPLIANCE_STORES = 'Electronics/Appliance Stores'
    ELECTRONICSAPPLIANCES = 'Electronics/Appliances'
    ENGINEERING_AND_CONSTRUCTION = 'Engineering & Construction'
    ENVIRONMENTAL_SERVICES = 'Environmental Services'
    FINANCERENTALLEASING = 'Finance/Rental/Leasing'
    FINANCIAL_CONGLOMERATES = 'Financial Conglomerates'
    FINANCIAL_PUBLISHINGSERVICES = 'Financial Publishing/Services'
    FOOD_DISTRIBUTORS = 'Food Distributors'
    FOOD_RETAIL = 'Food Retail'
    FOOD_MAJOR_DIVERSIFIED = 'Food: Major Diversified'
    FOOD_MEATFISHDAIRY = 'Food: Meat/Fish/Dairy'
    FOOD_SPECIALTYCANDY = 'Food: Specialty/Candy'
    FOREST_PRODUCTS = 'Forest Products'
    GAS_DISTRIBUTORS = 'Gas Distributors'
    GENERAL_GOVERNMENT = 'General Government'
    HOME_FURNISHINGS = 'Home Furnishings'
    HOME_IMPROVEMENT_CHAINS = 'Home Improvement Chains'
    HOMEBUILDING = 'Homebuilding'
    HOSPITALNURSING_MANAGEMENT = 'Hospital/Nursing Management'
    HOTELSRESORTSCRUISE_LINES = 'Hotels/Resorts/Cruise lines'
    HOUSEHOLDPERSONAL_CARE = 'Household/Personal Care'
    INDUSTRIAL_CONGLOMERATES = 'Industrial Conglomerates'
    INDUSTRIAL_MACHINERY = 'Industrial Machinery'
    INDUSTRIAL_SPECIALTIES = 'Industrial Specialties'
    INFORMATION_TECHNOLOGY_SERVICES = 'Information Technology Services'
    INSURANCE_BROKERSSERVICES = 'Insurance Brokers/Services'
    INTEGRATED_OIL = 'Integrated Oil'
    INTERNET_RETAIL = 'Internet Retail'
    INTERNET_SOFTWARESERVICES = 'Internet Software/Services'
    INVESTMENT_BANKSBROKERS = 'Investment Banks/Brokers'
    INVESTMENT_MANAGERS = 'Investment Managers'
    INVESTMENT_TRUSTSMUTUAL_FUNDS = 'Investment Trusts/Mutual Funds'
    LIFEHEALTH_INSURANCE = 'Life/Health Insurance'
    MAJOR_BANKS = 'Major Banks'
    MAJOR_TELECOMMUNICATIONS = 'Major Telecommunications'
    MANAGED_HEALTH_CARE = 'Managed Health Care'
    MARINE_SHIPPING = 'Marine Shipping'
    MEDIA_CONGLOMERATES = 'Media Conglomerates'
    MEDICAL_DISTRIBUTORS = 'Medical Distributors'
    MEDICAL_SPECIALTIES = 'Medical Specialties'
    MEDICALNURSING_SERVICES = 'Medical/Nursing Services'
    METAL_FABRICATION = 'Metal Fabrication'
    MISCELLANEOUS = 'Miscellaneous'
    MISCELLANEOUS_COMMERCIAL_SERVICES = 'Miscellaneous Commercial Services'
    MISCELLANEOUS_MANUFACTURING = 'Miscellaneous Manufacturing'
    MOTOR_VEHICLES = 'Motor Vehicles'
    MOVIESENTERTAINMENT = 'Movies/Entertainment'
    MULTILINE_INSURANCE = 'Multi-Line Insurance'
    OFFICE_EQUIPMENTSUPPLIES = 'Office Equipment/Supplies'
    OIL_AND_GAS_PIPELINES = 'Oil & Gas Pipelines'
    OIL_AND_GAS_PRODUCTION = 'Oil & Gas Production'
    OIL_REFININGMARKETING = 'Oil Refining/Marketing'
    OILFIELD_SERVICESEQUIPMENT = 'Oilfield Services/Equipment'
    OTHER_CONSUMER_SERVICES = 'Other Consumer Services'
    OTHER_CONSUMER_SPECIALTIES = 'Other Consumer Specialties'
    OTHER_METALSMINERALS = 'Other Metals/Minerals'
    OTHER_TRANSPORTATION = 'Other Transportation'
    PACKAGED_SOFTWARE = 'Packaged Software'
    PERSONNEL_SERVICES = 'Personnel Services'
    PHARMACEUTICALS_GENERIC = 'Pharmaceuticals: Generic'
    PHARMACEUTICALS_MAJOR = 'Pharmaceuticals: Major'
    PHARMACEUTICALS_OTHER = 'Pharmaceuticals: Other'
    PRECIOUS_METALS = 'Precious Metals'
    PROPERTYCASUALTY_INSURANCE = 'Property/Casualty Insurance'
    PUBLISHING_BOOKSMAGAZINES = 'Publishing: Books/Magazines'
    PUBLISHING_NEWSPAPERS = 'Publishing: Newspapers'
    PULP_AND_PAPER = 'Pulp & Paper'
    RAILROADS = 'Railroads'
    REAL_ESTATE_DEVELOPMENT = 'Real Estate Development'
    REAL_ESTATE_INVESTMENT_TRUSTS = 'Real Estate Investment Trusts'
    RECREATIONAL_PRODUCTS = 'Recreational Products'
    REGIONAL_BANKS = 'Regional Banks'
    RESTAURANTS = 'Restaurants'
    SAVINGS_BANKS = 'Savings Banks'
    SEMICONDUCTORS = 'Semiconductors'
    SERVICES_TO_THE_HEALTH_INDUSTRY = 'Services to the Health Industry'
    SPECIALTY_INSURANCE = 'Specialty Insurance'
    SPECIALTY_STORES = 'Specialty Stores'
    SPECIALTY_TELECOMMUNICATIONS = 'Specialty Telecommunications'
    STEEL = 'Steel'
    TELECOMMUNICATIONS_EQUIPMENT = 'Telecommunications Equipment'
    TEXTILES = 'Textiles'
    TOBACCO = 'Tobacco'
    TOOLS_AND_HARDWARE = 'Tools & Hardware'
    TRUCKING = 'Trucking'
    TRUCKSCONSTRUCTIONFARM_MACHINERY = 'Trucks/Construction/Farm Machinery'
    WATER_UTILITIES = 'Water Utilities'
    WHOLESALE_DISTRIBUTORS = 'Wholesale Distributors'
    WIRELESS_TELECOMMUNICATIONS = 'Wireless Telecommunications'


class Sector(Enum):
    ANY = "Any"
    COMMERCIAL_SERVICES = "Commercial Services"
    COMMUNICATIONS = "Communications"
    CONSUMER_DURABLES = "Consumer Durables"
    CONSUMER_NON_DURABLES = "Consumer Non-Durables"
    CONSUMER_SERVICES = "Consumer Services"
    DISTRIBUTION_SERVICES = "Distribution Services"
    ELECTRONIC_TECHNOLOGY = "Electronic Technology"
    ENERGY_MINERALS = "Energy Minerals"
    FINANCE = "Finance"
    GOVERNMENT = "Government"
    HEALTH_SERVICES = "Health Services"
    HEALTH_TECHNOLOGY = "Health Technology"
    INDUSTRIAL_SERVICES = "Industrial Services"
    MISCELLANEOUS = "Miscellaneous"
    NON_ENERGY_MINERALS = "Non-Energy Minerals"
    PROCESS_INDUSTRIES = "Process Industries"
    PRODUCER_MANUFACTURING = "Producer Manufacturing"
    RETAIL_TRADE = "Retail Trade"
    TECHNOLOGY_SERVICES = "Technology Services"
    TRANSPORTATION = "Transportation"
    UTILITIES = "Utilities"


class Market(Enum):
    ALL = "ALL"
    AMERICA = "america"
    UK = "uk"
    INDIA = "india"
    SPAIN = "spain"
    RUSSIA = "russia"
    AUSTRALIA = "australia"
    BRAZIL = "brazil"
    JAPAN = "japan"
    NEWZEALAND = "newzealand"
    TURKEY = "turkey"
    SWITZERLAND = "switzerland"
    HONGKONG = "hongkong"
    TAIWAN = "taiwan"
    NETHERLANDS = "netherlands"
    BELGIUM = "belgium"
    PORTUGAL = "portugal"
    FRANCE = "france"
    MEXICO = "mexico"
    CANADA = "canada"
    COLOMBIA = "colombia"
    UAE = "uae"
    NIGERIA = "nigeria"
    SINGAPORE = "singapore"
    GERMANY = "germany"
    PAKISTAN = "pakistan"
    PERU = "peru"
    POLAND = "poland"
    ITALY = "italy"
    ARGENTINA = "argentina"
    ISRAEL = "israel"
    EGYPT = "egypt"
    SRILANKA = "srilanka"
    SERBIA = "serbia"
    CHILE = "chile"
    CHINA = "china"
    MALAYSIA = "malaysia"
    MOROCCO = "morocco"
    KSA = "ksa"
    BAHRAIN = "bahrain"
    QATAR = "qatar"
    INDONESIA = "indonesia"
    FINLAND = "finland"
    ICELAND = "iceland"
    DENMARK = "denmark"
    ROMANIA = "romania"
    HUNGARY = "hungary"
    SWEDEN = "sweden"
    SLOVAKIA = "slovakia"
    LITHUANIA = "lithuania"
    LUXEMBOURG = "luxembourg"
    ESTONIA = "estonia"
    LATVIA = "latvia"
    VIETNAM = "vietnam"
    RSA = "rsa"
    THAILAND = "thailand"
    TUNISIA = "tunisia"
    KOREA = "korea"
    KENYA = "kenya"
    KUWAIT = "kuwait"
    NORWAY = "norway"
    PHILIPPINES = "philippines"
    GREECE = "greece"
    VENEZUELA = "venezuela"
    CYPRUS = "cyprus"
    BANGLADESH = "bangladesh"

    @classmethod
    def names(cls):
        return list(map(lambda c: c.name, cls))

    @classmethod
    def values(cls):
        return list(map(lambda c: c.value, cls))


class Region(Enum):
    AFRICA = "Africa"
    AMERICAS = "Americas"
    ASIA = "Asia"
    EUROPE = "Europe"
    MIDDLE_EAST = "Middle East"
    PACIFIC = "Pacific"


class SubMarket(Enum):
    OTCQB = "OTCQB"
    OTCQX = "OTCQX"
    PINK = "PINK"


class SymbolType(Enum):
    CLOSED_END_FUND = ["closedend"]
    COMMON_STOCK = ["common"]
    DEPOSITORY_RECEIPT = ["foreign-issuer"]
    ETF = ["etf", "etf,odd", "etf,otc", "etf,cfd"]
    ETN = ["etn"]
    MUTUAL_FUND = ["mutual"]
    PREFERRED_STOCK = ["preferred"]
    REIT = ["reit", "reit,cfd", "trust,reit"]
    STRUCTURED = [""]  # ["SP"]
    TRUST_FUND = ["trust"]
    UIT = ["unit"]


class IndexSymbol(Enum):
    """
    Index symbols for filtering screener results to index constituents.

    Use with Screener.set_index() to filter results to stocks belonging to a specific index.

    Example:
        >>> ss = StockScreener()
        >>> ss.set_index(IndexSymbol.SP500)
        >>> df = ss.get()  # Returns only S&P 500 constituents
    """
    # Major US Indices
    SP500 = ("SP;SPX", "S&P 500")
    NASDAQ_100 = ("NASDAQ;NDX", "NASDAQ 100")
    DOW_JONES = ("DJ;DJI", "Dow Jones Industrial Average")
    NASDAQ_COMPOSITE = ("NASDAQ;IXIC", "NASDAQ Composite")
    RUSSELL_2000 = ("TVC;RUT", "Russell 2000")
    RUSSELL_1000 = ("TVC;RUI", "Russell 1000")
    RUSSELL_3000 = ("TVC;RUA", "Russell 3000")
    SP100 = ("SP;OEX", "S&P 100")
    SP_MIDCAP_400 = ("SP;MID", "S&P MidCap 400")
    MINI_RUSSELL_2000 = ("CBOEFTSE;MRUT", "Mini-Russell 2000")

    # S&P 500 Sectors
    SP500_ENERGY = ("SP;SPN", "S&P 500 Energy")
    SP500_INFORMATION_TECHNOLOGY = ("SP;S5INFT", "S&P 500 Information Technology")
    SP500_HEALTH_CARE = ("SP;S5HLTH", "S&P 500 Health Care")
    SP500_CONSUMER_STAPLES = ("SP;S5CONS", "S&P 500 Consumer Staples")
    SP500_UTILITIES = ("SP;S5UTIL", "S&P 500 Utilities")
    SP500_COMMUNICATION_SERVICES = ("SP;S5TELS", "S&P 500 Communication Services")
    SP500_CONSUMER_DISCRETIONARY = ("SP;S5COND", "S&P 500 Consumer Discretionary")
    SP500_INDUSTRIALS = ("SP;S5INDU", "S&P 500 Industrials")
    SP500_REAL_ESTATE = ("SP;S5REAS", "S&P 500 Real Estate")
    SP500_MATERIALS = ("SP;S5MATR", "S&P 500 Materials")
    SP500_FINANCIALS = ("SP;SPF", "S&P 500 Financials")
    SP500_ESG = ("CBOE;SPESG", "S&P 500 ESG")

    # Dow Jones
    DOW_JONES_TRANSPORTATION = ("DJ;DJT", "Dow Jones Transportation Average")
    DOW_JONES_UTILITY = ("DJ;DJU", "Dow Jones Utility Average")
    DOW_JONES_COMPOSITE = ("DJ;DJA", "Dow Jones Composite Average")

    # NASDAQ Sector Indices
    NASDAQ_BANK = ("NASDAQ;BANK", "NASDAQ Bank")
    NASDAQ_BIOTECHNOLOGY = ("NASDAQ;NBI", "NASDAQ Biotechnology")
    NASDAQ_COMPUTER = ("NASDAQ;IXCO", "NASDAQ Computer")
    NASDAQ_TELECOMMUNICATIONS = ("NASDAQ;IXTC", "NASDAQ Telecommunications")
    NASDAQ_TRANSPORTATION = ("NASDAQ;TRAN", "NASDAQ Transportation")
    NASDAQ_INSURANCE = ("NASDAQ;INSR", "NASDAQ Insurance")
    NASDAQ_INDUSTRIALS = ("NASDAQ;INDS", "NASDAQ Industrials")
    NASDAQ_GOLDEN_DRAGON_CHINA = ("NASDAQ;HXC", "NASDAQ Golden Dragon China")
    NASDAQ_100_TECHNOLOGY = ("NASDAQ;NDXT", "NASDAQ-100 Technology Sector")
    NASDAQ_INNOVATORS_COMPLETION = ("NASDAQ;NCX", "Nasdaq Innovators Completion Cap")
    NASDAQ_REAL_ESTATE_FINANCIAL = ("NASDAQ;OFIN", "NASDAQ Real Estate and Other Financial Services")
    NASDAQ_FOOD_PRODUCERS = ("NASDAQ;NQUSB451020", "NASDAQ US Benchmark Food Producers")
    NASDAQ_CLEAN_EDGE_GREEN_ENERGY = ("NASDAQ;CELS", "NASDAQ Clean Edge Green Energy")
    NASDAQ_METAVERSE = ("NASDAQ;NYMETA", "NASDAQ CB Insights Metaverse US Index")

    # NASDAQ Cap Indices
    NASDAQ_US_LARGE_CAP_GROWTH = ("NASDAQ;NQUSLG", "Nasdaq US Large Cap Growth")
    NASDAQ_US_MID_CAP_GROWTH = ("NASDAQ;NQUSMG", "Nasdaq US Mid Cap Growth")
    NASDAQ_US_SMALL_CAP_GROWTH = ("NASDAQ;NQUSSG", "Nasdaq US Small Cap Growth")

    # PHLX Indices
    PHLX_SEMICONDUCTOR = ("NASDAQ;SOX", "PHLX Semiconductor Sector")
    PHLX_GOLD_SILVER = ("NASDAQ;XAU", "PHLX Gold/Silver Sector")
    PHLX_HOUSING = ("NASDAQ;HGX", "PHLX Housing Sector")
    PHLX_OIL_SERVICE = ("NASDAQ;OSX", "PHLX Oil Service Sector")
    PHLX_UTILITIES = ("NASDAQ;UTY", "PHLX Utilities Sector")

    # KBW Indices
    KBW_NASDAQ_BANK = ("NASDAQ;BKX", "KBW NASDAQ Bank")
    KBW_FINANCIAL_TECHNOLOGY = ("NASDAQ;KFTX", "KBW NASDAQ Financial Technology Index")

    # Other
    ISE_CLOUD_COMPUTING = ("NASDAQ;CPQ", "ISE CTA Cloud Computing")

    def __init__(self, symbol: str, label: str):
        self.symbol = symbol
        self.label = label

    @property
    def symbolset_value(self) -> str:
        """Returns the value formatted for the symbolset API parameter."""
        return f"SYML:{self.symbol}"

    @classmethod
    def search(cls, query: str) -> list:
        """
        Search indices by name or label.

        :param query: Search query (case-insensitive)
        :return: List of matching IndexSymbol enum members
        """
        query = query.lower()
        return [i for i in cls if query in i.name.lower() or query in i.label.lower()]
