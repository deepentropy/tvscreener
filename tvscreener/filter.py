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
    HAS = "has"
    HAS_NONE_OF = "has_none_of"
    EMPTY = "empty"
    NOT_EMPTY = "nempty"
    IN_DAY_RANGE = "in_day_range"
    ABOVE_PERCENT = "above%"
    BELOW_PERCENT = "below%"
    IN_RANGE_PERCENT = "in_range%"
    NOT_IN_RANGE_PERCENT = "not_in_range%"


# Operations that take no right-hand value
_NO_VALUE_OPERATIONS = {FilterOperator.EMPTY, FilterOperator.NOT_EMPTY}


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
        StockField.SECTOR == 'Electronic Technology'

    Field-to-field comparisons are also supported:
        StockField.EXPONENTIAL_MOVING_AVERAGE_5 >= StockField.EXPONENTIAL_MOVING_AVERAGE_25

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

    def __and__(self, other) -> 'ConditionGroup':
        return ConditionGroup("and", [self, other])

    def __or__(self, other) -> 'ConditionGroup':
        return ConditionGroup("or", [self, other])

    def __repr__(self):
        return f"FieldCondition({self.field.name}, {self.operation.name}, {self.value})"


class ConditionGroup:
    """
    Conditions combined with AND / OR, sent to TradingView as a ``filter2`` tree.

    Built with the ``&`` and ``|`` operators on conditions. Python evaluates
    ``&`` and ``|`` before comparisons, so each comparison needs parentheses.

    Example:
        >>> group = (StockField.SECTOR == 'Finance') | (StockField.SECTOR == 'Utilities')
        >>> ss.where(group & (StockField.MARKET_CAPITALIZATION > 1e11))
    """

    def __init__(self, operator: str, operands: list):
        if operator not in ("and", "or"):
            raise ValueError(f"operator must be 'and' or 'or', got {operator!r}")
        self.operator = operator
        self.operands = []
        for operand in operands:
            if not isinstance(operand, (FieldCondition, ConditionGroup)):
                raise TypeError(
                    f"Cannot combine {type(operand).__name__} in a condition group; "
                    "use comparisons such as (StockField.PRICE > 10)"
                )
            # (a | b) | c is flattened to a single OR of a, b and c
            if isinstance(operand, ConditionGroup) and operand.operator == operator:
                self.operands.extend(operand.operands)
            else:
                self.operands.append(operand)

    def __and__(self, other) -> 'ConditionGroup':
        return ConditionGroup("and", [self, other])

    def __or__(self, other) -> 'ConditionGroup':
        return ConditionGroup("or", [self, other])

    def conditions(self):
        """Yield every FieldCondition in the group, at any depth."""
        for operand in self.operands:
            if isinstance(operand, ConditionGroup):
                yield from operand.conditions()
            else:
                yield operand

    def to_dict(self, prepare_values=None) -> dict:
        """
        Build the ``filter2`` tree.

        :param prepare_values: Optional callable (field, values) -> values applied to each condition
        """
        operands = []
        for operand in self.operands:
            if isinstance(operand, ConditionGroup):
                operands.append({"operation": operand.to_dict(prepare_values)})
            else:
                value = operand.value
                if prepare_values is not None:
                    value = prepare_values(operand.field, value)
                operands.append({"expression": Filter(operand.field, operand.operation, value).to_dict()})
        return {"operator": self.operator, "operands": operands}

    def __repr__(self):
        return f"ConditionGroup({self.operator}, {self.operands})"


class Filter:
    def __init__(self, field: Field | ExtraFilter, operation: FilterOperator, values):
        self.field = field
        self.operation = operation
        self.values = values if isinstance(values, list) else [values]

    #    def name(self):
    #        return self.field.field_name if isinstance(self.field, Field) else self.field.value

    def to_dict(self):
        left = self.field.field_name
        if self.operation in _NO_VALUE_OPERATIONS:
            return {"left": left, "operation": self.operation.value}
        right = [v.field_name if hasattr(v, 'field_name') else v.value if isinstance(v, Enum) else v for v in self.values]
        right = right[0] if len(right) == 1 else right
        return {"left": left, "operation": self.operation.value, "right": right}
