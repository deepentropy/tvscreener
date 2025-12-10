"""Tests for the new Pythonic comparison operator syntax on Fields."""
import pytest
from tvscreener import StockScreener, StockField, FilterOperator
from tvscreener.filter import FieldCondition


class TestFieldCondition:
    """Test FieldCondition class."""

    def test_greater_than(self):
        """Test > operator."""
        cond = StockField.PRICE > 100
        assert isinstance(cond, FieldCondition)
        assert cond.field == StockField.PRICE
        assert cond.operation == FilterOperator.ABOVE
        assert cond.value == 100

    def test_greater_than_or_equal(self):
        """Test >= operator."""
        cond = StockField.VOLUME >= 1_000_000
        assert isinstance(cond, FieldCondition)
        assert cond.field == StockField.VOLUME
        assert cond.operation == FilterOperator.ABOVE_OR_EQUAL
        assert cond.value == 1_000_000

    def test_less_than(self):
        """Test < operator."""
        cond = StockField.RELATIVE_STRENGTH_INDEX_14 < 30
        assert isinstance(cond, FieldCondition)
        assert cond.field == StockField.RELATIVE_STRENGTH_INDEX_14
        assert cond.operation == FilterOperator.BELOW
        assert cond.value == 30

    def test_less_than_or_equal(self):
        """Test <= operator."""
        cond = StockField.PRICE <= 50
        assert isinstance(cond, FieldCondition)
        assert cond.field == StockField.PRICE
        assert cond.operation == FilterOperator.BELOW_OR_EQUAL
        assert cond.value == 50

    def test_equal(self):
        """Test == operator with value comparison."""
        cond = StockField.SECTOR == 'Technology'
        assert isinstance(cond, FieldCondition)
        assert cond.field == StockField.SECTOR
        assert cond.operation == FilterOperator.EQUAL
        assert cond.value == 'Technology'

    def test_not_equal(self):
        """Test != operator with value comparison."""
        cond = StockField.SECTOR != 'Finance'
        assert isinstance(cond, FieldCondition)
        assert cond.field == StockField.SECTOR
        assert cond.operation == FilterOperator.NOT_EQUAL
        assert cond.value == 'Finance'

    def test_between(self):
        """Test between() method."""
        cond = StockField.MARKET_CAPITALIZATION.between(1e9, 10e9)
        assert isinstance(cond, FieldCondition)
        assert cond.field == StockField.MARKET_CAPITALIZATION
        assert cond.operation == FilterOperator.IN_RANGE
        assert cond.value == [1e9, 10e9]

    def test_not_between(self):
        """Test not_between() method."""
        cond = StockField.PRICE.not_between(50, 100)
        assert isinstance(cond, FieldCondition)
        assert cond.field == StockField.PRICE
        assert cond.operation == FilterOperator.NOT_IN_RANGE
        assert cond.value == [50, 100]

    def test_isin(self):
        """Test isin() method."""
        cond = StockField.SECTOR.isin(['Technology', 'Healthcare'])
        assert isinstance(cond, FieldCondition)
        assert cond.field == StockField.SECTOR
        assert cond.operation == FilterOperator.IN_RANGE
        assert cond.value == ['Technology', 'Healthcare']

    def test_not_in(self):
        """Test not_in() method."""
        cond = StockField.SECTOR.not_in(['Finance', 'Utilities'])
        assert isinstance(cond, FieldCondition)
        assert cond.field == StockField.SECTOR
        assert cond.operation == FilterOperator.NOT_IN_RANGE
        assert cond.value == ['Finance', 'Utilities']

    def test_enum_equality_preserved(self):
        """Test that enum-to-enum equality still works."""
        assert StockField.PRICE == StockField.PRICE
        assert StockField.PRICE != StockField.VOLUME

    def test_to_filter(self):
        """Test to_filter() method."""
        cond = StockField.PRICE > 100
        filter_ = cond.to_filter()
        assert filter_.field == StockField.PRICE
        assert filter_.operation == FilterOperator.ABOVE
        assert filter_.values == [100]

    def test_repr(self):
        """Test string representation."""
        cond = StockField.PRICE > 100
        assert 'PRICE' in repr(cond)
        assert 'ABOVE' in repr(cond)
        assert '100' in repr(cond)


