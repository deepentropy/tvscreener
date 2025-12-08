# ForexField Reference

Fields available for forex/currency pair screening. Includes price data and technical indicators.

**Total Fields:** 2965

## Table of Contents

- [Metadata](#metadata) (20 fields)
- [Price Data](#price-data) (175 fields)
- [Volume](#volume) (81 fields)
- [Performance](#performance) (30 fields)
- [Moving Averages](#moving-averages) (715 fields)
- [Oscillators](#oscillators) (670 fields)
- [Trend Indicators](#trend-indicators) (400 fields)
- [Volatility Indicators](#volatility-indicators) (143 fields)
- [Pivot Points](#pivot-points) (210 fields)
- [Candlestick Patterns](#candlestick-patterns) (271 fields)
- [Recommendations](#recommendations) (40 fields)
- [Dividends & Yield](#dividends--yield) (2 fields)
- [Earnings & Income](#earnings--income) (2 fields)
- [Bond Data](#bond-data) (3 fields)
- [Crypto Data](#crypto-data) (2 fields)
- [DEX Data](#dex-data) (2 fields)
- [Time & Dates](#time--dates) (35 fields)
- [Other](#other) (164 fields)

---

## Metadata

*20 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `ACTIVE_SYMBOL` | Active Symbol | `active_symbol` | float |
| `BASE_CURRENCY_KIND` | Base Currency Kind | `base_currency_kind` | text |
| `COUNTRY2` | Country2 | `country2` | text |
| `COUNTRY_CODE` | Country Code | `country_code` | text |
| `CURRENCY` | Currency | `currency` | text |
| `CURRENCY_ID` | Currency Id | `currency_id` | text |
| `CURRENCY_KIND` | Currency Kind | `currency_kind` | text |
| `DESCRIPTION` | Description | `description` | text |
| `EXCHANGE` | Exchange | `exchange` | percent |
| `FUNDAMENTAL_CURRENCY_CODE` | Fundamental Currency Code | `fundamental_currency_code` | text |
| `GROUP` | Group | `sector` | text |
| `IS_SYMBOL_PRIMARY_LISTING` | Is Symbol Primary Listing | `is_symbol_primary_listing` | float |
| `LOGOID` | Logoid | `logoid` | text |
| `NAME` | Name | `name` | text |
| `REGION` | Region | `country` | text |
| `SOURCE_MINUS_LOGOID` | Source-Logoid | `source-logoid` | text |
| `SUBTYPE` | Subtype | `subtype` | text |
| `SYMBOL` | Symbol | `symbol` | float |
| `TYPE` | Type | `type` | text |
| `TYPESPECS` | Typespecs | `typespecs` | text |

## Price Data

*175 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `ALL_TIME_HIGH` | All Time High | `High.All` | float |
| `ALL_TIME_HIGH_2` | All Time High | `all_time_high` | date |
| `ALL_TIME_HIGH_DAY` | All Time High Day | `all_time_high_day` | date |
| `ALL_TIME_LOW` | All Time Low | `Low.All` | float |
| `ALL_TIME_LOW_2` | All Time Low | `all_time_low` | date |
| `ALL_TIME_LOW_DAY` | All Time Low Day | `all_time_low_day` | date |
| `ALL_TIME_OPEN` | All Time Open | `all_time_open` | date |
| `ASK` | Ask | `ask` | float |
| `BID` | Bid | `bid` | float |
| `BID_ASK_SPREAD_PCT` | Bid Ask Spread Pct | `bid_ask_spread_pct` | percent |
| `CHAIKINMONEYFLOW` | Chaikinmoneyflow | `ChaikinMoneyFlow` | float |
| `CHAIKINMONEYFLOW_1` | Chaikinmoneyflow\|1 | `ChaikinMoneyFlow\|1` | float |
| `CHAIKINMONEYFLOW_120` | Chaikinmoneyflow\|120 | `ChaikinMoneyFlow\|120` | float |
| `CHAIKINMONEYFLOW_15` | Chaikinmoneyflow\|15 | `ChaikinMoneyFlow\|15` | float |
| `CHAIKINMONEYFLOW_1M` | Chaikinmoneyflow\|1M | `ChaikinMoneyFlow\|1M` | float |
| `CHAIKINMONEYFLOW_1W` | Chaikinmoneyflow\|1W | `ChaikinMoneyFlow\|1W` | float |
| `CHAIKINMONEYFLOW_240` | Chaikinmoneyflow\|240 | `ChaikinMoneyFlow\|240` | float |
| `CHAIKINMONEYFLOW_30` | Chaikinmoneyflow\|30 | `ChaikinMoneyFlow\|30` | float |
| `CHAIKINMONEYFLOW_5` | Chaikinmoneyflow\|5 | `ChaikinMoneyFlow\|5` | float |
| `CHAIKINMONEYFLOW_60` | Chaikinmoneyflow\|60 | `ChaikinMoneyFlow\|60` | float |
| `CHANGE_FROM_OPEN` | Change from Open | `change_from_open_abs` | float |
| `CHANGE_FROM_OPEN_1` | Change From Open\|1 | `change_from_open\|1` | percent |
| `CHANGE_FROM_OPEN_120` | Change From Open\|120 | `change_from_open\|120` | percent |
| `CHANGE_FROM_OPEN_15` | Change From Open\|15 | `change_from_open\|15` | percent |
| `CHANGE_FROM_OPEN_1M` | Change From Open\|1M | `change_from_open\|1M` | percent |
| `CHANGE_FROM_OPEN_1W` | Change From Open\|1W | `change_from_open\|1W` | percent |
| `CHANGE_FROM_OPEN_240` | Change From Open\|240 | `change_from_open\|240` | percent |
| `CHANGE_FROM_OPEN_30` | Change From Open\|30 | `change_from_open\|30` | percent |
| `CHANGE_FROM_OPEN_5` | Change From Open\|5 | `change_from_open\|5` | percent |
| `CHANGE_FROM_OPEN_60` | Change From Open\|60 | `change_from_open\|60` | percent |
| `CHANGE_FROM_OPEN_ABS_1` | Change From Open Abs\|1 | `change_from_open_abs\|1` | percent |
| `CHANGE_FROM_OPEN_ABS_120` | Change From Open Abs\|120 | `change_from_open_abs\|120` | percent |
| `CHANGE_FROM_OPEN_ABS_15` | Change From Open Abs\|15 | `change_from_open_abs\|15` | percent |
| `CHANGE_FROM_OPEN_ABS_1M` | Change From Open Abs\|1M | `change_from_open_abs\|1M` | percent |
| `CHANGE_FROM_OPEN_ABS_1W` | Change From Open Abs\|1W | `change_from_open_abs\|1W` | percent |
| `CHANGE_FROM_OPEN_ABS_240` | Change From Open Abs\|240 | `change_from_open_abs\|240` | percent |
| `CHANGE_FROM_OPEN_ABS_30` | Change From Open Abs\|30 | `change_from_open_abs\|30` | percent |
| `CHANGE_FROM_OPEN_ABS_5` | Change From Open Abs\|5 | `change_from_open_abs\|5` | percent |
| `CHANGE_FROM_OPEN_ABS_60` | Change From Open Abs\|60 | `change_from_open_abs\|60` | percent |
| `CHANGE_FROM_OPEN_PERCENT` | Change from Open % | `change_from_open` | percent |
| `CLOSE_1` | Close\|1 | `close\|1` | float |
| `CLOSE_120` | Close\|120 | `close\|120` | float |
| `CLOSE_15` | Close\|15 | `close\|15` | float |
| `CLOSE_1M` | Close\|1M | `close\|1M` | float |
| `CLOSE_1W` | Close\|1W | `close\|1W` | float |
| `CLOSE_240` | Close\|240 | `close\|240` | float |
| `CLOSE_30` | Close\|30 | `close\|30` | float |
| `CLOSE_5` | Close\|5 | `close\|5` | float |
| `CLOSE_60` | Close\|60 | `close\|60` | float |
| `FUND_FLOWS_1M` | Fund Flows 1M | `fund_flows.1M` | float |
| `FUND_FLOWS_1Y` | Fund Flows 1Y | `fund_flows.1Y` | float |
| `FUND_FLOWS_3M` | Fund Flows 3M | `fund_flows.3M` | float |
| `FUND_FLOWS_3Y` | Fund Flows 3Y | `fund_flows.3Y` | float |
| `FUND_FLOWS_5Y` | Fund Flows 5Y | `fund_flows.5Y` | float |
| `FUND_FLOWS_YTD` | Fund Flows YTD | `fund_flows.YTD` | float |
| `GAP_1` | Gap\|1 | `gap\|1` | float |
| `GAP_120` | Gap\|120 | `gap\|120` | float |
| `GAP_15` | Gap\|15 | `gap\|15` | float |
| `GAP_1M` | Gap\|1M | `gap\|1M` | float |
| `GAP_1W` | Gap\|1W | `gap\|1W` | float |
| `GAP_240` | Gap\|240 | `gap\|240` | float |
| `GAP_30` | Gap\|30 | `gap\|30` | float |
| `GAP_5` | Gap\|5 | `gap\|5` | float |
| `GAP_60` | Gap\|60 | `gap\|60` | float |
| `GAP_DOWN` | Gap Down | `gap_down` | float |
| `GAP_DOWN_1` | Gap Down\|1 | `gap_down\|1` | float |
| `GAP_DOWN_120` | Gap Down\|120 | `gap_down\|120` | float |
| `GAP_DOWN_15` | Gap Down\|15 | `gap_down\|15` | float |
| `GAP_DOWN_1M` | Gap Down\|1M | `gap_down\|1M` | float |
| `GAP_DOWN_1W` | Gap Down\|1W | `gap_down\|1W` | float |
| `GAP_DOWN_240` | Gap Down\|240 | `gap_down\|240` | float |
| `GAP_DOWN_30` | Gap Down\|30 | `gap_down\|30` | float |
| `GAP_DOWN_5` | Gap Down\|5 | `gap_down\|5` | float |
| `GAP_DOWN_60` | Gap Down\|60 | `gap_down\|60` | float |
| `GAP_DOWN_ABS` | Gap Down Abs | `gap_down_abs` | float |
| `GAP_DOWN_ABS_1` | Gap Down Abs\|1 | `gap_down_abs\|1` | float |
| `GAP_DOWN_ABS_120` | Gap Down Abs\|120 | `gap_down_abs\|120` | float |
| `GAP_DOWN_ABS_15` | Gap Down Abs\|15 | `gap_down_abs\|15` | float |
| `GAP_DOWN_ABS_1M` | Gap Down Abs\|1M | `gap_down_abs\|1M` | float |
| `GAP_DOWN_ABS_1W` | Gap Down Abs\|1W | `gap_down_abs\|1W` | float |
| `GAP_DOWN_ABS_240` | Gap Down Abs\|240 | `gap_down_abs\|240` | float |
| `GAP_DOWN_ABS_30` | Gap Down Abs\|30 | `gap_down_abs\|30` | float |
| `GAP_DOWN_ABS_5` | Gap Down Abs\|5 | `gap_down_abs\|5` | float |
| `GAP_DOWN_ABS_60` | Gap Down Abs\|60 | `gap_down_abs\|60` | float |
| `GAP_PERCENT` | Gap % | `gap` | percent |
| `GAP_UP` | Gap Up | `gap_up` | float |
| `GAP_UP_1` | Gap Up\|1 | `gap_up\|1` | float |
| `GAP_UP_120` | Gap Up\|120 | `gap_up\|120` | float |
| `GAP_UP_15` | Gap Up\|15 | `gap_up\|15` | float |
| `GAP_UP_1M` | Gap Up\|1M | `gap_up\|1M` | float |
| `GAP_UP_1W` | Gap Up\|1W | `gap_up\|1W` | float |
| `GAP_UP_240` | Gap Up\|240 | `gap_up\|240` | float |
| `GAP_UP_30` | Gap Up\|30 | `gap_up\|30` | float |
| `GAP_UP_5` | Gap Up\|5 | `gap_up\|5` | float |
| `GAP_UP_60` | Gap Up\|60 | `gap_up\|60` | float |
| `GAP_UP_ABS` | Gap Up Abs | `gap_up_abs` | float |
| `GAP_UP_ABS_1` | Gap Up Abs\|1 | `gap_up_abs\|1` | float |
| `GAP_UP_ABS_120` | Gap Up Abs\|120 | `gap_up_abs\|120` | float |
| `GAP_UP_ABS_15` | Gap Up Abs\|15 | `gap_up_abs\|15` | float |
| `GAP_UP_ABS_1M` | Gap Up Abs\|1M | `gap_up_abs\|1M` | float |
| `GAP_UP_ABS_1W` | Gap Up Abs\|1W | `gap_up_abs\|1W` | float |
| `GAP_UP_ABS_240` | Gap Up Abs\|240 | `gap_up_abs\|240` | float |
| `GAP_UP_ABS_30` | Gap Up Abs\|30 | `gap_up_abs\|30` | float |
| `GAP_UP_ABS_5` | Gap Up Abs\|5 | `gap_up_abs\|5` | float |
| `GAP_UP_ABS_60` | Gap Up Abs\|60 | `gap_up_abs\|60` | float |
| `HIGH` | High | `high` | float |
| `HIGH_1` | High\|1 | `high\|1` | float |
| `HIGH_120` | High\|120 | `high\|120` | float |
| `HIGH_15` | High\|15 | `high\|15` | float |
| `HIGH_1M` | High\|1M | `high\|1M` | float |
| `HIGH_1M_DATE` | High 1M Date | `High.1M.Date` | date |
| `HIGH_1W` | High\|1W | `high\|1W` | float |
| `HIGH_240` | High\|240 | `high\|240` | float |
| `HIGH_30` | High\|30 | `high\|30` | float |
| `HIGH_3M_DATE` | High 3M Date | `High.3M.Date` | date |
| `HIGH_5` | High\|5 | `high\|5` | float |
| `HIGH_5D` | High 5D | `High.5D` | float |
| `HIGH_60` | High\|60 | `high\|60` | float |
| `HIGH_6M_DATE` | High 6M Date | `High.6M.Date` | date |
| `HIGH_ALL_CALC` | High All Calc | `High.All.Calc` | float |
| `HIGH_ALL_CALC_DATE` | High All Calc Date | `High.All.Calc.Date` | date |
| `HIGH_ALL_DATE` | High All Date | `High.All.Date` | date |
| `LOW` | Low | `low` | float |
| `LOW_1` | Low\|1 | `low\|1` | float |
| `LOW_120` | Low\|120 | `low\|120` | float |
| `LOW_15` | Low\|15 | `low\|15` | float |
| `LOW_1M` | Low\|1M | `low\|1M` | float |
| `LOW_1M_DATE` | Low 1M Date | `Low.1M.Date` | date |
| `LOW_1W` | Low\|1W | `low\|1W` | float |
| `LOW_240` | Low\|240 | `low\|240` | float |
| `LOW_30` | Low\|30 | `low\|30` | float |
| `LOW_3M_DATE` | Low 3M Date | `Low.3M.Date` | date |
| `LOW_5` | Low\|5 | `low\|5` | float |
| `LOW_5D` | Low 5D | `Low.5D` | float |
| `LOW_60` | Low\|60 | `low\|60` | float |
| `LOW_6M_DATE` | Low 6M Date | `Low.6M.Date` | date |
| `LOW_AFTER_HIGH_ALL` | Low After High All | `Low.After.High.All` | float |
| `LOW_AFTER_HIGH_ALL_CHANGE` | Low After High All Change | `low_after_high_all_change` | percent |
| `LOW_AFTER_HIGH_ALL_CHANGE_ABS` | Low After High All Change Abs | `low_after_high_all_change_abs` | percent |
| `LOW_ALL_CALC` | Low All Calc | `Low.All.Calc` | float |
| `LOW_ALL_CALC_DATE` | Low All Calc Date | `Low.All.Calc.Date` | date |
| `LOW_ALL_DATE` | Low All Date | `Low.All.Date` | date |
| `MONEYFLOW` | Moneyflow | `MoneyFlow` | float |
| `MONEYFLOW_1` | Moneyflow\|1 | `MoneyFlow\|1` | float |
| `MONEYFLOW_120` | Moneyflow\|120 | `MoneyFlow\|120` | float |
| `MONEYFLOW_15` | Moneyflow\|15 | `MoneyFlow\|15` | float |
| `MONEYFLOW_1M` | Moneyflow\|1M | `MoneyFlow\|1M` | float |
| `MONEYFLOW_1W` | Moneyflow\|1W | `MoneyFlow\|1W` | float |
| `MONEYFLOW_240` | Moneyflow\|240 | `MoneyFlow\|240` | float |
| `MONEYFLOW_30` | Moneyflow\|30 | `MoneyFlow\|30` | float |
| `MONEYFLOW_5` | Moneyflow\|5 | `MoneyFlow\|5` | float |
| `MONEYFLOW_60` | Moneyflow\|60 | `MoneyFlow\|60` | float |
| `MONTH_HIGH_1` | 1-Month High | `High.1M` | float |
| `MONTH_HIGH_3` | 3-Month High | `High.3M` | float |
| `MONTH_HIGH_6` | 6-Month High | `High.6M` | float |
| `MONTH_LOW_1` | 1-Month Low | `Low.1M` | float |
| `MONTH_LOW_3` | 3-Month Low | `Low.3M` | float |
| `MONTH_LOW_6` | 6-Month Low | `Low.6M` | float |
| `OPEN` | Open | `open` | float |
| `OPEN_1` | Open\|1 | `open\|1` | float |
| `OPEN_120` | Open\|120 | `open\|120` | float |
| `OPEN_15` | Open\|15 | `open\|15` | float |
| `OPEN_1M` | Open\|1M | `open\|1M` | float |
| `OPEN_1W` | Open\|1W | `open\|1W` | float |
| `OPEN_240` | Open\|240 | `open\|240` | float |
| `OPEN_30` | Open\|30 | `open\|30` | float |
| `OPEN_5` | Open\|5 | `open\|5` | float |
| `OPEN_60` | Open\|60 | `open\|60` | float |
| `OPEN_ALL_CALC` | Open All Calc | `Open.All.Calc` | float |
| `PRICE` | Price | `close` | float |
| `PRICESCALE` | Pricescale | `pricescale` | float |
| `PRICE_52_WEEK_HIGH_DATE` | Price 52 Week High Date | `price_52_week_high_date` | date |
| `PRICE_52_WEEK_LOW_DATE` | Price 52 Week Low Date | `price_52_week_low_date` | date |
| `WEEK_HIGH_52` | 52 Week High | `price_52_week_high` | float |
| `WEEK_LOW_52` | 52 Week Low | `price_52_week_low` | float |

## Volume

*81 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `AVERAGE_VOLUME_10D_CALC` | Average Volume 10D Calc | `average_volume_10d_calc` | number_group |
| `AVERAGE_VOLUME_10D_CALC_1` | Average Volume 10D Calc\|1 | `average_volume_10d_calc\|1` | number_group |
| `AVERAGE_VOLUME_10D_CALC_120` | Average Volume 10D Calc\|120 | `average_volume_10d_calc\|120` | number_group |
| `AVERAGE_VOLUME_10D_CALC_15` | Average Volume 10D Calc\|15 | `average_volume_10d_calc\|15` | number_group |
| `AVERAGE_VOLUME_10D_CALC_1M` | Average Volume 10D Calc\|1M | `average_volume_10d_calc\|1M` | number_group |
| `AVERAGE_VOLUME_10D_CALC_1W` | Average Volume 10D Calc\|1W | `average_volume_10d_calc\|1W` | number_group |
| `AVERAGE_VOLUME_10D_CALC_240` | Average Volume 10D Calc\|240 | `average_volume_10d_calc\|240` | number_group |
| `AVERAGE_VOLUME_10D_CALC_30` | Average Volume 10D Calc\|30 | `average_volume_10d_calc\|30` | number_group |
| `AVERAGE_VOLUME_10D_CALC_5` | Average Volume 10D Calc\|5 | `average_volume_10d_calc\|5` | number_group |
| `AVERAGE_VOLUME_10D_CALC_60` | Average Volume 10D Calc\|60 | `average_volume_10d_calc\|60` | number_group |
| `AVERAGE_VOLUME_30D_CALC` | Average Volume 30D Calc | `average_volume_30d_calc` | number_group |
| `AVERAGE_VOLUME_30D_CALC_1` | Average Volume 30D Calc\|1 | `average_volume_30d_calc\|1` | number_group |
| `AVERAGE_VOLUME_30D_CALC_120` | Average Volume 30D Calc\|120 | `average_volume_30d_calc\|120` | number_group |
| `AVERAGE_VOLUME_30D_CALC_15` | Average Volume 30D Calc\|15 | `average_volume_30d_calc\|15` | number_group |
| `AVERAGE_VOLUME_30D_CALC_1M` | Average Volume 30D Calc\|1M | `average_volume_30d_calc\|1M` | number_group |
| `AVERAGE_VOLUME_30D_CALC_1W` | Average Volume 30D Calc\|1W | `average_volume_30d_calc\|1W` | number_group |
| `AVERAGE_VOLUME_30D_CALC_240` | Average Volume 30D Calc\|240 | `average_volume_30d_calc\|240` | number_group |
| `AVERAGE_VOLUME_30D_CALC_30` | Average Volume 30D Calc\|30 | `average_volume_30d_calc\|30` | number_group |
| `AVERAGE_VOLUME_30D_CALC_5` | Average Volume 30D Calc\|5 | `average_volume_30d_calc\|5` | number_group |
| `AVERAGE_VOLUME_30D_CALC_60` | Average Volume 30D Calc\|60 | `average_volume_30d_calc\|60` | number_group |
| `AVERAGE_VOLUME_60D_CALC` | Average Volume 60D Calc | `average_volume_60d_calc` | number_group |
| `AVERAGE_VOLUME_60D_CALC_1` | Average Volume 60D Calc\|1 | `average_volume_60d_calc\|1` | number_group |
| `AVERAGE_VOLUME_60D_CALC_120` | Average Volume 60D Calc\|120 | `average_volume_60d_calc\|120` | number_group |
| `AVERAGE_VOLUME_60D_CALC_15` | Average Volume 60D Calc\|15 | `average_volume_60d_calc\|15` | number_group |
| `AVERAGE_VOLUME_60D_CALC_1M` | Average Volume 60D Calc\|1M | `average_volume_60d_calc\|1M` | number_group |
| `AVERAGE_VOLUME_60D_CALC_1W` | Average Volume 60D Calc\|1W | `average_volume_60d_calc\|1W` | number_group |
| `AVERAGE_VOLUME_60D_CALC_240` | Average Volume 60D Calc\|240 | `average_volume_60d_calc\|240` | number_group |
| `AVERAGE_VOLUME_60D_CALC_30` | Average Volume 60D Calc\|30 | `average_volume_60d_calc\|30` | number_group |
| `AVERAGE_VOLUME_60D_CALC_5` | Average Volume 60D Calc\|5 | `average_volume_60d_calc\|5` | number_group |
| `AVERAGE_VOLUME_60D_CALC_60` | Average Volume 60D Calc\|60 | `average_volume_60d_calc\|60` | number_group |
| `AVERAGE_VOLUME_90D_CALC` | Average Volume 90D Calc | `average_volume_90d_calc` | number_group |
| `AVERAGE_VOLUME_90D_CALC_1` | Average Volume 90D Calc\|1 | `average_volume_90d_calc\|1` | number_group |
| `AVERAGE_VOLUME_90D_CALC_120` | Average Volume 90D Calc\|120 | `average_volume_90d_calc\|120` | number_group |
| `AVERAGE_VOLUME_90D_CALC_15` | Average Volume 90D Calc\|15 | `average_volume_90d_calc\|15` | number_group |
| `AVERAGE_VOLUME_90D_CALC_1M` | Average Volume 90D Calc\|1M | `average_volume_90d_calc\|1M` | number_group |
| `AVERAGE_VOLUME_90D_CALC_1W` | Average Volume 90D Calc\|1W | `average_volume_90d_calc\|1W` | number_group |
| `AVERAGE_VOLUME_90D_CALC_240` | Average Volume 90D Calc\|240 | `average_volume_90d_calc\|240` | number_group |
| `AVERAGE_VOLUME_90D_CALC_30` | Average Volume 90D Calc\|30 | `average_volume_90d_calc\|30` | number_group |
| `AVERAGE_VOLUME_90D_CALC_5` | Average Volume 90D Calc\|5 | `average_volume_90d_calc\|5` | number_group |
| `AVERAGE_VOLUME_90D_CALC_60` | Average Volume 90D Calc\|60 | `average_volume_90d_calc\|60` | number_group |
| `RELATIVE_VOLUME_10D_CALC` | Relative Volume 10D Calc | `relative_volume_10d_calc` | number_group |
| `RELATIVE_VOLUME_10D_CALC_1` | Relative Volume 10D Calc\|1 | `relative_volume_10d_calc\|1` | number_group |
| `RELATIVE_VOLUME_10D_CALC_120` | Relative Volume 10D Calc\|120 | `relative_volume_10d_calc\|120` | number_group |
| `RELATIVE_VOLUME_10D_CALC_15` | Relative Volume 10D Calc\|15 | `relative_volume_10d_calc\|15` | number_group |
| `RELATIVE_VOLUME_10D_CALC_1M` | Relative Volume 10D Calc\|1M | `relative_volume_10d_calc\|1M` | number_group |
| `RELATIVE_VOLUME_10D_CALC_1W` | Relative Volume 10D Calc\|1W | `relative_volume_10d_calc\|1W` | number_group |
| `RELATIVE_VOLUME_10D_CALC_240` | Relative Volume 10D Calc\|240 | `relative_volume_10d_calc\|240` | number_group |
| `RELATIVE_VOLUME_10D_CALC_30` | Relative Volume 10D Calc\|30 | `relative_volume_10d_calc\|30` | number_group |
| `RELATIVE_VOLUME_10D_CALC_5` | Relative Volume 10D Calc\|5 | `relative_volume_10d_calc\|5` | number_group |
| `RELATIVE_VOLUME_10D_CALC_60` | Relative Volume 10D Calc\|60 | `relative_volume_10d_calc\|60` | number_group |
| `RELATIVE_VOLUME_INTRADAY_5` | Relative Volume Intraday\|5 | `relative_volume_intraday\|5` | number_group |
| `VOLUME` | Volume | `volume` | number_group |
| `VOLUME_1` | Volume\|1 | `volume\|1` | number_group |
| `VOLUME_120` | Volume\|120 | `volume\|120` | number_group |
| `VOLUME_15` | Volume\|15 | `volume\|15` | number_group |
| `VOLUME_1M` | Volume\|1M | `volume\|1M` | number_group |
| `VOLUME_1W` | Volume\|1W | `volume\|1W` | number_group |
| `VOLUME_240` | Volume\|240 | `volume\|240` | number_group |
| `VOLUME_30` | Volume\|30 | `volume\|30` | number_group |
| `VOLUME_5` | Volume\|5 | `volume\|5` | number_group |
| `VOLUME_60` | Volume\|60 | `volume\|60` | number_group |
| `VOLUME_CHANGE` | Volume Change | `volume_change` | percent |
| `VOLUME_CHANGE_1` | Volume Change\|1 | `volume_change\|1` | percent |
| `VOLUME_CHANGE_120` | Volume Change\|120 | `volume_change\|120` | percent |
| `VOLUME_CHANGE_15` | Volume Change\|15 | `volume_change\|15` | percent |
| `VOLUME_CHANGE_1M` | Volume Change\|1M | `volume_change\|1M` | percent |
| `VOLUME_CHANGE_1W` | Volume Change\|1W | `volume_change\|1W` | percent |
| `VOLUME_CHANGE_240` | Volume Change\|240 | `volume_change\|240` | percent |
| `VOLUME_CHANGE_30` | Volume Change\|30 | `volume_change\|30` | percent |
| `VOLUME_CHANGE_5` | Volume Change\|5 | `volume_change\|5` | percent |
| `VOLUME_CHANGE_60` | Volume Change\|60 | `volume_change\|60` | percent |
| `VOLUME_CHANGE_ABS` | Volume Change Abs | `volume_change_abs` | percent |
| `VOLUME_CHANGE_ABS_1` | Volume Change Abs\|1 | `volume_change_abs\|1` | percent |
| `VOLUME_CHANGE_ABS_120` | Volume Change Abs\|120 | `volume_change_abs\|120` | percent |
| `VOLUME_CHANGE_ABS_15` | Volume Change Abs\|15 | `volume_change_abs\|15` | percent |
| `VOLUME_CHANGE_ABS_1M` | Volume Change Abs\|1M | `volume_change_abs\|1M` | percent |
| `VOLUME_CHANGE_ABS_1W` | Volume Change Abs\|1W | `volume_change_abs\|1W` | percent |
| `VOLUME_CHANGE_ABS_240` | Volume Change Abs\|240 | `volume_change_abs\|240` | percent |
| `VOLUME_CHANGE_ABS_30` | Volume Change Abs\|30 | `volume_change_abs\|30` | percent |
| `VOLUME_CHANGE_ABS_5` | Volume Change Abs\|5 | `volume_change_abs\|5` | percent |
| `VOLUME_CHANGE_ABS_60` | Volume Change Abs\|60 | `volume_change_abs\|60` | percent |

## Performance

*30 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `ALL_TIME_PERFORMANCE` | All Time Performance | `Perf.All` | percent |
| `AUM_PERF_1M` | Aum Perf 1M | `aum_perf.1M` | percent |
| `AUM_PERF_1Y` | Aum Perf 1Y | `aum_perf.1Y` | percent |
| `AUM_PERF_3M` | Aum Perf 3M | `aum_perf.3M` | percent |
| `AUM_PERF_3Y` | Aum Perf 3Y | `aum_perf.3Y` | percent |
| `AUM_PERF_5Y` | Aum Perf 5Y | `aum_perf.5Y` | percent |
| `AUM_PERF_YTD` | Aum Perf YTD | `aum_perf.YTD` | percent |
| `MONTHLY_PERFORMANCE` | Monthly Performance | `Perf.1M` | percent |
| `MONTH_PERFORMANCE_3` | 3-Month Performance | `Perf.3M` | percent |
| `MONTH_PERFORMANCE_6` | 6-Month Performance | `Perf.6M` | percent |
| `NAV_PERF_1M` | Nav Perf 1M | `nav_perf.1M` | percent |
| `NAV_PERF_1Y` | Nav Perf 1Y | `nav_perf.1Y` | percent |
| `NAV_PERF_3M` | Nav Perf 3M | `nav_perf.3M` | percent |
| `NAV_PERF_3Y` | Nav Perf 3Y | `nav_perf.3Y` | percent |
| `NAV_PERF_5Y` | Nav Perf 5Y | `nav_perf.5Y` | percent |
| `NAV_PERF_YTD` | Nav Perf YTD | `nav_perf.YTD` | percent |
| `PERF_10Y` | Perf 10Y | `Perf.10Y` | percent |
| `PERF_1M_MARKETCAP` | Perf 1M Marketcap | `Perf.1M.MarketCap` | percent |
| `PERF_1W_MARKETCAP` | Perf 1W Marketcap | `Perf.1W.MarketCap` | percent |
| `PERF_1Y_MARKETCAP` | Perf 1Y Marketcap | `Perf.1Y.MarketCap` | percent |
| `PERF_3M_MARKETCAP` | Perf 3M Marketcap | `Perf.3M.MarketCap` | percent |
| `PERF_3Y` | Perf 3Y | `Perf.3Y` | percent |
| `PERF_5D` | Perf 5D | `Perf.5D` | percent |
| `PERF_5Y_MARKETCAP` | Perf 5Y Marketcap | `Perf.5Y.MarketCap` | percent |
| `PERF_6M_MARKETCAP` | Perf 6M Marketcap | `Perf.6M.MarketCap` | percent |
| `PERF_YTD_MARKETCAP` | Perf YTD Marketcap | `Perf.YTD.MarketCap` | percent |
| `WEEKLY_PERFORMANCE` | Weekly Performance | `Perf.W` | percent |
| `YEARLY_PERFORMANCE` | Yearly Performance | `Perf.Y` | percent |
| `YTD_PERFORMANCE` | YTD Performance | `Perf.YTD` | percent |
| `Y_PERFORMANCE_5` | 5Y Performance | `Perf.5Y` | percent |

## Moving Averages

*715 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `EMA100_1` | Ema100\|1 | `EMA100\|1` | float |
| `EMA100_120` | Ema100\|120 | `EMA100\|120` | float |
| `EMA100_15` | Ema100\|15 | `EMA100\|15` | float |
| `EMA100_1M` | Ema100\|1M | `EMA100\|1M` | float |
| `EMA100_1W` | Ema100\|1W | `EMA100\|1W` | float |
| `EMA100_240` | Ema100\|240 | `EMA100\|240` | float |
| `EMA100_30` | Ema100\|30 | `EMA100\|30` | float |
| `EMA100_5` | Ema100\|5 | `EMA100\|5` | float |
| `EMA100_60` | Ema100\|60 | `EMA100\|60` | float |
| `EMA10_1` | Ema10\|1 | `EMA10\|1` | float |
| `EMA10_120` | Ema10\|120 | `EMA10\|120` | float |
| `EMA10_15` | Ema10\|15 | `EMA10\|15` | float |
| `EMA10_1M` | Ema10\|1M | `EMA10\|1M` | float |
| `EMA10_1W` | Ema10\|1W | `EMA10\|1W` | float |
| `EMA10_240` | Ema10\|240 | `EMA10\|240` | float |
| `EMA10_30` | Ema10\|30 | `EMA10\|30` | float |
| `EMA10_5` | Ema10\|5 | `EMA10\|5` | float |
| `EMA10_60` | Ema10\|60 | `EMA10\|60` | float |
| `EMA12` | Ema12 | `EMA12` | float |
| `EMA120` | Ema120 | `EMA120` | float |
| `EMA120_1` | Ema120\|1 | `EMA120\|1` | float |
| `EMA120_120` | Ema120\|120 | `EMA120\|120` | float |
| `EMA120_15` | Ema120\|15 | `EMA120\|15` | float |
| `EMA120_1M` | Ema120\|1M | `EMA120\|1M` | float |
| `EMA120_1W` | Ema120\|1W | `EMA120\|1W` | float |
| `EMA120_240` | Ema120\|240 | `EMA120\|240` | float |
| `EMA120_30` | Ema120\|30 | `EMA120\|30` | float |
| `EMA120_5` | Ema120\|5 | `EMA120\|5` | float |
| `EMA120_60` | Ema120\|60 | `EMA120\|60` | float |
| `EMA12_1` | Ema12\|1 | `EMA12\|1` | float |
| `EMA12_120` | Ema12\|120 | `EMA12\|120` | float |
| `EMA12_15` | Ema12\|15 | `EMA12\|15` | float |
| `EMA12_1M` | Ema12\|1M | `EMA12\|1M` | float |
| `EMA12_1W` | Ema12\|1W | `EMA12\|1W` | float |
| `EMA12_240` | Ema12\|240 | `EMA12\|240` | float |
| `EMA12_30` | Ema12\|30 | `EMA12\|30` | float |
| `EMA12_5` | Ema12\|5 | `EMA12\|5` | float |
| `EMA12_60` | Ema12\|60 | `EMA12\|60` | float |
| `EMA13` | Ema13 | `EMA13` | float |
| `EMA13_1` | Ema13\|1 | `EMA13\|1` | float |
| `EMA13_120` | Ema13\|120 | `EMA13\|120` | float |
| `EMA13_15` | Ema13\|15 | `EMA13\|15` | float |
| `EMA13_1M` | Ema13\|1M | `EMA13\|1M` | float |
| `EMA13_1W` | Ema13\|1W | `EMA13\|1W` | float |
| `EMA13_240` | Ema13\|240 | `EMA13\|240` | float |
| `EMA13_30` | Ema13\|30 | `EMA13\|30` | float |
| `EMA13_5` | Ema13\|5 | `EMA13\|5` | float |
| `EMA13_60` | Ema13\|60 | `EMA13\|60` | float |
| `EMA14` | Ema14 | `EMA14` | float |
| `EMA144` | Ema144 | `EMA144` | float |
| `EMA144_1` | Ema144\|1 | `EMA144\|1` | float |
| `EMA144_120` | Ema144\|120 | `EMA144\|120` | float |
| `EMA144_15` | Ema144\|15 | `EMA144\|15` | float |
| `EMA144_1M` | Ema144\|1M | `EMA144\|1M` | float |
| `EMA144_1W` | Ema144\|1W | `EMA144\|1W` | float |
| `EMA144_240` | Ema144\|240 | `EMA144\|240` | float |
| `EMA144_30` | Ema144\|30 | `EMA144\|30` | float |
| `EMA144_5` | Ema144\|5 | `EMA144\|5` | float |
| `EMA144_60` | Ema144\|60 | `EMA144\|60` | float |
| `EMA14_1` | Ema14\|1 | `EMA14\|1` | float |
| `EMA14_120` | Ema14\|120 | `EMA14\|120` | float |
| `EMA14_15` | Ema14\|15 | `EMA14\|15` | float |
| `EMA14_1M` | Ema14\|1M | `EMA14\|1M` | float |
| `EMA14_1W` | Ema14\|1W | `EMA14\|1W` | float |
| `EMA14_240` | Ema14\|240 | `EMA14\|240` | float |
| `EMA14_30` | Ema14\|30 | `EMA14\|30` | float |
| `EMA14_5` | Ema14\|5 | `EMA14\|5` | float |
| `EMA14_60` | Ema14\|60 | `EMA14\|60` | float |
| `EMA15` | Ema15 | `EMA15` | float |
| `EMA150` | Ema150 | `EMA150` | float |
| `EMA150_1` | Ema150\|1 | `EMA150\|1` | float |
| `EMA150_120` | Ema150\|120 | `EMA150\|120` | float |
| `EMA150_15` | Ema150\|15 | `EMA150\|15` | float |
| `EMA150_1M` | Ema150\|1M | `EMA150\|1M` | float |
| `EMA150_1W` | Ema150\|1W | `EMA150\|1W` | float |
| `EMA150_240` | Ema150\|240 | `EMA150\|240` | float |
| `EMA150_30` | Ema150\|30 | `EMA150\|30` | float |
| `EMA150_5` | Ema150\|5 | `EMA150\|5` | float |
| `EMA150_60` | Ema150\|60 | `EMA150\|60` | float |
| `EMA15_1` | Ema15\|1 | `EMA15\|1` | float |
| `EMA15_120` | Ema15\|120 | `EMA15\|120` | float |
| `EMA15_15` | Ema15\|15 | `EMA15\|15` | float |
| `EMA15_1M` | Ema15\|1M | `EMA15\|1M` | float |
| `EMA15_1W` | Ema15\|1W | `EMA15\|1W` | float |
| `EMA15_240` | Ema15\|240 | `EMA15\|240` | float |
| `EMA15_30` | Ema15\|30 | `EMA15\|30` | float |
| `EMA15_5` | Ema15\|5 | `EMA15\|5` | float |
| `EMA15_60` | Ema15\|60 | `EMA15\|60` | float |
| `EMA2` | Ema2 | `EMA2` | float |
| `EMA200_1` | Ema200\|1 | `EMA200\|1` | float |
| `EMA200_120` | Ema200\|120 | `EMA200\|120` | float |
| `EMA200_15` | Ema200\|15 | `EMA200\|15` | float |
| `EMA200_1M` | Ema200\|1M | `EMA200\|1M` | float |
| `EMA200_1W` | Ema200\|1W | `EMA200\|1W` | float |
| `EMA200_240` | Ema200\|240 | `EMA200\|240` | float |
| `EMA200_30` | Ema200\|30 | `EMA200\|30` | float |
| `EMA200_5` | Ema200\|5 | `EMA200\|5` | float |
| `EMA200_60` | Ema200\|60 | `EMA200\|60` | float |
| `EMA20_1` | Ema20\|1 | `EMA20\|1` | float |
| `EMA20_120` | Ema20\|120 | `EMA20\|120` | float |
| `EMA20_15` | Ema20\|15 | `EMA20\|15` | float |
| `EMA20_1M` | Ema20\|1M | `EMA20\|1M` | float |
| `EMA20_1W` | Ema20\|1W | `EMA20\|1W` | float |
| `EMA20_240` | Ema20\|240 | `EMA20\|240` | float |
| `EMA20_30` | Ema20\|30 | `EMA20\|30` | float |
| `EMA20_5` | Ema20\|5 | `EMA20\|5` | float |
| `EMA20_60` | Ema20\|60 | `EMA20\|60` | float |
| `EMA21` | Ema21 | `EMA21` | float |
| `EMA21_1` | Ema21\|1 | `EMA21\|1` | float |
| `EMA21_120` | Ema21\|120 | `EMA21\|120` | float |
| `EMA21_15` | Ema21\|15 | `EMA21\|15` | float |
| `EMA21_1M` | Ema21\|1M | `EMA21\|1M` | float |
| `EMA21_1W` | Ema21\|1W | `EMA21\|1W` | float |
| `EMA21_240` | Ema21\|240 | `EMA21\|240` | float |
| `EMA21_30` | Ema21\|30 | `EMA21\|30` | float |
| `EMA21_5` | Ema21\|5 | `EMA21\|5` | float |
| `EMA21_60` | Ema21\|60 | `EMA21\|60` | float |
| `EMA25` | Ema25 | `EMA25` | float |
| `EMA250` | Ema250 | `EMA250` | float |
| `EMA250_1` | Ema250\|1 | `EMA250\|1` | float |
| `EMA250_120` | Ema250\|120 | `EMA250\|120` | float |
| `EMA250_15` | Ema250\|15 | `EMA250\|15` | float |
| `EMA250_1M` | Ema250\|1M | `EMA250\|1M` | float |
| `EMA250_1W` | Ema250\|1W | `EMA250\|1W` | float |
| `EMA250_240` | Ema250\|240 | `EMA250\|240` | float |
| `EMA250_30` | Ema250\|30 | `EMA250\|30` | float |
| `EMA250_5` | Ema250\|5 | `EMA250\|5` | float |
| `EMA250_60` | Ema250\|60 | `EMA250\|60` | float |
| `EMA25_1` | Ema25\|1 | `EMA25\|1` | float |
| `EMA25_120` | Ema25\|120 | `EMA25\|120` | float |
| `EMA25_15` | Ema25\|15 | `EMA25\|15` | float |
| `EMA25_1M` | Ema25\|1M | `EMA25\|1M` | float |
| `EMA25_1W` | Ema25\|1W | `EMA25\|1W` | float |
| `EMA25_240` | Ema25\|240 | `EMA25\|240` | float |
| `EMA25_30` | Ema25\|30 | `EMA25\|30` | float |
| `EMA25_5` | Ema25\|5 | `EMA25\|5` | float |
| `EMA25_60` | Ema25\|60 | `EMA25\|60` | float |
| `EMA26` | Ema26 | `EMA26` | float |
| `EMA26_1` | Ema26\|1 | `EMA26\|1` | float |
| `EMA26_120` | Ema26\|120 | `EMA26\|120` | float |
| `EMA26_15` | Ema26\|15 | `EMA26\|15` | float |
| `EMA26_1M` | Ema26\|1M | `EMA26\|1M` | float |
| `EMA26_1W` | Ema26\|1W | `EMA26\|1W` | float |
| `EMA26_240` | Ema26\|240 | `EMA26\|240` | float |
| `EMA26_30` | Ema26\|30 | `EMA26\|30` | float |
| `EMA26_5` | Ema26\|5 | `EMA26\|5` | float |
| `EMA26_60` | Ema26\|60 | `EMA26\|60` | float |
| `EMA2_1` | Ema2\|1 | `EMA2\|1` | float |
| `EMA2_120` | Ema2\|120 | `EMA2\|120` | float |
| `EMA2_15` | Ema2\|15 | `EMA2\|15` | float |
| `EMA2_1M` | Ema2\|1M | `EMA2\|1M` | float |
| `EMA2_1W` | Ema2\|1W | `EMA2\|1W` | float |
| `EMA2_240` | Ema2\|240 | `EMA2\|240` | float |
| `EMA2_30` | Ema2\|30 | `EMA2\|30` | float |
| `EMA2_5` | Ema2\|5 | `EMA2\|5` | float |
| `EMA2_60` | Ema2\|60 | `EMA2\|60` | float |
| `EMA3` | Ema3 | `EMA3` | float |
| `EMA300` | Ema300 | `EMA300` | float |
| `EMA300_1` | Ema300\|1 | `EMA300\|1` | float |
| `EMA300_120` | Ema300\|120 | `EMA300\|120` | float |
| `EMA300_15` | Ema300\|15 | `EMA300\|15` | float |
| `EMA300_1M` | Ema300\|1M | `EMA300\|1M` | float |
| `EMA300_1W` | Ema300\|1W | `EMA300\|1W` | float |
| `EMA300_240` | Ema300\|240 | `EMA300\|240` | float |
| `EMA300_30` | Ema300\|30 | `EMA300\|30` | float |
| `EMA300_5` | Ema300\|5 | `EMA300\|5` | float |
| `EMA300_60` | Ema300\|60 | `EMA300\|60` | float |
| `EMA30_1` | Ema30\|1 | `EMA30\|1` | float |
| `EMA30_120` | Ema30\|120 | `EMA30\|120` | float |
| `EMA30_15` | Ema30\|15 | `EMA30\|15` | float |
| `EMA30_1M` | Ema30\|1M | `EMA30\|1M` | float |
| `EMA30_1W` | Ema30\|1W | `EMA30\|1W` | float |
| `EMA30_240` | Ema30\|240 | `EMA30\|240` | float |
| `EMA30_30` | Ema30\|30 | `EMA30\|30` | float |
| `EMA30_5` | Ema30\|5 | `EMA30\|5` | float |
| `EMA30_60` | Ema30\|60 | `EMA30\|60` | float |
| `EMA34` | Ema34 | `EMA34` | float |
| `EMA34_1` | Ema34\|1 | `EMA34\|1` | float |
| `EMA34_120` | Ema34\|120 | `EMA34\|120` | float |
| `EMA34_15` | Ema34\|15 | `EMA34\|15` | float |
| `EMA34_1M` | Ema34\|1M | `EMA34\|1M` | float |
| `EMA34_1W` | Ema34\|1W | `EMA34\|1W` | float |
| `EMA34_240` | Ema34\|240 | `EMA34\|240` | float |
| `EMA34_30` | Ema34\|30 | `EMA34\|30` | float |
| `EMA34_5` | Ema34\|5 | `EMA34\|5` | float |
| `EMA34_60` | Ema34\|60 | `EMA34\|60` | float |
| `EMA3_1` | Ema3\|1 | `EMA3\|1` | float |
| `EMA3_120` | Ema3\|120 | `EMA3\|120` | float |
| `EMA3_15` | Ema3\|15 | `EMA3\|15` | float |
| `EMA3_1M` | Ema3\|1M | `EMA3\|1M` | float |
| `EMA3_1W` | Ema3\|1W | `EMA3\|1W` | float |
| `EMA3_240` | Ema3\|240 | `EMA3\|240` | float |
| `EMA3_30` | Ema3\|30 | `EMA3\|30` | float |
| `EMA3_5` | Ema3\|5 | `EMA3\|5` | float |
| `EMA3_60` | Ema3\|60 | `EMA3\|60` | float |
| `EMA40` | Ema40 | `EMA40` | float |
| `EMA40_1` | Ema40\|1 | `EMA40\|1` | float |
| `EMA40_120` | Ema40\|120 | `EMA40\|120` | float |
| `EMA40_15` | Ema40\|15 | `EMA40\|15` | float |
| `EMA40_1M` | Ema40\|1M | `EMA40\|1M` | float |
| `EMA40_1W` | Ema40\|1W | `EMA40\|1W` | float |
| `EMA40_240` | Ema40\|240 | `EMA40\|240` | float |
| `EMA40_30` | Ema40\|30 | `EMA40\|30` | float |
| `EMA40_5` | Ema40\|5 | `EMA40\|5` | float |
| `EMA40_60` | Ema40\|60 | `EMA40\|60` | float |
| `EMA50_1` | Ema50\|1 | `EMA50\|1` | float |
| `EMA50_120` | Ema50\|120 | `EMA50\|120` | float |
| `EMA50_15` | Ema50\|15 | `EMA50\|15` | float |
| `EMA50_1M` | Ema50\|1M | `EMA50\|1M` | float |
| `EMA50_1W` | Ema50\|1W | `EMA50\|1W` | float |
| `EMA50_240` | Ema50\|240 | `EMA50\|240` | float |
| `EMA50_30` | Ema50\|30 | `EMA50\|30` | float |
| `EMA50_5` | Ema50\|5 | `EMA50\|5` | float |
| `EMA50_60` | Ema50\|60 | `EMA50\|60` | float |
| `EMA55` | Ema55 | `EMA55` | float |
| `EMA55_1` | Ema55\|1 | `EMA55\|1` | float |
| `EMA55_120` | Ema55\|120 | `EMA55\|120` | float |
| `EMA55_15` | Ema55\|15 | `EMA55\|15` | float |
| `EMA55_1M` | Ema55\|1M | `EMA55\|1M` | float |
| `EMA55_1W` | Ema55\|1W | `EMA55\|1W` | float |
| `EMA55_240` | Ema55\|240 | `EMA55\|240` | float |
| `EMA55_30` | Ema55\|30 | `EMA55\|30` | float |
| `EMA55_5` | Ema55\|5 | `EMA55\|5` | float |
| `EMA55_60` | Ema55\|60 | `EMA55\|60` | float |
| `EMA5_1` | Ema5\|1 | `EMA5\|1` | float |
| `EMA5_120` | Ema5\|120 | `EMA5\|120` | float |
| `EMA5_15` | Ema5\|15 | `EMA5\|15` | float |
| `EMA5_1M` | Ema5\|1M | `EMA5\|1M` | float |
| `EMA5_1W` | Ema5\|1W | `EMA5\|1W` | float |
| `EMA5_240` | Ema5\|240 | `EMA5\|240` | float |
| `EMA5_30` | Ema5\|30 | `EMA5\|30` | float |
| `EMA5_5` | Ema5\|5 | `EMA5\|5` | float |
| `EMA5_60` | Ema5\|60 | `EMA5\|60` | float |
| `EMA6` | Ema6 | `EMA6` | float |
| `EMA60` | Ema60 | `EMA60` | float |
| `EMA60_1` | Ema60\|1 | `EMA60\|1` | float |
| `EMA60_120` | Ema60\|120 | `EMA60\|120` | float |
| `EMA60_15` | Ema60\|15 | `EMA60\|15` | float |
| `EMA60_1M` | Ema60\|1M | `EMA60\|1M` | float |
| `EMA60_1W` | Ema60\|1W | `EMA60\|1W` | float |
| `EMA60_240` | Ema60\|240 | `EMA60\|240` | float |
| `EMA60_30` | Ema60\|30 | `EMA60\|30` | float |
| `EMA60_5` | Ema60\|5 | `EMA60\|5` | float |
| `EMA60_60` | Ema60\|60 | `EMA60\|60` | float |
| `EMA6_1` | Ema6\|1 | `EMA6\|1` | float |
| `EMA6_120` | Ema6\|120 | `EMA6\|120` | float |
| `EMA6_15` | Ema6\|15 | `EMA6\|15` | float |
| `EMA6_1M` | Ema6\|1M | `EMA6\|1M` | float |
| `EMA6_1W` | Ema6\|1W | `EMA6\|1W` | float |
| `EMA6_240` | Ema6\|240 | `EMA6\|240` | float |
| `EMA6_30` | Ema6\|30 | `EMA6\|30` | float |
| `EMA6_5` | Ema6\|5 | `EMA6\|5` | float |
| `EMA6_60` | Ema6\|60 | `EMA6\|60` | float |
| `EMA7` | Ema7 | `EMA7` | float |
| `EMA75` | Ema75 | `EMA75` | float |
| `EMA75_1` | Ema75\|1 | `EMA75\|1` | float |
| `EMA75_120` | Ema75\|120 | `EMA75\|120` | float |
| `EMA75_15` | Ema75\|15 | `EMA75\|15` | float |
| `EMA75_1M` | Ema75\|1M | `EMA75\|1M` | float |
| `EMA75_1W` | Ema75\|1W | `EMA75\|1W` | float |
| `EMA75_240` | Ema75\|240 | `EMA75\|240` | float |
| `EMA75_30` | Ema75\|30 | `EMA75\|30` | float |
| `EMA75_5` | Ema75\|5 | `EMA75\|5` | float |
| `EMA75_60` | Ema75\|60 | `EMA75\|60` | float |
| `EMA7_1` | Ema7\|1 | `EMA7\|1` | float |
| `EMA7_120` | Ema7\|120 | `EMA7\|120` | float |
| `EMA7_15` | Ema7\|15 | `EMA7\|15` | float |
| `EMA7_1M` | Ema7\|1M | `EMA7\|1M` | float |
| `EMA7_1W` | Ema7\|1W | `EMA7\|1W` | float |
| `EMA7_240` | Ema7\|240 | `EMA7\|240` | float |
| `EMA7_30` | Ema7\|30 | `EMA7\|30` | float |
| `EMA7_5` | Ema7\|5 | `EMA7\|5` | float |
| `EMA7_60` | Ema7\|60 | `EMA7\|60` | float |
| `EMA8` | Ema8 | `EMA8` | float |
| `EMA89` | Ema89 | `EMA89` | float |
| `EMA89_1` | Ema89\|1 | `EMA89\|1` | float |
| `EMA89_120` | Ema89\|120 | `EMA89\|120` | float |
| `EMA89_15` | Ema89\|15 | `EMA89\|15` | float |
| `EMA89_1M` | Ema89\|1M | `EMA89\|1M` | float |
| `EMA89_1W` | Ema89\|1W | `EMA89\|1W` | float |
| `EMA89_240` | Ema89\|240 | `EMA89\|240` | float |
| `EMA89_30` | Ema89\|30 | `EMA89\|30` | float |
| `EMA89_5` | Ema89\|5 | `EMA89\|5` | float |
| `EMA89_60` | Ema89\|60 | `EMA89\|60` | float |
| `EMA8_1` | Ema8\|1 | `EMA8\|1` | float |
| `EMA8_120` | Ema8\|120 | `EMA8\|120` | float |
| `EMA8_15` | Ema8\|15 | `EMA8\|15` | float |
| `EMA8_1M` | Ema8\|1M | `EMA8\|1M` | float |
| `EMA8_1W` | Ema8\|1W | `EMA8\|1W` | float |
| `EMA8_240` | Ema8\|240 | `EMA8\|240` | float |
| `EMA8_30` | Ema8\|30 | `EMA8\|30` | float |
| `EMA8_5` | Ema8\|5 | `EMA8\|5` | float |
| `EMA8_60` | Ema8\|60 | `EMA8\|60` | float |
| `EMA9` | Ema9 | `EMA9` | float |
| `EMA9_1` | Ema9\|1 | `EMA9\|1` | float |
| `EMA9_120` | Ema9\|120 | `EMA9\|120` | float |
| `EMA9_15` | Ema9\|15 | `EMA9\|15` | float |
| `EMA9_1M` | Ema9\|1M | `EMA9\|1M` | float |
| `EMA9_1W` | Ema9\|1W | `EMA9\|1W` | float |
| `EMA9_240` | Ema9\|240 | `EMA9\|240` | float |
| `EMA9_30` | Ema9\|30 | `EMA9\|30` | float |
| `EMA9_5` | Ema9\|5 | `EMA9\|5` | float |
| `EMA9_60` | Ema9\|60 | `EMA9\|60` | float |
| `EXPONENTIAL_MOVING_AVERAGE_10` | Exponential Moving Average (10) | `EMA10` | computed_recommendation |
| `EXPONENTIAL_MOVING_AVERAGE_100` | Exponential Moving Average (100) | `EMA100` | computed_recommendation |
| `EXPONENTIAL_MOVING_AVERAGE_20` | Exponential Moving Average (20) | `EMA20` | computed_recommendation |
| `EXPONENTIAL_MOVING_AVERAGE_200` | Exponential Moving Average (200) | `EMA200` | computed_recommendation |
| `EXPONENTIAL_MOVING_AVERAGE_30` | Exponential Moving Average (30) | `EMA30` | computed_recommendation |
| `EXPONENTIAL_MOVING_AVERAGE_5` | Exponential Moving Average (5) | `EMA5` | computed_recommendation |
| `EXPONENTIAL_MOVING_AVERAGE_50` | Exponential Moving Average (50) | `EMA50` | computed_recommendation |
| `HULLMA20` | Hullma20 | `HullMA20` | float |
| `HULLMA200` | Hullma200 | `HullMA200` | float |
| `HULLMA200_1` | Hullma200\|1 | `HullMA200\|1` | float |
| `HULLMA200_120` | Hullma200\|120 | `HullMA200\|120` | float |
| `HULLMA200_15` | Hullma200\|15 | `HullMA200\|15` | float |
| `HULLMA200_1M` | Hullma200\|1M | `HullMA200\|1M` | float |
| `HULLMA200_1W` | Hullma200\|1W | `HullMA200\|1W` | float |
| `HULLMA200_240` | Hullma200\|240 | `HullMA200\|240` | float |
| `HULLMA200_30` | Hullma200\|30 | `HullMA200\|30` | float |
| `HULLMA200_5` | Hullma200\|5 | `HullMA200\|5` | float |
| `HULLMA200_60` | Hullma200\|60 | `HullMA200\|60` | float |
| `HULLMA20_1` | Hullma20\|1 | `HullMA20\|1` | float |
| `HULLMA20_120` | Hullma20\|120 | `HullMA20\|120` | float |
| `HULLMA20_15` | Hullma20\|15 | `HullMA20\|15` | float |
| `HULLMA20_1M` | Hullma20\|1M | `HullMA20\|1M` | float |
| `HULLMA20_1W` | Hullma20\|1W | `HullMA20\|1W` | float |
| `HULLMA20_240` | Hullma20\|240 | `HullMA20\|240` | float |
| `HULLMA20_30` | Hullma20\|30 | `HullMA20\|30` | float |
| `HULLMA20_5` | Hullma20\|5 | `HullMA20\|5` | float |
| `HULLMA20_60` | Hullma20\|60 | `HullMA20\|60` | float |
| `HULLMA9_1` | Hullma9\|1 | `HullMA9\|1` | float |
| `HULLMA9_120` | Hullma9\|120 | `HullMA9\|120` | float |
| `HULLMA9_15` | Hullma9\|15 | `HullMA9\|15` | float |
| `HULLMA9_1M` | Hullma9\|1M | `HullMA9\|1M` | float |
| `HULLMA9_1W` | Hullma9\|1W | `HullMA9\|1W` | float |
| `HULLMA9_240` | Hullma9\|240 | `HullMA9\|240` | float |
| `HULLMA9_30` | Hullma9\|30 | `HullMA9\|30` | float |
| `HULLMA9_5` | Hullma9\|5 | `HullMA9\|5` | float |
| `HULLMA9_60` | Hullma9\|60 | `HullMA9\|60` | float |
| `HULL_MOVING_AVERAGE_9` | Hull Moving Average (9) | `HullMA9` | recommendation |
| `PIVOT_DM_P` | Pivot DM P | `Pivot.M.Demark.Middle` | float |
| `PIVOT_DM_R1` | Pivot DM R1 | `Pivot.M.Demark.R1` | float |
| `PIVOT_DM_S1` | Pivot DM S1 | `Pivot.M.Demark.S1` | float |
| `PIVOT_M_DEMARK_MIDDLE_1` | Pivot M Demark Middle\|1 | `Pivot.M.Demark.Middle\|1` | float |
| `PIVOT_M_DEMARK_MIDDLE_120` | Pivot M Demark Middle\|120 | `Pivot.M.Demark.Middle\|120` | float |
| `PIVOT_M_DEMARK_MIDDLE_15` | Pivot M Demark Middle\|15 | `Pivot.M.Demark.Middle\|15` | float |
| `PIVOT_M_DEMARK_MIDDLE_1M` | Pivot M Demark Middle\|1M | `Pivot.M.Demark.Middle\|1M` | float |
| `PIVOT_M_DEMARK_MIDDLE_1W` | Pivot M Demark Middle\|1W | `Pivot.M.Demark.Middle\|1W` | float |
| `PIVOT_M_DEMARK_MIDDLE_240` | Pivot M Demark Middle\|240 | `Pivot.M.Demark.Middle\|240` | float |
| `PIVOT_M_DEMARK_MIDDLE_30` | Pivot M Demark Middle\|30 | `Pivot.M.Demark.Middle\|30` | float |
| `PIVOT_M_DEMARK_MIDDLE_5` | Pivot M Demark Middle\|5 | `Pivot.M.Demark.Middle\|5` | float |
| `PIVOT_M_DEMARK_MIDDLE_60` | Pivot M Demark Middle\|60 | `Pivot.M.Demark.Middle\|60` | float |
| `PIVOT_M_DEMARK_R1_1` | Pivot M Demark R1\|1 | `Pivot.M.Demark.R1\|1` | float |
| `PIVOT_M_DEMARK_R1_120` | Pivot M Demark R1\|120 | `Pivot.M.Demark.R1\|120` | float |
| `PIVOT_M_DEMARK_R1_15` | Pivot M Demark R1\|15 | `Pivot.M.Demark.R1\|15` | float |
| `PIVOT_M_DEMARK_R1_1M` | Pivot M Demark R1\|1M | `Pivot.M.Demark.R1\|1M` | float |
| `PIVOT_M_DEMARK_R1_1W` | Pivot M Demark R1\|1W | `Pivot.M.Demark.R1\|1W` | float |
| `PIVOT_M_DEMARK_R1_240` | Pivot M Demark R1\|240 | `Pivot.M.Demark.R1\|240` | float |
| `PIVOT_M_DEMARK_R1_30` | Pivot M Demark R1\|30 | `Pivot.M.Demark.R1\|30` | float |
| `PIVOT_M_DEMARK_R1_5` | Pivot M Demark R1\|5 | `Pivot.M.Demark.R1\|5` | float |
| `PIVOT_M_DEMARK_R1_60` | Pivot M Demark R1\|60 | `Pivot.M.Demark.R1\|60` | float |
| `PIVOT_M_DEMARK_S1_1` | Pivot M Demark S1\|1 | `Pivot.M.Demark.S1\|1` | float |
| `PIVOT_M_DEMARK_S1_120` | Pivot M Demark S1\|120 | `Pivot.M.Demark.S1\|120` | float |
| `PIVOT_M_DEMARK_S1_15` | Pivot M Demark S1\|15 | `Pivot.M.Demark.S1\|15` | float |
| `PIVOT_M_DEMARK_S1_1M` | Pivot M Demark S1\|1M | `Pivot.M.Demark.S1\|1M` | float |
| `PIVOT_M_DEMARK_S1_1W` | Pivot M Demark S1\|1W | `Pivot.M.Demark.S1\|1W` | float |
| `PIVOT_M_DEMARK_S1_240` | Pivot M Demark S1\|240 | `Pivot.M.Demark.S1\|240` | float |
| `PIVOT_M_DEMARK_S1_30` | Pivot M Demark S1\|30 | `Pivot.M.Demark.S1\|30` | float |
| `PIVOT_M_DEMARK_S1_5` | Pivot M Demark S1\|5 | `Pivot.M.Demark.S1\|5` | float |
| `PIVOT_M_DEMARK_S1_60` | Pivot M Demark S1\|60 | `Pivot.M.Demark.S1\|60` | float |
| `PREMARKET_CHANGE` | Premarket Change | `premarket_change` | percent |
| `PREMARKET_CHANGE_ABS` | Premarket Change Abs | `premarket_change_abs` | percent |
| `PREMARKET_CHANGE_FROM_OPEN` | Premarket Change From Open | `premarket_change_from_open` | percent |
| `PREMARKET_CHANGE_FROM_OPEN_ABS` | Premarket Change From Open Abs | `premarket_change_from_open_abs` | percent |
| `PREMARKET_GAP` | Premarket Gap | `premarket_gap` | float |
| `REC_HULLMA9` | Rec Hullma9 | `Rec.HullMA9` | rating |
| `REC_HULLMA9_1` | Rec Hullma9\|1 | `Rec.HullMA9\|1` | rating |
| `REC_HULLMA9_120` | Rec Hullma9\|120 | `Rec.HullMA9\|120` | rating |
| `REC_HULLMA9_15` | Rec Hullma9\|15 | `Rec.HullMA9\|15` | rating |
| `REC_HULLMA9_1M` | Rec Hullma9\|1M | `Rec.HullMA9\|1M` | rating |
| `REC_HULLMA9_1W` | Rec Hullma9\|1W | `Rec.HullMA9\|1W` | rating |
| `REC_HULLMA9_240` | Rec Hullma9\|240 | `Rec.HullMA9\|240` | rating |
| `REC_HULLMA9_30` | Rec Hullma9\|30 | `Rec.HullMA9\|30` | rating |
| `REC_HULLMA9_5` | Rec Hullma9\|5 | `Rec.HullMA9\|5` | rating |
| `REC_HULLMA9_60` | Rec Hullma9\|60 | `Rec.HullMA9\|60` | rating |
| `REC_VWMA` | Rec VWMA | `Rec.VWMA` | rating |
| `REC_VWMA_1` | Rec VWMA\|1 | `Rec.VWMA\|1` | rating |
| `REC_VWMA_120` | Rec VWMA\|120 | `Rec.VWMA\|120` | rating |
| `REC_VWMA_15` | Rec VWMA\|15 | `Rec.VWMA\|15` | rating |
| `REC_VWMA_1M` | Rec VWMA\|1M | `Rec.VWMA\|1M` | rating |
| `REC_VWMA_1W` | Rec VWMA\|1W | `Rec.VWMA\|1W` | rating |
| `REC_VWMA_240` | Rec VWMA\|240 | `Rec.VWMA\|240` | rating |
| `REC_VWMA_30` | Rec VWMA\|30 | `Rec.VWMA\|30` | rating |
| `REC_VWMA_5` | Rec VWMA\|5 | `Rec.VWMA\|5` | rating |
| `REC_VWMA_60` | Rec VWMA\|60 | `Rec.VWMA\|60` | rating |
| `SIMPLE_MOVING_AVERAGE_10` | Simple Moving Average (10) | `SMA10` | computed_recommendation |
| `SIMPLE_MOVING_AVERAGE_100` | Simple Moving Average (100) | `SMA100` | computed_recommendation |
| `SIMPLE_MOVING_AVERAGE_20` | Simple Moving Average (20) | `SMA20` | computed_recommendation |
| `SIMPLE_MOVING_AVERAGE_200` | Simple Moving Average (200) | `SMA200` | computed_recommendation |
| `SIMPLE_MOVING_AVERAGE_30` | Simple Moving Average (30) | `SMA30` | computed_recommendation |
| `SIMPLE_MOVING_AVERAGE_5` | Simple Moving Average (5) | `SMA5` | computed_recommendation |
| `SIMPLE_MOVING_AVERAGE_50` | Simple Moving Average (50) | `SMA50` | computed_recommendation |
| `SMA100_1` | Sma100\|1 | `SMA100\|1` | float |
| `SMA100_120` | Sma100\|120 | `SMA100\|120` | float |
| `SMA100_15` | Sma100\|15 | `SMA100\|15` | float |
| `SMA100_1M` | Sma100\|1M | `SMA100\|1M` | float |
| `SMA100_1W` | Sma100\|1W | `SMA100\|1W` | float |
| `SMA100_240` | Sma100\|240 | `SMA100\|240` | float |
| `SMA100_30` | Sma100\|30 | `SMA100\|30` | float |
| `SMA100_5` | Sma100\|5 | `SMA100\|5` | float |
| `SMA100_60` | Sma100\|60 | `SMA100\|60` | float |
| `SMA10_1` | Sma10\|1 | `SMA10\|1` | float |
| `SMA10_120` | Sma10\|120 | `SMA10\|120` | float |
| `SMA10_15` | Sma10\|15 | `SMA10\|15` | float |
| `SMA10_1M` | Sma10\|1M | `SMA10\|1M` | float |
| `SMA10_1W` | Sma10\|1W | `SMA10\|1W` | float |
| `SMA10_240` | Sma10\|240 | `SMA10\|240` | float |
| `SMA10_30` | Sma10\|30 | `SMA10\|30` | float |
| `SMA10_5` | Sma10\|5 | `SMA10\|5` | float |
| `SMA10_60` | Sma10\|60 | `SMA10\|60` | float |
| `SMA12` | Sma12 | `SMA12` | float |
| `SMA120` | Sma120 | `SMA120` | float |
| `SMA120_1` | Sma120\|1 | `SMA120\|1` | float |
| `SMA120_120` | Sma120\|120 | `SMA120\|120` | float |
| `SMA120_15` | Sma120\|15 | `SMA120\|15` | float |
| `SMA120_1M` | Sma120\|1M | `SMA120\|1M` | float |
| `SMA120_1W` | Sma120\|1W | `SMA120\|1W` | float |
| `SMA120_240` | Sma120\|240 | `SMA120\|240` | float |
| `SMA120_30` | Sma120\|30 | `SMA120\|30` | float |
| `SMA120_5` | Sma120\|5 | `SMA120\|5` | float |
| `SMA120_60` | Sma120\|60 | `SMA120\|60` | float |
| `SMA12_1` | Sma12\|1 | `SMA12\|1` | float |
| `SMA12_120` | Sma12\|120 | `SMA12\|120` | float |
| `SMA12_15` | Sma12\|15 | `SMA12\|15` | float |
| `SMA12_1M` | Sma12\|1M | `SMA12\|1M` | float |
| `SMA12_1W` | Sma12\|1W | `SMA12\|1W` | float |
| `SMA12_240` | Sma12\|240 | `SMA12\|240` | float |
| `SMA12_30` | Sma12\|30 | `SMA12\|30` | float |
| `SMA12_5` | Sma12\|5 | `SMA12\|5` | float |
| `SMA12_60` | Sma12\|60 | `SMA12\|60` | float |
| `SMA13` | Sma13 | `SMA13` | float |
| `SMA13_1` | Sma13\|1 | `SMA13\|1` | float |
| `SMA13_120` | Sma13\|120 | `SMA13\|120` | float |
| `SMA13_15` | Sma13\|15 | `SMA13\|15` | float |
| `SMA13_1M` | Sma13\|1M | `SMA13\|1M` | float |
| `SMA13_1W` | Sma13\|1W | `SMA13\|1W` | float |
| `SMA13_240` | Sma13\|240 | `SMA13\|240` | float |
| `SMA13_30` | Sma13\|30 | `SMA13\|30` | float |
| `SMA13_5` | Sma13\|5 | `SMA13\|5` | float |
| `SMA13_60` | Sma13\|60 | `SMA13\|60` | float |
| `SMA14` | Sma14 | `SMA14` | float |
| `SMA144` | Sma144 | `SMA144` | float |
| `SMA144_1` | Sma144\|1 | `SMA144\|1` | float |
| `SMA144_120` | Sma144\|120 | `SMA144\|120` | float |
| `SMA144_15` | Sma144\|15 | `SMA144\|15` | float |
| `SMA144_1M` | Sma144\|1M | `SMA144\|1M` | float |
| `SMA144_1W` | Sma144\|1W | `SMA144\|1W` | float |
| `SMA144_240` | Sma144\|240 | `SMA144\|240` | float |
| `SMA144_30` | Sma144\|30 | `SMA144\|30` | float |
| `SMA144_5` | Sma144\|5 | `SMA144\|5` | float |
| `SMA144_60` | Sma144\|60 | `SMA144\|60` | float |
| `SMA14_1` | Sma14\|1 | `SMA14\|1` | float |
| `SMA14_120` | Sma14\|120 | `SMA14\|120` | float |
| `SMA14_15` | Sma14\|15 | `SMA14\|15` | float |
| `SMA14_1M` | Sma14\|1M | `SMA14\|1M` | float |
| `SMA14_1W` | Sma14\|1W | `SMA14\|1W` | float |
| `SMA14_240` | Sma14\|240 | `SMA14\|240` | float |
| `SMA14_30` | Sma14\|30 | `SMA14\|30` | float |
| `SMA14_5` | Sma14\|5 | `SMA14\|5` | float |
| `SMA14_60` | Sma14\|60 | `SMA14\|60` | float |
| `SMA15` | Sma15 | `SMA15` | float |
| `SMA150` | Sma150 | `SMA150` | float |
| `SMA150_1` | Sma150\|1 | `SMA150\|1` | float |
| `SMA150_120` | Sma150\|120 | `SMA150\|120` | float |
| `SMA150_15` | Sma150\|15 | `SMA150\|15` | float |
| `SMA150_1M` | Sma150\|1M | `SMA150\|1M` | float |
| `SMA150_1W` | Sma150\|1W | `SMA150\|1W` | float |
| `SMA150_240` | Sma150\|240 | `SMA150\|240` | float |
| `SMA150_30` | Sma150\|30 | `SMA150\|30` | float |
| `SMA150_5` | Sma150\|5 | `SMA150\|5` | float |
| `SMA150_60` | Sma150\|60 | `SMA150\|60` | float |
| `SMA15_1` | Sma15\|1 | `SMA15\|1` | float |
| `SMA15_120` | Sma15\|120 | `SMA15\|120` | float |
| `SMA15_15` | Sma15\|15 | `SMA15\|15` | float |
| `SMA15_1M` | Sma15\|1M | `SMA15\|1M` | float |
| `SMA15_1W` | Sma15\|1W | `SMA15\|1W` | float |
| `SMA15_240` | Sma15\|240 | `SMA15\|240` | float |
| `SMA15_30` | Sma15\|30 | `SMA15\|30` | float |
| `SMA15_5` | Sma15\|5 | `SMA15\|5` | float |
| `SMA15_60` | Sma15\|60 | `SMA15\|60` | float |
| `SMA2` | Sma2 | `SMA2` | float |
| `SMA200_1` | Sma200\|1 | `SMA200\|1` | float |
| `SMA200_120` | Sma200\|120 | `SMA200\|120` | float |
| `SMA200_15` | Sma200\|15 | `SMA200\|15` | float |
| `SMA200_1M` | Sma200\|1M | `SMA200\|1M` | float |
| `SMA200_1W` | Sma200\|1W | `SMA200\|1W` | float |
| `SMA200_240` | Sma200\|240 | `SMA200\|240` | float |
| `SMA200_30` | Sma200\|30 | `SMA200\|30` | float |
| `SMA200_5` | Sma200\|5 | `SMA200\|5` | float |
| `SMA200_60` | Sma200\|60 | `SMA200\|60` | float |
| `SMA20_1` | Sma20\|1 | `SMA20\|1` | float |
| `SMA20_120` | Sma20\|120 | `SMA20\|120` | float |
| `SMA20_15` | Sma20\|15 | `SMA20\|15` | float |
| `SMA20_1M` | Sma20\|1M | `SMA20\|1M` | float |
| `SMA20_1W` | Sma20\|1W | `SMA20\|1W` | float |
| `SMA20_240` | Sma20\|240 | `SMA20\|240` | float |
| `SMA20_30` | Sma20\|30 | `SMA20\|30` | float |
| `SMA20_5` | Sma20\|5 | `SMA20\|5` | float |
| `SMA20_60` | Sma20\|60 | `SMA20\|60` | float |
| `SMA21` | Sma21 | `SMA21` | float |
| `SMA21_1` | Sma21\|1 | `SMA21\|1` | float |
| `SMA21_120` | Sma21\|120 | `SMA21\|120` | float |
| `SMA21_15` | Sma21\|15 | `SMA21\|15` | float |
| `SMA21_1M` | Sma21\|1M | `SMA21\|1M` | float |
| `SMA21_1W` | Sma21\|1W | `SMA21\|1W` | float |
| `SMA21_240` | Sma21\|240 | `SMA21\|240` | float |
| `SMA21_30` | Sma21\|30 | `SMA21\|30` | float |
| `SMA21_5` | Sma21\|5 | `SMA21\|5` | float |
| `SMA21_60` | Sma21\|60 | `SMA21\|60` | float |
| `SMA25` | Sma25 | `SMA25` | float |
| `SMA250` | Sma250 | `SMA250` | float |
| `SMA250_1` | Sma250\|1 | `SMA250\|1` | float |
| `SMA250_120` | Sma250\|120 | `SMA250\|120` | float |
| `SMA250_15` | Sma250\|15 | `SMA250\|15` | float |
| `SMA250_1M` | Sma250\|1M | `SMA250\|1M` | float |
| `SMA250_1W` | Sma250\|1W | `SMA250\|1W` | float |
| `SMA250_240` | Sma250\|240 | `SMA250\|240` | float |
| `SMA250_30` | Sma250\|30 | `SMA250\|30` | float |
| `SMA250_5` | Sma250\|5 | `SMA250\|5` | float |
| `SMA250_60` | Sma250\|60 | `SMA250\|60` | float |
| `SMA25_1` | Sma25\|1 | `SMA25\|1` | float |
| `SMA25_120` | Sma25\|120 | `SMA25\|120` | float |
| `SMA25_15` | Sma25\|15 | `SMA25\|15` | float |
| `SMA25_1M` | Sma25\|1M | `SMA25\|1M` | float |
| `SMA25_1W` | Sma25\|1W | `SMA25\|1W` | float |
| `SMA25_240` | Sma25\|240 | `SMA25\|240` | float |
| `SMA25_30` | Sma25\|30 | `SMA25\|30` | float |
| `SMA25_5` | Sma25\|5 | `SMA25\|5` | float |
| `SMA25_60` | Sma25\|60 | `SMA25\|60` | float |
| `SMA26` | Sma26 | `SMA26` | float |
| `SMA26_1` | Sma26\|1 | `SMA26\|1` | float |
| `SMA26_120` | Sma26\|120 | `SMA26\|120` | float |
| `SMA26_15` | Sma26\|15 | `SMA26\|15` | float |
| `SMA26_1M` | Sma26\|1M | `SMA26\|1M` | float |
| `SMA26_1W` | Sma26\|1W | `SMA26\|1W` | float |
| `SMA26_240` | Sma26\|240 | `SMA26\|240` | float |
| `SMA26_30` | Sma26\|30 | `SMA26\|30` | float |
| `SMA26_5` | Sma26\|5 | `SMA26\|5` | float |
| `SMA26_60` | Sma26\|60 | `SMA26\|60` | float |
| `SMA2_1` | Sma2\|1 | `SMA2\|1` | float |
| `SMA2_120` | Sma2\|120 | `SMA2\|120` | float |
| `SMA2_15` | Sma2\|15 | `SMA2\|15` | float |
| `SMA2_1M` | Sma2\|1M | `SMA2\|1M` | float |
| `SMA2_1W` | Sma2\|1W | `SMA2\|1W` | float |
| `SMA2_240` | Sma2\|240 | `SMA2\|240` | float |
| `SMA2_30` | Sma2\|30 | `SMA2\|30` | float |
| `SMA2_5` | Sma2\|5 | `SMA2\|5` | float |
| `SMA2_60` | Sma2\|60 | `SMA2\|60` | float |
| `SMA3` | Sma3 | `SMA3` | float |
| `SMA300` | Sma300 | `SMA300` | float |
| `SMA300_1` | Sma300\|1 | `SMA300\|1` | float |
| `SMA300_120` | Sma300\|120 | `SMA300\|120` | float |
| `SMA300_15` | Sma300\|15 | `SMA300\|15` | float |
| `SMA300_1M` | Sma300\|1M | `SMA300\|1M` | float |
| `SMA300_1W` | Sma300\|1W | `SMA300\|1W` | float |
| `SMA300_240` | Sma300\|240 | `SMA300\|240` | float |
| `SMA300_30` | Sma300\|30 | `SMA300\|30` | float |
| `SMA300_5` | Sma300\|5 | `SMA300\|5` | float |
| `SMA300_60` | Sma300\|60 | `SMA300\|60` | float |
| `SMA30_1` | Sma30\|1 | `SMA30\|1` | float |
| `SMA30_120` | Sma30\|120 | `SMA30\|120` | float |
| `SMA30_15` | Sma30\|15 | `SMA30\|15` | float |
| `SMA30_1M` | Sma30\|1M | `SMA30\|1M` | float |
| `SMA30_1W` | Sma30\|1W | `SMA30\|1W` | float |
| `SMA30_240` | Sma30\|240 | `SMA30\|240` | float |
| `SMA30_30` | Sma30\|30 | `SMA30\|30` | float |
| `SMA30_5` | Sma30\|5 | `SMA30\|5` | float |
| `SMA30_60` | Sma30\|60 | `SMA30\|60` | float |
| `SMA34` | Sma34 | `SMA34` | float |
| `SMA34_1` | Sma34\|1 | `SMA34\|1` | float |
| `SMA34_120` | Sma34\|120 | `SMA34\|120` | float |
| `SMA34_15` | Sma34\|15 | `SMA34\|15` | float |
| `SMA34_1M` | Sma34\|1M | `SMA34\|1M` | float |
| `SMA34_1W` | Sma34\|1W | `SMA34\|1W` | float |
| `SMA34_240` | Sma34\|240 | `SMA34\|240` | float |
| `SMA34_30` | Sma34\|30 | `SMA34\|30` | float |
| `SMA34_5` | Sma34\|5 | `SMA34\|5` | float |
| `SMA34_60` | Sma34\|60 | `SMA34\|60` | float |
| `SMA3_1` | Sma3\|1 | `SMA3\|1` | float |
| `SMA3_120` | Sma3\|120 | `SMA3\|120` | float |
| `SMA3_15` | Sma3\|15 | `SMA3\|15` | float |
| `SMA3_1M` | Sma3\|1M | `SMA3\|1M` | float |
| `SMA3_1W` | Sma3\|1W | `SMA3\|1W` | float |
| `SMA3_240` | Sma3\|240 | `SMA3\|240` | float |
| `SMA3_30` | Sma3\|30 | `SMA3\|30` | float |
| `SMA3_5` | Sma3\|5 | `SMA3\|5` | float |
| `SMA3_60` | Sma3\|60 | `SMA3\|60` | float |
| `SMA40` | Sma40 | `SMA40` | float |
| `SMA40_1` | Sma40\|1 | `SMA40\|1` | float |
| `SMA40_120` | Sma40\|120 | `SMA40\|120` | float |
| `SMA40_15` | Sma40\|15 | `SMA40\|15` | float |
| `SMA40_1M` | Sma40\|1M | `SMA40\|1M` | float |
| `SMA40_1W` | Sma40\|1W | `SMA40\|1W` | float |
| `SMA40_240` | Sma40\|240 | `SMA40\|240` | float |
| `SMA40_30` | Sma40\|30 | `SMA40\|30` | float |
| `SMA40_5` | Sma40\|5 | `SMA40\|5` | float |
| `SMA40_60` | Sma40\|60 | `SMA40\|60` | float |
| `SMA50_1` | Sma50\|1 | `SMA50\|1` | float |
| `SMA50_120` | Sma50\|120 | `SMA50\|120` | float |
| `SMA50_15` | Sma50\|15 | `SMA50\|15` | float |
| `SMA50_1M` | Sma50\|1M | `SMA50\|1M` | float |
| `SMA50_1W` | Sma50\|1W | `SMA50\|1W` | float |
| `SMA50_240` | Sma50\|240 | `SMA50\|240` | float |
| `SMA50_30` | Sma50\|30 | `SMA50\|30` | float |
| `SMA50_5` | Sma50\|5 | `SMA50\|5` | float |
| `SMA50_60` | Sma50\|60 | `SMA50\|60` | float |
| `SMA55` | Sma55 | `SMA55` | float |
| `SMA55_1` | Sma55\|1 | `SMA55\|1` | float |
| `SMA55_120` | Sma55\|120 | `SMA55\|120` | float |
| `SMA55_15` | Sma55\|15 | `SMA55\|15` | float |
| `SMA55_1M` | Sma55\|1M | `SMA55\|1M` | float |
| `SMA55_1W` | Sma55\|1W | `SMA55\|1W` | float |
| `SMA55_240` | Sma55\|240 | `SMA55\|240` | float |
| `SMA55_30` | Sma55\|30 | `SMA55\|30` | float |
| `SMA55_5` | Sma55\|5 | `SMA55\|5` | float |
| `SMA55_60` | Sma55\|60 | `SMA55\|60` | float |
| `SMA5_1` | Sma5\|1 | `SMA5\|1` | float |
| `SMA5_120` | Sma5\|120 | `SMA5\|120` | float |
| `SMA5_15` | Sma5\|15 | `SMA5\|15` | float |
| `SMA5_1M` | Sma5\|1M | `SMA5\|1M` | float |
| `SMA5_1W` | Sma5\|1W | `SMA5\|1W` | float |
| `SMA5_240` | Sma5\|240 | `SMA5\|240` | float |
| `SMA5_30` | Sma5\|30 | `SMA5\|30` | float |
| `SMA5_5` | Sma5\|5 | `SMA5\|5` | float |
| `SMA5_60` | Sma5\|60 | `SMA5\|60` | float |
| `SMA6` | Sma6 | `SMA6` | float |
| `SMA60` | Sma60 | `SMA60` | float |
| `SMA60_1` | Sma60\|1 | `SMA60\|1` | float |
| `SMA60_120` | Sma60\|120 | `SMA60\|120` | float |
| `SMA60_15` | Sma60\|15 | `SMA60\|15` | float |
| `SMA60_1M` | Sma60\|1M | `SMA60\|1M` | float |
| `SMA60_1W` | Sma60\|1W | `SMA60\|1W` | float |
| `SMA60_240` | Sma60\|240 | `SMA60\|240` | float |
| `SMA60_30` | Sma60\|30 | `SMA60\|30` | float |
| `SMA60_5` | Sma60\|5 | `SMA60\|5` | float |
| `SMA60_60` | Sma60\|60 | `SMA60\|60` | float |
| `SMA6_1` | Sma6\|1 | `SMA6\|1` | float |
| `SMA6_120` | Sma6\|120 | `SMA6\|120` | float |
| `SMA6_15` | Sma6\|15 | `SMA6\|15` | float |
| `SMA6_1M` | Sma6\|1M | `SMA6\|1M` | float |
| `SMA6_1W` | Sma6\|1W | `SMA6\|1W` | float |
| `SMA6_240` | Sma6\|240 | `SMA6\|240` | float |
| `SMA6_30` | Sma6\|30 | `SMA6\|30` | float |
| `SMA6_5` | Sma6\|5 | `SMA6\|5` | float |
| `SMA6_60` | Sma6\|60 | `SMA6\|60` | float |
| `SMA7` | Sma7 | `SMA7` | float |
| `SMA75` | Sma75 | `SMA75` | float |
| `SMA75_1` | Sma75\|1 | `SMA75\|1` | float |
| `SMA75_120` | Sma75\|120 | `SMA75\|120` | float |
| `SMA75_15` | Sma75\|15 | `SMA75\|15` | float |
| `SMA75_1M` | Sma75\|1M | `SMA75\|1M` | float |
| `SMA75_1W` | Sma75\|1W | `SMA75\|1W` | float |
| `SMA75_240` | Sma75\|240 | `SMA75\|240` | float |
| `SMA75_30` | Sma75\|30 | `SMA75\|30` | float |
| `SMA75_5` | Sma75\|5 | `SMA75\|5` | float |
| `SMA75_60` | Sma75\|60 | `SMA75\|60` | float |
| `SMA7_1` | Sma7\|1 | `SMA7\|1` | float |
| `SMA7_120` | Sma7\|120 | `SMA7\|120` | float |
| `SMA7_15` | Sma7\|15 | `SMA7\|15` | float |
| `SMA7_1M` | Sma7\|1M | `SMA7\|1M` | float |
| `SMA7_1W` | Sma7\|1W | `SMA7\|1W` | float |
| `SMA7_240` | Sma7\|240 | `SMA7\|240` | float |
| `SMA7_30` | Sma7\|30 | `SMA7\|30` | float |
| `SMA7_5` | Sma7\|5 | `SMA7\|5` | float |
| `SMA7_60` | Sma7\|60 | `SMA7\|60` | float |
| `SMA8` | Sma8 | `SMA8` | float |
| `SMA89` | Sma89 | `SMA89` | float |
| `SMA89_1` | Sma89\|1 | `SMA89\|1` | float |
| `SMA89_120` | Sma89\|120 | `SMA89\|120` | float |
| `SMA89_15` | Sma89\|15 | `SMA89\|15` | float |
| `SMA89_1M` | Sma89\|1M | `SMA89\|1M` | float |
| `SMA89_1W` | Sma89\|1W | `SMA89\|1W` | float |
| `SMA89_240` | Sma89\|240 | `SMA89\|240` | float |
| `SMA89_30` | Sma89\|30 | `SMA89\|30` | float |
| `SMA89_5` | Sma89\|5 | `SMA89\|5` | float |
| `SMA89_60` | Sma89\|60 | `SMA89\|60` | float |
| `SMA8_1` | Sma8\|1 | `SMA8\|1` | float |
| `SMA8_120` | Sma8\|120 | `SMA8\|120` | float |
| `SMA8_15` | Sma8\|15 | `SMA8\|15` | float |
| `SMA8_1M` | Sma8\|1M | `SMA8\|1M` | float |
| `SMA8_1W` | Sma8\|1W | `SMA8\|1W` | float |
| `SMA8_240` | Sma8\|240 | `SMA8\|240` | float |
| `SMA8_30` | Sma8\|30 | `SMA8\|30` | float |
| `SMA8_5` | Sma8\|5 | `SMA8\|5` | float |
| `SMA8_60` | Sma8\|60 | `SMA8\|60` | float |
| `SMA9` | Sma9 | `SMA9` | float |
| `SMA9_1` | Sma9\|1 | `SMA9\|1` | float |
| `SMA9_120` | Sma9\|120 | `SMA9\|120` | float |
| `SMA9_15` | Sma9\|15 | `SMA9\|15` | float |
| `SMA9_1M` | Sma9\|1M | `SMA9\|1M` | float |
| `SMA9_1W` | Sma9\|1W | `SMA9\|1W` | float |
| `SMA9_240` | Sma9\|240 | `SMA9\|240` | float |
| `SMA9_30` | Sma9\|30 | `SMA9\|30` | float |
| `SMA9_5` | Sma9\|5 | `SMA9\|5` | float |
| `SMA9_60` | Sma9\|60 | `SMA9\|60` | float |
| `VOLUME_WEIGHTED_MOVING_AVERAGE_20` | Volume Weighted Moving Average (20) | `VWMA` | missing |
| `VWMA_1` | VWMA\|1 | `VWMA\|1` | float |
| `VWMA_120` | VWMA\|120 | `VWMA\|120` | float |
| `VWMA_15` | VWMA\|15 | `VWMA\|15` | float |
| `VWMA_1M` | VWMA\|1M | `VWMA\|1M` | float |
| `VWMA_1W` | VWMA\|1W | `VWMA\|1W` | float |
| `VWMA_240` | VWMA\|240 | `VWMA\|240` | float |
| `VWMA_30` | VWMA\|30 | `VWMA\|30` | float |
| `VWMA_5` | VWMA\|5 | `VWMA\|5` | float |
| `VWMA_60` | VWMA\|60 | `VWMA\|60` | float |

## Oscillators

*670 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `AO_1` | AO[1] | `AO[1]` | float |
| `AO_120` | AO\|120 | `AO\|120` | float |
| `AO_15` | AO\|15 | `AO\|15` | float |
| `AO_1M` | AO\|1M | `AO\|1M` | float |
| `AO_1W` | AO\|1W | `AO\|1W` | float |
| `AO_1_1` | AO[1]\|1 | `AO[1]\|1` | float |
| `AO_1_120` | AO[1]\|120 | `AO[1]\|120` | float |
| `AO_1_15` | AO[1]\|15 | `AO[1]\|15` | float |
| `AO_1_1M` | AO[1]\|1M | `AO[1]\|1M` | float |
| `AO_1_1W` | AO[1]\|1W | `AO[1]\|1W` | float |
| `AO_1_2` | AO\|1 | `AO\|1` | float |
| `AO_1_240` | AO[1]\|240 | `AO[1]\|240` | float |
| `AO_1_30` | AO[1]\|30 | `AO[1]\|30` | float |
| `AO_1_5` | AO[1]\|5 | `AO[1]\|5` | float |
| `AO_1_60` | AO[1]\|60 | `AO[1]\|60` | float |
| `AO_2` | AO[2] | `AO[2]` | float |
| `AO_240` | AO\|240 | `AO\|240` | float |
| `AO_2_1` | AO[2]\|1 | `AO[2]\|1` | float |
| `AO_2_120` | AO[2]\|120 | `AO[2]\|120` | float |
| `AO_2_15` | AO[2]\|15 | `AO[2]\|15` | float |
| `AO_2_1M` | AO[2]\|1M | `AO[2]\|1M` | float |
| `AO_2_1W` | AO[2]\|1W | `AO[2]\|1W` | float |
| `AO_2_240` | AO[2]\|240 | `AO[2]\|240` | float |
| `AO_2_30` | AO[2]\|30 | `AO[2]\|30` | float |
| `AO_2_5` | AO[2]\|5 | `AO[2]\|5` | float |
| `AO_2_60` | AO[2]\|60 | `AO[2]\|60` | float |
| `AO_30` | AO\|30 | `AO\|30` | float |
| `AO_5` | AO\|5 | `AO\|5` | float |
| `AO_60` | AO\|60 | `AO\|60` | float |
| `AWESOME_OSCILLATOR` | Awesome Oscillator | `AO` | computed_recommendation |
| `BBPOWER_1` | Bbpower\|1 | `BBPower\|1` | float |
| `BBPOWER_120` | Bbpower\|120 | `BBPower\|120` | float |
| `BBPOWER_15` | Bbpower\|15 | `BBPower\|15` | float |
| `BBPOWER_1M` | Bbpower\|1M | `BBPower\|1M` | float |
| `BBPOWER_1W` | Bbpower\|1W | `BBPower\|1W` | float |
| `BBPOWER_240` | Bbpower\|240 | `BBPower\|240` | float |
| `BBPOWER_30` | Bbpower\|30 | `BBPower\|30` | float |
| `BBPOWER_5` | Bbpower\|5 | `BBPower\|5` | float |
| `BBPOWER_60` | Bbpower\|60 | `BBPower\|60` | float |
| `BULL_BEAR_POWER` | Bull Bear Power | `BBPower` | recommendation |
| `CCI20_1` | Cci20[1] | `CCI20[1]` | float |
| `CCI20_120` | Cci20\|120 | `CCI20\|120` | float |
| `CCI20_15` | Cci20\|15 | `CCI20\|15` | float |
| `CCI20_1M` | Cci20\|1M | `CCI20\|1M` | float |
| `CCI20_1W` | Cci20\|1W | `CCI20\|1W` | float |
| `CCI20_1_1` | Cci20[1]\|1 | `CCI20[1]\|1` | float |
| `CCI20_1_120` | Cci20[1]\|120 | `CCI20[1]\|120` | float |
| `CCI20_1_15` | Cci20[1]\|15 | `CCI20[1]\|15` | float |
| `CCI20_1_1M` | Cci20[1]\|1M | `CCI20[1]\|1M` | float |
| `CCI20_1_1W` | Cci20[1]\|1W | `CCI20[1]\|1W` | float |
| `CCI20_1_2` | Cci20\|1 | `CCI20\|1` | float |
| `CCI20_1_240` | Cci20[1]\|240 | `CCI20[1]\|240` | float |
| `CCI20_1_30` | Cci20[1]\|30 | `CCI20[1]\|30` | float |
| `CCI20_1_5` | Cci20[1]\|5 | `CCI20[1]\|5` | float |
| `CCI20_1_60` | Cci20[1]\|60 | `CCI20[1]\|60` | float |
| `CCI20_240` | Cci20\|240 | `CCI20\|240` | float |
| `CCI20_30` | Cci20\|30 | `CCI20\|30` | float |
| `CCI20_5` | Cci20\|5 | `CCI20\|5` | float |
| `CCI20_60` | Cci20\|60 | `CCI20\|60` | float |
| `COMMODITY_CHANNEL_INDEX_20` | Commodity Channel Index (20) | `CCI20` | computed_recommendation |
| `MOMENTUM_10` | Momentum (10) | `Mom` | computed_recommendation |
| `MOM_1` | Mom[1] | `Mom[1]` | float |
| `MOM_120` | Mom\|120 | `Mom\|120` | float |
| `MOM_14` | Mom 14 | `Mom_14` | float |
| `MOM_14_1` | Mom 14[1] | `Mom_14[1]` | float |
| `MOM_14_120` | Mom 14\|120 | `Mom_14\|120` | float |
| `MOM_14_15` | Mom 14\|15 | `Mom_14\|15` | float |
| `MOM_14_1M` | Mom 14\|1M | `Mom_14\|1M` | float |
| `MOM_14_1W` | Mom 14\|1W | `Mom_14\|1W` | float |
| `MOM_14_1_1` | Mom 14[1]\|1 | `Mom_14[1]\|1` | float |
| `MOM_14_1_120` | Mom 14[1]\|120 | `Mom_14[1]\|120` | float |
| `MOM_14_1_15` | Mom 14[1]\|15 | `Mom_14[1]\|15` | float |
| `MOM_14_1_1M` | Mom 14[1]\|1M | `Mom_14[1]\|1M` | float |
| `MOM_14_1_1W` | Mom 14[1]\|1W | `Mom_14[1]\|1W` | float |
| `MOM_14_1_2` | Mom 14\|1 | `Mom_14\|1` | float |
| `MOM_14_1_240` | Mom 14[1]\|240 | `Mom_14[1]\|240` | float |
| `MOM_14_1_30` | Mom 14[1]\|30 | `Mom_14[1]\|30` | float |
| `MOM_14_1_5` | Mom 14[1]\|5 | `Mom_14[1]\|5` | float |
| `MOM_14_1_60` | Mom 14[1]\|60 | `Mom_14[1]\|60` | float |
| `MOM_14_240` | Mom 14\|240 | `Mom_14\|240` | float |
| `MOM_14_30` | Mom 14\|30 | `Mom_14\|30` | float |
| `MOM_14_5` | Mom 14\|5 | `Mom_14\|5` | float |
| `MOM_14_60` | Mom 14\|60 | `Mom_14\|60` | float |
| `MOM_15` | Mom\|15 | `Mom\|15` | float |
| `MOM_1M` | Mom\|1M | `Mom\|1M` | float |
| `MOM_1W` | Mom\|1W | `Mom\|1W` | float |
| `MOM_1_1` | Mom[1]\|1 | `Mom[1]\|1` | float |
| `MOM_1_120` | Mom[1]\|120 | `Mom[1]\|120` | float |
| `MOM_1_15` | Mom[1]\|15 | `Mom[1]\|15` | float |
| `MOM_1_1M` | Mom[1]\|1M | `Mom[1]\|1M` | float |
| `MOM_1_1W` | Mom[1]\|1W | `Mom[1]\|1W` | float |
| `MOM_1_2` | Mom\|1 | `Mom\|1` | float |
| `MOM_1_240` | Mom[1]\|240 | `Mom[1]\|240` | float |
| `MOM_1_30` | Mom[1]\|30 | `Mom[1]\|30` | float |
| `MOM_1_5` | Mom[1]\|5 | `Mom[1]\|5` | float |
| `MOM_1_60` | Mom[1]\|60 | `Mom[1]\|60` | float |
| `MOM_240` | Mom\|240 | `Mom\|240` | float |
| `MOM_30` | Mom\|30 | `Mom\|30` | float |
| `MOM_5` | Mom\|5 | `Mom\|5` | float |
| `MOM_60` | Mom\|60 | `Mom\|60` | float |
| `PIVOT_FIBONACCI_P` | Pivot Fibonacci P | `Pivot.M.Fibonacci.Middle` | float |
| `PIVOT_FIBONACCI_R1` | Pivot Fibonacci R1 | `Pivot.M.Fibonacci.R1` | float |
| `PIVOT_FIBONACCI_R2` | Pivot Fibonacci R2 | `Pivot.M.Fibonacci.R2` | float |
| `PIVOT_FIBONACCI_R3` | Pivot Fibonacci R3 | `Pivot.M.Fibonacci.R3` | float |
| `PIVOT_FIBONACCI_S1` | Pivot Fibonacci S1 | `Pivot.M.Fibonacci.S1` | float |
| `PIVOT_FIBONACCI_S2` | Pivot Fibonacci S2 | `Pivot.M.Fibonacci.S2` | float |
| `PIVOT_FIBONACCI_S3` | Pivot Fibonacci S3 | `Pivot.M.Fibonacci.S3` | float |
| `PIVOT_M_FIBONACCI_MIDDLE_1` | Pivot M Fibonacci Middle\|1 | `Pivot.M.Fibonacci.Middle\|1` | float |
| `PIVOT_M_FIBONACCI_MIDDLE_120` | Pivot M Fibonacci Middle\|120 | `Pivot.M.Fibonacci.Middle\|120` | float |
| `PIVOT_M_FIBONACCI_MIDDLE_15` | Pivot M Fibonacci Middle\|15 | `Pivot.M.Fibonacci.Middle\|15` | float |
| `PIVOT_M_FIBONACCI_MIDDLE_1M` | Pivot M Fibonacci Middle\|1M | `Pivot.M.Fibonacci.Middle\|1M` | float |
| `PIVOT_M_FIBONACCI_MIDDLE_1W` | Pivot M Fibonacci Middle\|1W | `Pivot.M.Fibonacci.Middle\|1W` | float |
| `PIVOT_M_FIBONACCI_MIDDLE_240` | Pivot M Fibonacci Middle\|240 | `Pivot.M.Fibonacci.Middle\|240` | float |
| `PIVOT_M_FIBONACCI_MIDDLE_30` | Pivot M Fibonacci Middle\|30 | `Pivot.M.Fibonacci.Middle\|30` | float |
| `PIVOT_M_FIBONACCI_MIDDLE_5` | Pivot M Fibonacci Middle\|5 | `Pivot.M.Fibonacci.Middle\|5` | float |
| `PIVOT_M_FIBONACCI_MIDDLE_60` | Pivot M Fibonacci Middle\|60 | `Pivot.M.Fibonacci.Middle\|60` | float |
| `PIVOT_M_FIBONACCI_R1_1` | Pivot M Fibonacci R1\|1 | `Pivot.M.Fibonacci.R1\|1` | float |
| `PIVOT_M_FIBONACCI_R1_120` | Pivot M Fibonacci R1\|120 | `Pivot.M.Fibonacci.R1\|120` | float |
| `PIVOT_M_FIBONACCI_R1_15` | Pivot M Fibonacci R1\|15 | `Pivot.M.Fibonacci.R1\|15` | float |
| `PIVOT_M_FIBONACCI_R1_1M` | Pivot M Fibonacci R1\|1M | `Pivot.M.Fibonacci.R1\|1M` | float |
| `PIVOT_M_FIBONACCI_R1_1W` | Pivot M Fibonacci R1\|1W | `Pivot.M.Fibonacci.R1\|1W` | float |
| `PIVOT_M_FIBONACCI_R1_240` | Pivot M Fibonacci R1\|240 | `Pivot.M.Fibonacci.R1\|240` | float |
| `PIVOT_M_FIBONACCI_R1_30` | Pivot M Fibonacci R1\|30 | `Pivot.M.Fibonacci.R1\|30` | float |
| `PIVOT_M_FIBONACCI_R1_5` | Pivot M Fibonacci R1\|5 | `Pivot.M.Fibonacci.R1\|5` | float |
| `PIVOT_M_FIBONACCI_R1_60` | Pivot M Fibonacci R1\|60 | `Pivot.M.Fibonacci.R1\|60` | float |
| `PIVOT_M_FIBONACCI_R2_1` | Pivot M Fibonacci R2\|1 | `Pivot.M.Fibonacci.R2\|1` | float |
| `PIVOT_M_FIBONACCI_R2_120` | Pivot M Fibonacci R2\|120 | `Pivot.M.Fibonacci.R2\|120` | float |
| `PIVOT_M_FIBONACCI_R2_15` | Pivot M Fibonacci R2\|15 | `Pivot.M.Fibonacci.R2\|15` | float |
| `PIVOT_M_FIBONACCI_R2_1M` | Pivot M Fibonacci R2\|1M | `Pivot.M.Fibonacci.R2\|1M` | float |
| `PIVOT_M_FIBONACCI_R2_1W` | Pivot M Fibonacci R2\|1W | `Pivot.M.Fibonacci.R2\|1W` | float |
| `PIVOT_M_FIBONACCI_R2_240` | Pivot M Fibonacci R2\|240 | `Pivot.M.Fibonacci.R2\|240` | float |
| `PIVOT_M_FIBONACCI_R2_30` | Pivot M Fibonacci R2\|30 | `Pivot.M.Fibonacci.R2\|30` | float |
| `PIVOT_M_FIBONACCI_R2_5` | Pivot M Fibonacci R2\|5 | `Pivot.M.Fibonacci.R2\|5` | float |
| `PIVOT_M_FIBONACCI_R2_60` | Pivot M Fibonacci R2\|60 | `Pivot.M.Fibonacci.R2\|60` | float |
| `PIVOT_M_FIBONACCI_R3_1` | Pivot M Fibonacci R3\|1 | `Pivot.M.Fibonacci.R3\|1` | float |
| `PIVOT_M_FIBONACCI_R3_120` | Pivot M Fibonacci R3\|120 | `Pivot.M.Fibonacci.R3\|120` | float |
| `PIVOT_M_FIBONACCI_R3_15` | Pivot M Fibonacci R3\|15 | `Pivot.M.Fibonacci.R3\|15` | float |
| `PIVOT_M_FIBONACCI_R3_1M` | Pivot M Fibonacci R3\|1M | `Pivot.M.Fibonacci.R3\|1M` | float |
| `PIVOT_M_FIBONACCI_R3_1W` | Pivot M Fibonacci R3\|1W | `Pivot.M.Fibonacci.R3\|1W` | float |
| `PIVOT_M_FIBONACCI_R3_240` | Pivot M Fibonacci R3\|240 | `Pivot.M.Fibonacci.R3\|240` | float |
| `PIVOT_M_FIBONACCI_R3_30` | Pivot M Fibonacci R3\|30 | `Pivot.M.Fibonacci.R3\|30` | float |
| `PIVOT_M_FIBONACCI_R3_5` | Pivot M Fibonacci R3\|5 | `Pivot.M.Fibonacci.R3\|5` | float |
| `PIVOT_M_FIBONACCI_R3_60` | Pivot M Fibonacci R3\|60 | `Pivot.M.Fibonacci.R3\|60` | float |
| `PIVOT_M_FIBONACCI_S1_1` | Pivot M Fibonacci S1\|1 | `Pivot.M.Fibonacci.S1\|1` | float |
| `PIVOT_M_FIBONACCI_S1_120` | Pivot M Fibonacci S1\|120 | `Pivot.M.Fibonacci.S1\|120` | float |
| `PIVOT_M_FIBONACCI_S1_15` | Pivot M Fibonacci S1\|15 | `Pivot.M.Fibonacci.S1\|15` | float |
| `PIVOT_M_FIBONACCI_S1_1M` | Pivot M Fibonacci S1\|1M | `Pivot.M.Fibonacci.S1\|1M` | float |
| `PIVOT_M_FIBONACCI_S1_1W` | Pivot M Fibonacci S1\|1W | `Pivot.M.Fibonacci.S1\|1W` | float |
| `PIVOT_M_FIBONACCI_S1_240` | Pivot M Fibonacci S1\|240 | `Pivot.M.Fibonacci.S1\|240` | float |
| `PIVOT_M_FIBONACCI_S1_30` | Pivot M Fibonacci S1\|30 | `Pivot.M.Fibonacci.S1\|30` | float |
| `PIVOT_M_FIBONACCI_S1_5` | Pivot M Fibonacci S1\|5 | `Pivot.M.Fibonacci.S1\|5` | float |
| `PIVOT_M_FIBONACCI_S1_60` | Pivot M Fibonacci S1\|60 | `Pivot.M.Fibonacci.S1\|60` | float |
| `PIVOT_M_FIBONACCI_S2_1` | Pivot M Fibonacci S2\|1 | `Pivot.M.Fibonacci.S2\|1` | float |
| `PIVOT_M_FIBONACCI_S2_120` | Pivot M Fibonacci S2\|120 | `Pivot.M.Fibonacci.S2\|120` | float |
| `PIVOT_M_FIBONACCI_S2_15` | Pivot M Fibonacci S2\|15 | `Pivot.M.Fibonacci.S2\|15` | float |
| `PIVOT_M_FIBONACCI_S2_1M` | Pivot M Fibonacci S2\|1M | `Pivot.M.Fibonacci.S2\|1M` | float |
| `PIVOT_M_FIBONACCI_S2_1W` | Pivot M Fibonacci S2\|1W | `Pivot.M.Fibonacci.S2\|1W` | float |
| `PIVOT_M_FIBONACCI_S2_240` | Pivot M Fibonacci S2\|240 | `Pivot.M.Fibonacci.S2\|240` | float |
| `PIVOT_M_FIBONACCI_S2_30` | Pivot M Fibonacci S2\|30 | `Pivot.M.Fibonacci.S2\|30` | float |
| `PIVOT_M_FIBONACCI_S2_5` | Pivot M Fibonacci S2\|5 | `Pivot.M.Fibonacci.S2\|5` | float |
| `PIVOT_M_FIBONACCI_S2_60` | Pivot M Fibonacci S2\|60 | `Pivot.M.Fibonacci.S2\|60` | float |
| `PIVOT_M_FIBONACCI_S3_1` | Pivot M Fibonacci S3\|1 | `Pivot.M.Fibonacci.S3\|1` | float |
| `PIVOT_M_FIBONACCI_S3_120` | Pivot M Fibonacci S3\|120 | `Pivot.M.Fibonacci.S3\|120` | float |
| `PIVOT_M_FIBONACCI_S3_15` | Pivot M Fibonacci S3\|15 | `Pivot.M.Fibonacci.S3\|15` | float |
| `PIVOT_M_FIBONACCI_S3_1M` | Pivot M Fibonacci S3\|1M | `Pivot.M.Fibonacci.S3\|1M` | float |
| `PIVOT_M_FIBONACCI_S3_1W` | Pivot M Fibonacci S3\|1W | `Pivot.M.Fibonacci.S3\|1W` | float |
| `PIVOT_M_FIBONACCI_S3_240` | Pivot M Fibonacci S3\|240 | `Pivot.M.Fibonacci.S3\|240` | float |
| `PIVOT_M_FIBONACCI_S3_30` | Pivot M Fibonacci S3\|30 | `Pivot.M.Fibonacci.S3\|30` | float |
| `PIVOT_M_FIBONACCI_S3_5` | Pivot M Fibonacci S3\|5 | `Pivot.M.Fibonacci.S3\|5` | float |
| `PIVOT_M_FIBONACCI_S3_60` | Pivot M Fibonacci S3\|60 | `Pivot.M.Fibonacci.S3\|60` | float |
| `RATE_OF_CHANGE_9` | Rate Of Change (9) | `ROC` | round |
| `REC_BBPOWER` | Rec Bbpower | `Rec.BBPower` | rating |
| `REC_BBPOWER_1` | Rec Bbpower\|1 | `Rec.BBPower\|1` | rating |
| `REC_BBPOWER_120` | Rec Bbpower\|120 | `Rec.BBPower\|120` | rating |
| `REC_BBPOWER_15` | Rec Bbpower\|15 | `Rec.BBPower\|15` | rating |
| `REC_BBPOWER_1M` | Rec Bbpower\|1M | `Rec.BBPower\|1M` | rating |
| `REC_BBPOWER_1W` | Rec Bbpower\|1W | `Rec.BBPower\|1W` | rating |
| `REC_BBPOWER_240` | Rec Bbpower\|240 | `Rec.BBPower\|240` | rating |
| `REC_BBPOWER_30` | Rec Bbpower\|30 | `Rec.BBPower\|30` | rating |
| `REC_BBPOWER_5` | Rec Bbpower\|5 | `Rec.BBPower\|5` | rating |
| `REC_BBPOWER_60` | Rec Bbpower\|60 | `Rec.BBPower\|60` | rating |
| `REC_STOCH_RSI` | Rec Stoch RSI | `Rec.Stoch.RSI` | rating |
| `REC_STOCH_RSI_1` | Rec Stoch RSI\|1 | `Rec.Stoch.RSI\|1` | rating |
| `REC_STOCH_RSI_120` | Rec Stoch RSI\|120 | `Rec.Stoch.RSI\|120` | rating |
| `REC_STOCH_RSI_15` | Rec Stoch RSI\|15 | `Rec.Stoch.RSI\|15` | rating |
| `REC_STOCH_RSI_1M` | Rec Stoch RSI\|1M | `Rec.Stoch.RSI\|1M` | rating |
| `REC_STOCH_RSI_1W` | Rec Stoch RSI\|1W | `Rec.Stoch.RSI\|1W` | rating |
| `REC_STOCH_RSI_240` | Rec Stoch RSI\|240 | `Rec.Stoch.RSI\|240` | rating |
| `REC_STOCH_RSI_30` | Rec Stoch RSI\|30 | `Rec.Stoch.RSI\|30` | rating |
| `REC_STOCH_RSI_5` | Rec Stoch RSI\|5 | `Rec.Stoch.RSI\|5` | rating |
| `REC_STOCH_RSI_60` | Rec Stoch RSI\|60 | `Rec.Stoch.RSI\|60` | rating |
| `REC_UO` | Rec UO | `Rec.UO` | rating |
| `REC_UO_1` | Rec UO\|1 | `Rec.UO\|1` | rating |
| `REC_UO_120` | Rec UO\|120 | `Rec.UO\|120` | rating |
| `REC_UO_15` | Rec UO\|15 | `Rec.UO\|15` | rating |
| `REC_UO_1M` | Rec UO\|1M | `Rec.UO\|1M` | rating |
| `REC_UO_1W` | Rec UO\|1W | `Rec.UO\|1W` | rating |
| `REC_UO_240` | Rec UO\|240 | `Rec.UO\|240` | rating |
| `REC_UO_30` | Rec UO\|30 | `Rec.UO\|30` | rating |
| `REC_UO_5` | Rec UO\|5 | `Rec.UO\|5` | rating |
| `REC_UO_60` | Rec UO\|60 | `Rec.UO\|60` | rating |
| `RELATIVE_STRENGTH_INDEX_14` | Relative Strength Index (14) | `RSI` | computed_recommendation |
| `RELATIVE_STRENGTH_INDEX_7` | Relative Strength Index (7) | `RSI7` | computed_recommendation |
| `ROC_1` | Roc\|1 | `ROC\|1` | float |
| `ROC_120` | Roc\|120 | `ROC\|120` | float |
| `ROC_15` | Roc\|15 | `ROC\|15` | float |
| `ROC_1M` | Roc\|1M | `ROC\|1M` | float |
| `ROC_1W` | Roc\|1W | `ROC\|1W` | float |
| `ROC_240` | Roc\|240 | `ROC\|240` | float |
| `ROC_30` | Roc\|30 | `ROC\|30` | float |
| `ROC_5` | Roc\|5 | `ROC\|5` | float |
| `ROC_60` | Roc\|60 | `ROC\|60` | float |
| `RSI10` | Rsi10 | `RSI10` | float |
| `RSI10_1` | Rsi10[1] | `RSI10[1]` | float |
| `RSI10_120` | Rsi10\|120 | `RSI10\|120` | float |
| `RSI10_15` | Rsi10\|15 | `RSI10\|15` | float |
| `RSI10_1M` | Rsi10\|1M | `RSI10\|1M` | float |
| `RSI10_1W` | Rsi10\|1W | `RSI10\|1W` | float |
| `RSI10_1_1` | Rsi10[1]\|1 | `RSI10[1]\|1` | float |
| `RSI10_1_120` | Rsi10[1]\|120 | `RSI10[1]\|120` | float |
| `RSI10_1_15` | Rsi10[1]\|15 | `RSI10[1]\|15` | float |
| `RSI10_1_1M` | Rsi10[1]\|1M | `RSI10[1]\|1M` | float |
| `RSI10_1_1W` | Rsi10[1]\|1W | `RSI10[1]\|1W` | float |
| `RSI10_1_2` | Rsi10\|1 | `RSI10\|1` | float |
| `RSI10_1_240` | Rsi10[1]\|240 | `RSI10[1]\|240` | float |
| `RSI10_1_30` | Rsi10[1]\|30 | `RSI10[1]\|30` | float |
| `RSI10_1_5` | Rsi10[1]\|5 | `RSI10[1]\|5` | float |
| `RSI10_1_60` | Rsi10[1]\|60 | `RSI10[1]\|60` | float |
| `RSI10_240` | Rsi10\|240 | `RSI10\|240` | float |
| `RSI10_30` | Rsi10\|30 | `RSI10\|30` | float |
| `RSI10_5` | Rsi10\|5 | `RSI10\|5` | float |
| `RSI10_60` | Rsi10\|60 | `RSI10\|60` | float |
| `RSI2` | Rsi2 | `RSI2` | float |
| `RSI20` | Rsi20 | `RSI20` | float |
| `RSI20_1` | Rsi20[1] | `RSI20[1]` | float |
| `RSI20_120` | Rsi20\|120 | `RSI20\|120` | float |
| `RSI20_15` | Rsi20\|15 | `RSI20\|15` | float |
| `RSI20_1M` | Rsi20\|1M | `RSI20\|1M` | float |
| `RSI20_1W` | Rsi20\|1W | `RSI20\|1W` | float |
| `RSI20_1_1` | Rsi20[1]\|1 | `RSI20[1]\|1` | float |
| `RSI20_1_120` | Rsi20[1]\|120 | `RSI20[1]\|120` | float |
| `RSI20_1_15` | Rsi20[1]\|15 | `RSI20[1]\|15` | float |
| `RSI20_1_1M` | Rsi20[1]\|1M | `RSI20[1]\|1M` | float |
| `RSI20_1_1W` | Rsi20[1]\|1W | `RSI20[1]\|1W` | float |
| `RSI20_1_2` | Rsi20\|1 | `RSI20\|1` | float |
| `RSI20_1_240` | Rsi20[1]\|240 | `RSI20[1]\|240` | float |
| `RSI20_1_30` | Rsi20[1]\|30 | `RSI20[1]\|30` | float |
| `RSI20_1_5` | Rsi20[1]\|5 | `RSI20[1]\|5` | float |
| `RSI20_1_60` | Rsi20[1]\|60 | `RSI20[1]\|60` | float |
| `RSI20_240` | Rsi20\|240 | `RSI20\|240` | float |
| `RSI20_30` | Rsi20\|30 | `RSI20\|30` | float |
| `RSI20_5` | Rsi20\|5 | `RSI20\|5` | float |
| `RSI20_60` | Rsi20\|60 | `RSI20\|60` | float |
| `RSI21` | Rsi21 | `RSI21` | float |
| `RSI21_1` | Rsi21[1] | `RSI21[1]` | float |
| `RSI21_120` | Rsi21\|120 | `RSI21\|120` | float |
| `RSI21_15` | Rsi21\|15 | `RSI21\|15` | float |
| `RSI21_1M` | Rsi21\|1M | `RSI21\|1M` | float |
| `RSI21_1W` | Rsi21\|1W | `RSI21\|1W` | float |
| `RSI21_1_1` | Rsi21[1]\|1 | `RSI21[1]\|1` | float |
| `RSI21_1_120` | Rsi21[1]\|120 | `RSI21[1]\|120` | float |
| `RSI21_1_15` | Rsi21[1]\|15 | `RSI21[1]\|15` | float |
| `RSI21_1_1M` | Rsi21[1]\|1M | `RSI21[1]\|1M` | float |
| `RSI21_1_1W` | Rsi21[1]\|1W | `RSI21[1]\|1W` | float |
| `RSI21_1_2` | Rsi21\|1 | `RSI21\|1` | float |
| `RSI21_1_240` | Rsi21[1]\|240 | `RSI21[1]\|240` | float |
| `RSI21_1_30` | Rsi21[1]\|30 | `RSI21[1]\|30` | float |
| `RSI21_1_5` | Rsi21[1]\|5 | `RSI21[1]\|5` | float |
| `RSI21_1_60` | Rsi21[1]\|60 | `RSI21[1]\|60` | float |
| `RSI21_240` | Rsi21\|240 | `RSI21\|240` | float |
| `RSI21_30` | Rsi21\|30 | `RSI21\|30` | float |
| `RSI21_5` | Rsi21\|5 | `RSI21\|5` | float |
| `RSI21_60` | Rsi21\|60 | `RSI21\|60` | float |
| `RSI2_1` | Rsi2[1] | `RSI2[1]` | float |
| `RSI2_120` | Rsi2\|120 | `RSI2\|120` | float |
| `RSI2_15` | Rsi2\|15 | `RSI2\|15` | float |
| `RSI2_1M` | Rsi2\|1M | `RSI2\|1M` | float |
| `RSI2_1W` | Rsi2\|1W | `RSI2\|1W` | float |
| `RSI2_1_1` | Rsi2[1]\|1 | `RSI2[1]\|1` | float |
| `RSI2_1_120` | Rsi2[1]\|120 | `RSI2[1]\|120` | float |
| `RSI2_1_15` | Rsi2[1]\|15 | `RSI2[1]\|15` | float |
| `RSI2_1_1M` | Rsi2[1]\|1M | `RSI2[1]\|1M` | float |
| `RSI2_1_1W` | Rsi2[1]\|1W | `RSI2[1]\|1W` | float |
| `RSI2_1_2` | Rsi2\|1 | `RSI2\|1` | float |
| `RSI2_1_240` | Rsi2[1]\|240 | `RSI2[1]\|240` | float |
| `RSI2_1_30` | Rsi2[1]\|30 | `RSI2[1]\|30` | float |
| `RSI2_1_5` | Rsi2[1]\|5 | `RSI2[1]\|5` | float |
| `RSI2_1_60` | Rsi2[1]\|60 | `RSI2[1]\|60` | float |
| `RSI2_240` | Rsi2\|240 | `RSI2\|240` | float |
| `RSI2_30` | Rsi2\|30 | `RSI2\|30` | float |
| `RSI2_5` | Rsi2\|5 | `RSI2\|5` | float |
| `RSI2_60` | Rsi2\|60 | `RSI2\|60` | float |
| `RSI3` | Rsi3 | `RSI3` | float |
| `RSI30` | Rsi30 | `RSI30` | float |
| `RSI30_1` | Rsi30[1] | `RSI30[1]` | float |
| `RSI30_120` | Rsi30\|120 | `RSI30\|120` | float |
| `RSI30_15` | Rsi30\|15 | `RSI30\|15` | float |
| `RSI30_1M` | Rsi30\|1M | `RSI30\|1M` | float |
| `RSI30_1W` | Rsi30\|1W | `RSI30\|1W` | float |
| `RSI30_1_1` | Rsi30[1]\|1 | `RSI30[1]\|1` | float |
| `RSI30_1_120` | Rsi30[1]\|120 | `RSI30[1]\|120` | float |
| `RSI30_1_15` | Rsi30[1]\|15 | `RSI30[1]\|15` | float |
| `RSI30_1_1M` | Rsi30[1]\|1M | `RSI30[1]\|1M` | float |
| `RSI30_1_1W` | Rsi30[1]\|1W | `RSI30[1]\|1W` | float |
| `RSI30_1_2` | Rsi30\|1 | `RSI30\|1` | float |
| `RSI30_1_240` | Rsi30[1]\|240 | `RSI30[1]\|240` | float |
| `RSI30_1_30` | Rsi30[1]\|30 | `RSI30[1]\|30` | float |
| `RSI30_1_5` | Rsi30[1]\|5 | `RSI30[1]\|5` | float |
| `RSI30_1_60` | Rsi30[1]\|60 | `RSI30[1]\|60` | float |
| `RSI30_240` | Rsi30\|240 | `RSI30\|240` | float |
| `RSI30_30` | Rsi30\|30 | `RSI30\|30` | float |
| `RSI30_5` | Rsi30\|5 | `RSI30\|5` | float |
| `RSI30_60` | Rsi30\|60 | `RSI30\|60` | float |
| `RSI3_1` | Rsi3[1] | `RSI3[1]` | float |
| `RSI3_120` | Rsi3\|120 | `RSI3\|120` | float |
| `RSI3_15` | Rsi3\|15 | `RSI3\|15` | float |
| `RSI3_1M` | Rsi3\|1M | `RSI3\|1M` | float |
| `RSI3_1W` | Rsi3\|1W | `RSI3\|1W` | float |
| `RSI3_1_1` | Rsi3[1]\|1 | `RSI3[1]\|1` | float |
| `RSI3_1_120` | Rsi3[1]\|120 | `RSI3[1]\|120` | float |
| `RSI3_1_15` | Rsi3[1]\|15 | `RSI3[1]\|15` | float |
| `RSI3_1_1M` | Rsi3[1]\|1M | `RSI3[1]\|1M` | float |
| `RSI3_1_1W` | Rsi3[1]\|1W | `RSI3[1]\|1W` | float |
| `RSI3_1_2` | Rsi3\|1 | `RSI3\|1` | float |
| `RSI3_1_240` | Rsi3[1]\|240 | `RSI3[1]\|240` | float |
| `RSI3_1_30` | Rsi3[1]\|30 | `RSI3[1]\|30` | float |
| `RSI3_1_5` | Rsi3[1]\|5 | `RSI3[1]\|5` | float |
| `RSI3_1_60` | Rsi3[1]\|60 | `RSI3[1]\|60` | float |
| `RSI3_240` | Rsi3\|240 | `RSI3\|240` | float |
| `RSI3_30` | Rsi3\|30 | `RSI3\|30` | float |
| `RSI3_5` | Rsi3\|5 | `RSI3\|5` | float |
| `RSI3_60` | Rsi3\|60 | `RSI3\|60` | float |
| `RSI4` | Rsi4 | `RSI4` | float |
| `RSI4_1` | Rsi4[1] | `RSI4[1]` | float |
| `RSI4_120` | Rsi4\|120 | `RSI4\|120` | float |
| `RSI4_15` | Rsi4\|15 | `RSI4\|15` | float |
| `RSI4_1M` | Rsi4\|1M | `RSI4\|1M` | float |
| `RSI4_1W` | Rsi4\|1W | `RSI4\|1W` | float |
| `RSI4_1_1` | Rsi4[1]\|1 | `RSI4[1]\|1` | float |
| `RSI4_1_120` | Rsi4[1]\|120 | `RSI4[1]\|120` | float |
| `RSI4_1_15` | Rsi4[1]\|15 | `RSI4[1]\|15` | float |
| `RSI4_1_1M` | Rsi4[1]\|1M | `RSI4[1]\|1M` | float |
| `RSI4_1_1W` | Rsi4[1]\|1W | `RSI4[1]\|1W` | float |
| `RSI4_1_2` | Rsi4\|1 | `RSI4\|1` | float |
| `RSI4_1_240` | Rsi4[1]\|240 | `RSI4[1]\|240` | float |
| `RSI4_1_30` | Rsi4[1]\|30 | `RSI4[1]\|30` | float |
| `RSI4_1_5` | Rsi4[1]\|5 | `RSI4[1]\|5` | float |
| `RSI4_1_60` | Rsi4[1]\|60 | `RSI4[1]\|60` | float |
| `RSI4_240` | Rsi4\|240 | `RSI4\|240` | float |
| `RSI4_30` | Rsi4\|30 | `RSI4\|30` | float |
| `RSI4_5` | Rsi4\|5 | `RSI4\|5` | float |
| `RSI4_60` | Rsi4\|60 | `RSI4\|60` | float |
| `RSI5` | Rsi5 | `RSI5` | float |
| `RSI5_1` | Rsi5[1] | `RSI5[1]` | float |
| `RSI5_120` | Rsi5\|120 | `RSI5\|120` | float |
| `RSI5_15` | Rsi5\|15 | `RSI5\|15` | float |
| `RSI5_1M` | Rsi5\|1M | `RSI5\|1M` | float |
| `RSI5_1W` | Rsi5\|1W | `RSI5\|1W` | float |
| `RSI5_1_1` | Rsi5[1]\|1 | `RSI5[1]\|1` | float |
| `RSI5_1_120` | Rsi5[1]\|120 | `RSI5[1]\|120` | float |
| `RSI5_1_15` | Rsi5[1]\|15 | `RSI5[1]\|15` | float |
| `RSI5_1_1M` | Rsi5[1]\|1M | `RSI5[1]\|1M` | float |
| `RSI5_1_1W` | Rsi5[1]\|1W | `RSI5[1]\|1W` | float |
| `RSI5_1_2` | Rsi5\|1 | `RSI5\|1` | float |
| `RSI5_1_240` | Rsi5[1]\|240 | `RSI5[1]\|240` | float |
| `RSI5_1_30` | Rsi5[1]\|30 | `RSI5[1]\|30` | float |
| `RSI5_1_5` | Rsi5[1]\|5 | `RSI5[1]\|5` | float |
| `RSI5_1_60` | Rsi5[1]\|60 | `RSI5[1]\|60` | float |
| `RSI5_240` | Rsi5\|240 | `RSI5\|240` | float |
| `RSI5_30` | Rsi5\|30 | `RSI5\|30` | float |
| `RSI5_5` | Rsi5\|5 | `RSI5\|5` | float |
| `RSI5_60` | Rsi5\|60 | `RSI5\|60` | float |
| `RSI7_1` | Rsi7[1] | `RSI7[1]` | float |
| `RSI7_120` | Rsi7\|120 | `RSI7\|120` | float |
| `RSI7_15` | Rsi7\|15 | `RSI7\|15` | float |
| `RSI7_1M` | Rsi7\|1M | `RSI7\|1M` | float |
| `RSI7_1W` | Rsi7\|1W | `RSI7\|1W` | float |
| `RSI7_1_1` | Rsi7[1]\|1 | `RSI7[1]\|1` | float |
| `RSI7_1_120` | Rsi7[1]\|120 | `RSI7[1]\|120` | float |
| `RSI7_1_15` | Rsi7[1]\|15 | `RSI7[1]\|15` | float |
| `RSI7_1_1M` | Rsi7[1]\|1M | `RSI7[1]\|1M` | float |
| `RSI7_1_1W` | Rsi7[1]\|1W | `RSI7[1]\|1W` | float |
| `RSI7_1_2` | Rsi7\|1 | `RSI7\|1` | float |
| `RSI7_1_240` | Rsi7[1]\|240 | `RSI7[1]\|240` | float |
| `RSI7_1_30` | Rsi7[1]\|30 | `RSI7[1]\|30` | float |
| `RSI7_1_5` | Rsi7[1]\|5 | `RSI7[1]\|5` | float |
| `RSI7_1_60` | Rsi7[1]\|60 | `RSI7[1]\|60` | float |
| `RSI7_240` | Rsi7\|240 | `RSI7\|240` | float |
| `RSI7_30` | Rsi7\|30 | `RSI7\|30` | float |
| `RSI7_5` | Rsi7\|5 | `RSI7\|5` | float |
| `RSI7_60` | Rsi7\|60 | `RSI7\|60` | float |
| `RSI9` | Rsi9 | `RSI9` | float |
| `RSI9_1` | Rsi9[1] | `RSI9[1]` | float |
| `RSI9_120` | Rsi9\|120 | `RSI9\|120` | float |
| `RSI9_15` | Rsi9\|15 | `RSI9\|15` | float |
| `RSI9_1M` | Rsi9\|1M | `RSI9\|1M` | float |
| `RSI9_1W` | Rsi9\|1W | `RSI9\|1W` | float |
| `RSI9_1_1` | Rsi9[1]\|1 | `RSI9[1]\|1` | float |
| `RSI9_1_120` | Rsi9[1]\|120 | `RSI9[1]\|120` | float |
| `RSI9_1_15` | Rsi9[1]\|15 | `RSI9[1]\|15` | float |
| `RSI9_1_1M` | Rsi9[1]\|1M | `RSI9[1]\|1M` | float |
| `RSI9_1_1W` | Rsi9[1]\|1W | `RSI9[1]\|1W` | float |
| `RSI9_1_2` | Rsi9\|1 | `RSI9\|1` | float |
| `RSI9_1_240` | Rsi9[1]\|240 | `RSI9[1]\|240` | float |
| `RSI9_1_30` | Rsi9[1]\|30 | `RSI9[1]\|30` | float |
| `RSI9_1_5` | Rsi9[1]\|5 | `RSI9[1]\|5` | float |
| `RSI9_1_60` | Rsi9[1]\|60 | `RSI9[1]\|60` | float |
| `RSI9_240` | Rsi9\|240 | `RSI9\|240` | float |
| `RSI9_30` | Rsi9\|30 | `RSI9\|30` | float |
| `RSI9_5` | Rsi9\|5 | `RSI9\|5` | float |
| `RSI9_60` | Rsi9\|60 | `RSI9\|60` | float |
| `RSI_1` | RSI[1] | `RSI[1]` | float |
| `RSI_120` | RSI\|120 | `RSI\|120` | float |
| `RSI_15` | RSI\|15 | `RSI\|15` | float |
| `RSI_1M` | RSI\|1M | `RSI\|1M` | float |
| `RSI_1W` | RSI\|1W | `RSI\|1W` | float |
| `RSI_1_1` | RSI[1]\|1 | `RSI[1]\|1` | float |
| `RSI_1_120` | RSI[1]\|120 | `RSI[1]\|120` | float |
| `RSI_1_15` | RSI[1]\|15 | `RSI[1]\|15` | float |
| `RSI_1_1M` | RSI[1]\|1M | `RSI[1]\|1M` | float |
| `RSI_1_1W` | RSI[1]\|1W | `RSI[1]\|1W` | float |
| `RSI_1_2` | RSI\|1 | `RSI\|1` | float |
| `RSI_1_240` | RSI[1]\|240 | `RSI[1]\|240` | float |
| `RSI_1_30` | RSI[1]\|30 | `RSI[1]\|30` | float |
| `RSI_1_5` | RSI[1]\|5 | `RSI[1]\|5` | float |
| `RSI_1_60` | RSI[1]\|60 | `RSI[1]\|60` | float |
| `RSI_240` | RSI\|240 | `RSI\|240` | float |
| `RSI_30` | RSI\|30 | `RSI\|30` | float |
| `RSI_5` | RSI\|5 | `RSI\|5` | float |
| `RSI_60` | RSI\|60 | `RSI\|60` | float |
| `STOCHASTIC_PERCENTD_14_3_3` | Stochastic %D (14, 3, 3) | `Stoch.D` | round |
| `STOCHASTIC_PERCENTK_14_3_3` | Stochastic %K (14, 3, 3) | `Stoch.K` | computed_recommendation |
| `STOCHASTIC_RSI_FAST_3_3_14_14` | Stochastic RSI Fast (3, 3, 14, 14) | `Stoch.RSI.K` | computed_recommendation |
| `STOCHASTIC_RSI_SLOW_3_3_14_14` | Stochastic RSI Slow (3, 3, 14, 14) | `Stoch.RSI.D` | round |
| `STOCH_D_1` | Stoch D[1] | `Stoch.D[1]` | float |
| `STOCH_D_120` | Stoch D\|120 | `Stoch.D\|120` | float |
| `STOCH_D_14_1_3` | Stoch D 14 1 3 | `Stoch.D_14_1_3` | float |
| `STOCH_D_14_1_3_1` | Stoch D 14 1 3[1] | `Stoch.D_14_1_3[1]` | float |
| `STOCH_D_14_1_3_120` | Stoch D 14 1 3\|120 | `Stoch.D_14_1_3\|120` | float |
| `STOCH_D_14_1_3_15` | Stoch D 14 1 3\|15 | `Stoch.D_14_1_3\|15` | float |
| `STOCH_D_14_1_3_1M` | Stoch D 14 1 3\|1M | `Stoch.D_14_1_3\|1M` | float |
| `STOCH_D_14_1_3_1W` | Stoch D 14 1 3\|1W | `Stoch.D_14_1_3\|1W` | float |
| `STOCH_D_14_1_3_1_1` | Stoch D 14 1 3[1]\|1 | `Stoch.D_14_1_3[1]\|1` | float |
| `STOCH_D_14_1_3_1_120` | Stoch D 14 1 3[1]\|120 | `Stoch.D_14_1_3[1]\|120` | float |
| `STOCH_D_14_1_3_1_15` | Stoch D 14 1 3[1]\|15 | `Stoch.D_14_1_3[1]\|15` | float |
| `STOCH_D_14_1_3_1_1M` | Stoch D 14 1 3[1]\|1M | `Stoch.D_14_1_3[1]\|1M` | float |
| `STOCH_D_14_1_3_1_1W` | Stoch D 14 1 3[1]\|1W | `Stoch.D_14_1_3[1]\|1W` | float |
| `STOCH_D_14_1_3_1_2` | Stoch D 14 1 3\|1 | `Stoch.D_14_1_3\|1` | float |
| `STOCH_D_14_1_3_1_240` | Stoch D 14 1 3[1]\|240 | `Stoch.D_14_1_3[1]\|240` | float |
| `STOCH_D_14_1_3_1_30` | Stoch D 14 1 3[1]\|30 | `Stoch.D_14_1_3[1]\|30` | float |
| `STOCH_D_14_1_3_1_5` | Stoch D 14 1 3[1]\|5 | `Stoch.D_14_1_3[1]\|5` | float |
| `STOCH_D_14_1_3_1_60` | Stoch D 14 1 3[1]\|60 | `Stoch.D_14_1_3[1]\|60` | float |
| `STOCH_D_14_1_3_240` | Stoch D 14 1 3\|240 | `Stoch.D_14_1_3\|240` | float |
| `STOCH_D_14_1_3_30` | Stoch D 14 1 3\|30 | `Stoch.D_14_1_3\|30` | float |
| `STOCH_D_14_1_3_5` | Stoch D 14 1 3\|5 | `Stoch.D_14_1_3\|5` | float |
| `STOCH_D_14_1_3_60` | Stoch D 14 1 3\|60 | `Stoch.D_14_1_3\|60` | float |
| `STOCH_D_15` | Stoch D\|15 | `Stoch.D\|15` | float |
| `STOCH_D_1M` | Stoch D\|1M | `Stoch.D\|1M` | float |
| `STOCH_D_1W` | Stoch D\|1W | `Stoch.D\|1W` | float |
| `STOCH_D_1_1` | Stoch D[1]\|1 | `Stoch.D[1]\|1` | float |
| `STOCH_D_1_120` | Stoch D[1]\|120 | `Stoch.D[1]\|120` | float |
| `STOCH_D_1_15` | Stoch D[1]\|15 | `Stoch.D[1]\|15` | float |
| `STOCH_D_1_1M` | Stoch D[1]\|1M | `Stoch.D[1]\|1M` | float |
| `STOCH_D_1_1W` | Stoch D[1]\|1W | `Stoch.D[1]\|1W` | float |
| `STOCH_D_1_2` | Stoch D\|1 | `Stoch.D\|1` | float |
| `STOCH_D_1_240` | Stoch D[1]\|240 | `Stoch.D[1]\|240` | float |
| `STOCH_D_1_30` | Stoch D[1]\|30 | `Stoch.D[1]\|30` | float |
| `STOCH_D_1_5` | Stoch D[1]\|5 | `Stoch.D[1]\|5` | float |
| `STOCH_D_1_60` | Stoch D[1]\|60 | `Stoch.D[1]\|60` | float |
| `STOCH_D_240` | Stoch D\|240 | `Stoch.D\|240` | float |
| `STOCH_D_30` | Stoch D\|30 | `Stoch.D\|30` | float |
| `STOCH_D_5` | Stoch D\|5 | `Stoch.D\|5` | float |
| `STOCH_D_5_3_3` | Stoch D 5 3 3 | `Stoch.D_5_3_3` | float |
| `STOCH_D_5_3_3_1` | Stoch D 5 3 3[1] | `Stoch.D_5_3_3[1]` | float |
| `STOCH_D_5_3_3_120` | Stoch D 5 3 3\|120 | `Stoch.D_5_3_3\|120` | float |
| `STOCH_D_5_3_3_15` | Stoch D 5 3 3\|15 | `Stoch.D_5_3_3\|15` | float |
| `STOCH_D_5_3_3_1M` | Stoch D 5 3 3\|1M | `Stoch.D_5_3_3\|1M` | float |
| `STOCH_D_5_3_3_1W` | Stoch D 5 3 3\|1W | `Stoch.D_5_3_3\|1W` | float |
| `STOCH_D_5_3_3_1_1` | Stoch D 5 3 3[1]\|1 | `Stoch.D_5_3_3[1]\|1` | float |
| `STOCH_D_5_3_3_1_120` | Stoch D 5 3 3[1]\|120 | `Stoch.D_5_3_3[1]\|120` | float |
| `STOCH_D_5_3_3_1_15` | Stoch D 5 3 3[1]\|15 | `Stoch.D_5_3_3[1]\|15` | float |
| `STOCH_D_5_3_3_1_1M` | Stoch D 5 3 3[1]\|1M | `Stoch.D_5_3_3[1]\|1M` | float |
| `STOCH_D_5_3_3_1_1W` | Stoch D 5 3 3[1]\|1W | `Stoch.D_5_3_3[1]\|1W` | float |
| `STOCH_D_5_3_3_1_2` | Stoch D 5 3 3\|1 | `Stoch.D_5_3_3\|1` | float |
| `STOCH_D_5_3_3_1_240` | Stoch D 5 3 3[1]\|240 | `Stoch.D_5_3_3[1]\|240` | float |
| `STOCH_D_5_3_3_1_30` | Stoch D 5 3 3[1]\|30 | `Stoch.D_5_3_3[1]\|30` | float |
| `STOCH_D_5_3_3_1_5` | Stoch D 5 3 3[1]\|5 | `Stoch.D_5_3_3[1]\|5` | float |
| `STOCH_D_5_3_3_1_60` | Stoch D 5 3 3[1]\|60 | `Stoch.D_5_3_3[1]\|60` | float |
| `STOCH_D_5_3_3_240` | Stoch D 5 3 3\|240 | `Stoch.D_5_3_3\|240` | float |
| `STOCH_D_5_3_3_30` | Stoch D 5 3 3\|30 | `Stoch.D_5_3_3\|30` | float |
| `STOCH_D_5_3_3_5` | Stoch D 5 3 3\|5 | `Stoch.D_5_3_3\|5` | float |
| `STOCH_D_5_3_3_60` | Stoch D 5 3 3\|60 | `Stoch.D_5_3_3\|60` | float |
| `STOCH_D_60` | Stoch D\|60 | `Stoch.D\|60` | float |
| `STOCH_D_6_3_3` | Stoch D 6 3 3 | `Stoch.D_6_3_3` | float |
| `STOCH_D_6_3_3_1` | Stoch D 6 3 3[1] | `Stoch.D_6_3_3[1]` | float |
| `STOCH_D_6_3_3_120` | Stoch D 6 3 3\|120 | `Stoch.D_6_3_3\|120` | float |
| `STOCH_D_6_3_3_15` | Stoch D 6 3 3\|15 | `Stoch.D_6_3_3\|15` | float |
| `STOCH_D_6_3_3_1M` | Stoch D 6 3 3\|1M | `Stoch.D_6_3_3\|1M` | float |
| `STOCH_D_6_3_3_1W` | Stoch D 6 3 3\|1W | `Stoch.D_6_3_3\|1W` | float |
| `STOCH_D_6_3_3_1_1` | Stoch D 6 3 3[1]\|1 | `Stoch.D_6_3_3[1]\|1` | float |
| `STOCH_D_6_3_3_1_120` | Stoch D 6 3 3[1]\|120 | `Stoch.D_6_3_3[1]\|120` | float |
| `STOCH_D_6_3_3_1_15` | Stoch D 6 3 3[1]\|15 | `Stoch.D_6_3_3[1]\|15` | float |
| `STOCH_D_6_3_3_1_1M` | Stoch D 6 3 3[1]\|1M | `Stoch.D_6_3_3[1]\|1M` | float |
| `STOCH_D_6_3_3_1_1W` | Stoch D 6 3 3[1]\|1W | `Stoch.D_6_3_3[1]\|1W` | float |
| `STOCH_D_6_3_3_1_2` | Stoch D 6 3 3\|1 | `Stoch.D_6_3_3\|1` | float |
| `STOCH_D_6_3_3_1_240` | Stoch D 6 3 3[1]\|240 | `Stoch.D_6_3_3[1]\|240` | float |
| `STOCH_D_6_3_3_1_30` | Stoch D 6 3 3[1]\|30 | `Stoch.D_6_3_3[1]\|30` | float |
| `STOCH_D_6_3_3_1_5` | Stoch D 6 3 3[1]\|5 | `Stoch.D_6_3_3[1]\|5` | float |
| `STOCH_D_6_3_3_1_60` | Stoch D 6 3 3[1]\|60 | `Stoch.D_6_3_3[1]\|60` | float |
| `STOCH_D_6_3_3_240` | Stoch D 6 3 3\|240 | `Stoch.D_6_3_3\|240` | float |
| `STOCH_D_6_3_3_30` | Stoch D 6 3 3\|30 | `Stoch.D_6_3_3\|30` | float |
| `STOCH_D_6_3_3_5` | Stoch D 6 3 3\|5 | `Stoch.D_6_3_3\|5` | float |
| `STOCH_D_6_3_3_60` | Stoch D 6 3 3\|60 | `Stoch.D_6_3_3\|60` | float |
| `STOCH_D_8_3_3` | Stoch D 8 3 3 | `Stoch.D_8_3_3` | float |
| `STOCH_D_8_3_3_1` | Stoch D 8 3 3[1] | `Stoch.D_8_3_3[1]` | float |
| `STOCH_D_8_3_3_120` | Stoch D 8 3 3\|120 | `Stoch.D_8_3_3\|120` | float |
| `STOCH_D_8_3_3_15` | Stoch D 8 3 3\|15 | `Stoch.D_8_3_3\|15` | float |
| `STOCH_D_8_3_3_1M` | Stoch D 8 3 3\|1M | `Stoch.D_8_3_3\|1M` | float |
| `STOCH_D_8_3_3_1W` | Stoch D 8 3 3\|1W | `Stoch.D_8_3_3\|1W` | float |
| `STOCH_D_8_3_3_1_1` | Stoch D 8 3 3[1]\|1 | `Stoch.D_8_3_3[1]\|1` | float |
| `STOCH_D_8_3_3_1_120` | Stoch D 8 3 3[1]\|120 | `Stoch.D_8_3_3[1]\|120` | float |
| `STOCH_D_8_3_3_1_15` | Stoch D 8 3 3[1]\|15 | `Stoch.D_8_3_3[1]\|15` | float |
| `STOCH_D_8_3_3_1_1M` | Stoch D 8 3 3[1]\|1M | `Stoch.D_8_3_3[1]\|1M` | float |
| `STOCH_D_8_3_3_1_1W` | Stoch D 8 3 3[1]\|1W | `Stoch.D_8_3_3[1]\|1W` | float |
| `STOCH_D_8_3_3_1_2` | Stoch D 8 3 3\|1 | `Stoch.D_8_3_3\|1` | float |
| `STOCH_D_8_3_3_1_240` | Stoch D 8 3 3[1]\|240 | `Stoch.D_8_3_3[1]\|240` | float |
| `STOCH_D_8_3_3_1_30` | Stoch D 8 3 3[1]\|30 | `Stoch.D_8_3_3[1]\|30` | float |
| `STOCH_D_8_3_3_1_5` | Stoch D 8 3 3[1]\|5 | `Stoch.D_8_3_3[1]\|5` | float |
| `STOCH_D_8_3_3_1_60` | Stoch D 8 3 3[1]\|60 | `Stoch.D_8_3_3[1]\|60` | float |
| `STOCH_D_8_3_3_240` | Stoch D 8 3 3\|240 | `Stoch.D_8_3_3\|240` | float |
| `STOCH_D_8_3_3_30` | Stoch D 8 3 3\|30 | `Stoch.D_8_3_3\|30` | float |
| `STOCH_D_8_3_3_5` | Stoch D 8 3 3\|5 | `Stoch.D_8_3_3\|5` | float |
| `STOCH_D_8_3_3_60` | Stoch D 8 3 3\|60 | `Stoch.D_8_3_3\|60` | float |
| `STOCH_K_1` | Stoch K[1] | `Stoch.K[1]` | float |
| `STOCH_K_120` | Stoch K\|120 | `Stoch.K\|120` | float |
| `STOCH_K_14_1_3` | Stoch K 14 1 3 | `Stoch.K_14_1_3` | float |
| `STOCH_K_14_1_3_1` | Stoch K 14 1 3[1] | `Stoch.K_14_1_3[1]` | float |
| `STOCH_K_14_1_3_120` | Stoch K 14 1 3\|120 | `Stoch.K_14_1_3\|120` | float |
| `STOCH_K_14_1_3_15` | Stoch K 14 1 3\|15 | `Stoch.K_14_1_3\|15` | float |
| `STOCH_K_14_1_3_1M` | Stoch K 14 1 3\|1M | `Stoch.K_14_1_3\|1M` | float |
| `STOCH_K_14_1_3_1W` | Stoch K 14 1 3\|1W | `Stoch.K_14_1_3\|1W` | float |
| `STOCH_K_14_1_3_1_1` | Stoch K 14 1 3[1]\|1 | `Stoch.K_14_1_3[1]\|1` | float |
| `STOCH_K_14_1_3_1_120` | Stoch K 14 1 3[1]\|120 | `Stoch.K_14_1_3[1]\|120` | float |
| `STOCH_K_14_1_3_1_15` | Stoch K 14 1 3[1]\|15 | `Stoch.K_14_1_3[1]\|15` | float |
| `STOCH_K_14_1_3_1_1M` | Stoch K 14 1 3[1]\|1M | `Stoch.K_14_1_3[1]\|1M` | float |
| `STOCH_K_14_1_3_1_1W` | Stoch K 14 1 3[1]\|1W | `Stoch.K_14_1_3[1]\|1W` | float |
| `STOCH_K_14_1_3_1_2` | Stoch K 14 1 3\|1 | `Stoch.K_14_1_3\|1` | float |
| `STOCH_K_14_1_3_1_240` | Stoch K 14 1 3[1]\|240 | `Stoch.K_14_1_3[1]\|240` | float |
| `STOCH_K_14_1_3_1_30` | Stoch K 14 1 3[1]\|30 | `Stoch.K_14_1_3[1]\|30` | float |
| `STOCH_K_14_1_3_1_5` | Stoch K 14 1 3[1]\|5 | `Stoch.K_14_1_3[1]\|5` | float |
| `STOCH_K_14_1_3_1_60` | Stoch K 14 1 3[1]\|60 | `Stoch.K_14_1_3[1]\|60` | float |
| `STOCH_K_14_1_3_240` | Stoch K 14 1 3\|240 | `Stoch.K_14_1_3\|240` | float |
| `STOCH_K_14_1_3_30` | Stoch K 14 1 3\|30 | `Stoch.K_14_1_3\|30` | float |
| `STOCH_K_14_1_3_5` | Stoch K 14 1 3\|5 | `Stoch.K_14_1_3\|5` | float |
| `STOCH_K_14_1_3_60` | Stoch K 14 1 3\|60 | `Stoch.K_14_1_3\|60` | float |
| `STOCH_K_15` | Stoch K\|15 | `Stoch.K\|15` | float |
| `STOCH_K_1M` | Stoch K\|1M | `Stoch.K\|1M` | float |
| `STOCH_K_1W` | Stoch K\|1W | `Stoch.K\|1W` | float |
| `STOCH_K_1_1` | Stoch K[1]\|1 | `Stoch.K[1]\|1` | float |
| `STOCH_K_1_120` | Stoch K[1]\|120 | `Stoch.K[1]\|120` | float |
| `STOCH_K_1_15` | Stoch K[1]\|15 | `Stoch.K[1]\|15` | float |
| `STOCH_K_1_1M` | Stoch K[1]\|1M | `Stoch.K[1]\|1M` | float |
| `STOCH_K_1_1W` | Stoch K[1]\|1W | `Stoch.K[1]\|1W` | float |
| `STOCH_K_1_2` | Stoch K\|1 | `Stoch.K\|1` | float |
| `STOCH_K_1_240` | Stoch K[1]\|240 | `Stoch.K[1]\|240` | float |
| `STOCH_K_1_30` | Stoch K[1]\|30 | `Stoch.K[1]\|30` | float |
| `STOCH_K_1_5` | Stoch K[1]\|5 | `Stoch.K[1]\|5` | float |
| `STOCH_K_1_60` | Stoch K[1]\|60 | `Stoch.K[1]\|60` | float |
| `STOCH_K_240` | Stoch K\|240 | `Stoch.K\|240` | float |
| `STOCH_K_30` | Stoch K\|30 | `Stoch.K\|30` | float |
| `STOCH_K_5` | Stoch K\|5 | `Stoch.K\|5` | float |
| `STOCH_K_5_3_3` | Stoch K 5 3 3 | `Stoch.K_5_3_3` | float |
| `STOCH_K_5_3_3_1` | Stoch K 5 3 3[1] | `Stoch.K_5_3_3[1]` | float |
| `STOCH_K_5_3_3_120` | Stoch K 5 3 3\|120 | `Stoch.K_5_3_3\|120` | float |
| `STOCH_K_5_3_3_15` | Stoch K 5 3 3\|15 | `Stoch.K_5_3_3\|15` | float |
| `STOCH_K_5_3_3_1M` | Stoch K 5 3 3\|1M | `Stoch.K_5_3_3\|1M` | float |
| `STOCH_K_5_3_3_1W` | Stoch K 5 3 3\|1W | `Stoch.K_5_3_3\|1W` | float |
| `STOCH_K_5_3_3_1_1` | Stoch K 5 3 3[1]\|1 | `Stoch.K_5_3_3[1]\|1` | float |
| `STOCH_K_5_3_3_1_120` | Stoch K 5 3 3[1]\|120 | `Stoch.K_5_3_3[1]\|120` | float |
| `STOCH_K_5_3_3_1_15` | Stoch K 5 3 3[1]\|15 | `Stoch.K_5_3_3[1]\|15` | float |
| `STOCH_K_5_3_3_1_1M` | Stoch K 5 3 3[1]\|1M | `Stoch.K_5_3_3[1]\|1M` | float |
| `STOCH_K_5_3_3_1_1W` | Stoch K 5 3 3[1]\|1W | `Stoch.K_5_3_3[1]\|1W` | float |
| `STOCH_K_5_3_3_1_2` | Stoch K 5 3 3\|1 | `Stoch.K_5_3_3\|1` | float |
| `STOCH_K_5_3_3_1_240` | Stoch K 5 3 3[1]\|240 | `Stoch.K_5_3_3[1]\|240` | float |
| `STOCH_K_5_3_3_1_30` | Stoch K 5 3 3[1]\|30 | `Stoch.K_5_3_3[1]\|30` | float |
| `STOCH_K_5_3_3_1_5` | Stoch K 5 3 3[1]\|5 | `Stoch.K_5_3_3[1]\|5` | float |
| `STOCH_K_5_3_3_1_60` | Stoch K 5 3 3[1]\|60 | `Stoch.K_5_3_3[1]\|60` | float |
| `STOCH_K_5_3_3_240` | Stoch K 5 3 3\|240 | `Stoch.K_5_3_3\|240` | float |
| `STOCH_K_5_3_3_30` | Stoch K 5 3 3\|30 | `Stoch.K_5_3_3\|30` | float |
| `STOCH_K_5_3_3_5` | Stoch K 5 3 3\|5 | `Stoch.K_5_3_3\|5` | float |
| `STOCH_K_5_3_3_60` | Stoch K 5 3 3\|60 | `Stoch.K_5_3_3\|60` | float |
| `STOCH_K_60` | Stoch K\|60 | `Stoch.K\|60` | float |
| `STOCH_K_6_3_3` | Stoch K 6 3 3 | `Stoch.K_6_3_3` | float |
| `STOCH_K_6_3_3_1` | Stoch K 6 3 3[1] | `Stoch.K_6_3_3[1]` | float |
| `STOCH_K_6_3_3_120` | Stoch K 6 3 3\|120 | `Stoch.K_6_3_3\|120` | float |
| `STOCH_K_6_3_3_15` | Stoch K 6 3 3\|15 | `Stoch.K_6_3_3\|15` | float |
| `STOCH_K_6_3_3_1M` | Stoch K 6 3 3\|1M | `Stoch.K_6_3_3\|1M` | float |
| `STOCH_K_6_3_3_1W` | Stoch K 6 3 3\|1W | `Stoch.K_6_3_3\|1W` | float |
| `STOCH_K_6_3_3_1_1` | Stoch K 6 3 3[1]\|1 | `Stoch.K_6_3_3[1]\|1` | float |
| `STOCH_K_6_3_3_1_120` | Stoch K 6 3 3[1]\|120 | `Stoch.K_6_3_3[1]\|120` | float |
| `STOCH_K_6_3_3_1_15` | Stoch K 6 3 3[1]\|15 | `Stoch.K_6_3_3[1]\|15` | float |
| `STOCH_K_6_3_3_1_1M` | Stoch K 6 3 3[1]\|1M | `Stoch.K_6_3_3[1]\|1M` | float |
| `STOCH_K_6_3_3_1_1W` | Stoch K 6 3 3[1]\|1W | `Stoch.K_6_3_3[1]\|1W` | float |
| `STOCH_K_6_3_3_1_2` | Stoch K 6 3 3\|1 | `Stoch.K_6_3_3\|1` | float |
| `STOCH_K_6_3_3_1_240` | Stoch K 6 3 3[1]\|240 | `Stoch.K_6_3_3[1]\|240` | float |
| `STOCH_K_6_3_3_1_30` | Stoch K 6 3 3[1]\|30 | `Stoch.K_6_3_3[1]\|30` | float |
| `STOCH_K_6_3_3_1_5` | Stoch K 6 3 3[1]\|5 | `Stoch.K_6_3_3[1]\|5` | float |
| `STOCH_K_6_3_3_1_60` | Stoch K 6 3 3[1]\|60 | `Stoch.K_6_3_3[1]\|60` | float |
| `STOCH_K_6_3_3_240` | Stoch K 6 3 3\|240 | `Stoch.K_6_3_3\|240` | float |
| `STOCH_K_6_3_3_30` | Stoch K 6 3 3\|30 | `Stoch.K_6_3_3\|30` | float |
| `STOCH_K_6_3_3_5` | Stoch K 6 3 3\|5 | `Stoch.K_6_3_3\|5` | float |
| `STOCH_K_6_3_3_60` | Stoch K 6 3 3\|60 | `Stoch.K_6_3_3\|60` | float |
| `STOCH_K_8_3_3` | Stoch K 8 3 3 | `Stoch.K_8_3_3` | float |
| `STOCH_K_8_3_3_1` | Stoch K 8 3 3[1] | `Stoch.K_8_3_3[1]` | float |
| `STOCH_K_8_3_3_120` | Stoch K 8 3 3\|120 | `Stoch.K_8_3_3\|120` | float |
| `STOCH_K_8_3_3_15` | Stoch K 8 3 3\|15 | `Stoch.K_8_3_3\|15` | float |
| `STOCH_K_8_3_3_1M` | Stoch K 8 3 3\|1M | `Stoch.K_8_3_3\|1M` | float |
| `STOCH_K_8_3_3_1W` | Stoch K 8 3 3\|1W | `Stoch.K_8_3_3\|1W` | float |
| `STOCH_K_8_3_3_1_1` | Stoch K 8 3 3[1]\|1 | `Stoch.K_8_3_3[1]\|1` | float |
| `STOCH_K_8_3_3_1_120` | Stoch K 8 3 3[1]\|120 | `Stoch.K_8_3_3[1]\|120` | float |
| `STOCH_K_8_3_3_1_15` | Stoch K 8 3 3[1]\|15 | `Stoch.K_8_3_3[1]\|15` | float |
| `STOCH_K_8_3_3_1_1M` | Stoch K 8 3 3[1]\|1M | `Stoch.K_8_3_3[1]\|1M` | float |
| `STOCH_K_8_3_3_1_1W` | Stoch K 8 3 3[1]\|1W | `Stoch.K_8_3_3[1]\|1W` | float |
| `STOCH_K_8_3_3_1_2` | Stoch K 8 3 3\|1 | `Stoch.K_8_3_3\|1` | float |
| `STOCH_K_8_3_3_1_240` | Stoch K 8 3 3[1]\|240 | `Stoch.K_8_3_3[1]\|240` | float |
| `STOCH_K_8_3_3_1_30` | Stoch K 8 3 3[1]\|30 | `Stoch.K_8_3_3[1]\|30` | float |
| `STOCH_K_8_3_3_1_5` | Stoch K 8 3 3[1]\|5 | `Stoch.K_8_3_3[1]\|5` | float |
| `STOCH_K_8_3_3_1_60` | Stoch K 8 3 3[1]\|60 | `Stoch.K_8_3_3[1]\|60` | float |
| `STOCH_K_8_3_3_240` | Stoch K 8 3 3\|240 | `Stoch.K_8_3_3\|240` | float |
| `STOCH_K_8_3_3_30` | Stoch K 8 3 3\|30 | `Stoch.K_8_3_3\|30` | float |
| `STOCH_K_8_3_3_5` | Stoch K 8 3 3\|5 | `Stoch.K_8_3_3\|5` | float |
| `STOCH_K_8_3_3_60` | Stoch K 8 3 3\|60 | `Stoch.K_8_3_3\|60` | float |
| `STOCH_RSI_D_1` | Stoch RSI D\|1 | `Stoch.RSI.D\|1` | float |
| `STOCH_RSI_D_120` | Stoch RSI D\|120 | `Stoch.RSI.D\|120` | float |
| `STOCH_RSI_D_15` | Stoch RSI D\|15 | `Stoch.RSI.D\|15` | float |
| `STOCH_RSI_D_1M` | Stoch RSI D\|1M | `Stoch.RSI.D\|1M` | float |
| `STOCH_RSI_D_1W` | Stoch RSI D\|1W | `Stoch.RSI.D\|1W` | float |
| `STOCH_RSI_D_240` | Stoch RSI D\|240 | `Stoch.RSI.D\|240` | float |
| `STOCH_RSI_D_30` | Stoch RSI D\|30 | `Stoch.RSI.D\|30` | float |
| `STOCH_RSI_D_5` | Stoch RSI D\|5 | `Stoch.RSI.D\|5` | float |
| `STOCH_RSI_D_60` | Stoch RSI D\|60 | `Stoch.RSI.D\|60` | float |
| `STOCH_RSI_K_1` | Stoch RSI K\|1 | `Stoch.RSI.K\|1` | float |
| `STOCH_RSI_K_120` | Stoch RSI K\|120 | `Stoch.RSI.K\|120` | float |
| `STOCH_RSI_K_15` | Stoch RSI K\|15 | `Stoch.RSI.K\|15` | float |
| `STOCH_RSI_K_1M` | Stoch RSI K\|1M | `Stoch.RSI.K\|1M` | float |
| `STOCH_RSI_K_1W` | Stoch RSI K\|1W | `Stoch.RSI.K\|1W` | float |
| `STOCH_RSI_K_240` | Stoch RSI K\|240 | `Stoch.RSI.K\|240` | float |
| `STOCH_RSI_K_30` | Stoch RSI K\|30 | `Stoch.RSI.K\|30` | float |
| `STOCH_RSI_K_5` | Stoch RSI K\|5 | `Stoch.RSI.K\|5` | float |
| `STOCH_RSI_K_60` | Stoch RSI K\|60 | `Stoch.RSI.K\|60` | float |
| `ULTIMATE_OSCILLATOR_7_14_28` | Ultimate Oscillator (7, 14, 28) | `UO` | recommendation |
| `UO_1` | UO\|1 | `UO\|1` | float |
| `UO_120` | UO\|120 | `UO\|120` | float |
| `UO_15` | UO\|15 | `UO\|15` | float |
| `UO_1M` | UO\|1M | `UO\|1M` | float |
| `UO_1W` | UO\|1W | `UO\|1W` | float |
| `UO_240` | UO\|240 | `UO\|240` | float |
| `UO_30` | UO\|30 | `UO\|30` | float |
| `UO_5` | UO\|5 | `UO\|5` | float |
| `UO_60` | UO\|60 | `UO\|60` | float |
| `WILLIAMS_PERCENT_RANGE_14` | Williams Percent Range (14) | `W.R` | computed_recommendation |
| `W_R_1` | W R\|1 | `W.R\|1` | float |
| `W_R_120` | W R\|120 | `W.R\|120` | float |
| `W_R_15` | W R\|15 | `W.R\|15` | float |
| `W_R_1M` | W R\|1M | `W.R\|1M` | float |
| `W_R_1W` | W R\|1W | `W.R\|1W` | float |
| `W_R_240` | W R\|240 | `W.R\|240` | float |
| `W_R_30` | W R\|30 | `W.R\|30` | float |
| `W_R_5` | W R\|5 | `W.R\|5` | float |
| `W_R_60` | W R\|60 | `W.R\|60` | float |

## Trend Indicators

*400 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `ADX_1` | ADX\|1 | `ADX\|1` | float |
| `ADX_100` | ADX 100 | `ADX_100` | float |
| `ADX_100_1` | ADX 100\|1 | `ADX_100\|1` | float |
| `ADX_100_120` | ADX 100\|120 | `ADX_100\|120` | float |
| `ADX_100_15` | ADX 100\|15 | `ADX_100\|15` | float |
| `ADX_100_1M` | ADX 100\|1M | `ADX_100\|1M` | float |
| `ADX_100_1W` | ADX 100\|1W | `ADX_100\|1W` | float |
| `ADX_100_240` | ADX 100\|240 | `ADX_100\|240` | float |
| `ADX_100_30` | ADX 100\|30 | `ADX_100\|30` | float |
| `ADX_100_5` | ADX 100\|5 | `ADX_100\|5` | float |
| `ADX_100_60` | ADX 100\|60 | `ADX_100\|60` | float |
| `ADX_120` | ADX\|120 | `ADX\|120` | float |
| `ADX_15` | ADX\|15 | `ADX\|15` | float |
| `ADX_1M` | ADX\|1M | `ADX\|1M` | float |
| `ADX_1W` | ADX\|1W | `ADX\|1W` | float |
| `ADX_20` | ADX 20 | `ADX_20` | float |
| `ADX_20_1` | ADX 20\|1 | `ADX_20\|1` | float |
| `ADX_20_120` | ADX 20\|120 | `ADX_20\|120` | float |
| `ADX_20_15` | ADX 20\|15 | `ADX_20\|15` | float |
| `ADX_20_1M` | ADX 20\|1M | `ADX_20\|1M` | float |
| `ADX_20_1W` | ADX 20\|1W | `ADX_20\|1W` | float |
| `ADX_20_240` | ADX 20\|240 | `ADX_20\|240` | float |
| `ADX_20_30` | ADX 20\|30 | `ADX_20\|30` | float |
| `ADX_20_5` | ADX 20\|5 | `ADX_20\|5` | float |
| `ADX_20_60` | ADX 20\|60 | `ADX_20\|60` | float |
| `ADX_240` | ADX\|240 | `ADX\|240` | float |
| `ADX_30` | ADX\|30 | `ADX\|30` | float |
| `ADX_5` | ADX\|5 | `ADX\|5` | float |
| `ADX_50` | ADX 50 | `ADX_50` | float |
| `ADX_50_1` | ADX 50\|1 | `ADX_50\|1` | float |
| `ADX_50_120` | ADX 50\|120 | `ADX_50\|120` | float |
| `ADX_50_15` | ADX 50\|15 | `ADX_50\|15` | float |
| `ADX_50_1M` | ADX 50\|1M | `ADX_50\|1M` | float |
| `ADX_50_1W` | ADX 50\|1W | `ADX_50\|1W` | float |
| `ADX_50_240` | ADX 50\|240 | `ADX_50\|240` | float |
| `ADX_50_30` | ADX 50\|30 | `ADX_50\|30` | float |
| `ADX_50_5` | ADX 50\|5 | `ADX_50\|5` | float |
| `ADX_50_60` | ADX 50\|60 | `ADX_50\|60` | float |
| `ADX_60` | ADX\|60 | `ADX\|60` | float |
| `ADX_9` | ADX 9 | `ADX_9` | float |
| `ADX_9_1` | ADX 9\|1 | `ADX_9\|1` | float |
| `ADX_9_120` | ADX 9\|120 | `ADX_9\|120` | float |
| `ADX_9_15` | ADX 9\|15 | `ADX_9\|15` | float |
| `ADX_9_1M` | ADX 9\|1M | `ADX_9\|1M` | float |
| `ADX_9_1W` | ADX 9\|1W | `ADX_9\|1W` | float |
| `ADX_9_240` | ADX 9\|240 | `ADX_9\|240` | float |
| `ADX_9_30` | ADX 9\|30 | `ADX_9\|30` | float |
| `ADX_9_5` | ADX 9\|5 | `ADX_9\|5` | float |
| `ADX_9_60` | ADX 9\|60 | `ADX_9\|60` | float |
| `ADX_MINUS_DI_1` | ADX-Di[1] | `ADX-DI[1]` | float |
| `ADX_MINUS_DI_100` | ADX-Di 100 | `ADX-DI_100` | float |
| `ADX_MINUS_DI_100_1` | ADX-Di 100[1] | `ADX-DI_100[1]` | float |
| `ADX_MINUS_DI_100_120` | ADX-Di 100\|120 | `ADX-DI_100\|120` | float |
| `ADX_MINUS_DI_100_15` | ADX-Di 100\|15 | `ADX-DI_100\|15` | float |
| `ADX_MINUS_DI_100_1M` | ADX-Di 100\|1M | `ADX-DI_100\|1M` | float |
| `ADX_MINUS_DI_100_1W` | ADX-Di 100\|1W | `ADX-DI_100\|1W` | float |
| `ADX_MINUS_DI_100_1_1` | ADX-Di 100[1]\|1 | `ADX-DI_100[1]\|1` | float |
| `ADX_MINUS_DI_100_1_120` | ADX-Di 100[1]\|120 | `ADX-DI_100[1]\|120` | float |
| `ADX_MINUS_DI_100_1_15` | ADX-Di 100[1]\|15 | `ADX-DI_100[1]\|15` | float |
| `ADX_MINUS_DI_100_1_1M` | ADX-Di 100[1]\|1M | `ADX-DI_100[1]\|1M` | float |
| `ADX_MINUS_DI_100_1_1W` | ADX-Di 100[1]\|1W | `ADX-DI_100[1]\|1W` | float |
| `ADX_MINUS_DI_100_1_2` | ADX-Di 100\|1 | `ADX-DI_100\|1` | float |
| `ADX_MINUS_DI_100_1_240` | ADX-Di 100[1]\|240 | `ADX-DI_100[1]\|240` | float |
| `ADX_MINUS_DI_100_1_30` | ADX-Di 100[1]\|30 | `ADX-DI_100[1]\|30` | float |
| `ADX_MINUS_DI_100_1_5` | ADX-Di 100[1]\|5 | `ADX-DI_100[1]\|5` | float |
| `ADX_MINUS_DI_100_1_60` | ADX-Di 100[1]\|60 | `ADX-DI_100[1]\|60` | float |
| `ADX_MINUS_DI_100_240` | ADX-Di 100\|240 | `ADX-DI_100\|240` | float |
| `ADX_MINUS_DI_100_30` | ADX-Di 100\|30 | `ADX-DI_100\|30` | float |
| `ADX_MINUS_DI_100_5` | ADX-Di 100\|5 | `ADX-DI_100\|5` | float |
| `ADX_MINUS_DI_100_60` | ADX-Di 100\|60 | `ADX-DI_100\|60` | float |
| `ADX_MINUS_DI_120` | ADX-Di\|120 | `ADX-DI\|120` | float |
| `ADX_MINUS_DI_15` | ADX-Di\|15 | `ADX-DI\|15` | float |
| `ADX_MINUS_DI_1M` | ADX-Di\|1M | `ADX-DI\|1M` | float |
| `ADX_MINUS_DI_1W` | ADX-Di\|1W | `ADX-DI\|1W` | float |
| `ADX_MINUS_DI_1_1` | ADX-Di[1]\|1 | `ADX-DI[1]\|1` | float |
| `ADX_MINUS_DI_1_120` | ADX-Di[1]\|120 | `ADX-DI[1]\|120` | float |
| `ADX_MINUS_DI_1_15` | ADX-Di[1]\|15 | `ADX-DI[1]\|15` | float |
| `ADX_MINUS_DI_1_1M` | ADX-Di[1]\|1M | `ADX-DI[1]\|1M` | float |
| `ADX_MINUS_DI_1_1W` | ADX-Di[1]\|1W | `ADX-DI[1]\|1W` | float |
| `ADX_MINUS_DI_1_2` | ADX-Di\|1 | `ADX-DI\|1` | float |
| `ADX_MINUS_DI_1_240` | ADX-Di[1]\|240 | `ADX-DI[1]\|240` | float |
| `ADX_MINUS_DI_1_30` | ADX-Di[1]\|30 | `ADX-DI[1]\|30` | float |
| `ADX_MINUS_DI_1_5` | ADX-Di[1]\|5 | `ADX-DI[1]\|5` | float |
| `ADX_MINUS_DI_1_60` | ADX-Di[1]\|60 | `ADX-DI[1]\|60` | float |
| `ADX_MINUS_DI_20` | ADX-Di 20 | `ADX-DI_20` | float |
| `ADX_MINUS_DI_20_1` | ADX-Di 20[1] | `ADX-DI_20[1]` | float |
| `ADX_MINUS_DI_20_120` | ADX-Di 20\|120 | `ADX-DI_20\|120` | float |
| `ADX_MINUS_DI_20_15` | ADX-Di 20\|15 | `ADX-DI_20\|15` | float |
| `ADX_MINUS_DI_20_1M` | ADX-Di 20\|1M | `ADX-DI_20\|1M` | float |
| `ADX_MINUS_DI_20_1W` | ADX-Di 20\|1W | `ADX-DI_20\|1W` | float |
| `ADX_MINUS_DI_20_1_1` | ADX-Di 20[1]\|1 | `ADX-DI_20[1]\|1` | float |
| `ADX_MINUS_DI_20_1_120` | ADX-Di 20[1]\|120 | `ADX-DI_20[1]\|120` | float |
| `ADX_MINUS_DI_20_1_15` | ADX-Di 20[1]\|15 | `ADX-DI_20[1]\|15` | float |
| `ADX_MINUS_DI_20_1_1M` | ADX-Di 20[1]\|1M | `ADX-DI_20[1]\|1M` | float |
| `ADX_MINUS_DI_20_1_1W` | ADX-Di 20[1]\|1W | `ADX-DI_20[1]\|1W` | float |
| `ADX_MINUS_DI_20_1_2` | ADX-Di 20\|1 | `ADX-DI_20\|1` | float |
| `ADX_MINUS_DI_20_1_240` | ADX-Di 20[1]\|240 | `ADX-DI_20[1]\|240` | float |
| `ADX_MINUS_DI_20_1_30` | ADX-Di 20[1]\|30 | `ADX-DI_20[1]\|30` | float |
| `ADX_MINUS_DI_20_1_5` | ADX-Di 20[1]\|5 | `ADX-DI_20[1]\|5` | float |
| `ADX_MINUS_DI_20_1_60` | ADX-Di 20[1]\|60 | `ADX-DI_20[1]\|60` | float |
| `ADX_MINUS_DI_20_240` | ADX-Di 20\|240 | `ADX-DI_20\|240` | float |
| `ADX_MINUS_DI_20_30` | ADX-Di 20\|30 | `ADX-DI_20\|30` | float |
| `ADX_MINUS_DI_20_5` | ADX-Di 20\|5 | `ADX-DI_20\|5` | float |
| `ADX_MINUS_DI_20_60` | ADX-Di 20\|60 | `ADX-DI_20\|60` | float |
| `ADX_MINUS_DI_240` | ADX-Di\|240 | `ADX-DI\|240` | float |
| `ADX_MINUS_DI_30` | ADX-Di\|30 | `ADX-DI\|30` | float |
| `ADX_MINUS_DI_5` | ADX-Di\|5 | `ADX-DI\|5` | float |
| `ADX_MINUS_DI_50` | ADX-Di 50 | `ADX-DI_50` | float |
| `ADX_MINUS_DI_50_1` | ADX-Di 50[1] | `ADX-DI_50[1]` | float |
| `ADX_MINUS_DI_50_120` | ADX-Di 50\|120 | `ADX-DI_50\|120` | float |
| `ADX_MINUS_DI_50_15` | ADX-Di 50\|15 | `ADX-DI_50\|15` | float |
| `ADX_MINUS_DI_50_1M` | ADX-Di 50\|1M | `ADX-DI_50\|1M` | float |
| `ADX_MINUS_DI_50_1W` | ADX-Di 50\|1W | `ADX-DI_50\|1W` | float |
| `ADX_MINUS_DI_50_1_1` | ADX-Di 50[1]\|1 | `ADX-DI_50[1]\|1` | float |
| `ADX_MINUS_DI_50_1_120` | ADX-Di 50[1]\|120 | `ADX-DI_50[1]\|120` | float |
| `ADX_MINUS_DI_50_1_15` | ADX-Di 50[1]\|15 | `ADX-DI_50[1]\|15` | float |
| `ADX_MINUS_DI_50_1_1M` | ADX-Di 50[1]\|1M | `ADX-DI_50[1]\|1M` | float |
| `ADX_MINUS_DI_50_1_1W` | ADX-Di 50[1]\|1W | `ADX-DI_50[1]\|1W` | float |
| `ADX_MINUS_DI_50_1_2` | ADX-Di 50\|1 | `ADX-DI_50\|1` | float |
| `ADX_MINUS_DI_50_1_240` | ADX-Di 50[1]\|240 | `ADX-DI_50[1]\|240` | float |
| `ADX_MINUS_DI_50_1_30` | ADX-Di 50[1]\|30 | `ADX-DI_50[1]\|30` | float |
| `ADX_MINUS_DI_50_1_5` | ADX-Di 50[1]\|5 | `ADX-DI_50[1]\|5` | float |
| `ADX_MINUS_DI_50_1_60` | ADX-Di 50[1]\|60 | `ADX-DI_50[1]\|60` | float |
| `ADX_MINUS_DI_50_240` | ADX-Di 50\|240 | `ADX-DI_50\|240` | float |
| `ADX_MINUS_DI_50_30` | ADX-Di 50\|30 | `ADX-DI_50\|30` | float |
| `ADX_MINUS_DI_50_5` | ADX-Di 50\|5 | `ADX-DI_50\|5` | float |
| `ADX_MINUS_DI_50_60` | ADX-Di 50\|60 | `ADX-DI_50\|60` | float |
| `ADX_MINUS_DI_60` | ADX-Di\|60 | `ADX-DI\|60` | float |
| `ADX_MINUS_DI_9` | ADX-Di 9 | `ADX-DI_9` | float |
| `ADX_MINUS_DI_9_1` | ADX-Di 9[1] | `ADX-DI_9[1]` | float |
| `ADX_MINUS_DI_9_120` | ADX-Di 9\|120 | `ADX-DI_9\|120` | float |
| `ADX_MINUS_DI_9_15` | ADX-Di 9\|15 | `ADX-DI_9\|15` | float |
| `ADX_MINUS_DI_9_1M` | ADX-Di 9\|1M | `ADX-DI_9\|1M` | float |
| `ADX_MINUS_DI_9_1W` | ADX-Di 9\|1W | `ADX-DI_9\|1W` | float |
| `ADX_MINUS_DI_9_1_1` | ADX-Di 9[1]\|1 | `ADX-DI_9[1]\|1` | float |
| `ADX_MINUS_DI_9_1_120` | ADX-Di 9[1]\|120 | `ADX-DI_9[1]\|120` | float |
| `ADX_MINUS_DI_9_1_15` | ADX-Di 9[1]\|15 | `ADX-DI_9[1]\|15` | float |
| `ADX_MINUS_DI_9_1_1M` | ADX-Di 9[1]\|1M | `ADX-DI_9[1]\|1M` | float |
| `ADX_MINUS_DI_9_1_1W` | ADX-Di 9[1]\|1W | `ADX-DI_9[1]\|1W` | float |
| `ADX_MINUS_DI_9_1_2` | ADX-Di 9\|1 | `ADX-DI_9\|1` | float |
| `ADX_MINUS_DI_9_1_240` | ADX-Di 9[1]\|240 | `ADX-DI_9[1]\|240` | float |
| `ADX_MINUS_DI_9_1_30` | ADX-Di 9[1]\|30 | `ADX-DI_9[1]\|30` | float |
| `ADX_MINUS_DI_9_1_5` | ADX-Di 9[1]\|5 | `ADX-DI_9[1]\|5` | float |
| `ADX_MINUS_DI_9_1_60` | ADX-Di 9[1]\|60 | `ADX-DI_9[1]\|60` | float |
| `ADX_MINUS_DI_9_240` | ADX-Di 9\|240 | `ADX-DI_9\|240` | float |
| `ADX_MINUS_DI_9_30` | ADX-Di 9\|30 | `ADX-DI_9\|30` | float |
| `ADX_MINUS_DI_9_5` | ADX-Di 9\|5 | `ADX-DI_9\|5` | float |
| `ADX_MINUS_DI_9_60` | ADX-Di 9\|60 | `ADX-DI_9\|60` | float |
| `ADX_PLUS_DI_1` | ADX+Di[1] | `ADX+DI[1]` | float |
| `ADX_PLUS_DI_100` | ADX+Di 100 | `ADX+DI_100` | float |
| `ADX_PLUS_DI_100_1` | ADX+Di 100[1] | `ADX+DI_100[1]` | float |
| `ADX_PLUS_DI_100_120` | ADX+Di 100\|120 | `ADX+DI_100\|120` | float |
| `ADX_PLUS_DI_100_15` | ADX+Di 100\|15 | `ADX+DI_100\|15` | float |
| `ADX_PLUS_DI_100_1M` | ADX+Di 100\|1M | `ADX+DI_100\|1M` | float |
| `ADX_PLUS_DI_100_1W` | ADX+Di 100\|1W | `ADX+DI_100\|1W` | float |
| `ADX_PLUS_DI_100_1_1` | ADX+Di 100[1]\|1 | `ADX+DI_100[1]\|1` | float |
| `ADX_PLUS_DI_100_1_120` | ADX+Di 100[1]\|120 | `ADX+DI_100[1]\|120` | float |
| `ADX_PLUS_DI_100_1_15` | ADX+Di 100[1]\|15 | `ADX+DI_100[1]\|15` | float |
| `ADX_PLUS_DI_100_1_1M` | ADX+Di 100[1]\|1M | `ADX+DI_100[1]\|1M` | float |
| `ADX_PLUS_DI_100_1_1W` | ADX+Di 100[1]\|1W | `ADX+DI_100[1]\|1W` | float |
| `ADX_PLUS_DI_100_1_2` | ADX+Di 100\|1 | `ADX+DI_100\|1` | float |
| `ADX_PLUS_DI_100_1_240` | ADX+Di 100[1]\|240 | `ADX+DI_100[1]\|240` | float |
| `ADX_PLUS_DI_100_1_30` | ADX+Di 100[1]\|30 | `ADX+DI_100[1]\|30` | float |
| `ADX_PLUS_DI_100_1_5` | ADX+Di 100[1]\|5 | `ADX+DI_100[1]\|5` | float |
| `ADX_PLUS_DI_100_1_60` | ADX+Di 100[1]\|60 | `ADX+DI_100[1]\|60` | float |
| `ADX_PLUS_DI_100_240` | ADX+Di 100\|240 | `ADX+DI_100\|240` | float |
| `ADX_PLUS_DI_100_30` | ADX+Di 100\|30 | `ADX+DI_100\|30` | float |
| `ADX_PLUS_DI_100_5` | ADX+Di 100\|5 | `ADX+DI_100\|5` | float |
| `ADX_PLUS_DI_100_60` | ADX+Di 100\|60 | `ADX+DI_100\|60` | float |
| `ADX_PLUS_DI_120` | ADX+Di\|120 | `ADX+DI\|120` | float |
| `ADX_PLUS_DI_15` | ADX+Di\|15 | `ADX+DI\|15` | float |
| `ADX_PLUS_DI_1M` | ADX+Di\|1M | `ADX+DI\|1M` | float |
| `ADX_PLUS_DI_1W` | ADX+Di\|1W | `ADX+DI\|1W` | float |
| `ADX_PLUS_DI_1_1` | ADX+Di[1]\|1 | `ADX+DI[1]\|1` | float |
| `ADX_PLUS_DI_1_120` | ADX+Di[1]\|120 | `ADX+DI[1]\|120` | float |
| `ADX_PLUS_DI_1_15` | ADX+Di[1]\|15 | `ADX+DI[1]\|15` | float |
| `ADX_PLUS_DI_1_1M` | ADX+Di[1]\|1M | `ADX+DI[1]\|1M` | float |
| `ADX_PLUS_DI_1_1W` | ADX+Di[1]\|1W | `ADX+DI[1]\|1W` | float |
| `ADX_PLUS_DI_1_2` | ADX+Di\|1 | `ADX+DI\|1` | float |
| `ADX_PLUS_DI_1_240` | ADX+Di[1]\|240 | `ADX+DI[1]\|240` | float |
| `ADX_PLUS_DI_1_30` | ADX+Di[1]\|30 | `ADX+DI[1]\|30` | float |
| `ADX_PLUS_DI_1_5` | ADX+Di[1]\|5 | `ADX+DI[1]\|5` | float |
| `ADX_PLUS_DI_1_60` | ADX+Di[1]\|60 | `ADX+DI[1]\|60` | float |
| `ADX_PLUS_DI_20` | ADX+Di 20 | `ADX+DI_20` | float |
| `ADX_PLUS_DI_20_1` | ADX+Di 20[1] | `ADX+DI_20[1]` | float |
| `ADX_PLUS_DI_20_120` | ADX+Di 20\|120 | `ADX+DI_20\|120` | float |
| `ADX_PLUS_DI_20_15` | ADX+Di 20\|15 | `ADX+DI_20\|15` | float |
| `ADX_PLUS_DI_20_1M` | ADX+Di 20\|1M | `ADX+DI_20\|1M` | float |
| `ADX_PLUS_DI_20_1W` | ADX+Di 20\|1W | `ADX+DI_20\|1W` | float |
| `ADX_PLUS_DI_20_1_1` | ADX+Di 20[1]\|1 | `ADX+DI_20[1]\|1` | float |
| `ADX_PLUS_DI_20_1_120` | ADX+Di 20[1]\|120 | `ADX+DI_20[1]\|120` | float |
| `ADX_PLUS_DI_20_1_15` | ADX+Di 20[1]\|15 | `ADX+DI_20[1]\|15` | float |
| `ADX_PLUS_DI_20_1_1M` | ADX+Di 20[1]\|1M | `ADX+DI_20[1]\|1M` | float |
| `ADX_PLUS_DI_20_1_1W` | ADX+Di 20[1]\|1W | `ADX+DI_20[1]\|1W` | float |
| `ADX_PLUS_DI_20_1_2` | ADX+Di 20\|1 | `ADX+DI_20\|1` | float |
| `ADX_PLUS_DI_20_1_240` | ADX+Di 20[1]\|240 | `ADX+DI_20[1]\|240` | float |
| `ADX_PLUS_DI_20_1_30` | ADX+Di 20[1]\|30 | `ADX+DI_20[1]\|30` | float |
| `ADX_PLUS_DI_20_1_5` | ADX+Di 20[1]\|5 | `ADX+DI_20[1]\|5` | float |
| `ADX_PLUS_DI_20_1_60` | ADX+Di 20[1]\|60 | `ADX+DI_20[1]\|60` | float |
| `ADX_PLUS_DI_20_240` | ADX+Di 20\|240 | `ADX+DI_20\|240` | float |
| `ADX_PLUS_DI_20_30` | ADX+Di 20\|30 | `ADX+DI_20\|30` | float |
| `ADX_PLUS_DI_20_5` | ADX+Di 20\|5 | `ADX+DI_20\|5` | float |
| `ADX_PLUS_DI_20_60` | ADX+Di 20\|60 | `ADX+DI_20\|60` | float |
| `ADX_PLUS_DI_240` | ADX+Di\|240 | `ADX+DI\|240` | float |
| `ADX_PLUS_DI_30` | ADX+Di\|30 | `ADX+DI\|30` | float |
| `ADX_PLUS_DI_5` | ADX+Di\|5 | `ADX+DI\|5` | float |
| `ADX_PLUS_DI_50` | ADX+Di 50 | `ADX+DI_50` | float |
| `ADX_PLUS_DI_50_1` | ADX+Di 50[1] | `ADX+DI_50[1]` | float |
| `ADX_PLUS_DI_50_120` | ADX+Di 50\|120 | `ADX+DI_50\|120` | float |
| `ADX_PLUS_DI_50_15` | ADX+Di 50\|15 | `ADX+DI_50\|15` | float |
| `ADX_PLUS_DI_50_1M` | ADX+Di 50\|1M | `ADX+DI_50\|1M` | float |
| `ADX_PLUS_DI_50_1W` | ADX+Di 50\|1W | `ADX+DI_50\|1W` | float |
| `ADX_PLUS_DI_50_1_1` | ADX+Di 50[1]\|1 | `ADX+DI_50[1]\|1` | float |
| `ADX_PLUS_DI_50_1_120` | ADX+Di 50[1]\|120 | `ADX+DI_50[1]\|120` | float |
| `ADX_PLUS_DI_50_1_15` | ADX+Di 50[1]\|15 | `ADX+DI_50[1]\|15` | float |
| `ADX_PLUS_DI_50_1_1M` | ADX+Di 50[1]\|1M | `ADX+DI_50[1]\|1M` | float |
| `ADX_PLUS_DI_50_1_1W` | ADX+Di 50[1]\|1W | `ADX+DI_50[1]\|1W` | float |
| `ADX_PLUS_DI_50_1_2` | ADX+Di 50\|1 | `ADX+DI_50\|1` | float |
| `ADX_PLUS_DI_50_1_240` | ADX+Di 50[1]\|240 | `ADX+DI_50[1]\|240` | float |
| `ADX_PLUS_DI_50_1_30` | ADX+Di 50[1]\|30 | `ADX+DI_50[1]\|30` | float |
| `ADX_PLUS_DI_50_1_5` | ADX+Di 50[1]\|5 | `ADX+DI_50[1]\|5` | float |
| `ADX_PLUS_DI_50_1_60` | ADX+Di 50[1]\|60 | `ADX+DI_50[1]\|60` | float |
| `ADX_PLUS_DI_50_240` | ADX+Di 50\|240 | `ADX+DI_50\|240` | float |
| `ADX_PLUS_DI_50_30` | ADX+Di 50\|30 | `ADX+DI_50\|30` | float |
| `ADX_PLUS_DI_50_5` | ADX+Di 50\|5 | `ADX+DI_50\|5` | float |
| `ADX_PLUS_DI_50_60` | ADX+Di 50\|60 | `ADX+DI_50\|60` | float |
| `ADX_PLUS_DI_60` | ADX+Di\|60 | `ADX+DI\|60` | float |
| `ADX_PLUS_DI_9` | ADX+Di 9 | `ADX+DI_9` | float |
| `ADX_PLUS_DI_9_1` | ADX+Di 9[1] | `ADX+DI_9[1]` | float |
| `ADX_PLUS_DI_9_120` | ADX+Di 9\|120 | `ADX+DI_9\|120` | float |
| `ADX_PLUS_DI_9_15` | ADX+Di 9\|15 | `ADX+DI_9\|15` | float |
| `ADX_PLUS_DI_9_1M` | ADX+Di 9\|1M | `ADX+DI_9\|1M` | float |
| `ADX_PLUS_DI_9_1W` | ADX+Di 9\|1W | `ADX+DI_9\|1W` | float |
| `ADX_PLUS_DI_9_1_1` | ADX+Di 9[1]\|1 | `ADX+DI_9[1]\|1` | float |
| `ADX_PLUS_DI_9_1_120` | ADX+Di 9[1]\|120 | `ADX+DI_9[1]\|120` | float |
| `ADX_PLUS_DI_9_1_15` | ADX+Di 9[1]\|15 | `ADX+DI_9[1]\|15` | float |
| `ADX_PLUS_DI_9_1_1M` | ADX+Di 9[1]\|1M | `ADX+DI_9[1]\|1M` | float |
| `ADX_PLUS_DI_9_1_1W` | ADX+Di 9[1]\|1W | `ADX+DI_9[1]\|1W` | float |
| `ADX_PLUS_DI_9_1_2` | ADX+Di 9\|1 | `ADX+DI_9\|1` | float |
| `ADX_PLUS_DI_9_1_240` | ADX+Di 9[1]\|240 | `ADX+DI_9[1]\|240` | float |
| `ADX_PLUS_DI_9_1_30` | ADX+Di 9[1]\|30 | `ADX+DI_9[1]\|30` | float |
| `ADX_PLUS_DI_9_1_5` | ADX+Di 9[1]\|5 | `ADX+DI_9[1]\|5` | float |
| `ADX_PLUS_DI_9_1_60` | ADX+Di 9[1]\|60 | `ADX+DI_9[1]\|60` | float |
| `ADX_PLUS_DI_9_240` | ADX+Di 9\|240 | `ADX+DI_9\|240` | float |
| `ADX_PLUS_DI_9_30` | ADX+Di 9\|30 | `ADX+DI_9\|30` | float |
| `ADX_PLUS_DI_9_5` | ADX+Di 9\|5 | `ADX+DI_9\|5` | float |
| `ADX_PLUS_DI_9_60` | ADX+Di 9\|60 | `ADX+DI_9\|60` | float |
| `AROON_DOWN_1` | Aroon Down\|1 | `Aroon.Down\|1` | float |
| `AROON_DOWN_120` | Aroon Down\|120 | `Aroon.Down\|120` | float |
| `AROON_DOWN_14` | Aroon Down (14) | `Aroon.Down` | round |
| `AROON_DOWN_15` | Aroon Down\|15 | `Aroon.Down\|15` | float |
| `AROON_DOWN_1M` | Aroon Down\|1M | `Aroon.Down\|1M` | float |
| `AROON_DOWN_1W` | Aroon Down\|1W | `Aroon.Down\|1W` | float |
| `AROON_DOWN_240` | Aroon Down\|240 | `Aroon.Down\|240` | float |
| `AROON_DOWN_30` | Aroon Down\|30 | `Aroon.Down\|30` | float |
| `AROON_DOWN_5` | Aroon Down\|5 | `Aroon.Down\|5` | float |
| `AROON_DOWN_60` | Aroon Down\|60 | `Aroon.Down\|60` | float |
| `AROON_UP_1` | Aroon Up\|1 | `Aroon.Up\|1` | float |
| `AROON_UP_120` | Aroon Up\|120 | `Aroon.Up\|120` | float |
| `AROON_UP_14` | Aroon Up (14) | `Aroon.Up` | round |
| `AROON_UP_15` | Aroon Up\|15 | `Aroon.Up\|15` | float |
| `AROON_UP_1M` | Aroon Up\|1M | `Aroon.Up\|1M` | float |
| `AROON_UP_1W` | Aroon Up\|1W | `Aroon.Up\|1W` | float |
| `AROON_UP_240` | Aroon Up\|240 | `Aroon.Up\|240` | float |
| `AROON_UP_30` | Aroon Up\|30 | `Aroon.Up\|30` | float |
| `AROON_UP_5` | Aroon Up\|5 | `Aroon.Up\|5` | float |
| `AROON_UP_60` | Aroon Up\|60 | `Aroon.Up\|60` | float |
| `AVERAGE_DIRECTIONAL_INDEX_14` | Average Directional Index (14) | `ADX` | computed_recommendation |
| `ICHIMOKU_BASE_LINE_9_26_52_26` | Ichimoku Base Line (9, 26, 52, 26) | `Ichimoku.BLine` | computed_recommendation |
| `ICHIMOKU_BLINE_1` | Ichimoku Bline\|1 | `Ichimoku.BLine\|1` | float |
| `ICHIMOKU_BLINE_120` | Ichimoku Bline\|120 | `Ichimoku.BLine\|120` | float |
| `ICHIMOKU_BLINE_15` | Ichimoku Bline\|15 | `Ichimoku.BLine\|15` | float |
| `ICHIMOKU_BLINE_1M` | Ichimoku Bline\|1M | `Ichimoku.BLine\|1M` | float |
| `ICHIMOKU_BLINE_1W` | Ichimoku Bline\|1W | `Ichimoku.BLine\|1W` | float |
| `ICHIMOKU_BLINE_20_60_120_30` | Ichimoku Bline 20 60 120 30 | `Ichimoku.BLine_20_60_120_30` | float |
| `ICHIMOKU_BLINE_20_60_120_30_1` | Ichimoku Bline 20 60 120 30\|1 | `Ichimoku.BLine_20_60_120_30\|1` | float |
| `ICHIMOKU_BLINE_20_60_120_30_120` | Ichimoku Bline 20 60 120 30\|120 | `Ichimoku.BLine_20_60_120_30\|120` | float |
| `ICHIMOKU_BLINE_20_60_120_30_15` | Ichimoku Bline 20 60 120 30\|15 | `Ichimoku.BLine_20_60_120_30\|15` | float |
| `ICHIMOKU_BLINE_20_60_120_30_1M` | Ichimoku Bline 20 60 120 30\|1M | `Ichimoku.BLine_20_60_120_30\|1M` | float |
| `ICHIMOKU_BLINE_20_60_120_30_1W` | Ichimoku Bline 20 60 120 30\|1W | `Ichimoku.BLine_20_60_120_30\|1W` | float |
| `ICHIMOKU_BLINE_20_60_120_30_240` | Ichimoku Bline 20 60 120 30\|240 | `Ichimoku.BLine_20_60_120_30\|240` | float |
| `ICHIMOKU_BLINE_20_60_120_30_30` | Ichimoku Bline 20 60 120 30\|30 | `Ichimoku.BLine_20_60_120_30\|30` | float |
| `ICHIMOKU_BLINE_20_60_120_30_5` | Ichimoku Bline 20 60 120 30\|5 | `Ichimoku.BLine_20_60_120_30\|5` | float |
| `ICHIMOKU_BLINE_20_60_120_30_60` | Ichimoku Bline 20 60 120 30\|60 | `Ichimoku.BLine_20_60_120_30\|60` | float |
| `ICHIMOKU_BLINE_240` | Ichimoku Bline\|240 | `Ichimoku.BLine\|240` | float |
| `ICHIMOKU_BLINE_30` | Ichimoku Bline\|30 | `Ichimoku.BLine\|30` | float |
| `ICHIMOKU_BLINE_5` | Ichimoku Bline\|5 | `Ichimoku.BLine\|5` | float |
| `ICHIMOKU_BLINE_60` | Ichimoku Bline\|60 | `Ichimoku.BLine\|60` | float |
| `ICHIMOKU_CLINE_1` | Ichimoku Cline\|1 | `Ichimoku.CLine\|1` | float |
| `ICHIMOKU_CLINE_120` | Ichimoku Cline\|120 | `Ichimoku.CLine\|120` | float |
| `ICHIMOKU_CLINE_15` | Ichimoku Cline\|15 | `Ichimoku.CLine\|15` | float |
| `ICHIMOKU_CLINE_1M` | Ichimoku Cline\|1M | `Ichimoku.CLine\|1M` | float |
| `ICHIMOKU_CLINE_1W` | Ichimoku Cline\|1W | `Ichimoku.CLine\|1W` | float |
| `ICHIMOKU_CLINE_20_60_120_30` | Ichimoku Cline 20 60 120 30 | `Ichimoku.CLine_20_60_120_30` | float |
| `ICHIMOKU_CLINE_20_60_120_30_1` | Ichimoku Cline 20 60 120 30\|1 | `Ichimoku.CLine_20_60_120_30\|1` | float |
| `ICHIMOKU_CLINE_20_60_120_30_120` | Ichimoku Cline 20 60 120 30\|120 | `Ichimoku.CLine_20_60_120_30\|120` | float |
| `ICHIMOKU_CLINE_20_60_120_30_15` | Ichimoku Cline 20 60 120 30\|15 | `Ichimoku.CLine_20_60_120_30\|15` | float |
| `ICHIMOKU_CLINE_20_60_120_30_1M` | Ichimoku Cline 20 60 120 30\|1M | `Ichimoku.CLine_20_60_120_30\|1M` | float |
| `ICHIMOKU_CLINE_20_60_120_30_1W` | Ichimoku Cline 20 60 120 30\|1W | `Ichimoku.CLine_20_60_120_30\|1W` | float |
| `ICHIMOKU_CLINE_20_60_120_30_240` | Ichimoku Cline 20 60 120 30\|240 | `Ichimoku.CLine_20_60_120_30\|240` | float |
| `ICHIMOKU_CLINE_20_60_120_30_30` | Ichimoku Cline 20 60 120 30\|30 | `Ichimoku.CLine_20_60_120_30\|30` | float |
| `ICHIMOKU_CLINE_20_60_120_30_5` | Ichimoku Cline 20 60 120 30\|5 | `Ichimoku.CLine_20_60_120_30\|5` | float |
| `ICHIMOKU_CLINE_20_60_120_30_60` | Ichimoku Cline 20 60 120 30\|60 | `Ichimoku.CLine_20_60_120_30\|60` | float |
| `ICHIMOKU_CLINE_240` | Ichimoku Cline\|240 | `Ichimoku.CLine\|240` | float |
| `ICHIMOKU_CLINE_30` | Ichimoku Cline\|30 | `Ichimoku.CLine\|30` | float |
| `ICHIMOKU_CLINE_5` | Ichimoku Cline\|5 | `Ichimoku.CLine\|5` | float |
| `ICHIMOKU_CLINE_60` | Ichimoku Cline\|60 | `Ichimoku.CLine\|60` | float |
| `ICHIMOKU_CONVERSION_LINE_9_26_52_26` | Ichimoku Conversion Line (9, 26, 52, 26) | `Ichimoku.CLine` | float |
| `ICHIMOKU_LEAD1_1` | Ichimoku Lead1\|1 | `Ichimoku.Lead1\|1` | float |
| `ICHIMOKU_LEAD1_120` | Ichimoku Lead1\|120 | `Ichimoku.Lead1\|120` | float |
| `ICHIMOKU_LEAD1_15` | Ichimoku Lead1\|15 | `Ichimoku.Lead1\|15` | float |
| `ICHIMOKU_LEAD1_1M` | Ichimoku Lead1\|1M | `Ichimoku.Lead1\|1M` | float |
| `ICHIMOKU_LEAD1_1W` | Ichimoku Lead1\|1W | `Ichimoku.Lead1\|1W` | float |
| `ICHIMOKU_LEAD1_20_60_120_30` | Ichimoku Lead1 20 60 120 30 | `Ichimoku.Lead1_20_60_120_30` | float |
| `ICHIMOKU_LEAD1_20_60_120_30_1` | Ichimoku Lead1 20 60 120 30\|1 | `Ichimoku.Lead1_20_60_120_30\|1` | float |
| `ICHIMOKU_LEAD1_20_60_120_30_120` | Ichimoku Lead1 20 60 120 30\|120 | `Ichimoku.Lead1_20_60_120_30\|120` | float |
| `ICHIMOKU_LEAD1_20_60_120_30_15` | Ichimoku Lead1 20 60 120 30\|15 | `Ichimoku.Lead1_20_60_120_30\|15` | float |
| `ICHIMOKU_LEAD1_20_60_120_30_1M` | Ichimoku Lead1 20 60 120 30\|1M | `Ichimoku.Lead1_20_60_120_30\|1M` | float |
| `ICHIMOKU_LEAD1_20_60_120_30_1W` | Ichimoku Lead1 20 60 120 30\|1W | `Ichimoku.Lead1_20_60_120_30\|1W` | float |
| `ICHIMOKU_LEAD1_20_60_120_30_240` | Ichimoku Lead1 20 60 120 30\|240 | `Ichimoku.Lead1_20_60_120_30\|240` | float |
| `ICHIMOKU_LEAD1_20_60_120_30_30` | Ichimoku Lead1 20 60 120 30\|30 | `Ichimoku.Lead1_20_60_120_30\|30` | float |
| `ICHIMOKU_LEAD1_20_60_120_30_5` | Ichimoku Lead1 20 60 120 30\|5 | `Ichimoku.Lead1_20_60_120_30\|5` | float |
| `ICHIMOKU_LEAD1_20_60_120_30_60` | Ichimoku Lead1 20 60 120 30\|60 | `Ichimoku.Lead1_20_60_120_30\|60` | float |
| `ICHIMOKU_LEAD1_240` | Ichimoku Lead1\|240 | `Ichimoku.Lead1\|240` | float |
| `ICHIMOKU_LEAD1_30` | Ichimoku Lead1\|30 | `Ichimoku.Lead1\|30` | float |
| `ICHIMOKU_LEAD1_5` | Ichimoku Lead1\|5 | `Ichimoku.Lead1\|5` | float |
| `ICHIMOKU_LEAD1_60` | Ichimoku Lead1\|60 | `Ichimoku.Lead1\|60` | float |
| `ICHIMOKU_LEAD2_1` | Ichimoku Lead2\|1 | `Ichimoku.Lead2\|1` | float |
| `ICHIMOKU_LEAD2_120` | Ichimoku Lead2\|120 | `Ichimoku.Lead2\|120` | float |
| `ICHIMOKU_LEAD2_15` | Ichimoku Lead2\|15 | `Ichimoku.Lead2\|15` | float |
| `ICHIMOKU_LEAD2_1M` | Ichimoku Lead2\|1M | `Ichimoku.Lead2\|1M` | float |
| `ICHIMOKU_LEAD2_1W` | Ichimoku Lead2\|1W | `Ichimoku.Lead2\|1W` | float |
| `ICHIMOKU_LEAD2_20_60_120_30` | Ichimoku Lead2 20 60 120 30 | `Ichimoku.Lead2_20_60_120_30` | float |
| `ICHIMOKU_LEAD2_20_60_120_30_1` | Ichimoku Lead2 20 60 120 30\|1 | `Ichimoku.Lead2_20_60_120_30\|1` | float |
| `ICHIMOKU_LEAD2_20_60_120_30_120` | Ichimoku Lead2 20 60 120 30\|120 | `Ichimoku.Lead2_20_60_120_30\|120` | float |
| `ICHIMOKU_LEAD2_20_60_120_30_15` | Ichimoku Lead2 20 60 120 30\|15 | `Ichimoku.Lead2_20_60_120_30\|15` | float |
| `ICHIMOKU_LEAD2_20_60_120_30_1M` | Ichimoku Lead2 20 60 120 30\|1M | `Ichimoku.Lead2_20_60_120_30\|1M` | float |
| `ICHIMOKU_LEAD2_20_60_120_30_1W` | Ichimoku Lead2 20 60 120 30\|1W | `Ichimoku.Lead2_20_60_120_30\|1W` | float |
| `ICHIMOKU_LEAD2_20_60_120_30_240` | Ichimoku Lead2 20 60 120 30\|240 | `Ichimoku.Lead2_20_60_120_30\|240` | float |
| `ICHIMOKU_LEAD2_20_60_120_30_30` | Ichimoku Lead2 20 60 120 30\|30 | `Ichimoku.Lead2_20_60_120_30\|30` | float |
| `ICHIMOKU_LEAD2_20_60_120_30_5` | Ichimoku Lead2 20 60 120 30\|5 | `Ichimoku.Lead2_20_60_120_30\|5` | float |
| `ICHIMOKU_LEAD2_20_60_120_30_60` | Ichimoku Lead2 20 60 120 30\|60 | `Ichimoku.Lead2_20_60_120_30\|60` | float |
| `ICHIMOKU_LEAD2_240` | Ichimoku Lead2\|240 | `Ichimoku.Lead2\|240` | float |
| `ICHIMOKU_LEAD2_30` | Ichimoku Lead2\|30 | `Ichimoku.Lead2\|30` | float |
| `ICHIMOKU_LEAD2_5` | Ichimoku Lead2\|5 | `Ichimoku.Lead2\|5` | float |
| `ICHIMOKU_LEAD2_60` | Ichimoku Lead2\|60 | `Ichimoku.Lead2\|60` | float |
| `ICHIMOKU_LEADING_SPAN_A_9_26_52_26` | Ichimoku Leading Span A (9, 26, 52, 26) | `Ichimoku.Lead1` | float |
| `ICHIMOKU_LEADING_SPAN_B_9_26_52_26` | Ichimoku Leading Span B (9, 26, 52, 26) | `Ichimoku.Lead2` | float |
| `MACD_HIST` | MACD Hist | `MACD.hist` | float |
| `MACD_HIST_1` | MACD Hist\|1 | `MACD.hist\|1` | float |
| `MACD_HIST_120` | MACD Hist\|120 | `MACD.hist\|120` | float |
| `MACD_HIST_15` | MACD Hist\|15 | `MACD.hist\|15` | float |
| `MACD_HIST_1M` | MACD Hist\|1M | `MACD.hist\|1M` | float |
| `MACD_HIST_1W` | MACD Hist\|1W | `MACD.hist\|1W` | float |
| `MACD_HIST_240` | MACD Hist\|240 | `MACD.hist\|240` | float |
| `MACD_HIST_30` | MACD Hist\|30 | `MACD.hist\|30` | float |
| `MACD_HIST_5` | MACD Hist\|5 | `MACD.hist\|5` | float |
| `MACD_HIST_60` | MACD Hist\|60 | `MACD.hist\|60` | float |
| `MACD_LEVEL_12_26` | MACD Level (12, 26) | `MACD.macd` | computed_recommendation |
| `MACD_MACD_1` | MACD MACD\|1 | `MACD.macd\|1` | float |
| `MACD_MACD_120` | MACD MACD\|120 | `MACD.macd\|120` | float |
| `MACD_MACD_15` | MACD MACD\|15 | `MACD.macd\|15` | float |
| `MACD_MACD_1M` | MACD MACD\|1M | `MACD.macd\|1M` | float |
| `MACD_MACD_1W` | MACD MACD\|1W | `MACD.macd\|1W` | float |
| `MACD_MACD_240` | MACD MACD\|240 | `MACD.macd\|240` | float |
| `MACD_MACD_30` | MACD MACD\|30 | `MACD.macd\|30` | float |
| `MACD_MACD_5` | MACD MACD\|5 | `MACD.macd\|5` | float |
| `MACD_MACD_60` | MACD MACD\|60 | `MACD.macd\|60` | float |
| `MACD_SIGNAL_1` | MACD Signal\|1 | `MACD.signal\|1` | float |
| `MACD_SIGNAL_120` | MACD Signal\|120 | `MACD.signal\|120` | float |
| `MACD_SIGNAL_12_26` | MACD Signal (12, 26) | `MACD.signal` | float |
| `MACD_SIGNAL_15` | MACD Signal\|15 | `MACD.signal\|15` | float |
| `MACD_SIGNAL_1M` | MACD Signal\|1M | `MACD.signal\|1M` | float |
| `MACD_SIGNAL_1W` | MACD Signal\|1W | `MACD.signal\|1W` | float |
| `MACD_SIGNAL_240` | MACD Signal\|240 | `MACD.signal\|240` | float |
| `MACD_SIGNAL_30` | MACD Signal\|30 | `MACD.signal\|30` | float |
| `MACD_SIGNAL_5` | MACD Signal\|5 | `MACD.signal\|5` | float |
| `MACD_SIGNAL_60` | MACD Signal\|60 | `MACD.signal\|60` | float |
| `NEGATIVE_DIRECTIONAL_INDICATOR_14` | Negative Directional Indicator (14) | `ADX-DI` | round |
| `PARABOLIC_SAR` | Parabolic SAR | `P.SAR` | computed_recommendation |
| `POSITIVE_DIRECTIONAL_INDICATOR_14` | Positive Directional Indicator (14) | `ADX+DI` | round |
| `P_SAR_1` | P Sar\|1 | `P.SAR\|1` | float |
| `P_SAR_120` | P Sar\|120 | `P.SAR\|120` | float |
| `P_SAR_15` | P Sar\|15 | `P.SAR\|15` | float |
| `P_SAR_1M` | P Sar\|1M | `P.SAR\|1M` | float |
| `P_SAR_1W` | P Sar\|1W | `P.SAR\|1W` | float |
| `P_SAR_240` | P Sar\|240 | `P.SAR\|240` | float |
| `P_SAR_30` | P Sar\|30 | `P.SAR\|30` | float |
| `P_SAR_5` | P Sar\|5 | `P.SAR\|5` | float |
| `P_SAR_60` | P Sar\|60 | `P.SAR\|60` | float |
| `REC_ICHIMOKU` | Rec Ichimoku | `Rec.Ichimoku` | rating |
| `REC_ICHIMOKU_1` | Rec Ichimoku\|1 | `Rec.Ichimoku\|1` | rating |
| `REC_ICHIMOKU_120` | Rec Ichimoku\|120 | `Rec.Ichimoku\|120` | rating |
| `REC_ICHIMOKU_15` | Rec Ichimoku\|15 | `Rec.Ichimoku\|15` | rating |
| `REC_ICHIMOKU_1M` | Rec Ichimoku\|1M | `Rec.Ichimoku\|1M` | rating |
| `REC_ICHIMOKU_1W` | Rec Ichimoku\|1W | `Rec.Ichimoku\|1W` | rating |
| `REC_ICHIMOKU_240` | Rec Ichimoku\|240 | `Rec.Ichimoku\|240` | rating |
| `REC_ICHIMOKU_30` | Rec Ichimoku\|30 | `Rec.Ichimoku\|30` | rating |
| `REC_ICHIMOKU_5` | Rec Ichimoku\|5 | `Rec.Ichimoku\|5` | rating |
| `REC_ICHIMOKU_60` | Rec Ichimoku\|60 | `Rec.Ichimoku\|60` | rating |

## Volatility Indicators

*143 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `ATRP` | Atrp | `ATRP` | float |
| `ATRP_1` | Atrp\|1 | `ATRP\|1` | float |
| `ATRP_120` | Atrp\|120 | `ATRP\|120` | float |
| `ATRP_15` | Atrp\|15 | `ATRP\|15` | float |
| `ATRP_1M` | Atrp\|1M | `ATRP\|1M` | float |
| `ATRP_1W` | Atrp\|1W | `ATRP\|1W` | float |
| `ATRP_240` | Atrp\|240 | `ATRP\|240` | float |
| `ATRP_30` | Atrp\|30 | `ATRP\|30` | float |
| `ATRP_5` | Atrp\|5 | `ATRP\|5` | float |
| `ATRP_60` | Atrp\|60 | `ATRP\|60` | float |
| `ATR_1` | ATR\|1 | `ATR\|1` | float |
| `ATR_120` | ATR\|120 | `ATR\|120` | float |
| `ATR_15` | ATR\|15 | `ATR\|15` | float |
| `ATR_1M` | ATR\|1M | `ATR\|1M` | float |
| `ATR_1W` | ATR\|1W | `ATR\|1W` | float |
| `ATR_240` | ATR\|240 | `ATR\|240` | float |
| `ATR_30` | ATR\|30 | `ATR\|30` | float |
| `ATR_5` | ATR\|5 | `ATR\|5` | float |
| `ATR_60` | ATR\|60 | `ATR\|60` | float |
| `AVERAGE_TRUE_RANGE_14` | Average True Range (14) | `ATR` | float |
| `BB_BASIS` | Bb Basis | `BB.basis` | float |
| `BB_BASIS_1` | Bb Basis\|1 | `BB.basis\|1` | float |
| `BB_BASIS_120` | Bb Basis\|120 | `BB.basis\|120` | float |
| `BB_BASIS_15` | Bb Basis\|15 | `BB.basis\|15` | float |
| `BB_BASIS_1M` | Bb Basis\|1M | `BB.basis\|1M` | float |
| `BB_BASIS_1W` | Bb Basis\|1W | `BB.basis\|1W` | float |
| `BB_BASIS_240` | Bb Basis\|240 | `BB.basis\|240` | float |
| `BB_BASIS_30` | Bb Basis\|30 | `BB.basis\|30` | float |
| `BB_BASIS_5` | Bb Basis\|5 | `BB.basis\|5` | float |
| `BB_BASIS_50` | Bb Basis 50 | `BB.basis_50` | float |
| `BB_BASIS_50_1` | Bb Basis 50\|1 | `BB.basis_50\|1` | float |
| `BB_BASIS_50_120` | Bb Basis 50\|120 | `BB.basis_50\|120` | float |
| `BB_BASIS_50_15` | Bb Basis 50\|15 | `BB.basis_50\|15` | float |
| `BB_BASIS_50_1M` | Bb Basis 50\|1M | `BB.basis_50\|1M` | float |
| `BB_BASIS_50_1W` | Bb Basis 50\|1W | `BB.basis_50\|1W` | float |
| `BB_BASIS_50_240` | Bb Basis 50\|240 | `BB.basis_50\|240` | float |
| `BB_BASIS_50_30` | Bb Basis 50\|30 | `BB.basis_50\|30` | float |
| `BB_BASIS_50_5` | Bb Basis 50\|5 | `BB.basis_50\|5` | float |
| `BB_BASIS_50_60` | Bb Basis 50\|60 | `BB.basis_50\|60` | float |
| `BB_BASIS_60` | Bb Basis\|60 | `BB.basis\|60` | float |
| `BB_LOWER_1` | Bb Lower\|1 | `BB.lower\|1` | float |
| `BB_LOWER_120` | Bb Lower\|120 | `BB.lower\|120` | float |
| `BB_LOWER_15` | Bb Lower\|15 | `BB.lower\|15` | float |
| `BB_LOWER_1M` | Bb Lower\|1M | `BB.lower\|1M` | float |
| `BB_LOWER_1W` | Bb Lower\|1W | `BB.lower\|1W` | float |
| `BB_LOWER_240` | Bb Lower\|240 | `BB.lower\|240` | float |
| `BB_LOWER_30` | Bb Lower\|30 | `BB.lower\|30` | float |
| `BB_LOWER_5` | Bb Lower\|5 | `BB.lower\|5` | float |
| `BB_LOWER_50` | Bb Lower 50 | `BB.lower_50` | float |
| `BB_LOWER_50_1` | Bb Lower 50\|1 | `BB.lower_50\|1` | float |
| `BB_LOWER_50_120` | Bb Lower 50\|120 | `BB.lower_50\|120` | float |
| `BB_LOWER_50_15` | Bb Lower 50\|15 | `BB.lower_50\|15` | float |
| `BB_LOWER_50_1M` | Bb Lower 50\|1M | `BB.lower_50\|1M` | float |
| `BB_LOWER_50_1W` | Bb Lower 50\|1W | `BB.lower_50\|1W` | float |
| `BB_LOWER_50_240` | Bb Lower 50\|240 | `BB.lower_50\|240` | float |
| `BB_LOWER_50_30` | Bb Lower 50\|30 | `BB.lower_50\|30` | float |
| `BB_LOWER_50_5` | Bb Lower 50\|5 | `BB.lower_50\|5` | float |
| `BB_LOWER_50_60` | Bb Lower 50\|60 | `BB.lower_50\|60` | float |
| `BB_LOWER_60` | Bb Lower\|60 | `BB.lower\|60` | float |
| `BB_UPPER_1` | Bb Upper\|1 | `BB.upper\|1` | float |
| `BB_UPPER_120` | Bb Upper\|120 | `BB.upper\|120` | float |
| `BB_UPPER_15` | Bb Upper\|15 | `BB.upper\|15` | float |
| `BB_UPPER_1M` | Bb Upper\|1M | `BB.upper\|1M` | float |
| `BB_UPPER_1W` | Bb Upper\|1W | `BB.upper\|1W` | float |
| `BB_UPPER_240` | Bb Upper\|240 | `BB.upper\|240` | float |
| `BB_UPPER_30` | Bb Upper\|30 | `BB.upper\|30` | float |
| `BB_UPPER_5` | Bb Upper\|5 | `BB.upper\|5` | float |
| `BB_UPPER_50` | Bb Upper 50 | `BB.upper_50` | float |
| `BB_UPPER_50_1` | Bb Upper 50\|1 | `BB.upper_50\|1` | float |
| `BB_UPPER_50_120` | Bb Upper 50\|120 | `BB.upper_50\|120` | float |
| `BB_UPPER_50_15` | Bb Upper 50\|15 | `BB.upper_50\|15` | float |
| `BB_UPPER_50_1M` | Bb Upper 50\|1M | `BB.upper_50\|1M` | float |
| `BB_UPPER_50_1W` | Bb Upper 50\|1W | `BB.upper_50\|1W` | float |
| `BB_UPPER_50_240` | Bb Upper 50\|240 | `BB.upper_50\|240` | float |
| `BB_UPPER_50_30` | Bb Upper 50\|30 | `BB.upper_50\|30` | float |
| `BB_UPPER_50_5` | Bb Upper 50\|5 | `BB.upper_50\|5` | float |
| `BB_UPPER_50_60` | Bb Upper 50\|60 | `BB.upper_50\|60` | float |
| `BB_UPPER_60` | Bb Upper\|60 | `BB.upper\|60` | float |
| `BOLLINGER_LOWER_BAND_20` | Bollinger Lower Band (20) | `BB.lower` | computed_recommendation |
| `BOLLINGER_UPPER_BAND_20` | Bollinger Upper Band (20) | `BB.upper` | computed_recommendation |
| `DONCHCH20_LOWER_1` | Donchch20 Lower\|1 | `DonchCh20.Lower\|1` | float |
| `DONCHCH20_LOWER_120` | Donchch20 Lower\|120 | `DonchCh20.Lower\|120` | float |
| `DONCHCH20_LOWER_15` | Donchch20 Lower\|15 | `DonchCh20.Lower\|15` | float |
| `DONCHCH20_LOWER_1M` | Donchch20 Lower\|1M | `DonchCh20.Lower\|1M` | float |
| `DONCHCH20_LOWER_1W` | Donchch20 Lower\|1W | `DonchCh20.Lower\|1W` | float |
| `DONCHCH20_LOWER_240` | Donchch20 Lower\|240 | `DonchCh20.Lower\|240` | float |
| `DONCHCH20_LOWER_30` | Donchch20 Lower\|30 | `DonchCh20.Lower\|30` | float |
| `DONCHCH20_LOWER_5` | Donchch20 Lower\|5 | `DonchCh20.Lower\|5` | float |
| `DONCHCH20_LOWER_60` | Donchch20 Lower\|60 | `DonchCh20.Lower\|60` | float |
| `DONCHCH20_MIDDLE` | Donchch20 Middle | `DonchCh20.Middle` | float |
| `DONCHCH20_MIDDLE_1` | Donchch20 Middle\|1 | `DonchCh20.Middle\|1` | float |
| `DONCHCH20_MIDDLE_120` | Donchch20 Middle\|120 | `DonchCh20.Middle\|120` | float |
| `DONCHCH20_MIDDLE_15` | Donchch20 Middle\|15 | `DonchCh20.Middle\|15` | float |
| `DONCHCH20_MIDDLE_1M` | Donchch20 Middle\|1M | `DonchCh20.Middle\|1M` | float |
| `DONCHCH20_MIDDLE_1W` | Donchch20 Middle\|1W | `DonchCh20.Middle\|1W` | float |
| `DONCHCH20_MIDDLE_240` | Donchch20 Middle\|240 | `DonchCh20.Middle\|240` | float |
| `DONCHCH20_MIDDLE_30` | Donchch20 Middle\|30 | `DonchCh20.Middle\|30` | float |
| `DONCHCH20_MIDDLE_5` | Donchch20 Middle\|5 | `DonchCh20.Middle\|5` | float |
| `DONCHCH20_MIDDLE_60` | Donchch20 Middle\|60 | `DonchCh20.Middle\|60` | float |
| `DONCHCH20_UPPER_1` | Donchch20 Upper\|1 | `DonchCh20.Upper\|1` | float |
| `DONCHCH20_UPPER_120` | Donchch20 Upper\|120 | `DonchCh20.Upper\|120` | float |
| `DONCHCH20_UPPER_15` | Donchch20 Upper\|15 | `DonchCh20.Upper\|15` | float |
| `DONCHCH20_UPPER_1M` | Donchch20 Upper\|1M | `DonchCh20.Upper\|1M` | float |
| `DONCHCH20_UPPER_1W` | Donchch20 Upper\|1W | `DonchCh20.Upper\|1W` | float |
| `DONCHCH20_UPPER_240` | Donchch20 Upper\|240 | `DonchCh20.Upper\|240` | float |
| `DONCHCH20_UPPER_30` | Donchch20 Upper\|30 | `DonchCh20.Upper\|30` | float |
| `DONCHCH20_UPPER_5` | Donchch20 Upper\|5 | `DonchCh20.Upper\|5` | float |
| `DONCHCH20_UPPER_60` | Donchch20 Upper\|60 | `DonchCh20.Upper\|60` | float |
| `DONCHIAN_CHANNELS_LOWER_BAND_20` | Donchian Channels Lower Band (20) | `DonchCh20.Lower` | float |
| `DONCHIAN_CHANNELS_UPPER_BAND_20` | Donchian Channels Upper Band (20) | `DonchCh20.Upper` | float |
| `KELTNER_CHANNELS_LOWER_BAND_20` | Keltner Channels Lower Band (20) | `KltChnl.lower` | float |
| `KELTNER_CHANNELS_UPPER_BAND_20` | Keltner Channels Upper Band (20) | `KltChnl.upper` | float |
| `KLTCHNL_BASIS` | Kltchnl Basis | `KltChnl.basis` | float |
| `KLTCHNL_BASIS_1` | Kltchnl Basis\|1 | `KltChnl.basis\|1` | float |
| `KLTCHNL_BASIS_120` | Kltchnl Basis\|120 | `KltChnl.basis\|120` | float |
| `KLTCHNL_BASIS_15` | Kltchnl Basis\|15 | `KltChnl.basis\|15` | float |
| `KLTCHNL_BASIS_1M` | Kltchnl Basis\|1M | `KltChnl.basis\|1M` | float |
| `KLTCHNL_BASIS_1W` | Kltchnl Basis\|1W | `KltChnl.basis\|1W` | float |
| `KLTCHNL_BASIS_240` | Kltchnl Basis\|240 | `KltChnl.basis\|240` | float |
| `KLTCHNL_BASIS_30` | Kltchnl Basis\|30 | `KltChnl.basis\|30` | float |
| `KLTCHNL_BASIS_5` | Kltchnl Basis\|5 | `KltChnl.basis\|5` | float |
| `KLTCHNL_BASIS_60` | Kltchnl Basis\|60 | `KltChnl.basis\|60` | float |
| `KLTCHNL_LOWER_1` | Kltchnl Lower\|1 | `KltChnl.lower\|1` | float |
| `KLTCHNL_LOWER_120` | Kltchnl Lower\|120 | `KltChnl.lower\|120` | float |
| `KLTCHNL_LOWER_15` | Kltchnl Lower\|15 | `KltChnl.lower\|15` | float |
| `KLTCHNL_LOWER_1M` | Kltchnl Lower\|1M | `KltChnl.lower\|1M` | float |
| `KLTCHNL_LOWER_1W` | Kltchnl Lower\|1W | `KltChnl.lower\|1W` | float |
| `KLTCHNL_LOWER_240` | Kltchnl Lower\|240 | `KltChnl.lower\|240` | float |
| `KLTCHNL_LOWER_30` | Kltchnl Lower\|30 | `KltChnl.lower\|30` | float |
| `KLTCHNL_LOWER_5` | Kltchnl Lower\|5 | `KltChnl.lower\|5` | float |
| `KLTCHNL_LOWER_60` | Kltchnl Lower\|60 | `KltChnl.lower\|60` | float |
| `KLTCHNL_UPPER_1` | Kltchnl Upper\|1 | `KltChnl.upper\|1` | float |
| `KLTCHNL_UPPER_120` | Kltchnl Upper\|120 | `KltChnl.upper\|120` | float |
| `KLTCHNL_UPPER_15` | Kltchnl Upper\|15 | `KltChnl.upper\|15` | float |
| `KLTCHNL_UPPER_1M` | Kltchnl Upper\|1M | `KltChnl.upper\|1M` | float |
| `KLTCHNL_UPPER_1W` | Kltchnl Upper\|1W | `KltChnl.upper\|1W` | float |
| `KLTCHNL_UPPER_240` | Kltchnl Upper\|240 | `KltChnl.upper\|240` | float |
| `KLTCHNL_UPPER_30` | Kltchnl Upper\|30 | `KltChnl.upper\|30` | float |
| `KLTCHNL_UPPER_5` | Kltchnl Upper\|5 | `KltChnl.upper\|5` | float |
| `KLTCHNL_UPPER_60` | Kltchnl Upper\|60 | `KltChnl.upper\|60` | float |
| `VOLATILITY` | Volatility | `Volatility.D` | percent |
| `VOLATILITY_MONTH` | Volatility Month | `Volatility.M` | percent |
| `VOLATILITY_WEEK` | Volatility Week | `Volatility.W` | percent |

## Pivot Points

*210 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `PIVOT_CAMARILLA_P` | Pivot Camarilla P | `Pivot.M.Camarilla.Middle` | float |
| `PIVOT_CAMARILLA_R1` | Pivot Camarilla R1 | `Pivot.M.Camarilla.R1` | float |
| `PIVOT_CAMARILLA_R2` | Pivot Camarilla R2 | `Pivot.M.Camarilla.R2` | float |
| `PIVOT_CAMARILLA_R3` | Pivot Camarilla R3 | `Pivot.M.Camarilla.R3` | float |
| `PIVOT_CAMARILLA_S1` | Pivot Camarilla S1 | `Pivot.M.Camarilla.S1` | float |
| `PIVOT_CAMARILLA_S2` | Pivot Camarilla S2 | `Pivot.M.Camarilla.S2` | float |
| `PIVOT_CAMARILLA_S3` | Pivot Camarilla S3 | `Pivot.M.Camarilla.S3` | float |
| `PIVOT_CLASSIC_P` | Pivot Classic P | `Pivot.M.Classic.Middle` | float |
| `PIVOT_CLASSIC_R1` | Pivot Classic R1 | `Pivot.M.Classic.R1` | float |
| `PIVOT_CLASSIC_R2` | Pivot Classic R2 | `Pivot.M.Classic.R2` | float |
| `PIVOT_CLASSIC_R3` | Pivot Classic R3 | `Pivot.M.Classic.R3` | float |
| `PIVOT_CLASSIC_S1` | Pivot Classic S1 | `Pivot.M.Classic.S1` | float |
| `PIVOT_CLASSIC_S2` | Pivot Classic S2 | `Pivot.M.Classic.S2` | float |
| `PIVOT_CLASSIC_S3` | Pivot Classic S3 | `Pivot.M.Classic.S3` | float |
| `PIVOT_M_CAMARILLA_MIDDLE_1` | Pivot M Camarilla Middle\|1 | `Pivot.M.Camarilla.Middle\|1` | float |
| `PIVOT_M_CAMARILLA_MIDDLE_120` | Pivot M Camarilla Middle\|120 | `Pivot.M.Camarilla.Middle\|120` | float |
| `PIVOT_M_CAMARILLA_MIDDLE_15` | Pivot M Camarilla Middle\|15 | `Pivot.M.Camarilla.Middle\|15` | float |
| `PIVOT_M_CAMARILLA_MIDDLE_1M` | Pivot M Camarilla Middle\|1M | `Pivot.M.Camarilla.Middle\|1M` | float |
| `PIVOT_M_CAMARILLA_MIDDLE_1W` | Pivot M Camarilla Middle\|1W | `Pivot.M.Camarilla.Middle\|1W` | float |
| `PIVOT_M_CAMARILLA_MIDDLE_240` | Pivot M Camarilla Middle\|240 | `Pivot.M.Camarilla.Middle\|240` | float |
| `PIVOT_M_CAMARILLA_MIDDLE_30` | Pivot M Camarilla Middle\|30 | `Pivot.M.Camarilla.Middle\|30` | float |
| `PIVOT_M_CAMARILLA_MIDDLE_5` | Pivot M Camarilla Middle\|5 | `Pivot.M.Camarilla.Middle\|5` | float |
| `PIVOT_M_CAMARILLA_MIDDLE_60` | Pivot M Camarilla Middle\|60 | `Pivot.M.Camarilla.Middle\|60` | float |
| `PIVOT_M_CAMARILLA_R1_1` | Pivot M Camarilla R1\|1 | `Pivot.M.Camarilla.R1\|1` | float |
| `PIVOT_M_CAMARILLA_R1_120` | Pivot M Camarilla R1\|120 | `Pivot.M.Camarilla.R1\|120` | float |
| `PIVOT_M_CAMARILLA_R1_15` | Pivot M Camarilla R1\|15 | `Pivot.M.Camarilla.R1\|15` | float |
| `PIVOT_M_CAMARILLA_R1_1M` | Pivot M Camarilla R1\|1M | `Pivot.M.Camarilla.R1\|1M` | float |
| `PIVOT_M_CAMARILLA_R1_1W` | Pivot M Camarilla R1\|1W | `Pivot.M.Camarilla.R1\|1W` | float |
| `PIVOT_M_CAMARILLA_R1_240` | Pivot M Camarilla R1\|240 | `Pivot.M.Camarilla.R1\|240` | float |
| `PIVOT_M_CAMARILLA_R1_30` | Pivot M Camarilla R1\|30 | `Pivot.M.Camarilla.R1\|30` | float |
| `PIVOT_M_CAMARILLA_R1_5` | Pivot M Camarilla R1\|5 | `Pivot.M.Camarilla.R1\|5` | float |
| `PIVOT_M_CAMARILLA_R1_60` | Pivot M Camarilla R1\|60 | `Pivot.M.Camarilla.R1\|60` | float |
| `PIVOT_M_CAMARILLA_R2_1` | Pivot M Camarilla R2\|1 | `Pivot.M.Camarilla.R2\|1` | float |
| `PIVOT_M_CAMARILLA_R2_120` | Pivot M Camarilla R2\|120 | `Pivot.M.Camarilla.R2\|120` | float |
| `PIVOT_M_CAMARILLA_R2_15` | Pivot M Camarilla R2\|15 | `Pivot.M.Camarilla.R2\|15` | float |
| `PIVOT_M_CAMARILLA_R2_1M` | Pivot M Camarilla R2\|1M | `Pivot.M.Camarilla.R2\|1M` | float |
| `PIVOT_M_CAMARILLA_R2_1W` | Pivot M Camarilla R2\|1W | `Pivot.M.Camarilla.R2\|1W` | float |
| `PIVOT_M_CAMARILLA_R2_240` | Pivot M Camarilla R2\|240 | `Pivot.M.Camarilla.R2\|240` | float |
| `PIVOT_M_CAMARILLA_R2_30` | Pivot M Camarilla R2\|30 | `Pivot.M.Camarilla.R2\|30` | float |
| `PIVOT_M_CAMARILLA_R2_5` | Pivot M Camarilla R2\|5 | `Pivot.M.Camarilla.R2\|5` | float |
| `PIVOT_M_CAMARILLA_R2_60` | Pivot M Camarilla R2\|60 | `Pivot.M.Camarilla.R2\|60` | float |
| `PIVOT_M_CAMARILLA_R3_1` | Pivot M Camarilla R3\|1 | `Pivot.M.Camarilla.R3\|1` | float |
| `PIVOT_M_CAMARILLA_R3_120` | Pivot M Camarilla R3\|120 | `Pivot.M.Camarilla.R3\|120` | float |
| `PIVOT_M_CAMARILLA_R3_15` | Pivot M Camarilla R3\|15 | `Pivot.M.Camarilla.R3\|15` | float |
| `PIVOT_M_CAMARILLA_R3_1M` | Pivot M Camarilla R3\|1M | `Pivot.M.Camarilla.R3\|1M` | float |
| `PIVOT_M_CAMARILLA_R3_1W` | Pivot M Camarilla R3\|1W | `Pivot.M.Camarilla.R3\|1W` | float |
| `PIVOT_M_CAMARILLA_R3_240` | Pivot M Camarilla R3\|240 | `Pivot.M.Camarilla.R3\|240` | float |
| `PIVOT_M_CAMARILLA_R3_30` | Pivot M Camarilla R3\|30 | `Pivot.M.Camarilla.R3\|30` | float |
| `PIVOT_M_CAMARILLA_R3_5` | Pivot M Camarilla R3\|5 | `Pivot.M.Camarilla.R3\|5` | float |
| `PIVOT_M_CAMARILLA_R3_60` | Pivot M Camarilla R3\|60 | `Pivot.M.Camarilla.R3\|60` | float |
| `PIVOT_M_CAMARILLA_S1_1` | Pivot M Camarilla S1\|1 | `Pivot.M.Camarilla.S1\|1` | float |
| `PIVOT_M_CAMARILLA_S1_120` | Pivot M Camarilla S1\|120 | `Pivot.M.Camarilla.S1\|120` | float |
| `PIVOT_M_CAMARILLA_S1_15` | Pivot M Camarilla S1\|15 | `Pivot.M.Camarilla.S1\|15` | float |
| `PIVOT_M_CAMARILLA_S1_1M` | Pivot M Camarilla S1\|1M | `Pivot.M.Camarilla.S1\|1M` | float |
| `PIVOT_M_CAMARILLA_S1_1W` | Pivot M Camarilla S1\|1W | `Pivot.M.Camarilla.S1\|1W` | float |
| `PIVOT_M_CAMARILLA_S1_240` | Pivot M Camarilla S1\|240 | `Pivot.M.Camarilla.S1\|240` | float |
| `PIVOT_M_CAMARILLA_S1_30` | Pivot M Camarilla S1\|30 | `Pivot.M.Camarilla.S1\|30` | float |
| `PIVOT_M_CAMARILLA_S1_5` | Pivot M Camarilla S1\|5 | `Pivot.M.Camarilla.S1\|5` | float |
| `PIVOT_M_CAMARILLA_S1_60` | Pivot M Camarilla S1\|60 | `Pivot.M.Camarilla.S1\|60` | float |
| `PIVOT_M_CAMARILLA_S2_1` | Pivot M Camarilla S2\|1 | `Pivot.M.Camarilla.S2\|1` | float |
| `PIVOT_M_CAMARILLA_S2_120` | Pivot M Camarilla S2\|120 | `Pivot.M.Camarilla.S2\|120` | float |
| `PIVOT_M_CAMARILLA_S2_15` | Pivot M Camarilla S2\|15 | `Pivot.M.Camarilla.S2\|15` | float |
| `PIVOT_M_CAMARILLA_S2_1M` | Pivot M Camarilla S2\|1M | `Pivot.M.Camarilla.S2\|1M` | float |
| `PIVOT_M_CAMARILLA_S2_1W` | Pivot M Camarilla S2\|1W | `Pivot.M.Camarilla.S2\|1W` | float |
| `PIVOT_M_CAMARILLA_S2_240` | Pivot M Camarilla S2\|240 | `Pivot.M.Camarilla.S2\|240` | float |
| `PIVOT_M_CAMARILLA_S2_30` | Pivot M Camarilla S2\|30 | `Pivot.M.Camarilla.S2\|30` | float |
| `PIVOT_M_CAMARILLA_S2_5` | Pivot M Camarilla S2\|5 | `Pivot.M.Camarilla.S2\|5` | float |
| `PIVOT_M_CAMARILLA_S2_60` | Pivot M Camarilla S2\|60 | `Pivot.M.Camarilla.S2\|60` | float |
| `PIVOT_M_CAMARILLA_S3_1` | Pivot M Camarilla S3\|1 | `Pivot.M.Camarilla.S3\|1` | float |
| `PIVOT_M_CAMARILLA_S3_120` | Pivot M Camarilla S3\|120 | `Pivot.M.Camarilla.S3\|120` | float |
| `PIVOT_M_CAMARILLA_S3_15` | Pivot M Camarilla S3\|15 | `Pivot.M.Camarilla.S3\|15` | float |
| `PIVOT_M_CAMARILLA_S3_1M` | Pivot M Camarilla S3\|1M | `Pivot.M.Camarilla.S3\|1M` | float |
| `PIVOT_M_CAMARILLA_S3_1W` | Pivot M Camarilla S3\|1W | `Pivot.M.Camarilla.S3\|1W` | float |
| `PIVOT_M_CAMARILLA_S3_240` | Pivot M Camarilla S3\|240 | `Pivot.M.Camarilla.S3\|240` | float |
| `PIVOT_M_CAMARILLA_S3_30` | Pivot M Camarilla S3\|30 | `Pivot.M.Camarilla.S3\|30` | float |
| `PIVOT_M_CAMARILLA_S3_5` | Pivot M Camarilla S3\|5 | `Pivot.M.Camarilla.S3\|5` | float |
| `PIVOT_M_CAMARILLA_S3_60` | Pivot M Camarilla S3\|60 | `Pivot.M.Camarilla.S3\|60` | float |
| `PIVOT_M_CLASSIC_MIDDLE_1` | Pivot M Classic Middle\|1 | `Pivot.M.Classic.Middle\|1` | float |
| `PIVOT_M_CLASSIC_MIDDLE_120` | Pivot M Classic Middle\|120 | `Pivot.M.Classic.Middle\|120` | float |
| `PIVOT_M_CLASSIC_MIDDLE_15` | Pivot M Classic Middle\|15 | `Pivot.M.Classic.Middle\|15` | float |
| `PIVOT_M_CLASSIC_MIDDLE_1M` | Pivot M Classic Middle\|1M | `Pivot.M.Classic.Middle\|1M` | float |
| `PIVOT_M_CLASSIC_MIDDLE_1W` | Pivot M Classic Middle\|1W | `Pivot.M.Classic.Middle\|1W` | float |
| `PIVOT_M_CLASSIC_MIDDLE_240` | Pivot M Classic Middle\|240 | `Pivot.M.Classic.Middle\|240` | float |
| `PIVOT_M_CLASSIC_MIDDLE_30` | Pivot M Classic Middle\|30 | `Pivot.M.Classic.Middle\|30` | float |
| `PIVOT_M_CLASSIC_MIDDLE_5` | Pivot M Classic Middle\|5 | `Pivot.M.Classic.Middle\|5` | float |
| `PIVOT_M_CLASSIC_MIDDLE_60` | Pivot M Classic Middle\|60 | `Pivot.M.Classic.Middle\|60` | float |
| `PIVOT_M_CLASSIC_R1_1` | Pivot M Classic R1\|1 | `Pivot.M.Classic.R1\|1` | float |
| `PIVOT_M_CLASSIC_R1_120` | Pivot M Classic R1\|120 | `Pivot.M.Classic.R1\|120` | float |
| `PIVOT_M_CLASSIC_R1_15` | Pivot M Classic R1\|15 | `Pivot.M.Classic.R1\|15` | float |
| `PIVOT_M_CLASSIC_R1_1M` | Pivot M Classic R1\|1M | `Pivot.M.Classic.R1\|1M` | float |
| `PIVOT_M_CLASSIC_R1_1W` | Pivot M Classic R1\|1W | `Pivot.M.Classic.R1\|1W` | float |
| `PIVOT_M_CLASSIC_R1_240` | Pivot M Classic R1\|240 | `Pivot.M.Classic.R1\|240` | float |
| `PIVOT_M_CLASSIC_R1_30` | Pivot M Classic R1\|30 | `Pivot.M.Classic.R1\|30` | float |
| `PIVOT_M_CLASSIC_R1_5` | Pivot M Classic R1\|5 | `Pivot.M.Classic.R1\|5` | float |
| `PIVOT_M_CLASSIC_R1_60` | Pivot M Classic R1\|60 | `Pivot.M.Classic.R1\|60` | float |
| `PIVOT_M_CLASSIC_R2_1` | Pivot M Classic R2\|1 | `Pivot.M.Classic.R2\|1` | float |
| `PIVOT_M_CLASSIC_R2_120` | Pivot M Classic R2\|120 | `Pivot.M.Classic.R2\|120` | float |
| `PIVOT_M_CLASSIC_R2_15` | Pivot M Classic R2\|15 | `Pivot.M.Classic.R2\|15` | float |
| `PIVOT_M_CLASSIC_R2_1M` | Pivot M Classic R2\|1M | `Pivot.M.Classic.R2\|1M` | float |
| `PIVOT_M_CLASSIC_R2_1W` | Pivot M Classic R2\|1W | `Pivot.M.Classic.R2\|1W` | float |
| `PIVOT_M_CLASSIC_R2_240` | Pivot M Classic R2\|240 | `Pivot.M.Classic.R2\|240` | float |
| `PIVOT_M_CLASSIC_R2_30` | Pivot M Classic R2\|30 | `Pivot.M.Classic.R2\|30` | float |
| `PIVOT_M_CLASSIC_R2_5` | Pivot M Classic R2\|5 | `Pivot.M.Classic.R2\|5` | float |
| `PIVOT_M_CLASSIC_R2_60` | Pivot M Classic R2\|60 | `Pivot.M.Classic.R2\|60` | float |
| `PIVOT_M_CLASSIC_R3_1` | Pivot M Classic R3\|1 | `Pivot.M.Classic.R3\|1` | float |
| `PIVOT_M_CLASSIC_R3_120` | Pivot M Classic R3\|120 | `Pivot.M.Classic.R3\|120` | float |
| `PIVOT_M_CLASSIC_R3_15` | Pivot M Classic R3\|15 | `Pivot.M.Classic.R3\|15` | float |
| `PIVOT_M_CLASSIC_R3_1M` | Pivot M Classic R3\|1M | `Pivot.M.Classic.R3\|1M` | float |
| `PIVOT_M_CLASSIC_R3_1W` | Pivot M Classic R3\|1W | `Pivot.M.Classic.R3\|1W` | float |
| `PIVOT_M_CLASSIC_R3_240` | Pivot M Classic R3\|240 | `Pivot.M.Classic.R3\|240` | float |
| `PIVOT_M_CLASSIC_R3_30` | Pivot M Classic R3\|30 | `Pivot.M.Classic.R3\|30` | float |
| `PIVOT_M_CLASSIC_R3_5` | Pivot M Classic R3\|5 | `Pivot.M.Classic.R3\|5` | float |
| `PIVOT_M_CLASSIC_R3_60` | Pivot M Classic R3\|60 | `Pivot.M.Classic.R3\|60` | float |
| `PIVOT_M_CLASSIC_S1_1` | Pivot M Classic S1\|1 | `Pivot.M.Classic.S1\|1` | float |
| `PIVOT_M_CLASSIC_S1_120` | Pivot M Classic S1\|120 | `Pivot.M.Classic.S1\|120` | float |
| `PIVOT_M_CLASSIC_S1_15` | Pivot M Classic S1\|15 | `Pivot.M.Classic.S1\|15` | float |
| `PIVOT_M_CLASSIC_S1_1M` | Pivot M Classic S1\|1M | `Pivot.M.Classic.S1\|1M` | float |
| `PIVOT_M_CLASSIC_S1_1W` | Pivot M Classic S1\|1W | `Pivot.M.Classic.S1\|1W` | float |
| `PIVOT_M_CLASSIC_S1_240` | Pivot M Classic S1\|240 | `Pivot.M.Classic.S1\|240` | float |
| `PIVOT_M_CLASSIC_S1_30` | Pivot M Classic S1\|30 | `Pivot.M.Classic.S1\|30` | float |
| `PIVOT_M_CLASSIC_S1_5` | Pivot M Classic S1\|5 | `Pivot.M.Classic.S1\|5` | float |
| `PIVOT_M_CLASSIC_S1_60` | Pivot M Classic S1\|60 | `Pivot.M.Classic.S1\|60` | float |
| `PIVOT_M_CLASSIC_S2_1` | Pivot M Classic S2\|1 | `Pivot.M.Classic.S2\|1` | float |
| `PIVOT_M_CLASSIC_S2_120` | Pivot M Classic S2\|120 | `Pivot.M.Classic.S2\|120` | float |
| `PIVOT_M_CLASSIC_S2_15` | Pivot M Classic S2\|15 | `Pivot.M.Classic.S2\|15` | float |
| `PIVOT_M_CLASSIC_S2_1M` | Pivot M Classic S2\|1M | `Pivot.M.Classic.S2\|1M` | float |
| `PIVOT_M_CLASSIC_S2_1W` | Pivot M Classic S2\|1W | `Pivot.M.Classic.S2\|1W` | float |
| `PIVOT_M_CLASSIC_S2_240` | Pivot M Classic S2\|240 | `Pivot.M.Classic.S2\|240` | float |
| `PIVOT_M_CLASSIC_S2_30` | Pivot M Classic S2\|30 | `Pivot.M.Classic.S2\|30` | float |
| `PIVOT_M_CLASSIC_S2_5` | Pivot M Classic S2\|5 | `Pivot.M.Classic.S2\|5` | float |
| `PIVOT_M_CLASSIC_S2_60` | Pivot M Classic S2\|60 | `Pivot.M.Classic.S2\|60` | float |
| `PIVOT_M_CLASSIC_S3_1` | Pivot M Classic S3\|1 | `Pivot.M.Classic.S3\|1` | float |
| `PIVOT_M_CLASSIC_S3_120` | Pivot M Classic S3\|120 | `Pivot.M.Classic.S3\|120` | float |
| `PIVOT_M_CLASSIC_S3_15` | Pivot M Classic S3\|15 | `Pivot.M.Classic.S3\|15` | float |
| `PIVOT_M_CLASSIC_S3_1M` | Pivot M Classic S3\|1M | `Pivot.M.Classic.S3\|1M` | float |
| `PIVOT_M_CLASSIC_S3_1W` | Pivot M Classic S3\|1W | `Pivot.M.Classic.S3\|1W` | float |
| `PIVOT_M_CLASSIC_S3_240` | Pivot M Classic S3\|240 | `Pivot.M.Classic.S3\|240` | float |
| `PIVOT_M_CLASSIC_S3_30` | Pivot M Classic S3\|30 | `Pivot.M.Classic.S3\|30` | float |
| `PIVOT_M_CLASSIC_S3_5` | Pivot M Classic S3\|5 | `Pivot.M.Classic.S3\|5` | float |
| `PIVOT_M_CLASSIC_S3_60` | Pivot M Classic S3\|60 | `Pivot.M.Classic.S3\|60` | float |
| `PIVOT_M_WOODIE_MIDDLE_1` | Pivot M Woodie Middle\|1 | `Pivot.M.Woodie.Middle\|1` | float |
| `PIVOT_M_WOODIE_MIDDLE_120` | Pivot M Woodie Middle\|120 | `Pivot.M.Woodie.Middle\|120` | float |
| `PIVOT_M_WOODIE_MIDDLE_15` | Pivot M Woodie Middle\|15 | `Pivot.M.Woodie.Middle\|15` | float |
| `PIVOT_M_WOODIE_MIDDLE_1M` | Pivot M Woodie Middle\|1M | `Pivot.M.Woodie.Middle\|1M` | float |
| `PIVOT_M_WOODIE_MIDDLE_1W` | Pivot M Woodie Middle\|1W | `Pivot.M.Woodie.Middle\|1W` | float |
| `PIVOT_M_WOODIE_MIDDLE_240` | Pivot M Woodie Middle\|240 | `Pivot.M.Woodie.Middle\|240` | float |
| `PIVOT_M_WOODIE_MIDDLE_30` | Pivot M Woodie Middle\|30 | `Pivot.M.Woodie.Middle\|30` | float |
| `PIVOT_M_WOODIE_MIDDLE_5` | Pivot M Woodie Middle\|5 | `Pivot.M.Woodie.Middle\|5` | float |
| `PIVOT_M_WOODIE_MIDDLE_60` | Pivot M Woodie Middle\|60 | `Pivot.M.Woodie.Middle\|60` | float |
| `PIVOT_M_WOODIE_R1_1` | Pivot M Woodie R1\|1 | `Pivot.M.Woodie.R1\|1` | float |
| `PIVOT_M_WOODIE_R1_120` | Pivot M Woodie R1\|120 | `Pivot.M.Woodie.R1\|120` | float |
| `PIVOT_M_WOODIE_R1_15` | Pivot M Woodie R1\|15 | `Pivot.M.Woodie.R1\|15` | float |
| `PIVOT_M_WOODIE_R1_1M` | Pivot M Woodie R1\|1M | `Pivot.M.Woodie.R1\|1M` | float |
| `PIVOT_M_WOODIE_R1_1W` | Pivot M Woodie R1\|1W | `Pivot.M.Woodie.R1\|1W` | float |
| `PIVOT_M_WOODIE_R1_240` | Pivot M Woodie R1\|240 | `Pivot.M.Woodie.R1\|240` | float |
| `PIVOT_M_WOODIE_R1_30` | Pivot M Woodie R1\|30 | `Pivot.M.Woodie.R1\|30` | float |
| `PIVOT_M_WOODIE_R1_5` | Pivot M Woodie R1\|5 | `Pivot.M.Woodie.R1\|5` | float |
| `PIVOT_M_WOODIE_R1_60` | Pivot M Woodie R1\|60 | `Pivot.M.Woodie.R1\|60` | float |
| `PIVOT_M_WOODIE_R2_1` | Pivot M Woodie R2\|1 | `Pivot.M.Woodie.R2\|1` | float |
| `PIVOT_M_WOODIE_R2_120` | Pivot M Woodie R2\|120 | `Pivot.M.Woodie.R2\|120` | float |
| `PIVOT_M_WOODIE_R2_15` | Pivot M Woodie R2\|15 | `Pivot.M.Woodie.R2\|15` | float |
| `PIVOT_M_WOODIE_R2_1M` | Pivot M Woodie R2\|1M | `Pivot.M.Woodie.R2\|1M` | float |
| `PIVOT_M_WOODIE_R2_1W` | Pivot M Woodie R2\|1W | `Pivot.M.Woodie.R2\|1W` | float |
| `PIVOT_M_WOODIE_R2_240` | Pivot M Woodie R2\|240 | `Pivot.M.Woodie.R2\|240` | float |
| `PIVOT_M_WOODIE_R2_30` | Pivot M Woodie R2\|30 | `Pivot.M.Woodie.R2\|30` | float |
| `PIVOT_M_WOODIE_R2_5` | Pivot M Woodie R2\|5 | `Pivot.M.Woodie.R2\|5` | float |
| `PIVOT_M_WOODIE_R2_60` | Pivot M Woodie R2\|60 | `Pivot.M.Woodie.R2\|60` | float |
| `PIVOT_M_WOODIE_R3_1` | Pivot M Woodie R3\|1 | `Pivot.M.Woodie.R3\|1` | float |
| `PIVOT_M_WOODIE_R3_120` | Pivot M Woodie R3\|120 | `Pivot.M.Woodie.R3\|120` | float |
| `PIVOT_M_WOODIE_R3_15` | Pivot M Woodie R3\|15 | `Pivot.M.Woodie.R3\|15` | float |
| `PIVOT_M_WOODIE_R3_1M` | Pivot M Woodie R3\|1M | `Pivot.M.Woodie.R3\|1M` | float |
| `PIVOT_M_WOODIE_R3_1W` | Pivot M Woodie R3\|1W | `Pivot.M.Woodie.R3\|1W` | float |
| `PIVOT_M_WOODIE_R3_240` | Pivot M Woodie R3\|240 | `Pivot.M.Woodie.R3\|240` | float |
| `PIVOT_M_WOODIE_R3_30` | Pivot M Woodie R3\|30 | `Pivot.M.Woodie.R3\|30` | float |
| `PIVOT_M_WOODIE_R3_5` | Pivot M Woodie R3\|5 | `Pivot.M.Woodie.R3\|5` | float |
| `PIVOT_M_WOODIE_R3_60` | Pivot M Woodie R3\|60 | `Pivot.M.Woodie.R3\|60` | float |
| `PIVOT_M_WOODIE_S1_1` | Pivot M Woodie S1\|1 | `Pivot.M.Woodie.S1\|1` | float |
| `PIVOT_M_WOODIE_S1_120` | Pivot M Woodie S1\|120 | `Pivot.M.Woodie.S1\|120` | float |
| `PIVOT_M_WOODIE_S1_15` | Pivot M Woodie S1\|15 | `Pivot.M.Woodie.S1\|15` | float |
| `PIVOT_M_WOODIE_S1_1M` | Pivot M Woodie S1\|1M | `Pivot.M.Woodie.S1\|1M` | float |
| `PIVOT_M_WOODIE_S1_1W` | Pivot M Woodie S1\|1W | `Pivot.M.Woodie.S1\|1W` | float |
| `PIVOT_M_WOODIE_S1_240` | Pivot M Woodie S1\|240 | `Pivot.M.Woodie.S1\|240` | float |
| `PIVOT_M_WOODIE_S1_30` | Pivot M Woodie S1\|30 | `Pivot.M.Woodie.S1\|30` | float |
| `PIVOT_M_WOODIE_S1_5` | Pivot M Woodie S1\|5 | `Pivot.M.Woodie.S1\|5` | float |
| `PIVOT_M_WOODIE_S1_60` | Pivot M Woodie S1\|60 | `Pivot.M.Woodie.S1\|60` | float |
| `PIVOT_M_WOODIE_S2_1` | Pivot M Woodie S2\|1 | `Pivot.M.Woodie.S2\|1` | float |
| `PIVOT_M_WOODIE_S2_120` | Pivot M Woodie S2\|120 | `Pivot.M.Woodie.S2\|120` | float |
| `PIVOT_M_WOODIE_S2_15` | Pivot M Woodie S2\|15 | `Pivot.M.Woodie.S2\|15` | float |
| `PIVOT_M_WOODIE_S2_1M` | Pivot M Woodie S2\|1M | `Pivot.M.Woodie.S2\|1M` | float |
| `PIVOT_M_WOODIE_S2_1W` | Pivot M Woodie S2\|1W | `Pivot.M.Woodie.S2\|1W` | float |
| `PIVOT_M_WOODIE_S2_240` | Pivot M Woodie S2\|240 | `Pivot.M.Woodie.S2\|240` | float |
| `PIVOT_M_WOODIE_S2_30` | Pivot M Woodie S2\|30 | `Pivot.M.Woodie.S2\|30` | float |
| `PIVOT_M_WOODIE_S2_5` | Pivot M Woodie S2\|5 | `Pivot.M.Woodie.S2\|5` | float |
| `PIVOT_M_WOODIE_S2_60` | Pivot M Woodie S2\|60 | `Pivot.M.Woodie.S2\|60` | float |
| `PIVOT_M_WOODIE_S3_1` | Pivot M Woodie S3\|1 | `Pivot.M.Woodie.S3\|1` | float |
| `PIVOT_M_WOODIE_S3_120` | Pivot M Woodie S3\|120 | `Pivot.M.Woodie.S3\|120` | float |
| `PIVOT_M_WOODIE_S3_15` | Pivot M Woodie S3\|15 | `Pivot.M.Woodie.S3\|15` | float |
| `PIVOT_M_WOODIE_S3_1M` | Pivot M Woodie S3\|1M | `Pivot.M.Woodie.S3\|1M` | float |
| `PIVOT_M_WOODIE_S3_1W` | Pivot M Woodie S3\|1W | `Pivot.M.Woodie.S3\|1W` | float |
| `PIVOT_M_WOODIE_S3_240` | Pivot M Woodie S3\|240 | `Pivot.M.Woodie.S3\|240` | float |
| `PIVOT_M_WOODIE_S3_30` | Pivot M Woodie S3\|30 | `Pivot.M.Woodie.S3\|30` | float |
| `PIVOT_M_WOODIE_S3_5` | Pivot M Woodie S3\|5 | `Pivot.M.Woodie.S3\|5` | float |
| `PIVOT_M_WOODIE_S3_60` | Pivot M Woodie S3\|60 | `Pivot.M.Woodie.S3\|60` | float |
| `PIVOT_WOODIE_P` | Pivot Woodie P | `Pivot.M.Woodie.Middle` | float |
| `PIVOT_WOODIE_R1` | Pivot Woodie R1 | `Pivot.M.Woodie.R1` | float |
| `PIVOT_WOODIE_R2` | Pivot Woodie R2 | `Pivot.M.Woodie.R2` | float |
| `PIVOT_WOODIE_R3` | Pivot Woodie R3 | `Pivot.M.Woodie.R3` | float |
| `PIVOT_WOODIE_S1` | Pivot Woodie S1 | `Pivot.M.Woodie.S1` | float |
| `PIVOT_WOODIE_S2` | Pivot Woodie S2 | `Pivot.M.Woodie.S2` | float |
| `PIVOT_WOODIE_S3` | Pivot Woodie S3 | `Pivot.M.Woodie.S3` | float |

## Candlestick Patterns

*271 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `CANDLE_3BLACKCROWS` | Candle.3BlackCrows | `Candle.3BlackCrows` | bool |
| `CANDLE_3BLACKCROWS_1` | Candle 3Blackcrows\|1 | `Candle.3BlackCrows\|1` | bool |
| `CANDLE_3BLACKCROWS_120` | Candle 3Blackcrows\|120 | `Candle.3BlackCrows\|120` | bool |
| `CANDLE_3BLACKCROWS_15` | Candle 3Blackcrows\|15 | `Candle.3BlackCrows\|15` | bool |
| `CANDLE_3BLACKCROWS_1M` | Candle 3Blackcrows\|1M | `Candle.3BlackCrows\|1M` | bool |
| `CANDLE_3BLACKCROWS_1W` | Candle 3Blackcrows\|1W | `Candle.3BlackCrows\|1W` | bool |
| `CANDLE_3BLACKCROWS_240` | Candle 3Blackcrows\|240 | `Candle.3BlackCrows\|240` | bool |
| `CANDLE_3BLACKCROWS_30` | Candle 3Blackcrows\|30 | `Candle.3BlackCrows\|30` | bool |
| `CANDLE_3BLACKCROWS_5` | Candle 3Blackcrows\|5 | `Candle.3BlackCrows\|5` | bool |
| `CANDLE_3BLACKCROWS_60` | Candle 3Blackcrows\|60 | `Candle.3BlackCrows\|60` | bool |
| `CANDLE_3WHITESOLDIERS` | Candle.3WhiteSoldiers | `Candle.3WhiteSoldiers` | bool |
| `CANDLE_3WHITESOLDIERS_1` | Candle 3Whitesoldiers\|1 | `Candle.3WhiteSoldiers\|1` | bool |
| `CANDLE_3WHITESOLDIERS_120` | Candle 3Whitesoldiers\|120 | `Candle.3WhiteSoldiers\|120` | bool |
| `CANDLE_3WHITESOLDIERS_15` | Candle 3Whitesoldiers\|15 | `Candle.3WhiteSoldiers\|15` | bool |
| `CANDLE_3WHITESOLDIERS_1M` | Candle 3Whitesoldiers\|1M | `Candle.3WhiteSoldiers\|1M` | bool |
| `CANDLE_3WHITESOLDIERS_1W` | Candle 3Whitesoldiers\|1W | `Candle.3WhiteSoldiers\|1W` | bool |
| `CANDLE_3WHITESOLDIERS_240` | Candle 3Whitesoldiers\|240 | `Candle.3WhiteSoldiers\|240` | bool |
| `CANDLE_3WHITESOLDIERS_30` | Candle 3Whitesoldiers\|30 | `Candle.3WhiteSoldiers\|30` | bool |
| `CANDLE_3WHITESOLDIERS_5` | Candle 3Whitesoldiers\|5 | `Candle.3WhiteSoldiers\|5` | bool |
| `CANDLE_3WHITESOLDIERS_60` | Candle 3Whitesoldiers\|60 | `Candle.3WhiteSoldiers\|60` | bool |
| `CANDLE_ABANDONEDBABY_BEARISH` | Candle.AbandonedBaby.Bearish | `Candle.AbandonedBaby.Bearish` | bool |
| `CANDLE_ABANDONEDBABY_BEARISH_1` | Candle Abandonedbaby Bearish\|1 | `Candle.AbandonedBaby.Bearish\|1` | bool |
| `CANDLE_ABANDONEDBABY_BEARISH_120` | Candle Abandonedbaby Bearish\|120 | `Candle.AbandonedBaby.Bearish\|120` | bool |
| `CANDLE_ABANDONEDBABY_BEARISH_15` | Candle Abandonedbaby Bearish\|15 | `Candle.AbandonedBaby.Bearish\|15` | bool |
| `CANDLE_ABANDONEDBABY_BEARISH_1M` | Candle Abandonedbaby Bearish\|1M | `Candle.AbandonedBaby.Bearish\|1M` | bool |
| `CANDLE_ABANDONEDBABY_BEARISH_1W` | Candle Abandonedbaby Bearish\|1W | `Candle.AbandonedBaby.Bearish\|1W` | bool |
| `CANDLE_ABANDONEDBABY_BEARISH_240` | Candle Abandonedbaby Bearish\|240 | `Candle.AbandonedBaby.Bearish\|240` | bool |
| `CANDLE_ABANDONEDBABY_BEARISH_30` | Candle Abandonedbaby Bearish\|30 | `Candle.AbandonedBaby.Bearish\|30` | bool |
| `CANDLE_ABANDONEDBABY_BEARISH_5` | Candle Abandonedbaby Bearish\|5 | `Candle.AbandonedBaby.Bearish\|5` | bool |
| `CANDLE_ABANDONEDBABY_BEARISH_60` | Candle Abandonedbaby Bearish\|60 | `Candle.AbandonedBaby.Bearish\|60` | bool |
| `CANDLE_ABANDONEDBABY_BULLISH` | Candle.AbandonedBaby.Bullish | `Candle.AbandonedBaby.Bullish` | bool |
| `CANDLE_ABANDONEDBABY_BULLISH_1` | Candle Abandonedbaby Bullish\|1 | `Candle.AbandonedBaby.Bullish\|1` | bool |
| `CANDLE_ABANDONEDBABY_BULLISH_120` | Candle Abandonedbaby Bullish\|120 | `Candle.AbandonedBaby.Bullish\|120` | bool |
| `CANDLE_ABANDONEDBABY_BULLISH_15` | Candle Abandonedbaby Bullish\|15 | `Candle.AbandonedBaby.Bullish\|15` | bool |
| `CANDLE_ABANDONEDBABY_BULLISH_1M` | Candle Abandonedbaby Bullish\|1M | `Candle.AbandonedBaby.Bullish\|1M` | bool |
| `CANDLE_ABANDONEDBABY_BULLISH_1W` | Candle Abandonedbaby Bullish\|1W | `Candle.AbandonedBaby.Bullish\|1W` | bool |
| `CANDLE_ABANDONEDBABY_BULLISH_240` | Candle Abandonedbaby Bullish\|240 | `Candle.AbandonedBaby.Bullish\|240` | bool |
| `CANDLE_ABANDONEDBABY_BULLISH_30` | Candle Abandonedbaby Bullish\|30 | `Candle.AbandonedBaby.Bullish\|30` | bool |
| `CANDLE_ABANDONEDBABY_BULLISH_5` | Candle Abandonedbaby Bullish\|5 | `Candle.AbandonedBaby.Bullish\|5` | bool |
| `CANDLE_ABANDONEDBABY_BULLISH_60` | Candle Abandonedbaby Bullish\|60 | `Candle.AbandonedBaby.Bullish\|60` | bool |
| `CANDLE_DOJI` | Candle.Doji | `Candle.Doji` | bool |
| `CANDLE_DOJI_1` | Candle Doji\|1 | `Candle.Doji\|1` | bool |
| `CANDLE_DOJI_120` | Candle Doji\|120 | `Candle.Doji\|120` | bool |
| `CANDLE_DOJI_15` | Candle Doji\|15 | `Candle.Doji\|15` | bool |
| `CANDLE_DOJI_1M` | Candle Doji\|1M | `Candle.Doji\|1M` | bool |
| `CANDLE_DOJI_1W` | Candle Doji\|1W | `Candle.Doji\|1W` | bool |
| `CANDLE_DOJI_240` | Candle Doji\|240 | `Candle.Doji\|240` | bool |
| `CANDLE_DOJI_30` | Candle Doji\|30 | `Candle.Doji\|30` | bool |
| `CANDLE_DOJI_5` | Candle Doji\|5 | `Candle.Doji\|5` | bool |
| `CANDLE_DOJI_60` | Candle Doji\|60 | `Candle.Doji\|60` | bool |
| `CANDLE_DOJI_DRAGONFLY` | Candle.Doji.Dragonfly | `Candle.Doji.Dragonfly` | bool |
| `CANDLE_DOJI_DRAGONFLY_1` | Candle Doji Dragonfly\|1 | `Candle.Doji.Dragonfly\|1` | bool |
| `CANDLE_DOJI_DRAGONFLY_120` | Candle Doji Dragonfly\|120 | `Candle.Doji.Dragonfly\|120` | bool |
| `CANDLE_DOJI_DRAGONFLY_15` | Candle Doji Dragonfly\|15 | `Candle.Doji.Dragonfly\|15` | bool |
| `CANDLE_DOJI_DRAGONFLY_1M` | Candle Doji Dragonfly\|1M | `Candle.Doji.Dragonfly\|1M` | bool |
| `CANDLE_DOJI_DRAGONFLY_1W` | Candle Doji Dragonfly\|1W | `Candle.Doji.Dragonfly\|1W` | bool |
| `CANDLE_DOJI_DRAGONFLY_240` | Candle Doji Dragonfly\|240 | `Candle.Doji.Dragonfly\|240` | bool |
| `CANDLE_DOJI_DRAGONFLY_30` | Candle Doji Dragonfly\|30 | `Candle.Doji.Dragonfly\|30` | bool |
| `CANDLE_DOJI_DRAGONFLY_5` | Candle Doji Dragonfly\|5 | `Candle.Doji.Dragonfly\|5` | bool |
| `CANDLE_DOJI_DRAGONFLY_60` | Candle Doji Dragonfly\|60 | `Candle.Doji.Dragonfly\|60` | bool |
| `CANDLE_DOJI_GRAVESTONE` | Candle.Doji.Gravestone | `Candle.Doji.Gravestone` | bool |
| `CANDLE_DOJI_GRAVESTONE_1` | Candle Doji Gravestone\|1 | `Candle.Doji.Gravestone\|1` | bool |
| `CANDLE_DOJI_GRAVESTONE_120` | Candle Doji Gravestone\|120 | `Candle.Doji.Gravestone\|120` | bool |
| `CANDLE_DOJI_GRAVESTONE_15` | Candle Doji Gravestone\|15 | `Candle.Doji.Gravestone\|15` | bool |
| `CANDLE_DOJI_GRAVESTONE_1M` | Candle Doji Gravestone\|1M | `Candle.Doji.Gravestone\|1M` | bool |
| `CANDLE_DOJI_GRAVESTONE_1W` | Candle Doji Gravestone\|1W | `Candle.Doji.Gravestone\|1W` | bool |
| `CANDLE_DOJI_GRAVESTONE_240` | Candle Doji Gravestone\|240 | `Candle.Doji.Gravestone\|240` | bool |
| `CANDLE_DOJI_GRAVESTONE_30` | Candle Doji Gravestone\|30 | `Candle.Doji.Gravestone\|30` | bool |
| `CANDLE_DOJI_GRAVESTONE_5` | Candle Doji Gravestone\|5 | `Candle.Doji.Gravestone\|5` | bool |
| `CANDLE_DOJI_GRAVESTONE_60` | Candle Doji Gravestone\|60 | `Candle.Doji.Gravestone\|60` | bool |
| `CANDLE_ENGULFING_BEARISH` | Candle.Engulfing.Bearish | `Candle.Engulfing.Bearish` | bool |
| `CANDLE_ENGULFING_BEARISH_1` | Candle Engulfing Bearish\|1 | `Candle.Engulfing.Bearish\|1` | bool |
| `CANDLE_ENGULFING_BEARISH_120` | Candle Engulfing Bearish\|120 | `Candle.Engulfing.Bearish\|120` | bool |
| `CANDLE_ENGULFING_BEARISH_15` | Candle Engulfing Bearish\|15 | `Candle.Engulfing.Bearish\|15` | bool |
| `CANDLE_ENGULFING_BEARISH_1M` | Candle Engulfing Bearish\|1M | `Candle.Engulfing.Bearish\|1M` | bool |
| `CANDLE_ENGULFING_BEARISH_1W` | Candle Engulfing Bearish\|1W | `Candle.Engulfing.Bearish\|1W` | bool |
| `CANDLE_ENGULFING_BEARISH_240` | Candle Engulfing Bearish\|240 | `Candle.Engulfing.Bearish\|240` | bool |
| `CANDLE_ENGULFING_BEARISH_30` | Candle Engulfing Bearish\|30 | `Candle.Engulfing.Bearish\|30` | bool |
| `CANDLE_ENGULFING_BEARISH_5` | Candle Engulfing Bearish\|5 | `Candle.Engulfing.Bearish\|5` | bool |
| `CANDLE_ENGULFING_BEARISH_60` | Candle Engulfing Bearish\|60 | `Candle.Engulfing.Bearish\|60` | bool |
| `CANDLE_ENGULFING_BULLISH` | Candle.Engulfing.Bullish | `Candle.Engulfing.Bullish` | bool |
| `CANDLE_ENGULFING_BULLISH_1` | Candle Engulfing Bullish\|1 | `Candle.Engulfing.Bullish\|1` | bool |
| `CANDLE_ENGULFING_BULLISH_120` | Candle Engulfing Bullish\|120 | `Candle.Engulfing.Bullish\|120` | bool |
| `CANDLE_ENGULFING_BULLISH_15` | Candle Engulfing Bullish\|15 | `Candle.Engulfing.Bullish\|15` | bool |
| `CANDLE_ENGULFING_BULLISH_1M` | Candle Engulfing Bullish\|1M | `Candle.Engulfing.Bullish\|1M` | bool |
| `CANDLE_ENGULFING_BULLISH_1W` | Candle Engulfing Bullish\|1W | `Candle.Engulfing.Bullish\|1W` | bool |
| `CANDLE_ENGULFING_BULLISH_240` | Candle Engulfing Bullish\|240 | `Candle.Engulfing.Bullish\|240` | bool |
| `CANDLE_ENGULFING_BULLISH_30` | Candle Engulfing Bullish\|30 | `Candle.Engulfing.Bullish\|30` | bool |
| `CANDLE_ENGULFING_BULLISH_5` | Candle Engulfing Bullish\|5 | `Candle.Engulfing.Bullish\|5` | bool |
| `CANDLE_ENGULFING_BULLISH_60` | Candle Engulfing Bullish\|60 | `Candle.Engulfing.Bullish\|60` | bool |
| `CANDLE_EVENINGSTAR` | Candle.EveningStar | `Candle.EveningStar` | bool |
| `CANDLE_EVENINGSTAR_1` | Candle Eveningstar\|1 | `Candle.EveningStar\|1` | bool |
| `CANDLE_EVENINGSTAR_120` | Candle Eveningstar\|120 | `Candle.EveningStar\|120` | bool |
| `CANDLE_EVENINGSTAR_15` | Candle Eveningstar\|15 | `Candle.EveningStar\|15` | bool |
| `CANDLE_EVENINGSTAR_1M` | Candle Eveningstar\|1M | `Candle.EveningStar\|1M` | bool |
| `CANDLE_EVENINGSTAR_1W` | Candle Eveningstar\|1W | `Candle.EveningStar\|1W` | bool |
| `CANDLE_EVENINGSTAR_240` | Candle Eveningstar\|240 | `Candle.EveningStar\|240` | bool |
| `CANDLE_EVENINGSTAR_30` | Candle Eveningstar\|30 | `Candle.EveningStar\|30` | bool |
| `CANDLE_EVENINGSTAR_5` | Candle Eveningstar\|5 | `Candle.EveningStar\|5` | bool |
| `CANDLE_EVENINGSTAR_60` | Candle Eveningstar\|60 | `Candle.EveningStar\|60` | bool |
| `CANDLE_HAMMER` | Candle.Hammer | `Candle.Hammer` | bool |
| `CANDLE_HAMMER_1` | Candle Hammer\|1 | `Candle.Hammer\|1` | bool |
| `CANDLE_HAMMER_120` | Candle Hammer\|120 | `Candle.Hammer\|120` | bool |
| `CANDLE_HAMMER_15` | Candle Hammer\|15 | `Candle.Hammer\|15` | bool |
| `CANDLE_HAMMER_1M` | Candle Hammer\|1M | `Candle.Hammer\|1M` | bool |
| `CANDLE_HAMMER_1W` | Candle Hammer\|1W | `Candle.Hammer\|1W` | bool |
| `CANDLE_HAMMER_240` | Candle Hammer\|240 | `Candle.Hammer\|240` | bool |
| `CANDLE_HAMMER_30` | Candle Hammer\|30 | `Candle.Hammer\|30` | bool |
| `CANDLE_HAMMER_5` | Candle Hammer\|5 | `Candle.Hammer\|5` | bool |
| `CANDLE_HAMMER_60` | Candle Hammer\|60 | `Candle.Hammer\|60` | bool |
| `CANDLE_HANGINGMAN` | Candle.HangingMan | `Candle.HangingMan` | bool |
| `CANDLE_HANGINGMAN_1` | Candle Hangingman\|1 | `Candle.HangingMan\|1` | bool |
| `CANDLE_HANGINGMAN_120` | Candle Hangingman\|120 | `Candle.HangingMan\|120` | bool |
| `CANDLE_HANGINGMAN_15` | Candle Hangingman\|15 | `Candle.HangingMan\|15` | bool |
| `CANDLE_HANGINGMAN_1M` | Candle Hangingman\|1M | `Candle.HangingMan\|1M` | bool |
| `CANDLE_HANGINGMAN_1W` | Candle Hangingman\|1W | `Candle.HangingMan\|1W` | bool |
| `CANDLE_HANGINGMAN_240` | Candle Hangingman\|240 | `Candle.HangingMan\|240` | bool |
| `CANDLE_HANGINGMAN_30` | Candle Hangingman\|30 | `Candle.HangingMan\|30` | bool |
| `CANDLE_HANGINGMAN_5` | Candle Hangingman\|5 | `Candle.HangingMan\|5` | bool |
| `CANDLE_HANGINGMAN_60` | Candle Hangingman\|60 | `Candle.HangingMan\|60` | bool |
| `CANDLE_HARAMI_BEARISH` | Candle.Harami.Bearish | `Candle.Harami.Bearish` | bool |
| `CANDLE_HARAMI_BEARISH_1` | Candle Harami Bearish\|1 | `Candle.Harami.Bearish\|1` | bool |
| `CANDLE_HARAMI_BEARISH_120` | Candle Harami Bearish\|120 | `Candle.Harami.Bearish\|120` | bool |
| `CANDLE_HARAMI_BEARISH_15` | Candle Harami Bearish\|15 | `Candle.Harami.Bearish\|15` | bool |
| `CANDLE_HARAMI_BEARISH_1M` | Candle Harami Bearish\|1M | `Candle.Harami.Bearish\|1M` | bool |
| `CANDLE_HARAMI_BEARISH_1W` | Candle Harami Bearish\|1W | `Candle.Harami.Bearish\|1W` | bool |
| `CANDLE_HARAMI_BEARISH_240` | Candle Harami Bearish\|240 | `Candle.Harami.Bearish\|240` | bool |
| `CANDLE_HARAMI_BEARISH_30` | Candle Harami Bearish\|30 | `Candle.Harami.Bearish\|30` | bool |
| `CANDLE_HARAMI_BEARISH_5` | Candle Harami Bearish\|5 | `Candle.Harami.Bearish\|5` | bool |
| `CANDLE_HARAMI_BEARISH_60` | Candle Harami Bearish\|60 | `Candle.Harami.Bearish\|60` | bool |
| `CANDLE_HARAMI_BULLISH` | Candle.Harami.Bullish | `Candle.Harami.Bullish` | bool |
| `CANDLE_HARAMI_BULLISH_1` | Candle Harami Bullish\|1 | `Candle.Harami.Bullish\|1` | bool |
| `CANDLE_HARAMI_BULLISH_120` | Candle Harami Bullish\|120 | `Candle.Harami.Bullish\|120` | bool |
| `CANDLE_HARAMI_BULLISH_15` | Candle Harami Bullish\|15 | `Candle.Harami.Bullish\|15` | bool |
| `CANDLE_HARAMI_BULLISH_1M` | Candle Harami Bullish\|1M | `Candle.Harami.Bullish\|1M` | bool |
| `CANDLE_HARAMI_BULLISH_1W` | Candle Harami Bullish\|1W | `Candle.Harami.Bullish\|1W` | bool |
| `CANDLE_HARAMI_BULLISH_240` | Candle Harami Bullish\|240 | `Candle.Harami.Bullish\|240` | bool |
| `CANDLE_HARAMI_BULLISH_30` | Candle Harami Bullish\|30 | `Candle.Harami.Bullish\|30` | bool |
| `CANDLE_HARAMI_BULLISH_5` | Candle Harami Bullish\|5 | `Candle.Harami.Bullish\|5` | bool |
| `CANDLE_HARAMI_BULLISH_60` | Candle Harami Bullish\|60 | `Candle.Harami.Bullish\|60` | bool |
| `CANDLE_INVERTEDHAMMER` | Candle.InvertedHammer | `Candle.InvertedHammer` | bool |
| `CANDLE_INVERTEDHAMMER_1` | Candle Invertedhammer\|1 | `Candle.InvertedHammer\|1` | bool |
| `CANDLE_INVERTEDHAMMER_120` | Candle Invertedhammer\|120 | `Candle.InvertedHammer\|120` | bool |
| `CANDLE_INVERTEDHAMMER_15` | Candle Invertedhammer\|15 | `Candle.InvertedHammer\|15` | bool |
| `CANDLE_INVERTEDHAMMER_1M` | Candle Invertedhammer\|1M | `Candle.InvertedHammer\|1M` | bool |
| `CANDLE_INVERTEDHAMMER_1W` | Candle Invertedhammer\|1W | `Candle.InvertedHammer\|1W` | bool |
| `CANDLE_INVERTEDHAMMER_240` | Candle Invertedhammer\|240 | `Candle.InvertedHammer\|240` | bool |
| `CANDLE_INVERTEDHAMMER_30` | Candle Invertedhammer\|30 | `Candle.InvertedHammer\|30` | bool |
| `CANDLE_INVERTEDHAMMER_5` | Candle Invertedhammer\|5 | `Candle.InvertedHammer\|5` | bool |
| `CANDLE_INVERTEDHAMMER_60` | Candle Invertedhammer\|60 | `Candle.InvertedHammer\|60` | bool |
| `CANDLE_KICKING_BEARISH` | Candle.Kicking.Bearish | `Candle.Kicking.Bearish` | bool |
| `CANDLE_KICKING_BEARISH_1` | Candle Kicking Bearish\|1 | `Candle.Kicking.Bearish\|1` | bool |
| `CANDLE_KICKING_BEARISH_120` | Candle Kicking Bearish\|120 | `Candle.Kicking.Bearish\|120` | bool |
| `CANDLE_KICKING_BEARISH_15` | Candle Kicking Bearish\|15 | `Candle.Kicking.Bearish\|15` | bool |
| `CANDLE_KICKING_BEARISH_1M` | Candle Kicking Bearish\|1M | `Candle.Kicking.Bearish\|1M` | bool |
| `CANDLE_KICKING_BEARISH_1W` | Candle Kicking Bearish\|1W | `Candle.Kicking.Bearish\|1W` | bool |
| `CANDLE_KICKING_BEARISH_240` | Candle Kicking Bearish\|240 | `Candle.Kicking.Bearish\|240` | bool |
| `CANDLE_KICKING_BEARISH_30` | Candle Kicking Bearish\|30 | `Candle.Kicking.Bearish\|30` | bool |
| `CANDLE_KICKING_BEARISH_5` | Candle Kicking Bearish\|5 | `Candle.Kicking.Bearish\|5` | bool |
| `CANDLE_KICKING_BEARISH_60` | Candle Kicking Bearish\|60 | `Candle.Kicking.Bearish\|60` | bool |
| `CANDLE_KICKING_BULLISH` | Candle.Kicking.Bullish | `Candle.Kicking.Bullish` | bool |
| `CANDLE_KICKING_BULLISH_1` | Candle Kicking Bullish\|1 | `Candle.Kicking.Bullish\|1` | bool |
| `CANDLE_KICKING_BULLISH_120` | Candle Kicking Bullish\|120 | `Candle.Kicking.Bullish\|120` | bool |
| `CANDLE_KICKING_BULLISH_15` | Candle Kicking Bullish\|15 | `Candle.Kicking.Bullish\|15` | bool |
| `CANDLE_KICKING_BULLISH_1M` | Candle Kicking Bullish\|1M | `Candle.Kicking.Bullish\|1M` | bool |
| `CANDLE_KICKING_BULLISH_1W` | Candle Kicking Bullish\|1W | `Candle.Kicking.Bullish\|1W` | bool |
| `CANDLE_KICKING_BULLISH_240` | Candle Kicking Bullish\|240 | `Candle.Kicking.Bullish\|240` | bool |
| `CANDLE_KICKING_BULLISH_30` | Candle Kicking Bullish\|30 | `Candle.Kicking.Bullish\|30` | bool |
| `CANDLE_KICKING_BULLISH_5` | Candle Kicking Bullish\|5 | `Candle.Kicking.Bullish\|5` | bool |
| `CANDLE_KICKING_BULLISH_60` | Candle Kicking Bullish\|60 | `Candle.Kicking.Bullish\|60` | bool |
| `CANDLE_LONGSHADOW_LOWER` | Candle.LongShadow.Lower | `Candle.LongShadow.Lower` | bool |
| `CANDLE_LONGSHADOW_LOWER_1` | Candle Longshadow Lower\|1 | `Candle.LongShadow.Lower\|1` | bool |
| `CANDLE_LONGSHADOW_LOWER_120` | Candle Longshadow Lower\|120 | `Candle.LongShadow.Lower\|120` | bool |
| `CANDLE_LONGSHADOW_LOWER_15` | Candle Longshadow Lower\|15 | `Candle.LongShadow.Lower\|15` | bool |
| `CANDLE_LONGSHADOW_LOWER_1M` | Candle Longshadow Lower\|1M | `Candle.LongShadow.Lower\|1M` | bool |
| `CANDLE_LONGSHADOW_LOWER_1W` | Candle Longshadow Lower\|1W | `Candle.LongShadow.Lower\|1W` | bool |
| `CANDLE_LONGSHADOW_LOWER_240` | Candle Longshadow Lower\|240 | `Candle.LongShadow.Lower\|240` | bool |
| `CANDLE_LONGSHADOW_LOWER_30` | Candle Longshadow Lower\|30 | `Candle.LongShadow.Lower\|30` | bool |
| `CANDLE_LONGSHADOW_LOWER_5` | Candle Longshadow Lower\|5 | `Candle.LongShadow.Lower\|5` | bool |
| `CANDLE_LONGSHADOW_LOWER_60` | Candle Longshadow Lower\|60 | `Candle.LongShadow.Lower\|60` | bool |
| `CANDLE_LONGSHADOW_UPPER` | Candle.LongShadow.Upper | `Candle.LongShadow.Upper` | bool |
| `CANDLE_LONGSHADOW_UPPER_1` | Candle Longshadow Upper\|1 | `Candle.LongShadow.Upper\|1` | bool |
| `CANDLE_LONGSHADOW_UPPER_120` | Candle Longshadow Upper\|120 | `Candle.LongShadow.Upper\|120` | bool |
| `CANDLE_LONGSHADOW_UPPER_15` | Candle Longshadow Upper\|15 | `Candle.LongShadow.Upper\|15` | bool |
| `CANDLE_LONGSHADOW_UPPER_1M` | Candle Longshadow Upper\|1M | `Candle.LongShadow.Upper\|1M` | bool |
| `CANDLE_LONGSHADOW_UPPER_1W` | Candle Longshadow Upper\|1W | `Candle.LongShadow.Upper\|1W` | bool |
| `CANDLE_LONGSHADOW_UPPER_240` | Candle Longshadow Upper\|240 | `Candle.LongShadow.Upper\|240` | bool |
| `CANDLE_LONGSHADOW_UPPER_30` | Candle Longshadow Upper\|30 | `Candle.LongShadow.Upper\|30` | bool |
| `CANDLE_LONGSHADOW_UPPER_5` | Candle Longshadow Upper\|5 | `Candle.LongShadow.Upper\|5` | bool |
| `CANDLE_LONGSHADOW_UPPER_60` | Candle Longshadow Upper\|60 | `Candle.LongShadow.Upper\|60` | bool |
| `CANDLE_MARUBOZU_BLACK` | Candle.Marubozu.Black | `Candle.Marubozu.Black` | bool |
| `CANDLE_MARUBOZU_BLACK_1` | Candle Marubozu Black\|1 | `Candle.Marubozu.Black\|1` | bool |
| `CANDLE_MARUBOZU_BLACK_120` | Candle Marubozu Black\|120 | `Candle.Marubozu.Black\|120` | bool |
| `CANDLE_MARUBOZU_BLACK_15` | Candle Marubozu Black\|15 | `Candle.Marubozu.Black\|15` | bool |
| `CANDLE_MARUBOZU_BLACK_1M` | Candle Marubozu Black\|1M | `Candle.Marubozu.Black\|1M` | bool |
| `CANDLE_MARUBOZU_BLACK_1W` | Candle Marubozu Black\|1W | `Candle.Marubozu.Black\|1W` | bool |
| `CANDLE_MARUBOZU_BLACK_240` | Candle Marubozu Black\|240 | `Candle.Marubozu.Black\|240` | bool |
| `CANDLE_MARUBOZU_BLACK_30` | Candle Marubozu Black\|30 | `Candle.Marubozu.Black\|30` | bool |
| `CANDLE_MARUBOZU_BLACK_5` | Candle Marubozu Black\|5 | `Candle.Marubozu.Black\|5` | bool |
| `CANDLE_MARUBOZU_BLACK_60` | Candle Marubozu Black\|60 | `Candle.Marubozu.Black\|60` | bool |
| `CANDLE_MARUBOZU_WHITE` | Candle.Marubozu.White | `Candle.Marubozu.White` | bool |
| `CANDLE_MARUBOZU_WHITE_1` | Candle Marubozu White\|1 | `Candle.Marubozu.White\|1` | bool |
| `CANDLE_MARUBOZU_WHITE_120` | Candle Marubozu White\|120 | `Candle.Marubozu.White\|120` | bool |
| `CANDLE_MARUBOZU_WHITE_15` | Candle Marubozu White\|15 | `Candle.Marubozu.White\|15` | bool |
| `CANDLE_MARUBOZU_WHITE_1M` | Candle Marubozu White\|1M | `Candle.Marubozu.White\|1M` | bool |
| `CANDLE_MARUBOZU_WHITE_1W` | Candle Marubozu White\|1W | `Candle.Marubozu.White\|1W` | bool |
| `CANDLE_MARUBOZU_WHITE_240` | Candle Marubozu White\|240 | `Candle.Marubozu.White\|240` | bool |
| `CANDLE_MARUBOZU_WHITE_30` | Candle Marubozu White\|30 | `Candle.Marubozu.White\|30` | bool |
| `CANDLE_MARUBOZU_WHITE_5` | Candle Marubozu White\|5 | `Candle.Marubozu.White\|5` | bool |
| `CANDLE_MARUBOZU_WHITE_60` | Candle Marubozu White\|60 | `Candle.Marubozu.White\|60` | bool |
| `CANDLE_MORNINGSTAR` | Candle.MorningStar | `Candle.MorningStar` | bool |
| `CANDLE_MORNINGSTAR_1` | Candle Morningstar\|1 | `Candle.MorningStar\|1` | bool |
| `CANDLE_MORNINGSTAR_120` | Candle Morningstar\|120 | `Candle.MorningStar\|120` | bool |
| `CANDLE_MORNINGSTAR_15` | Candle Morningstar\|15 | `Candle.MorningStar\|15` | bool |
| `CANDLE_MORNINGSTAR_1M` | Candle Morningstar\|1M | `Candle.MorningStar\|1M` | bool |
| `CANDLE_MORNINGSTAR_1W` | Candle Morningstar\|1W | `Candle.MorningStar\|1W` | bool |
| `CANDLE_MORNINGSTAR_240` | Candle Morningstar\|240 | `Candle.MorningStar\|240` | bool |
| `CANDLE_MORNINGSTAR_30` | Candle Morningstar\|30 | `Candle.MorningStar\|30` | bool |
| `CANDLE_MORNINGSTAR_5` | Candle Morningstar\|5 | `Candle.MorningStar\|5` | bool |
| `CANDLE_MORNINGSTAR_60` | Candle Morningstar\|60 | `Candle.MorningStar\|60` | bool |
| `CANDLE_SHOOTINGSTAR` | Candle.ShootingStar | `Candle.ShootingStar` | bool |
| `CANDLE_SHOOTINGSTAR_1` | Candle Shootingstar\|1 | `Candle.ShootingStar\|1` | bool |
| `CANDLE_SHOOTINGSTAR_120` | Candle Shootingstar\|120 | `Candle.ShootingStar\|120` | bool |
| `CANDLE_SHOOTINGSTAR_15` | Candle Shootingstar\|15 | `Candle.ShootingStar\|15` | bool |
| `CANDLE_SHOOTINGSTAR_1M` | Candle Shootingstar\|1M | `Candle.ShootingStar\|1M` | bool |
| `CANDLE_SHOOTINGSTAR_1W` | Candle Shootingstar\|1W | `Candle.ShootingStar\|1W` | bool |
| `CANDLE_SHOOTINGSTAR_240` | Candle Shootingstar\|240 | `Candle.ShootingStar\|240` | bool |
| `CANDLE_SHOOTINGSTAR_30` | Candle Shootingstar\|30 | `Candle.ShootingStar\|30` | bool |
| `CANDLE_SHOOTINGSTAR_5` | Candle Shootingstar\|5 | `Candle.ShootingStar\|5` | bool |
| `CANDLE_SHOOTINGSTAR_60` | Candle Shootingstar\|60 | `Candle.ShootingStar\|60` | bool |
| `CANDLE_SPINNINGTOP_BLACK` | Candle.SpinningTop.Black | `Candle.SpinningTop.Black` | bool |
| `CANDLE_SPINNINGTOP_BLACK_1` | Candle Spinningtop Black\|1 | `Candle.SpinningTop.Black\|1` | bool |
| `CANDLE_SPINNINGTOP_BLACK_120` | Candle Spinningtop Black\|120 | `Candle.SpinningTop.Black\|120` | bool |
| `CANDLE_SPINNINGTOP_BLACK_15` | Candle Spinningtop Black\|15 | `Candle.SpinningTop.Black\|15` | bool |
| `CANDLE_SPINNINGTOP_BLACK_1M` | Candle Spinningtop Black\|1M | `Candle.SpinningTop.Black\|1M` | bool |
| `CANDLE_SPINNINGTOP_BLACK_1W` | Candle Spinningtop Black\|1W | `Candle.SpinningTop.Black\|1W` | bool |
| `CANDLE_SPINNINGTOP_BLACK_240` | Candle Spinningtop Black\|240 | `Candle.SpinningTop.Black\|240` | bool |
| `CANDLE_SPINNINGTOP_BLACK_30` | Candle Spinningtop Black\|30 | `Candle.SpinningTop.Black\|30` | bool |
| `CANDLE_SPINNINGTOP_BLACK_5` | Candle Spinningtop Black\|5 | `Candle.SpinningTop.Black\|5` | bool |
| `CANDLE_SPINNINGTOP_BLACK_60` | Candle Spinningtop Black\|60 | `Candle.SpinningTop.Black\|60` | bool |
| `CANDLE_SPINNINGTOP_WHITE` | Candle.SpinningTop.White | `Candle.SpinningTop.White` | bool |
| `CANDLE_SPINNINGTOP_WHITE_1` | Candle Spinningtop White\|1 | `Candle.SpinningTop.White\|1` | bool |
| `CANDLE_SPINNINGTOP_WHITE_120` | Candle Spinningtop White\|120 | `Candle.SpinningTop.White\|120` | bool |
| `CANDLE_SPINNINGTOP_WHITE_15` | Candle Spinningtop White\|15 | `Candle.SpinningTop.White\|15` | bool |
| `CANDLE_SPINNINGTOP_WHITE_1M` | Candle Spinningtop White\|1M | `Candle.SpinningTop.White\|1M` | bool |
| `CANDLE_SPINNINGTOP_WHITE_1W` | Candle Spinningtop White\|1W | `Candle.SpinningTop.White\|1W` | bool |
| `CANDLE_SPINNINGTOP_WHITE_240` | Candle Spinningtop White\|240 | `Candle.SpinningTop.White\|240` | bool |
| `CANDLE_SPINNINGTOP_WHITE_30` | Candle Spinningtop White\|30 | `Candle.SpinningTop.White\|30` | bool |
| `CANDLE_SPINNINGTOP_WHITE_5` | Candle Spinningtop White\|5 | `Candle.SpinningTop.White\|5` | bool |
| `CANDLE_SPINNINGTOP_WHITE_60` | Candle Spinningtop White\|60 | `Candle.SpinningTop.White\|60` | bool |
| `CANDLE_TRISTAR_BEARISH` | Candle.TriStar.Bearish | `Candle.TriStar.Bearish` | bool |
| `CANDLE_TRISTAR_BEARISH_1` | Candle Tristar Bearish\|1 | `Candle.TriStar.Bearish\|1` | bool |
| `CANDLE_TRISTAR_BEARISH_120` | Candle Tristar Bearish\|120 | `Candle.TriStar.Bearish\|120` | bool |
| `CANDLE_TRISTAR_BEARISH_15` | Candle Tristar Bearish\|15 | `Candle.TriStar.Bearish\|15` | bool |
| `CANDLE_TRISTAR_BEARISH_1M` | Candle Tristar Bearish\|1M | `Candle.TriStar.Bearish\|1M` | bool |
| `CANDLE_TRISTAR_BEARISH_1W` | Candle Tristar Bearish\|1W | `Candle.TriStar.Bearish\|1W` | bool |
| `CANDLE_TRISTAR_BEARISH_240` | Candle Tristar Bearish\|240 | `Candle.TriStar.Bearish\|240` | bool |
| `CANDLE_TRISTAR_BEARISH_30` | Candle Tristar Bearish\|30 | `Candle.TriStar.Bearish\|30` | bool |
| `CANDLE_TRISTAR_BEARISH_5` | Candle Tristar Bearish\|5 | `Candle.TriStar.Bearish\|5` | bool |
| `CANDLE_TRISTAR_BEARISH_60` | Candle Tristar Bearish\|60 | `Candle.TriStar.Bearish\|60` | bool |
| `CANDLE_TRISTAR_BULLISH` | Candle.TriStar.Bullish | `Candle.TriStar.Bullish` | bool |
| `CANDLE_TRISTAR_BULLISH_1` | Candle Tristar Bullish\|1 | `Candle.TriStar.Bullish\|1` | bool |
| `CANDLE_TRISTAR_BULLISH_120` | Candle Tristar Bullish\|120 | `Candle.TriStar.Bullish\|120` | bool |
| `CANDLE_TRISTAR_BULLISH_15` | Candle Tristar Bullish\|15 | `Candle.TriStar.Bullish\|15` | bool |
| `CANDLE_TRISTAR_BULLISH_1M` | Candle Tristar Bullish\|1M | `Candle.TriStar.Bullish\|1M` | bool |
| `CANDLE_TRISTAR_BULLISH_1W` | Candle Tristar Bullish\|1W | `Candle.TriStar.Bullish\|1W` | bool |
| `CANDLE_TRISTAR_BULLISH_240` | Candle Tristar Bullish\|240 | `Candle.TriStar.Bullish\|240` | bool |
| `CANDLE_TRISTAR_BULLISH_30` | Candle Tristar Bullish\|30 | `Candle.TriStar.Bullish\|30` | bool |
| `CANDLE_TRISTAR_BULLISH_5` | Candle Tristar Bullish\|5 | `Candle.TriStar.Bullish\|5` | bool |
| `CANDLE_TRISTAR_BULLISH_60` | Candle Tristar Bullish\|60 | `Candle.TriStar.Bullish\|60` | bool |
| `PATTERN` | Pattern | `candlestick` | missing |

## Recommendations

*40 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `MOVING_AVERAGES_RATING` | Moving Averages Rating | `Recommend.MA` | text |
| `OSCILLATORS_RATING` | Oscillators Rating | `Recommend.Other` | text |
| `RECOMMEND_ALL_1` | Recommend All\|1 | `Recommend.All\|1` | rating |
| `RECOMMEND_ALL_120` | Recommend All\|120 | `Recommend.All\|120` | rating |
| `RECOMMEND_ALL_15` | Recommend All\|15 | `Recommend.All\|15` | rating |
| `RECOMMEND_ALL_1M` | Recommend All\|1M | `Recommend.All\|1M` | rating |
| `RECOMMEND_ALL_1W` | Recommend All\|1W | `Recommend.All\|1W` | rating |
| `RECOMMEND_ALL_240` | Recommend All\|240 | `Recommend.All\|240` | rating |
| `RECOMMEND_ALL_30` | Recommend All\|30 | `Recommend.All\|30` | rating |
| `RECOMMEND_ALL_5` | Recommend All\|5 | `Recommend.All\|5` | rating |
| `RECOMMEND_ALL_60` | Recommend All\|60 | `Recommend.All\|60` | rating |
| `RECOMMEND_MA_1` | Recommend Ma\|1 | `Recommend.MA\|1` | rating |
| `RECOMMEND_MA_120` | Recommend Ma\|120 | `Recommend.MA\|120` | rating |
| `RECOMMEND_MA_15` | Recommend Ma\|15 | `Recommend.MA\|15` | rating |
| `RECOMMEND_MA_1M` | Recommend Ma\|1M | `Recommend.MA\|1M` | rating |
| `RECOMMEND_MA_1W` | Recommend Ma\|1W | `Recommend.MA\|1W` | rating |
| `RECOMMEND_MA_240` | Recommend Ma\|240 | `Recommend.MA\|240` | rating |
| `RECOMMEND_MA_30` | Recommend Ma\|30 | `Recommend.MA\|30` | rating |
| `RECOMMEND_MA_5` | Recommend Ma\|5 | `Recommend.MA\|5` | rating |
| `RECOMMEND_MA_60` | Recommend Ma\|60 | `Recommend.MA\|60` | rating |
| `RECOMMEND_OTHER_1` | Recommend Other\|1 | `Recommend.Other\|1` | rating |
| `RECOMMEND_OTHER_120` | Recommend Other\|120 | `Recommend.Other\|120` | rating |
| `RECOMMEND_OTHER_15` | Recommend Other\|15 | `Recommend.Other\|15` | rating |
| `RECOMMEND_OTHER_1M` | Recommend Other\|1M | `Recommend.Other\|1M` | rating |
| `RECOMMEND_OTHER_1W` | Recommend Other\|1W | `Recommend.Other\|1W` | rating |
| `RECOMMEND_OTHER_240` | Recommend Other\|240 | `Recommend.Other\|240` | rating |
| `RECOMMEND_OTHER_30` | Recommend Other\|30 | `Recommend.Other\|30` | rating |
| `RECOMMEND_OTHER_5` | Recommend Other\|5 | `Recommend.Other\|5` | rating |
| `RECOMMEND_OTHER_60` | Recommend Other\|60 | `Recommend.Other\|60` | rating |
| `REC_WR` | Rec Wr | `Rec.WR` | rating |
| `REC_WR_1` | Rec Wr\|1 | `Rec.WR\|1` | rating |
| `REC_WR_120` | Rec Wr\|120 | `Rec.WR\|120` | rating |
| `REC_WR_15` | Rec Wr\|15 | `Rec.WR\|15` | rating |
| `REC_WR_1M` | Rec Wr\|1M | `Rec.WR\|1M` | rating |
| `REC_WR_1W` | Rec Wr\|1W | `Rec.WR\|1W` | rating |
| `REC_WR_240` | Rec Wr\|240 | `Rec.WR\|240` | rating |
| `REC_WR_30` | Rec Wr\|30 | `Rec.WR\|30` | rating |
| `REC_WR_5` | Rec Wr\|5 | `Rec.WR\|5` | rating |
| `REC_WR_60` | Rec Wr\|60 | `Rec.WR\|60` | rating |
| `TECHNICAL_RATING` | Technical Rating | `Recommend.All` | rating |

## Dividends & Yield

*2 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `RATES_DIVIDEND_RECENT` | Rates Dividend Recent | `rates_dividend_recent` | float |
| `RATES_DIVIDEND_UPCOMING` | Rates Dividend Upcoming | `rates_dividend_upcoming` | float |

## Earnings & Income

*2 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `RATES_EARNINGS_FQ` | Rates Earnings FQ | `rates_earnings_fq` | float |
| `RATES_EARNINGS_NEXT_FQ` | Rates Earnings Next FQ | `rates_earnings_next_fq` | float |

## Bond Data

*3 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `COUPON` | Coupon | `coupon` | float |
| `DAYS_TO_MATURITY` | Days To Maturity | `days_to_maturity` | float |
| `MATURITY_DATE` | Maturity Date | `maturity_date` | date |

## Crypto Data

*2 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `CRYPTOASSET_MINUS_INFO_DESCRIPTION` | Cryptoasset-Info Description | `cryptoasset-info.description` | text |
| `CRYPTOASSET_MINUS_INFO_ID` | Cryptoasset-Info Id | `cryptoasset-info.id` | float |

## DEX Data

*2 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `INDEXES` | Indexes | `indexes` | float |
| `INDEX_PRIORITY` | Index Priority | `index_priority` | float |

## Time & Dates

*35 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `FIRST_BAR_TIME` | First Bar Time | `first_bar_time` | date |
| `LAST_BAR_UPDATE_TIME` | Last Bar Update Time | `last_bar_update_time` | date |
| `LAST_BAR_UPDATE_TIME_1` | Last Bar Update Time\|1 | `last_bar_update_time\|1` | date |
| `LAST_BAR_UPDATE_TIME_120` | Last Bar Update Time\|120 | `last_bar_update_time\|120` | date |
| `LAST_BAR_UPDATE_TIME_15` | Last Bar Update Time\|15 | `last_bar_update_time\|15` | date |
| `LAST_BAR_UPDATE_TIME_1M` | Last Bar Update Time\|1M | `last_bar_update_time\|1M` | date |
| `LAST_BAR_UPDATE_TIME_1W` | Last Bar Update Time\|1W | `last_bar_update_time\|1W` | date |
| `LAST_BAR_UPDATE_TIME_240` | Last Bar Update Time\|240 | `last_bar_update_time\|240` | date |
| `LAST_BAR_UPDATE_TIME_30` | Last Bar Update Time\|30 | `last_bar_update_time\|30` | date |
| `LAST_BAR_UPDATE_TIME_5` | Last Bar Update Time\|5 | `last_bar_update_time\|5` | date |
| `LAST_BAR_UPDATE_TIME_60` | Last Bar Update Time\|60 | `last_bar_update_time\|60` | date |
| `RATES_TIME_SERIES` | Rates Time Series | `rates_time_series` | date |
| `TIME` | Time | `time` | date |
| `TIME_1` | Time\|1 | `time\|1` | date |
| `TIME_120` | Time\|120 | `time\|120` | date |
| `TIME_15` | Time\|15 | `time\|15` | date |
| `TIME_1M` | Time\|1M | `time\|1M` | date |
| `TIME_1W` | Time\|1W | `time\|1W` | date |
| `TIME_240` | Time\|240 | `time\|240` | date |
| `TIME_30` | Time\|30 | `time\|30` | date |
| `TIME_5` | Time\|5 | `time\|5` | date |
| `TIME_60` | Time\|60 | `time\|60` | date |
| `TIME_BUSINESS_DAY` | Time Business Day | `time_business_day` | date |
| `UPDATE_MINUS_TIME` | Update-Time | `update-time` | date |
| `UPDATE_MODE` | Update Mode | `update_mode` | date |
| `UPDATE_MODE_1` | Update Mode\|1 | `update_mode\|1` | date |
| `UPDATE_MODE_120` | Update Mode\|120 | `update_mode\|120` | date |
| `UPDATE_MODE_15` | Update Mode\|15 | `update_mode\|15` | date |
| `UPDATE_MODE_1M` | Update Mode\|1M | `update_mode\|1M` | date |
| `UPDATE_MODE_1W` | Update Mode\|1W | `update_mode\|1W` | date |
| `UPDATE_MODE_240` | Update Mode\|240 | `update_mode\|240` | date |
| `UPDATE_MODE_30` | Update Mode\|30 | `update_mode\|30` | date |
| `UPDATE_MODE_5` | Update Mode\|5 | `update_mode\|5` | date |
| `UPDATE_MODE_60` | Update Mode\|60 | `update_mode\|60` | date |
| `UPDATE_TIME` | Update Time | `update_time` | date |

## Other

*164 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `ADRP` | Adrp | `ADRP` | float |
| `ADRP_1` | Adrp\|1 | `ADRP\|1` | float |
| `ADRP_120` | Adrp\|120 | `ADRP\|120` | float |
| `ADRP_15` | Adrp\|15 | `ADRP\|15` | float |
| `ADRP_1M` | Adrp\|1M | `ADRP\|1M` | float |
| `ADRP_1W` | Adrp\|1W | `ADRP\|1W` | float |
| `ADRP_240` | Adrp\|240 | `ADRP\|240` | float |
| `ADRP_30` | Adrp\|30 | `ADRP\|30` | float |
| `ADRP_5` | Adrp\|5 | `ADRP\|5` | float |
| `ADRP_60` | Adrp\|60 | `ADRP\|60` | float |
| `ADR_1` | Adr\|1 | `ADR\|1` | float |
| `ADR_120` | Adr\|120 | `ADR\|120` | float |
| `ADR_15` | Adr\|15 | `ADR\|15` | float |
| `ADR_1M` | Adr\|1M | `ADR\|1M` | float |
| `ADR_1W` | Adr\|1W | `ADR\|1W` | float |
| `ADR_240` | Adr\|240 | `ADR\|240` | float |
| `ADR_30` | Adr\|30 | `ADR\|30` | float |
| `ADR_5` | Adr\|5 | `ADR\|5` | float |
| `ADR_60` | Adr\|60 | `ADR\|60` | float |
| `AVERAGE_DAY_RANGE_14` | Average Day Range (14) | `ADR` | float |
| `AVGVALUE_TRADED_10D` | Avgvalue Traded 10D | `AvgValue.Traded_10d` | float |
| `AVGVALUE_TRADED_30D` | Avgvalue Traded 30D | `AvgValue.Traded_30d` | float |
| `AVGVALUE_TRADED_60D` | Avgvalue Traded 60D | `AvgValue.Traded_60d` | float |
| `AVGVALUE_TRADED_90D` | Avgvalue Traded 90D | `AvgValue.Traded_90d` | float |
| `BARS_COUNT` | Bars Count | `bars_count` | float |
| `BARS_COUNT_1` | Bars Count\|1 | `bars_count\|1` | float |
| `BARS_COUNT_120` | Bars Count\|120 | `bars_count\|120` | float |
| `BARS_COUNT_15` | Bars Count\|15 | `bars_count\|15` | float |
| `BARS_COUNT_1M` | Bars Count\|1M | `bars_count\|1M` | float |
| `BARS_COUNT_1W` | Bars Count\|1W | `bars_count\|1W` | float |
| `BARS_COUNT_240` | Bars Count\|240 | `bars_count\|240` | float |
| `BARS_COUNT_30` | Bars Count\|30 | `bars_count\|30` | float |
| `BARS_COUNT_5` | Bars Count\|5 | `bars_count\|5` | float |
| `BARS_COUNT_60` | Bars Count\|60 | `bars_count\|60` | float |
| `CHANGE` | Change | `change_abs` | float |
| `CHANGE_1` | Change\|1 | `change\|1` | percent |
| `CHANGE_120` | Change\|120 | `change\|120` | percent |
| `CHANGE_15` | Change\|15 | `change\|15` | percent |
| `CHANGE_15MIN` | Change 15m | `change_abs.15` | float |
| `CHANGE_15MIN_PERCENT` | Change 15m, % | `change.15` | percent |
| `CHANGE_1H` | Change 1h | `change_abs.60` | float |
| `CHANGE_1H_PERCENT` | Change 1h, % | `change.60` | percent |
| `CHANGE_1M` | Change 1M | `change_abs.1M` | float |
| `CHANGE_1MIN` | Change 1m | `change_abs.1` | float |
| `CHANGE_1MIN_PERCENT` | Change 1m, % | `change.1` | percent |
| `CHANGE_1M_2` | Change\|1M | `change\|1M` | percent |
| `CHANGE_1M_PERCENT` | Change 1M, % | `change.1M` | percent |
| `CHANGE_1W` | Change 1W | `change_abs.1W` | float |
| `CHANGE_1W_2` | Change\|1W | `change\|1W` | percent |
| `CHANGE_1W_PERCENT` | Change 1W, % | `change.1W` | percent |
| `CHANGE_240` | Change\|240 | `change\|240` | percent |
| `CHANGE_30` | Change\|30 | `change\|30` | percent |
| `CHANGE_4H` | Change 4h | `change_abs.240` | float |
| `CHANGE_4H_PERCENT` | Change 4h, % | `change.240` | percent |
| `CHANGE_5` | Change\|5 | `change\|5` | percent |
| `CHANGE_5MIN` | Change 5m | `change_abs.5` | float |
| `CHANGE_5MIN_PERCENT` | Change 5m, % | `change.5` | percent |
| `CHANGE_60` | Change\|60 | `change\|60` | percent |
| `CHANGE_ABS_1` | Change Abs\|1 | `change_abs\|1` | percent |
| `CHANGE_ABS_120` | Change Abs\|120 | `change_abs\|120` | percent |
| `CHANGE_ABS_15` | Change Abs\|15 | `change_abs\|15` | percent |
| `CHANGE_ABS_1M` | Change Abs\|1M | `change_abs\|1M` | percent |
| `CHANGE_ABS_1W` | Change Abs\|1W | `change_abs\|1W` | percent |
| `CHANGE_ABS_240` | Change Abs\|240 | `change_abs\|240` | percent |
| `CHANGE_ABS_30` | Change Abs\|30 | `change_abs\|30` | percent |
| `CHANGE_ABS_5` | Change Abs\|5 | `change_abs\|5` | percent |
| `CHANGE_ABS_60` | Change Abs\|60 | `change_abs\|60` | percent |
| `CHANGE_PERCENT` | Change % | `change` | percent |
| `CURRENT_SESSION` | Current Session | `current_session` | float |
| `EXPIRATION` | Expiration | `expiration` | percent |
| `FOREX_EXOTIC_PRIORITY` | Forex Exotic Priority | `forex_exotic_priority` | float |
| `FOREX_MINOR_PRIORITY` | Forex Minor Priority | `forex_minor_priority` | float |
| `FOREX_PRIORITY` | Forex Priority | `forex_priority` | float |
| `FRACTIONAL` | Fractional | `fractional` | float |
| `INDICATORS_BARS_COUNT` | Indicators Bars Count | `indicators_bars_count` | float |
| `INDICATORS_BARS_COUNT_1` | Indicators Bars Count\|1 | `indicators_bars_count\|1` | float |
| `INDICATORS_BARS_COUNT_120` | Indicators Bars Count\|120 | `indicators_bars_count\|120` | float |
| `INDICATORS_BARS_COUNT_15` | Indicators Bars Count\|15 | `indicators_bars_count\|15` | float |
| `INDICATORS_BARS_COUNT_1M` | Indicators Bars Count\|1M | `indicators_bars_count\|1M` | float |
| `INDICATORS_BARS_COUNT_1W` | Indicators Bars Count\|1W | `indicators_bars_count\|1W` | float |
| `INDICATORS_BARS_COUNT_240` | Indicators Bars Count\|240 | `indicators_bars_count\|240` | float |
| `INDICATORS_BARS_COUNT_30` | Indicators Bars Count\|30 | `indicators_bars_count\|30` | float |
| `INDICATORS_BARS_COUNT_5` | Indicators Bars Count\|5 | `indicators_bars_count\|5` | float |
| `INDICATORS_BARS_COUNT_60` | Indicators Bars Count\|60 | `indicators_bars_count\|60` | float |
| `IS_BLACKLISTED` | Is Blacklisted | `is_blacklisted` | float |
| `IS_PRIMARY` | Is Primary | `is_primary` | float |
| `IS_SHARIAH_COMPLIANT` | Is Shariah Compliant | `is_shariah_compliant` | float |
| `KIND` | Kind | `kind` | float |
| `KIND_MINUS_DELAY` | Kind-Delay | `kind-delay` | float |
| `MARKET` | Market | `market` | float |
| `MINMOV` | Minmov | `minmov` | float |
| `MINMOVE2` | Minmove2 | `minmove2` | float |
| `NAV_DISCOUNT_PREMIUM` | Nav Discount Premium | `nav_discount_premium` | float |
| `NAV_TOTAL_RETURN_1M` | Nav Total Return 1M | `nav_total_return.1M` | float |
| `NAV_TOTAL_RETURN_1Y` | Nav Total Return 1Y | `nav_total_return.1Y` | float |
| `NAV_TOTAL_RETURN_3M` | Nav Total Return 3M | `nav_total_return.3M` | float |
| `NAV_TOTAL_RETURN_3Y` | Nav Total Return 3Y | `nav_total_return.3Y` | float |
| `NAV_TOTAL_RETURN_5Y` | Nav Total Return 5Y | `nav_total_return.5Y` | float |
| `NAV_TOTAL_RETURN_6M` | Nav Total Return 6M | `nav_total_return.6M` | float |
| `NAV_TOTAL_RETURN_YTD` | Nav Total Return YTD | `nav_total_return.YTD` | float |
| `POPULARITY_RANK` | Popularity Rank | `popularity_rank` | float |
| `POSTMARKET_CHANGE` | Postmarket Change | `postmarket_change` | percent |
| `POSTMARKET_CHANGE_ABS` | Postmarket Change Abs | `postmarket_change_abs` | percent |
| `POST_CHANGE` | Post Change | `post_change` | percent |
| `POST_CHANGE_1` | Post Change\|1 | `post_change\|1` | percent |
| `POST_CHANGE_120` | Post Change\|120 | `post_change\|120` | percent |
| `POST_CHANGE_15` | Post Change\|15 | `post_change\|15` | percent |
| `POST_CHANGE_1M` | Post Change\|1M | `post_change\|1M` | percent |
| `POST_CHANGE_1W` | Post Change\|1W | `post_change\|1W` | percent |
| `POST_CHANGE_240` | Post Change\|240 | `post_change\|240` | percent |
| `POST_CHANGE_30` | Post Change\|30 | `post_change\|30` | percent |
| `POST_CHANGE_5` | Post Change\|5 | `post_change\|5` | percent |
| `POST_CHANGE_60` | Post Change\|60 | `post_change\|60` | percent |
| `PRE_CHANGE` | Pre Change | `pre_change` | percent |
| `PRE_CHANGE_1` | Pre Change\|1 | `pre_change\|1` | percent |
| `PRE_CHANGE_120` | Pre Change\|120 | `pre_change\|120` | percent |
| `PRE_CHANGE_15` | Pre Change\|15 | `pre_change\|15` | percent |
| `PRE_CHANGE_1M` | Pre Change\|1M | `pre_change\|1M` | percent |
| `PRE_CHANGE_1W` | Pre Change\|1W | `pre_change\|1W` | percent |
| `PRE_CHANGE_240` | Pre Change\|240 | `pre_change\|240` | percent |
| `PRE_CHANGE_30` | Pre Change\|30 | `pre_change\|30` | percent |
| `PRE_CHANGE_5` | Pre Change\|5 | `pre_change\|5` | percent |
| `PRE_CHANGE_60` | Pre Change\|60 | `pre_change\|60` | percent |
| `PRE_CHANGE_ABS` | Pre Change Abs | `pre_change_abs` | percent |
| `PRE_CHANGE_ABS_1` | Pre Change Abs\|1 | `pre_change_abs\|1` | percent |
| `PRE_CHANGE_ABS_120` | Pre Change Abs\|120 | `pre_change_abs\|120` | percent |
| `PRE_CHANGE_ABS_15` | Pre Change Abs\|15 | `pre_change_abs\|15` | percent |
| `PRE_CHANGE_ABS_1M` | Pre Change Abs\|1M | `pre_change_abs\|1M` | percent |
| `PRE_CHANGE_ABS_1W` | Pre Change Abs\|1W | `pre_change_abs\|1W` | percent |
| `PRE_CHANGE_ABS_240` | Pre Change Abs\|240 | `pre_change_abs\|240` | percent |
| `PRE_CHANGE_ABS_30` | Pre Change Abs\|30 | `pre_change_abs\|30` | percent |
| `PRE_CHANGE_ABS_5` | Pre Change Abs\|5 | `pre_change_abs\|5` | percent |
| `PRE_CHANGE_ABS_60` | Pre Change Abs\|60 | `pre_change_abs\|60` | percent |
| `PROVIDER_MINUS_ID` | Provider-Id | `provider-id` | float |
| `RATES_CF` | Rates Cf | `rates_cf` | float |
| `RATES_CURRENT` | Rates Current | `rates_current` | float |
| `RATES_FH` | Rates FH | `rates_fh` | float |
| `RATES_FQ` | Rates FQ | `rates_fq` | float |
| `RATES_FY` | Rates FY | `rates_fy` | float |
| `RATES_MC` | Rates Mc | `rates_mc` | float |
| `RATES_PT` | Rates Pt | `rates_pt` | float |
| `RATES_TTM` | Rates TTM | `rates_ttm` | float |
| `RTC` | Rtc | `rtc` | float |
| `SUBMARKET` | Submarket | `submarket` | float |
| `VALUE_TRADED` | Value Traded | `Value.Traded` | float |
| `VALUE_TRADED_1` | Value Traded\|1 | `Value.Traded\|1` | float |
| `VALUE_TRADED_120` | Value Traded\|120 | `Value.Traded\|120` | float |
| `VALUE_TRADED_15` | Value Traded\|15 | `Value.Traded\|15` | float |
| `VALUE_TRADED_1M` | Value Traded\|1M | `Value.Traded\|1M` | float |
| `VALUE_TRADED_1W` | Value Traded\|1W | `Value.Traded\|1W` | float |
| `VALUE_TRADED_240` | Value Traded\|240 | `Value.Traded\|240` | float |
| `VALUE_TRADED_30` | Value Traded\|30 | `Value.Traded\|30` | float |
| `VALUE_TRADED_5` | Value Traded\|5 | `Value.Traded\|5` | float |
| `VALUE_TRADED_60` | Value Traded\|60 | `Value.Traded\|60` | float |
| `VOLUME_WEIGHTED_AVERAGE_PRICE` | Volume Weighted Average Price | `VWAP` | missing |
| `VWAP_1` | VWAP\|1 | `VWAP\|1` | float |
| `VWAP_120` | VWAP\|120 | `VWAP\|120` | float |
| `VWAP_15` | VWAP\|15 | `VWAP\|15` | float |
| `VWAP_1M` | VWAP\|1M | `VWAP\|1M` | float |
| `VWAP_1W` | VWAP\|1W | `VWAP\|1W` | float |
| `VWAP_240` | VWAP\|240 | `VWAP\|240` | float |
| `VWAP_30` | VWAP\|30 | `VWAP\|30` | float |
| `VWAP_5` | VWAP\|5 | `VWAP\|5` | float |
| `VWAP_60` | VWAP\|60 | `VWAP\|60` | float |
