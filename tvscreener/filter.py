from enum import Enum

from tvscreener.field import Field


class FilterOperator(Enum):
    BELOW = "less"
    BELOW_OR_EQUAL = "eless"
    ABOVE = "greater"
    ABOVE_OR_EQUAL = "egreater"
    CROSSES = "crosses"
    CROSSES_UP = "crosses_above"
    CROSSES_DOWN = "crosses_below"
    IN_RANGE = "in_range"
    NOT_IN_RANGE = "not_in_range"
    EQUAL = "equal"
    NOT_EQUAL = "nequal"
    MATCH = "match"


class ExtraFilter(Enum):
    CURRENT_TRADING_DAY = "active_symbol"
    SEARCH = "name,description"
    PRIMARY = "is_primary"

    def __init__(self, value):
        self.field_name = value


class FieldCondition:
    """
    Represents a comparison condition on a field.

    This class enables Pythonic comparison syntax like:
        StockField.PRICE > 100
        StockField.VOLUME.between(1e6, 10e6)
        StockField.SECTOR == 'Technology'

    Note: Field-to-field comparisons (e.g., StockField.PRICE > StockField.SMA50)
    are NOT supported by the TradingView API. Use scalar values only.

    Example:
        >>> condition = StockField.PRICE > 100
        >>> ss.where(condition)
    """

    def __init__(self, field, operation: FilterOperator, value):
        # Check for field-to-field comparison which is not supported by TradingView API
        self._validate_value(value)
        self.field = field
        self.operation = operation
        self.value = value

    @staticmethod
    def _validate_value(value):
        """Validate that value is not a Field (field-to-field comparisons not supported)."""
        # Import here to avoid circular imports
        from tvscreener.field import Field, FieldWithInterval, FieldWithHistory

        # Check single values
        if isinstance(value, (Field, FieldWithInterval, FieldWithHistory)):
            raise TypeError(
                f"Field-to-field comparisons are not supported by the TradingView API. "
                f"Got: {type(value).__name__}. "
                f"Retrieve the data first and filter using pandas DataFrame operations instead."
            )

        # Check list values (for between, isin, etc.)
        if isinstance(value, list):
            for v in value:
                if isinstance(v, (Field, FieldWithInterval, FieldWithHistory)):
                    raise TypeError(
                        f"Field-to-field comparisons are not supported by the TradingView API. "
                        f"Got: {type(v).__name__}. "
                        f"Retrieve the data first and filter using pandas DataFrame operations instead."
                    )

    def to_filter(self) -> 'Filter':
        """Convert this condition to a Filter object."""
        return Filter(self.field, self.operation, self.value)

    def __repr__(self):
        return f"FieldCondition({self.field.name}, {self.operation.name}, {self.value})"


class Filter:
    def __init__(self, field: Field | ExtraFilter, operation: FilterOperator, values):
        self.field = field
        self.operation = operation
        self.values = values if isinstance(values, list) else [values]

    #    def name(self):
    #        return self.field.field_name if isinstance(self.field, Field) else self.field.value

    def to_dict(self):
        right = [filter_enum.value if isinstance(filter_enum, Enum) else filter_enum for filter_enum in self.values]
        right = right[0] if len(right) == 1 else right
        left = self.field.field_name
        return {"left": left, "operation": self.operation.value, "right": right}
