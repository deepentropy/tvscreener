from tvscreener import ETFScreener, StockScreener, StockField


def test_universe_and_sort():
    es = ETFScreener()
    payload = es._build_payload(["name"])
    assert payload["filter2"] == {"operator": "or", "operands": [
        {"expression": {"left": "typespecs", "operation": "has", "right": "etf"}},
        {"expression": {"left": "type", "operation": "equal", "right": "structured"}},
    ]}
    assert payload["sort"] == {"sortBy": "aum", "sortOrder": "desc"}
    assert payload["markets"] == ["america"]


def test_user_groups_are_anded_with_universe():
    es = ETFScreener()
    es.where((StockField.ISSUER == 'BlackRock, Inc.') | (StockField.ISSUER == 'The Vanguard Group, Inc.'))
    filter2 = es._build_payload(["name"])["filter2"]
    assert filter2["operator"] == "and"
    assert len(filter2["operands"]) == 2


def test_instances_do_not_share_filters():
    first = ETFScreener()
    first.where((StockField.AUM > 1) | (StockField.AUM < 0))
    assert len(ETFScreener().filter_groups) == 1


def test_etf_name_fields_use_translated_columns():
    assert StockField.ASSET_CLASS_NAME.field_name == "asset_class.tr"
    assert StockField.INDEX_TRACKED.field_name == "index_tracked"


def test_is_a_stock_screener():
    assert isinstance(ETFScreener(), StockScreener)