class TestFieldWithIntervalConditions:
    """Test comparison operators on FieldWithInterval."""

    def test_greater_than(self):
        """Test > operator on FieldWithInterval."""
        rsi_1h = StockField.RELATIVE_STRENGTH_INDEX_14.with_interval('60')
        cond = rsi_1h > 70
        assert isinstance(cond, FieldCondition)
        assert cond.operation == FilterOperator.ABOVE
        assert cond.value == 70
        assert cond.field.field_name == 'RSI|60'

    def test_between(self):
        """Test between() on FieldWithInterval."""
        rsi_1h = StockField.RELATIVE_STRENGTH_INDEX_14.with_interval('60')
        cond = rsi_1h.between(30, 70)
        assert isinstance(cond, FieldCondition)
        assert cond.operation == FilterOperator.IN_RANGE
        assert cond.value == [30, 70]


class TestFieldWithHistoryConditions:
    """Test comparison operators on FieldWithHistory."""

    def test_greater_than(self):
        """Test > operator on FieldWithHistory."""
        # Use a field that supports historical lookback
        prev_rsi = StockField.RELATIVE_STRENGTH_INDEX_14.with_history(1)
        cond = prev_rsi > 70
        assert isinstance(cond, FieldCondition)
        assert cond.operation == FilterOperator.ABOVE
        assert cond.value == 70


class TestScreenerWhereMethod:
    """Test Screener.where() with new syntax."""

    def test_where_with_condition(self):
        """Test where() with FieldCondition."""
        ss = StockScreener()
        ss.where(StockField.PRICE > 100)

        assert len(ss.filters) == 1
        filter_dict = ss.filters[0].to_dict()
        assert filter_dict['left'] == 'close'
        assert filter_dict['operation'] == 'greater'
        assert filter_dict['right'] == 100

    def test_where_with_legacy_syntax(self):
        """Test where() with legacy (field, operator, value) syntax."""
        ss = StockScreener()
        ss.where(StockField.PRICE, FilterOperator.ABOVE, 100)

        assert len(ss.filters) == 1
        filter_dict = ss.filters[0].to_dict()
        assert filter_dict['left'] == 'close'
        assert filter_dict['operation'] == 'greater'
        assert filter_dict['right'] == 100

    def test_where_chaining(self):
        """Test method chaining with where()."""
        ss = StockScreener()
        result = ss.where(StockField.PRICE > 100).where(StockField.VOLUME > 1e6)

        assert result is ss  # Returns self for chaining
        assert len(ss.filters) == 2

    def test_where_mixed_syntax(self):
        """Test mixing new and legacy syntax."""
        ss = StockScreener()
        ss.where(StockField.PRICE > 100)  # New syntax
        ss.where(StockField.VOLUME, FilterOperator.ABOVE, 1e6)  # Legacy syntax

        assert len(ss.filters) == 2

    def test_where_with_between(self):
        """Test where() with between() condition."""
        ss = StockScreener()
        ss.where(StockField.MARKET_CAPITALIZATION.between(1e9, 10e9))

        assert len(ss.filters) == 1
        filter_dict = ss.filters[0].to_dict()
        assert filter_dict['operation'] == 'in_range'
        assert filter_dict['right'] == [1e9, 10e9]

    def test_where_with_interval_field(self):
        """Test where() with FieldWithInterval."""
        ss = StockScreener()
        rsi_1h = StockField.RELATIVE_STRENGTH_INDEX_14.with_interval('60')
        ss.where(rsi_1h > 70)

        assert len(ss.filters) == 1
        filter_dict = ss.filters[0].to_dict()
        assert filter_dict['left'] == 'RSI|60'
        assert filter_dict['operation'] == 'greater'
        assert filter_dict['right'] == 70
