"""Tests for OR / nested filter groups (#62), the new filter operations (#63) and history flags (#65)."""
import datetime as dt

import pytest

from tvscreener import (
    StockScreener, StockField, CryptoField, OptionScreener, OptionField,
    FilterOperator, FieldCondition, ConditionGroup,
)
from tvscreener.mcp.tools import build_condition


def _payload(screener):
    return screener._build_payload(["name"])


class TestNewOperations:

    def test_has_single_and_list(self):
        assert StockField.TYPESPECS.has('etf').to_filter().to_dict() == \
            {"left": "typespecs", "operation": "has", "right": "etf"}
        assert StockField.TYPESPECS.has(['etf', 'preferred']).to_filter().to_dict() == \
            {"left": "typespecs", "operation": "has", "right": ['etf', 'preferred']}

    def test_has_none_of(self):
        assert StockField.TYPESPECS.has_none_of(['preferred']).to_filter().to_dict() == \
            {"left": "typespecs", "operation": "has_none_of", "right": "preferred"}

    def test_empty_operations_have_no_right(self):
        assert StockField.DIVIDENDS_YIELD.is_empty().to_filter().to_dict() == \
            {"left": "dividends_yield", "operation": "empty"}
        assert StockField.DIVIDENDS_YIELD.not_empty().to_filter().to_dict() == \
            {"left": "dividends_yield", "operation": "nempty"}

    def test_in_day_range(self):
        assert StockField.UPCOMING_EARNINGS_DATE.in_day_range(0, 7).to_filter().to_dict() == \
            {"left": "earnings_release_next_date", "operation": "in_day_range", "right": [0, 7]}

    def test_above_pct_with_field(self):
        cond = StockField.PRICE.above_pct(StockField.SIMPLE_MOVING_AVERAGE_50, 5)
        assert cond.operation == FilterOperator.ABOVE_PERCENT
        assert cond.to_filter().to_dict() == {"left": "close", "operation": "above%", "right": ["SMA50", 1.05]}

    def test_below_pct_with_number(self):
        cond = StockField.PRICE.below_pct(100, 10)
        assert cond.to_filter().to_dict() == {"left": "close", "operation": "below%", "right": [100, 0.9]}

    def test_within_and_not_within_pct(self):
        assert StockField.PRICE.within_pct(StockField.ALL_TIME_HIGH, -5, 0).to_filter().to_dict() == \
            {"left": "close", "operation": "in_range%", "right": ["High.All", 0.95, 1.0]}
        assert StockField.PRICE.not_within_pct(StockField.SIMPLE_MOVING_AVERAGE_200, -10, 10).to_filter().to_dict() == \
            {"left": "close", "operation": "not_in_range%", "right": ["SMA200", 0.9, 1.1]}

    def test_helpers_on_interval_and_history_fields(self):
        rsi_1h = StockField.RELATIVE_STRENGTH_INDEX_14.with_interval('60')
        assert rsi_1h.not_empty().to_filter().to_dict() == {"left": "RSI|60", "operation": "nempty"}
        prev_rsi = StockField.RELATIVE_STRENGTH_INDEX_14.with_history(1)
        assert prev_rsi.above_pct(StockField.RELATIVE_STRENGTH_INDEX_14, 2).to_filter().to_dict() == \
            {"left": "RSI[1]", "operation": "above%", "right": ["RSI", 1.02]}

    def test_new_operations_are_not_merged(self):
        ss = StockScreener()
        ss.where(StockField.PRICE > 10)
        ss.where(StockField.PRICE.above_pct(StockField.SIMPLE_MOVING_AVERAGE_50, 5))
        filters = _payload(ss)["filter"]
        assert {"left": "close", "operation": "greater", "right": 10} in filters
        assert {"left": "close", "operation": "above%", "right": ["SMA50", 1.05]} in filters

    def test_legacy_merge_unchanged(self):
        ss = StockScreener()
        ss.where(StockField.PRICE > 10)
        ss.where(StockField.PRICE < 100)
        assert _payload(ss)["filter"] == [{"left": "close", "operation": "in_range", "right": [10, 100]}]


