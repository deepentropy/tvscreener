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

    Example:
        >>> condition = StockField.PRICE > 100
        >>> ss.where(condition)
    """

    def __init__(self, field, operation: FilterOperator, value):
        self.field = field
        self.operation = operation
        self.value = value

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