class TestConditionGroup:

    def test_or_builds_group(self):
        group = (StockField.SECTOR == 'Finance') | (StockField.SECTOR == 'Utilities')
        assert isinstance(group, ConditionGroup)
        assert group.to_dict() == {"operator": "or", "operands": [
            {"expression": {"left": "sector", "operation": "equal", "right": "Finance"}},
            {"expression": {"left": "sector", "operation": "equal", "right": "Utilities"}},
        ]}

    def test_same_operator_is_flattened(self):
        group = (StockField.PRICE > 1) | (StockField.PRICE > 2) | (StockField.PRICE > 3)
        assert len(group.operands) == 3

    def test_nested_groups(self):
        rsi = StockField.RELATIVE_STRENGTH_INDEX_14
        group = (StockField.MARKET_CAPITALIZATION > 1e10) & ((rsi < 30) | (rsi > 70))
        assert group.to_dict() == {"operator": "and", "operands": [
            {"expression": {"left": "market_cap_basic", "operation": "greater", "right": 1e10}},
            {"operation": {"operator": "or", "operands": [
                {"expression": {"left": "RSI", "operation": "less", "right": 30}},
                {"expression": {"left": "RSI", "operation": "greater", "right": 70}},
            ]}},
        ]}

    def test_conditions_iterates_all_depths(self):
        group = (StockField.PRICE > 1) & ((StockField.VOLUME > 2) | (StockField.CHANGE_PERCENT > 3))
        assert [c.field for c in group.conditions()] == [StockField.PRICE, StockField.VOLUME, StockField.CHANGE_PERCENT]

    def test_rejects_non_conditions(self):
        with pytest.raises(TypeError):
            (StockField.PRICE > 1) | 5
        with pytest.raises(ValueError):
            ConditionGroup("xor", [StockField.PRICE > 1])

    def test_where_puts_group_in_filter2(self):
        ss = StockScreener()
        ss.where(StockField.MARKET_CAPITALIZATION > 1e11)
        ss.where((StockField.SECTOR == 'Finance') | (StockField.SECTOR == 'Utilities'))
        payload = _payload(ss)
        assert payload["filter"] == [{"left": "market_cap_basic", "operation": "greater", "right": 1e11}]
        assert payload["filter2"]["operator"] == "or"
        assert len(payload["filter2"]["operands"]) == 2

    def test_several_groups_are_anded(self):
        ss = StockScreener()
        ss.where((StockField.PRICE > 1) | (StockField.PRICE < 0))
        ss.where((StockField.VOLUME > 1) | (StockField.VOLUME < 0))
        filter2 = _payload(ss)["filter2"]
        assert filter2["operator"] == "and"
        assert [o["operation"]["operator"] for o in filter2["operands"]] == ["or", "or"]

    def test_no_filter2_without_groups(self):
        ss = StockScreener()
        ss.where(StockField.PRICE > 1)
        assert "filter2" not in _payload(ss)

    def test_group_field_type_validated(self):
        ss = StockScreener()
        with pytest.raises(TypeError):
            ss.where((StockField.PRICE > 1) | (CryptoField.VOLUME > 1))

    def test_option_expiration_dates_converted_in_groups(self):
        os_ = OptionScreener("NASDAQ:AAPL")
        os_.where((OptionField.EXPIRATION == dt.date(2026, 11, 20)) | (OptionField.EXPIRATION == "2026-12-18"))
        rights = [o["expression"]["right"] for o in _payload(os_)["filter2"]["operands"]]
        assert rights == [20261120, 20261218]


class TestMcpBuildCondition:

    def test_leaf(self):
        cond = build_condition({"field": "PRICE", "op": ">", "value": 10})
        assert isinstance(cond, FieldCondition)
        assert cond.to_filter().to_dict() == {"left": "close", "operation": "greater", "right": 10}

    def test_or_group(self):
        cond = build_condition({"or": [
            {"field": "SECTOR", "op": "==", "value": "Finance"},
            {"field": "SECTOR", "op": "==", "value": "Utilities"},
        ]})
        assert isinstance(cond, ConditionGroup)
        assert cond.operator == "or"

    def test_pct_op_resolves_field_name(self):
        cond = build_condition({"field": "PRICE", "op": "above_pct", "value": ["SIMPLE_MOVING_AVERAGE_50", 5]})
        assert cond.to_filter().to_dict() == {"left": "close", "operation": "above%", "right": ["SMA50", 1.05]}

    def test_new_operators(self):
        assert build_condition({"field": "TYPESPECS", "op": "has", "value": ["etf"]}).operation == FilterOperator.HAS
        assert build_condition({"field": "DIVIDENDS_YIELD", "op": "not_empty"}).to_filter().to_dict() == \
            {"left": "dividends_yield", "operation": "nempty"}

    def test_unknown_parts_skipped(self):
        assert build_condition({"field": "NOT_A_FIELD", "op": ">", "value": 1}) is None
        assert build_condition({"field": "PRICE", "op": "bogus", "value": 1}) is None
        cond = build_condition({"or": [{"field": "NOT_A_FIELD", "op": ">", "value": 1},
                                       {"field": "PRICE", "op": ">", "value": 1}]})
        assert isinstance(cond, FieldCondition)


class TestHistoryFlags:

    @pytest.mark.parametrize("field", [
        StockField.RSI2, StockField.RSI30, StockField.MOM_14, StockField.ADX_PLUS_DI_50,
        StockField.STOCH_K_5_3_3, StockField.STOCH_D_14_1_3,
    ])
    def test_with_history_accepted(self, field):
        assert field.with_history(1).field_name == f"{field.field_name}[1]"
