# StockField Reference

Fields available for stock and ETF screening. Includes price data, technicals, and fundamentals.

**Total Fields:** 3526

## Table of Contents

- [Metadata](#metadata) (21 fields)
- [Price Data](#price-data) (232 fields)
- [Volume](#volume) (85 fields)
- [Performance](#performance) (31 fields)
- [Moving Averages](#moving-averages) (721 fields)
- [Oscillators](#oscillators) (672 fields)
- [Trend Indicators](#trend-indicators) (400 fields)
- [Volatility Indicators](#volatility-indicators) (143 fields)
- [Pivot Points](#pivot-points) (210 fields)
- [Candlestick Patterns](#candlestick-patterns) (271 fields)
- [Recommendations](#recommendations) (47 fields)
- [Valuation Ratios](#valuation-ratios) (23 fields)
- [Profitability](#profitability) (39 fields)
- [Growth Metrics](#growth-metrics) (37 fields)
- [Dividends & Yield](#dividends--yield) (44 fields)
- [Earnings & Income](#earnings--income) (86 fields)
- [Revenue & Sales](#revenue--sales) (25 fields)
- [Balance Sheet](#balance-sheet) (103 fields)
- [Cash Flow](#cash-flow) (5 fields)
- [Shares & Market Cap](#shares--market-cap) (16 fields)
- [Bond Data](#bond-data) (4 fields)
- [Crypto Data](#crypto-data) (2 fields)
- [DEX Data](#dex-data) (3 fields)
- [Time & Dates](#time--dates) (43 fields)
- [Other](#other) (263 fields)

---

## Metadata

*21 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `ACTIVE_SYMBOL` | Active Symbol | `active_symbol` | bool |
| `BASE_CURRENCY_KIND` | Base Currency Kind | `base_currency_kind` | text |
| `COUNTRY` | Country | `country` | text |
| `COUNTRY_CODE_FUND` | Country Code Fund | `country_code_fund` | text |
| `CURRENCY` | Currency | `currency` | text |
| `CURRENCY_HEDGED_FLAG` | Currency Hedged Flag | `currency_hedged_flag` | text |
| `CURRENCY_ID` | Currency Id | `currency_id` | text |
| `CURRENCY_KIND` | Currency Kind | `currency_kind` | text |
| `DESCRIPTION` | Description | `description` | text |
| `ETF_FUND_CURRENCY` | Etf Fund Currency | `etf_fund_currency` | text |
| `EXCHANGE` | Exchange | `exchange` | text |
| `FUNDAMENTAL_CURRENCY_CODE` | Fundamental Currency Code | `fundamental_currency_code` | text |
| `INDUSTRY` | Industry | `industry` | text |
| `IS_SYMBOL_PRIMARY_LISTING` | Is Symbol Primary Listing | `is_symbol_primary_listing` | bool |
| `LOGOID` | Logoid | `logoid` | text |
| `NAME` | Name | `name` | text |
| `SECTOR` | Sector | `sector` | text |
| `SOURCE_LOGOID` | Source-logoid | `source-logoid` | text |
| `SUBTYPE` | Subtype | `subtype` | text |
| `TYPE` | Type | `type` | text |
| `TYPESPECS` | Typespecs | `typespecs` | text |

## Price Data

*232 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `ALL_TIME_HIGH` | All Time High | `High.All` | round |
| `ALL_TIME_HIGH_2` | All Time High | `all_time_high` | currency |
| `ALL_TIME_HIGH_DAY` | All Time High Day | `all_time_high_day` | date |
| `ALL_TIME_LOW` | All Time Low | `Low.All` | round |
| `ALL_TIME_LOW_2` | All Time Low | `all_time_low` | currency |
| `ALL_TIME_LOW_DAY` | All Time Low Day | `all_time_low_day` | date |
| `ALL_TIME_OPEN` | All Time Open | `all_time_open` | currency |
| `CHAIKINMONEYFLOW_1` | Chaikinmoneyflow\|1 | `ChaikinMoneyFlow\|1` | round |
| `CHAIKINMONEYFLOW_120` | Chaikinmoneyflow\|120 | `ChaikinMoneyFlow\|120` | round |
| `CHAIKINMONEYFLOW_15` | Chaikinmoneyflow\|15 | `ChaikinMoneyFlow\|15` | round |
| `CHAIKINMONEYFLOW_1M` | Chaikinmoneyflow\|1m | `ChaikinMoneyFlow\|1M` | round |
| `CHAIKINMONEYFLOW_1W` | Chaikinmoneyflow\|1w | `ChaikinMoneyFlow\|1W` | round |
| `CHAIKINMONEYFLOW_240` | Chaikinmoneyflow\|240 | `ChaikinMoneyFlow\|240` | round |
| `CHAIKINMONEYFLOW_30` | Chaikinmoneyflow\|30 | `ChaikinMoneyFlow\|30` | round |
| `CHAIKINMONEYFLOW_5` | Chaikinmoneyflow\|5 | `ChaikinMoneyFlow\|5` | round |
| `CHAIKINMONEYFLOW_60` | Chaikinmoneyflow\|60 | `ChaikinMoneyFlow\|60` | round |
| `CHAIKIN_MONEY_FLOW_20` | Chaikin Money Flow (20) | `ChaikinMoneyFlow` | round |
| `CHANGE_FROM_OPEN` | Change from Open | `change_from_open_abs` | currency |
| `CHANGE_FROM_OPEN_1` | Change From Open\|1 | `change_from_open\|1` | percent |
| `CHANGE_FROM_OPEN_120` | Change From Open\|120 | `change_from_open\|120` | percent |
| `CHANGE_FROM_OPEN_15` | Change From Open\|15 | `change_from_open\|15` | percent |
| `CHANGE_FROM_OPEN_1M` | Change From Open\|1m | `change_from_open\|1M` | percent |
| `CHANGE_FROM_OPEN_1W` | Change From Open\|1w | `change_from_open\|1W` | percent |
| `CHANGE_FROM_OPEN_240` | Change From Open\|240 | `change_from_open\|240` | percent |
| `CHANGE_FROM_OPEN_30` | Change From Open\|30 | `change_from_open\|30` | percent |
| `CHANGE_FROM_OPEN_5` | Change From Open\|5 | `change_from_open\|5` | percent |
| `CHANGE_FROM_OPEN_60` | Change From Open\|60 | `change_from_open\|60` | percent |
| `CHANGE_FROM_OPEN_ABS_1` | Change From Open Abs\|1 | `change_from_open_abs\|1` | currency |
| `CHANGE_FROM_OPEN_ABS_120` | Change From Open Abs\|120 | `change_from_open_abs\|120` | currency |
| `CHANGE_FROM_OPEN_ABS_15` | Change From Open Abs\|15 | `change_from_open_abs\|15` | currency |
| `CHANGE_FROM_OPEN_ABS_1M` | Change From Open Abs\|1m | `change_from_open_abs\|1M` | currency |
| `CHANGE_FROM_OPEN_ABS_1W` | Change From Open Abs\|1w | `change_from_open_abs\|1W` | currency |
| `CHANGE_FROM_OPEN_ABS_240` | Change From Open Abs\|240 | `change_from_open_abs\|240` | currency |
| `CHANGE_FROM_OPEN_ABS_30` | Change From Open Abs\|30 | `change_from_open_abs\|30` | currency |
| `CHANGE_FROM_OPEN_ABS_5` | Change From Open Abs\|5 | `change_from_open_abs\|5` | currency |
| `CHANGE_FROM_OPEN_ABS_60` | Change From Open Abs\|60 | `change_from_open_abs\|60` | currency |
| `CHANGE_FROM_OPEN_PERCENT` | Change from Open % | `change_from_open` | percent |
| `CLOSE_1` | Close\|1 | `close\|1` | currency |
| `CLOSE_120` | Close\|120 | `close\|120` | currency |
| `CLOSE_15` | Close\|15 | `close\|15` | currency |
| `CLOSE_1M` | Close\|1m | `close\|1M` | currency |
| `CLOSE_1W` | Close\|1w | `close\|1W` | currency |
| `CLOSE_240` | Close\|240 | `close\|240` | currency |
| `CLOSE_30` | Close\|30 | `close\|30` | currency |
| `CLOSE_5` | Close\|5 | `close\|5` | currency |
| `CLOSE_60` | Close\|60 | `close\|60` | currency |
| `ENTERPRISE_VALUE_TO_FREE_CASH_FLOW_TTM` | Enterprise Value to Free Cash Flow TTM | `enterprise_value_to_free_cash_flow_ttm` | round |
| `FREE_CASH_FLOW` | Free Cash Flow | `free_cash_flow` | currency |
| `FREE_CASH_FLOW_ANNUAL_YOY_GROWTH` | Free Cash Flow (Annual YoY Growth) | `free_cash_flow_yoy_growth_fy` | percent |
| `FREE_CASH_FLOW_CAGR_5Y` | Free Cash Flow Cagr 5y | `free_cash_flow_cagr_5y` | percent |
| `FREE_CASH_FLOW_FH` | Free Cash Flow Fh | `free_cash_flow_fh` | currency |
| `FREE_CASH_FLOW_FQ` | Free Cash Flow FQ | `free_cash_flow_fq` | currency |
| `FREE_CASH_FLOW_FQ_H` | Free Cash Flow FQ H | `free_cash_flow_fq_h` | round |
| `FREE_CASH_FLOW_FY` | Free Cash Flow (FY) | `free_cash_flow_fy` | currency |
| `FREE_CASH_FLOW_FY_H` | Free Cash Flow FY H | `free_cash_flow_fy_h` | round |
| `FREE_CASH_FLOW_MARGIN_FY` | Free Cash Flow Margin (FY) | `free_cash_flow_margin_fy` | percent |
| `FREE_CASH_FLOW_MARGIN_TTM` | Free Cash Flow Margin (TTM) | `free_cash_flow_margin_ttm` | percent |
| `FREE_CASH_FLOW_PER_EMPLOYEE_FY` | Free Cash Flow per Employee (FY) | `free_cash_flow_per_employee_fy` | currency |
| `FREE_CASH_FLOW_PER_SHARE_CURRENT` | Free Cash Flow per Share Current | `free_cash_flow_per_share_current` | currency |
| `FREE_CASH_FLOW_PER_SHARE_FH` | Free Cash Flow per Share Fh | `free_cash_flow_per_share_fh` | currency |
| `FREE_CASH_FLOW_PER_SHARE_FQ` | Free Cash Flow per Share FQ | `free_cash_flow_per_share_fq` | currency |
| `FREE_CASH_FLOW_PER_SHARE_FY` | Free Cash Flow per Share FY | `free_cash_flow_per_share_fy` | currency |
| `FREE_CASH_FLOW_PER_SHARE_TTM` | Free Cash Flow per Share (TTM) | `free_cash_flow_per_share_ttm` | currency |
| `FREE_CASH_FLOW_QUARTERLY_QOQ_GROWTH` | Free Cash Flow (Quarterly QoQ Growth) | `free_cash_flow_qoq_growth_fq` | percent |
| `FREE_CASH_FLOW_QUARTERLY_YOY_GROWTH` | Free Cash Flow (Quarterly YoY Growth) | `free_cash_flow_yoy_growth_fq` | percent |
| `FREE_CASH_FLOW_TTM` | Free Cash Flow (TTM) | `free_cash_flow_ttm` | currency |
| `FREE_CASH_FLOW_TTM_H` | Free Cash Flow TTM H | `free_cash_flow_ttm_h` | round |
| `FREE_CASH_FLOW_TTM_YOY_GROWTH` | Free Cash Flow (TTM YoY Growth) | `free_cash_flow_yoy_growth_ttm` | percent |
| `FUND_FLOWS_1M` | Fund Flows 1m | `fund_flows.1M` | currency |
| `FUND_FLOWS_1Y` | Fund Flows 1y | `fund_flows.1Y` | currency |
| `FUND_FLOWS_3M` | Fund Flows 3m | `fund_flows.3M` | currency |
| `FUND_FLOWS_3Y` | Fund Flows 3y | `fund_flows.3Y` | currency |
| `FUND_FLOWS_5Y` | Fund Flows 5y | `fund_flows.5Y` | currency |
| `FUND_FLOWS_YTD` | Fund Flows Ytd | `fund_flows.YTD` | currency |
| `GAP_1` | Gap\|1 | `gap\|1` | percent |
| `GAP_120` | Gap\|120 | `gap\|120` | percent |
| `GAP_15` | Gap\|15 | `gap\|15` | percent |
| `GAP_1M` | Gap\|1m | `gap\|1M` | percent |
| `GAP_1W` | Gap\|1w | `gap\|1W` | percent |
| `GAP_240` | Gap\|240 | `gap\|240` | percent |
| `GAP_30` | Gap\|30 | `gap\|30` | percent |
| `GAP_5` | Gap\|5 | `gap\|5` | percent |
| `GAP_60` | Gap\|60 | `gap\|60` | percent |
| `GAP_DOWN` | Gap Down | `gap_down` | percent |
| `GAP_DOWN_1` | Gap Down\|1 | `gap_down\|1` | percent |
| `GAP_DOWN_120` | Gap Down\|120 | `gap_down\|120` | percent |
| `GAP_DOWN_15` | Gap Down\|15 | `gap_down\|15` | percent |
| `GAP_DOWN_1M` | Gap Down\|1m | `gap_down\|1M` | percent |
| `GAP_DOWN_1W` | Gap Down\|1w | `gap_down\|1W` | percent |
| `GAP_DOWN_240` | Gap Down\|240 | `gap_down\|240` | percent |
| `GAP_DOWN_30` | Gap Down\|30 | `gap_down\|30` | percent |
| `GAP_DOWN_5` | Gap Down\|5 | `gap_down\|5` | percent |
| `GAP_DOWN_60` | Gap Down\|60 | `gap_down\|60` | percent |
| `GAP_DOWN_ABS` | Gap Down Abs | `gap_down_abs` | currency |
| `GAP_DOWN_ABS_1` | Gap Down Abs\|1 | `gap_down_abs\|1` | currency |
| `GAP_DOWN_ABS_120` | Gap Down Abs\|120 | `gap_down_abs\|120` | currency |
| `GAP_DOWN_ABS_15` | Gap Down Abs\|15 | `gap_down_abs\|15` | currency |
| `GAP_DOWN_ABS_1M` | Gap Down Abs\|1m | `gap_down_abs\|1M` | currency |
| `GAP_DOWN_ABS_1W` | Gap Down Abs\|1w | `gap_down_abs\|1W` | currency |
| `GAP_DOWN_ABS_240` | Gap Down Abs\|240 | `gap_down_abs\|240` | currency |
| `GAP_DOWN_ABS_30` | Gap Down Abs\|30 | `gap_down_abs\|30` | currency |
| `GAP_DOWN_ABS_5` | Gap Down Abs\|5 | `gap_down_abs\|5` | currency |
| `GAP_DOWN_ABS_60` | Gap Down Abs\|60 | `gap_down_abs\|60` | currency |
| `GAP_PERCENT` | Gap % | `gap` | percent |
| `GAP_UP` | Gap Up | `gap_up` | percent |
| `GAP_UP_1` | Gap Up\|1 | `gap_up\|1` | percent |
| `GAP_UP_120` | Gap Up\|120 | `gap_up\|120` | percent |
| `GAP_UP_15` | Gap Up\|15 | `gap_up\|15` | percent |
| `GAP_UP_1M` | Gap Up\|1m | `gap_up\|1M` | percent |
| `GAP_UP_1W` | Gap Up\|1w | `gap_up\|1W` | percent |
| `GAP_UP_240` | Gap Up\|240 | `gap_up\|240` | percent |
| `GAP_UP_30` | Gap Up\|30 | `gap_up\|30` | percent |
| `GAP_UP_5` | Gap Up\|5 | `gap_up\|5` | percent |
| `GAP_UP_60` | Gap Up\|60 | `gap_up\|60` | percent |
| `GAP_UP_ABS` | Gap Up Abs | `gap_up_abs` | currency |
| `GAP_UP_ABS_1` | Gap Up Abs\|1 | `gap_up_abs\|1` | currency |
| `GAP_UP_ABS_120` | Gap Up Abs\|120 | `gap_up_abs\|120` | currency |
| `GAP_UP_ABS_15` | Gap Up Abs\|15 | `gap_up_abs\|15` | currency |
| `GAP_UP_ABS_1M` | Gap Up Abs\|1m | `gap_up_abs\|1M` | currency |
| `GAP_UP_ABS_1W` | Gap Up Abs\|1w | `gap_up_abs\|1W` | currency |
| `GAP_UP_ABS_240` | Gap Up Abs\|240 | `gap_up_abs\|240` | currency |
| `GAP_UP_ABS_30` | Gap Up Abs\|30 | `gap_up_abs\|30` | currency |
| `GAP_UP_ABS_5` | Gap Up Abs\|5 | `gap_up_abs\|5` | currency |
| `GAP_UP_ABS_60` | Gap Up Abs\|60 | `gap_up_abs\|60` | currency |
| `HIGH` | High | `high` | currency |
| `HIGH_1` | High\|1 | `high\|1` | currency |
| `HIGH_120` | High\|120 | `high\|120` | currency |
| `HIGH_15` | High\|15 | `high\|15` | currency |
| `HIGH_1M` | High\|1m | `high\|1M` | currency |
| `HIGH_1M_DATE` | High 1m Date | `High.1M.Date` | date |
| `HIGH_1W` | High\|1w | `high\|1W` | currency |
| `HIGH_240` | High\|240 | `high\|240` | currency |
| `HIGH_30` | High\|30 | `high\|30` | currency |
| `HIGH_3M_DATE` | High 3m Date | `High.3M.Date` | date |
| `HIGH_5` | High\|5 | `high\|5` | currency |
| `HIGH_5D` | High 5d | `High.5D` | round |
| `HIGH_60` | High\|60 | `high\|60` | currency |
| `HIGH_6M_DATE` | High 6m Date | `High.6M.Date` | date |
| `HIGH_ALL_CALC` | High All Calc | `High.All.Calc` | round |
| `HIGH_ALL_CALC_DATE` | High All Calc Date | `High.All.Calc.Date` | date |
| `HIGH_ALL_DATE` | High All Date | `High.All.Date` | date |
| `IPO_OFFER_PRICE_USD` | IPO Offer Price Usd | `ipo_offer_price_usd` | round |
| `IPO_PRICE_RANGE_USD_MAX` | IPO Price Range Usd Max | `ipo_price_range_usd_max` | round |
| `IPO_PRICE_RANGE_USD_MIN` | IPO Price Range Usd Min | `ipo_price_range_usd_min` | round |
| `LOW` | Low | `low` | currency |
| `LOW_1` | Low\|1 | `low\|1` | currency |
| `LOW_120` | Low\|120 | `low\|120` | currency |
| `LOW_15` | Low\|15 | `low\|15` | currency |
| `LOW_1M` | Low\|1m | `low\|1M` | currency |
| `LOW_1M_DATE` | Low 1m Date | `Low.1M.Date` | date |
| `LOW_1W` | Low\|1w | `low\|1W` | currency |
| `LOW_240` | Low\|240 | `low\|240` | currency |
| `LOW_30` | Low\|30 | `low\|30` | currency |
| `LOW_3M_DATE` | Low 3m Date | `Low.3M.Date` | date |
| `LOW_5` | Low\|5 | `low\|5` | currency |
| `LOW_5D` | Low 5d | `Low.5D` | round |
| `LOW_60` | Low\|60 | `low\|60` | currency |
| `LOW_6M_DATE` | Low 6m Date | `Low.6M.Date` | date |
| `LOW_AFTER_HIGH_ALL` | Low After High All | `Low.After.High.All` | currency |
| `LOW_AFTER_HIGH_ALL_CHANGE` | Low After High All Change | `low_after_high_all_change` | percent |
| `LOW_AFTER_HIGH_ALL_CHANGE_ABS` | Low After High All Change Abs | `low_after_high_all_change_abs` | currency |
| `LOW_ALL_CALC` | Low All Calc | `Low.All.Calc` | round |
| `LOW_ALL_CALC_DATE` | Low All Calc Date | `Low.All.Calc.Date` | date |
| `LOW_ALL_DATE` | Low All Date | `Low.All.Date` | date |
| `MONEYFLOW_1` | Moneyflow\|1 | `MoneyFlow\|1` | round |
| `MONEYFLOW_120` | Moneyflow\|120 | `MoneyFlow\|120` | round |
| `MONEYFLOW_15` | Moneyflow\|15 | `MoneyFlow\|15` | round |
| `MONEYFLOW_1M` | Moneyflow\|1m | `MoneyFlow\|1M` | round |
| `MONEYFLOW_1W` | Moneyflow\|1w | `MoneyFlow\|1W` | round |
| `MONEYFLOW_240` | Moneyflow\|240 | `MoneyFlow\|240` | round |
| `MONEYFLOW_30` | Moneyflow\|30 | `MoneyFlow\|30` | round |
| `MONEYFLOW_5` | Moneyflow\|5 | `MoneyFlow\|5` | round |
| `MONEYFLOW_60` | Moneyflow\|60 | `MoneyFlow\|60` | round |
| `MONEY_FLOW_14` | Money Flow (14) | `MoneyFlow` | round |
| `MONTH_HIGH_1` | 1-Month High | `High.1M` | round |
| `MONTH_HIGH_3` | 3-Month High | `High.3M` | round |
| `MONTH_HIGH_6` | 6-Month High | `High.6M` | round |
| `MONTH_LOW_1` | 1-Month Low | `Low.1M` | round |
| `MONTH_LOW_3` | 3-Month Low | `Low.3M` | round |
| `MONTH_LOW_6` | 6-Month Low | `Low.6M` | round |
| `NON_GAAP_PRICE_TO_EARNINGS_PER_SHARE_FORECAST_NEXT_FY` | Forward P/E (Non-GAAP) | `non_gaap_price_to_earnings_per_share_forecast_next_fy` | round |
| `OPEN` | Open | `open` | currency |
| `OPEN_1` | Open\|1 | `open\|1` | currency |
| `OPEN_120` | Open\|120 | `open\|120` | currency |
| `OPEN_15` | Open\|15 | `open\|15` | currency |
| `OPEN_1M` | Open\|1m | `open\|1M` | currency |
| `OPEN_1W` | Open\|1w | `open\|1W` | currency |
| `OPEN_240` | Open\|240 | `open\|240` | currency |
| `OPEN_30` | Open\|30 | `open\|30` | currency |
| `OPEN_5` | Open\|5 | `open\|5` | currency |
| `OPEN_60` | Open\|60 | `open\|60` | currency |
| `OPEN_ALL_CALC` | Open All Calc | `Open.All.Calc` | round |
| `OPERATING_CASH_FLOW_PER_SHARE_CURRENT` | Operating Cash Flow per Share Current | `operating_cash_flow_per_share_current` | currency |
| `OPERATING_CASH_FLOW_PER_SHARE_FH` | Operating Cash Flow per Share Fh | `operating_cash_flow_per_share_fh` | currency |
| `OPERATING_CASH_FLOW_PER_SHARE_FQ` | Operating Cash Flow per Share FQ | `operating_cash_flow_per_share_fq` | currency |
| `OPERATING_CASH_FLOW_PER_SHARE_FY` | Operating Cash Flow per Share FY | `operating_cash_flow_per_share_fy` | currency |
| `OPERATING_CASH_FLOW_PER_SHARE_TTM` | Operating Cash Flow per Share (TTM) | `operating_cash_flow_per_share_ttm` | currency |
| `POSTMARKET_CLOSE` | Post-market Close | `postmarket_close` | missing |
| `POSTMARKET_HIGH` | Post-market High | `postmarket_high` | missing |
| `POSTMARKET_LOW` | Post-market Low | `postmarket_low` | missing |
| `POSTMARKET_OPEN` | Post-market Open | `postmarket_open` | missing |
| `PRICE` | Price | `close` | currency |
| `PRICESCALE` | Pricescale | `pricescale` | round |
| `PRICE_52_WEEK_HIGH_DATE` | Price 52 Week High Date | `price_52_week_high_date` | date |
| `PRICE_52_WEEK_LOW_DATE` | Price 52 Week Low Date | `price_52_week_low_date` | date |
| `PRICE_ANNUAL_BOOK` | Price Annual Book | `price_annual_book` | round |
| `PRICE_ANNUAL_SALES` | Price Annual Sales | `price_annual_sales` | round |
| `PRICE_BOOK_CURRENT` | Price Book Current | `price_book_current` | round |
| `PRICE_CASH_FLOW_CURRENT` | Price Cash Flow Current | `price_cash_flow_current` | round |
| `PRICE_EARNINGS_CURRENT` | Price Earnings Current | `price_earnings_current` | round |
| `PRICE_EARNINGS_FORWARD_FY` | Price Earnings Forward FY | `price_earnings_forward_fy` | round |
| `PRICE_EARNINGS_GROWTH_TTM` | PEG Ratio (TTM) | `price_earnings_growth_ttm` | round |
| `PRICE_FREE_CASH_FLOW_CURRENT` | Price Free Cash Flow Current | `price_free_cash_flow_current` | round |
| `PRICE_SALES` | Price Sales | `price_sales` | currency |
| `PRICE_SALES_CURRENT` | Price Sales Current | `price_sales_current` | round |
| `PRICE_TARGET_1Y` | Price Target 1y | `price_target_1y` | currency |
| `PRICE_TARGET_1Y_DELTA` | Price Target 1y Delta | `price_target_1y_delta` | percent |
| `PRICE_TARGET_AVERAGE` | Target Price (Average) | `price_target_average` | currency |
| `PRICE_TARGET_HIGH` | Price Target High | `price_target_high` | round |
| `PRICE_TARGET_LOW` | Price Target Low | `price_target_low` | round |
| `PRICE_TARGET_MEDIAN` | Price Target Median | `price_target_median` | round |
| `PRICE_TO_BOOK_FY` | Price to Book (FY) | `price_book_ratio` | round |
| `PRICE_TO_BOOK_MRQ` | Price to Book (MRQ) | `price_book_fq` | round |
| `PRICE_TO_CASH_F_OPERATING_ACTIVITIES_TTM` | Price to Cash Flow (TTM) | `price_to_cash_f_operating_activities_ttm` | round |
| `PRICE_TO_CASH_RATIO` | Price to Cash Ratio | `price_to_cash_ratio` | round |
| `PRICE_TO_EARNINGS_RATIO_TTM` | Price to Earnings Ratio (TTM) | `price_earnings_ttm` | round |
| `PRICE_TO_FREE_CASH_FLOW_TTM` | Price to Free Cash Flow (TTM) | `price_free_cash_flow_ttm` | round |
| `PRICE_TO_REVENUE_RATIO_TTM` | Price to Revenue Ratio (TTM) | `price_revenue_ttm` | round |
| `PRICE_TO_SALES_FY` | Price to Sales (FY) | `price_sales_ratio` | round |
| `PRICE_TO_WORKING_CAPITAL_FQ` | Price to Net Working Capital | `price_to_working_capital_fq` | round |
| `WEEK_HIGH_52` | 52 Week High | `price_52_week_high` | round |
| `WEEK_LOW_52` | 52 Week Low | `price_52_week_low` | round |

## Volume

*85 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `AVERAGE_VOLUME` | Average Volume | `average_volume` | round |
| `AVERAGE_VOLUME_10D_CALC_1` | Average Volume 10d Calc\|1 | `average_volume_10d_calc\|1` | round |
| `AVERAGE_VOLUME_10D_CALC_120` | Average Volume 10d Calc\|120 | `average_volume_10d_calc\|120` | round |
| `AVERAGE_VOLUME_10D_CALC_15` | Average Volume 10d Calc\|15 | `average_volume_10d_calc\|15` | round |
| `AVERAGE_VOLUME_10D_CALC_1M` | Average Volume 10d Calc\|1m | `average_volume_10d_calc\|1M` | round |
| `AVERAGE_VOLUME_10D_CALC_1W` | Average Volume 10d Calc\|1w | `average_volume_10d_calc\|1W` | round |
| `AVERAGE_VOLUME_10D_CALC_240` | Average Volume 10d Calc\|240 | `average_volume_10d_calc\|240` | round |
| `AVERAGE_VOLUME_10D_CALC_30` | Average Volume 10d Calc\|30 | `average_volume_10d_calc\|30` | round |
| `AVERAGE_VOLUME_10D_CALC_5` | Average Volume 10d Calc\|5 | `average_volume_10d_calc\|5` | round |
| `AVERAGE_VOLUME_10D_CALC_60` | Average Volume 10d Calc\|60 | `average_volume_10d_calc\|60` | round |
| `AVERAGE_VOLUME_10_DAY` | Average Volume (10 day) | `average_volume_10d_calc` | number_group |
| `AVERAGE_VOLUME_30D_CALC_1` | Average Volume 30d Calc\|1 | `average_volume_30d_calc\|1` | round |
| `AVERAGE_VOLUME_30D_CALC_120` | Average Volume 30d Calc\|120 | `average_volume_30d_calc\|120` | round |
| `AVERAGE_VOLUME_30D_CALC_15` | Average Volume 30d Calc\|15 | `average_volume_30d_calc\|15` | round |
| `AVERAGE_VOLUME_30D_CALC_1M` | Average Volume 30d Calc\|1m | `average_volume_30d_calc\|1M` | round |
| `AVERAGE_VOLUME_30D_CALC_1W` | Average Volume 30d Calc\|1w | `average_volume_30d_calc\|1W` | round |
| `AVERAGE_VOLUME_30D_CALC_240` | Average Volume 30d Calc\|240 | `average_volume_30d_calc\|240` | round |
| `AVERAGE_VOLUME_30D_CALC_30` | Average Volume 30d Calc\|30 | `average_volume_30d_calc\|30` | round |
| `AVERAGE_VOLUME_30D_CALC_5` | Average Volume 30d Calc\|5 | `average_volume_30d_calc\|5` | round |
| `AVERAGE_VOLUME_30D_CALC_60` | Average Volume 30d Calc\|60 | `average_volume_30d_calc\|60` | round |
| `AVERAGE_VOLUME_30_DAY` | Average Volume (30 day) | `average_volume_30d_calc` | number_group |
| `AVERAGE_VOLUME_60D_CALC_1` | Average Volume 60d Calc\|1 | `average_volume_60d_calc\|1` | round |
| `AVERAGE_VOLUME_60D_CALC_120` | Average Volume 60d Calc\|120 | `average_volume_60d_calc\|120` | round |
| `AVERAGE_VOLUME_60D_CALC_15` | Average Volume 60d Calc\|15 | `average_volume_60d_calc\|15` | round |
| `AVERAGE_VOLUME_60D_CALC_1M` | Average Volume 60d Calc\|1m | `average_volume_60d_calc\|1M` | round |
| `AVERAGE_VOLUME_60D_CALC_1W` | Average Volume 60d Calc\|1w | `average_volume_60d_calc\|1W` | round |
| `AVERAGE_VOLUME_60D_CALC_240` | Average Volume 60d Calc\|240 | `average_volume_60d_calc\|240` | round |
| `AVERAGE_VOLUME_60D_CALC_30` | Average Volume 60d Calc\|30 | `average_volume_60d_calc\|30` | round |
| `AVERAGE_VOLUME_60D_CALC_5` | Average Volume 60d Calc\|5 | `average_volume_60d_calc\|5` | round |
| `AVERAGE_VOLUME_60D_CALC_60` | Average Volume 60d Calc\|60 | `average_volume_60d_calc\|60` | round |
| `AVERAGE_VOLUME_60_DAY` | Average Volume (60 day) | `average_volume_60d_calc` | number_group |
| `AVERAGE_VOLUME_90D_CALC_1` | Average Volume 90d Calc\|1 | `average_volume_90d_calc\|1` | round |
| `AVERAGE_VOLUME_90D_CALC_120` | Average Volume 90d Calc\|120 | `average_volume_90d_calc\|120` | round |
| `AVERAGE_VOLUME_90D_CALC_15` | Average Volume 90d Calc\|15 | `average_volume_90d_calc\|15` | round |
| `AVERAGE_VOLUME_90D_CALC_1M` | Average Volume 90d Calc\|1m | `average_volume_90d_calc\|1M` | round |
| `AVERAGE_VOLUME_90D_CALC_1W` | Average Volume 90d Calc\|1w | `average_volume_90d_calc\|1W` | round |
| `AVERAGE_VOLUME_90D_CALC_240` | Average Volume 90d Calc\|240 | `average_volume_90d_calc\|240` | round |
| `AVERAGE_VOLUME_90D_CALC_30` | Average Volume 90d Calc\|30 | `average_volume_90d_calc\|30` | round |
| `AVERAGE_VOLUME_90D_CALC_5` | Average Volume 90d Calc\|5 | `average_volume_90d_calc\|5` | round |
| `AVERAGE_VOLUME_90D_CALC_60` | Average Volume 90d Calc\|60 | `average_volume_90d_calc\|60` | round |
| `AVERAGE_VOLUME_90_DAY` | Average Volume (90 day) | `average_volume_90d_calc` | number_group |
| `POSTMARKET_VOLUME` | Post-market Volume | `postmarket_volume` | missing |
| `RELATIVE_VOLUME` | Relative Volume | `relative_volume_10d_calc` | round |
| `RELATIVE_VOLUME_10D_CALC_1` | Relative Volume 10d Calc\|1 | `relative_volume_10d_calc\|1` | round |
| `RELATIVE_VOLUME_10D_CALC_120` | Relative Volume 10d Calc\|120 | `relative_volume_10d_calc\|120` | round |
| `RELATIVE_VOLUME_10D_CALC_15` | Relative Volume 10d Calc\|15 | `relative_volume_10d_calc\|15` | round |
| `RELATIVE_VOLUME_10D_CALC_1M` | Relative Volume 10d Calc\|1m | `relative_volume_10d_calc\|1M` | round |
| `RELATIVE_VOLUME_10D_CALC_1W` | Relative Volume 10d Calc\|1w | `relative_volume_10d_calc\|1W` | round |
| `RELATIVE_VOLUME_10D_CALC_240` | Relative Volume 10d Calc\|240 | `relative_volume_10d_calc\|240` | round |
| `RELATIVE_VOLUME_10D_CALC_30` | Relative Volume 10d Calc\|30 | `relative_volume_10d_calc\|30` | round |
| `RELATIVE_VOLUME_10D_CALC_5` | Relative Volume 10d Calc\|5 | `relative_volume_10d_calc\|5` | round |
| `RELATIVE_VOLUME_10D_CALC_60` | Relative Volume 10d Calc\|60 | `relative_volume_10d_calc\|60` | round |
| `RELATIVE_VOLUME_2` | Relative Volume | `relative_volume` | round |
| `RELATIVE_VOLUME_AT_TIME` | Relative Volume at Time | `relative_volume_intraday.5` | round |
| `RELATIVE_VOLUME_INTRADAY_5` | Relative Volume Intraday\|5 | `relative_volume_intraday\|5` | round |
| `VOLUME` | Volume | `volume` | number_group |
| `VOLUME_1` | Volume\|1 | `volume\|1` | round |
| `VOLUME_120` | Volume\|120 | `volume\|120` | round |
| `VOLUME_15` | Volume\|15 | `volume\|15` | round |
| `VOLUME_1M` | Volume\|1m | `volume\|1M` | round |
| `VOLUME_1W` | Volume\|1w | `volume\|1W` | round |
| `VOLUME_240` | Volume\|240 | `volume\|240` | round |
| `VOLUME_30` | Volume\|30 | `volume\|30` | round |
| `VOLUME_5` | Volume\|5 | `volume\|5` | round |
| `VOLUME_60` | Volume\|60 | `volume\|60` | round |
| `VOLUME_CHANGE` | Volume Change | `volume_change` | percent |
| `VOLUME_CHANGE_1` | Volume Change\|1 | `volume_change\|1` | percent |
| `VOLUME_CHANGE_120` | Volume Change\|120 | `volume_change\|120` | percent |
| `VOLUME_CHANGE_15` | Volume Change\|15 | `volume_change\|15` | percent |
| `VOLUME_CHANGE_1M` | Volume Change\|1m | `volume_change\|1M` | percent |
| `VOLUME_CHANGE_1W` | Volume Change\|1w | `volume_change\|1W` | percent |
| `VOLUME_CHANGE_240` | Volume Change\|240 | `volume_change\|240` | percent |
| `VOLUME_CHANGE_30` | Volume Change\|30 | `volume_change\|30` | percent |
| `VOLUME_CHANGE_5` | Volume Change\|5 | `volume_change\|5` | percent |
| `VOLUME_CHANGE_60` | Volume Change\|60 | `volume_change\|60` | percent |
| `VOLUME_CHANGE_ABS` | Volume Change Abs | `volume_change_abs` | round |
| `VOLUME_CHANGE_ABS_1` | Volume Change Abs\|1 | `volume_change_abs\|1` | round |
| `VOLUME_CHANGE_ABS_120` | Volume Change Abs\|120 | `volume_change_abs\|120` | round |
| `VOLUME_CHANGE_ABS_15` | Volume Change Abs\|15 | `volume_change_abs\|15` | round |
| `VOLUME_CHANGE_ABS_1M` | Volume Change Abs\|1m | `volume_change_abs\|1M` | round |
| `VOLUME_CHANGE_ABS_1W` | Volume Change Abs\|1w | `volume_change_abs\|1W` | round |
| `VOLUME_CHANGE_ABS_240` | Volume Change Abs\|240 | `volume_change_abs\|240` | round |
| `VOLUME_CHANGE_ABS_30` | Volume Change Abs\|30 | `volume_change_abs\|30` | round |
| `VOLUME_CHANGE_ABS_5` | Volume Change Abs\|5 | `volume_change_abs\|5` | round |
| `VOLUME_CHANGE_ABS_60` | Volume Change Abs\|60 | `volume_change_abs\|60` | round |

## Performance

*31 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `ALL_TIME_PERFORMANCE` | All Time Performance | `Perf.All` | percent |
| `AUM_PERF_1M` | Aum Perf 1m | `aum_perf.1M` | round |
| `AUM_PERF_1Y` | Aum Perf 1y | `aum_perf.1Y` | round |
| `AUM_PERF_3M` | Aum Perf 3m | `aum_perf.3M` | round |
| `AUM_PERF_3Y` | Aum Perf 3y | `aum_perf.3Y` | round |
| `AUM_PERF_5Y` | Aum Perf 5y | `aum_perf.5Y` | round |
| `AUM_PERF_YTD` | Aum Perf Ytd | `aum_perf.YTD` | round |
| `MONTHLY_PERFORMANCE` | Monthly Performance | `Perf.1M` | percent |
| `MONTH_PERFORMANCE_3` | 3-Month Performance | `Perf.3M` | percent |
| `MONTH_PERFORMANCE_6` | 6-Month Performance | `Perf.6M` | percent |
| `NAV_PERF_1M` | Nav Perf 1m | `nav_perf.1M` | round |
| `NAV_PERF_1Y` | Nav Perf 1y | `nav_perf.1Y` | round |
| `NAV_PERF_3M` | Nav Perf 3m | `nav_perf.3M` | round |
| `NAV_PERF_3Y` | Nav Perf 3y | `nav_perf.3Y` | round |
| `NAV_PERF_5Y` | Nav Perf 5y | `nav_perf.5Y` | round |
| `NAV_PERF_YTD` | Nav Perf Ytd | `nav_perf.YTD` | round |
| `PERF_10Y` | Perf 10y | `Perf.10Y` | round |
| `PERF_1M_MARKETCAP` | Market Cap Performance 1M % | `Perf.1M.MarketCap` | percent |
| `PERF_1W_MARKETCAP` | Market Cap Performance 1W % | `Perf.1W.MarketCap` | percent |
| `PERF_1Y_MARKETCAP` | Perf 1y Marketcap | `Perf.1Y.MarketCap` | round |
| `PERF_3M_MARKETCAP` | Market Cap Performance 3M % | `Perf.3M.MarketCap` | percent |
| `PERF_3Y` | Perf 3y | `Perf.3Y` | round |
| `PERF_5D` | Perf 5d | `Perf.5D` | round |
| `PERF_5Y_MARKETCAP` | Perf 5y Marketcap | `Perf.5Y.MarketCap` | round |
| `PERF_6M_MARKETCAP` | Market Cap Performance 6M % | `Perf.6M.MarketCap` | percent |
| `PERF_YTD_MARKETCAP` | Market Cap Performance YTD % | `Perf.YTD.MarketCap` | percent |
| `PERF_Y_MARKETCAP` | Market Cap Performance 1Y % | `Perf.Y.MarketCap` | percent |
| `WEEKLY_PERFORMANCE` | Weekly Performance | `Perf.W` | percent |
| `YEARLY_PERFORMANCE` | Yearly Performance | `Perf.Y` | percent |
| `YTD_PERFORMANCE` | YTD Performance | `Perf.YTD` | percent |
| `Y_PERFORMANCE_5` | 5Y Performance | `Perf.5Y` | percent |

## Moving Averages

*721 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `EMA100_1` | Ema100\|1 | `EMA100\|1` | round |
| `EMA100_120` | Ema100\|120 | `EMA100\|120` | round |
| `EMA100_15` | Ema100\|15 | `EMA100\|15` | round |
| `EMA100_1M` | Ema100\|1m | `EMA100\|1M` | round |
| `EMA100_1W` | Ema100\|1w | `EMA100\|1W` | round |
| `EMA100_240` | Ema100\|240 | `EMA100\|240` | round |
| `EMA100_30` | Ema100\|30 | `EMA100\|30` | round |
| `EMA100_5` | Ema100\|5 | `EMA100\|5` | round |
| `EMA100_60` | Ema100\|60 | `EMA100\|60` | round |
| `EMA10_1` | Ema10\|1 | `EMA10\|1` | round |
| `EMA10_120` | Ema10\|120 | `EMA10\|120` | round |
| `EMA10_15` | Ema10\|15 | `EMA10\|15` | round |
| `EMA10_1M` | Ema10\|1m | `EMA10\|1M` | round |
| `EMA10_1W` | Ema10\|1w | `EMA10\|1W` | round |
| `EMA10_240` | Ema10\|240 | `EMA10\|240` | round |
| `EMA10_30` | Ema10\|30 | `EMA10\|30` | round |
| `EMA10_5` | Ema10\|5 | `EMA10\|5` | round |
| `EMA10_60` | Ema10\|60 | `EMA10\|60` | round |
| `EMA12` | Ema12 | `EMA12` | round |
| `EMA120` | Ema120 | `EMA120` | round |
| `EMA120_1` | Ema120\|1 | `EMA120\|1` | round |
| `EMA120_120` | Ema120\|120 | `EMA120\|120` | round |
| `EMA120_15` | Ema120\|15 | `EMA120\|15` | round |
| `EMA120_1M` | Ema120\|1m | `EMA120\|1M` | round |
| `EMA120_1W` | Ema120\|1w | `EMA120\|1W` | round |
| `EMA120_240` | Ema120\|240 | `EMA120\|240` | round |
| `EMA120_30` | Ema120\|30 | `EMA120\|30` | round |
| `EMA120_5` | Ema120\|5 | `EMA120\|5` | round |
| `EMA120_60` | Ema120\|60 | `EMA120\|60` | round |
| `EMA12_1` | Ema12\|1 | `EMA12\|1` | round |
| `EMA12_120` | Ema12\|120 | `EMA12\|120` | round |
| `EMA12_15` | Ema12\|15 | `EMA12\|15` | round |
| `EMA12_1M` | Ema12\|1m | `EMA12\|1M` | round |
| `EMA12_1W` | Ema12\|1w | `EMA12\|1W` | round |
| `EMA12_240` | Ema12\|240 | `EMA12\|240` | round |
| `EMA12_30` | Ema12\|30 | `EMA12\|30` | round |
| `EMA12_5` | Ema12\|5 | `EMA12\|5` | round |
| `EMA12_60` | Ema12\|60 | `EMA12\|60` | round |
| `EMA13` | Ema13 | `EMA13` | round |
| `EMA13_1` | Ema13\|1 | `EMA13\|1` | round |
| `EMA13_120` | Ema13\|120 | `EMA13\|120` | round |
| `EMA13_15` | Ema13\|15 | `EMA13\|15` | round |
| `EMA13_1M` | Ema13\|1m | `EMA13\|1M` | round |
| `EMA13_1W` | Ema13\|1w | `EMA13\|1W` | round |
| `EMA13_240` | Ema13\|240 | `EMA13\|240` | round |
| `EMA13_30` | Ema13\|30 | `EMA13\|30` | round |
| `EMA13_5` | Ema13\|5 | `EMA13\|5` | round |
| `EMA13_60` | Ema13\|60 | `EMA13\|60` | round |
| `EMA14` | Ema14 | `EMA14` | round |
| `EMA144` | Ema144 | `EMA144` | round |
| `EMA144_1` | Ema144\|1 | `EMA144\|1` | round |
| `EMA144_120` | Ema144\|120 | `EMA144\|120` | round |
| `EMA144_15` | Ema144\|15 | `EMA144\|15` | round |
| `EMA144_1M` | Ema144\|1m | `EMA144\|1M` | round |
| `EMA144_1W` | Ema144\|1w | `EMA144\|1W` | round |
| `EMA144_240` | Ema144\|240 | `EMA144\|240` | round |
| `EMA144_30` | Ema144\|30 | `EMA144\|30` | round |
| `EMA144_5` | Ema144\|5 | `EMA144\|5` | round |
| `EMA144_60` | Ema144\|60 | `EMA144\|60` | round |
| `EMA14_1` | Ema14\|1 | `EMA14\|1` | round |
| `EMA14_120` | Ema14\|120 | `EMA14\|120` | round |
| `EMA14_15` | Ema14\|15 | `EMA14\|15` | round |
| `EMA14_1M` | Ema14\|1m | `EMA14\|1M` | round |
| `EMA14_1W` | Ema14\|1w | `EMA14\|1W` | round |
| `EMA14_240` | Ema14\|240 | `EMA14\|240` | round |
| `EMA14_30` | Ema14\|30 | `EMA14\|30` | round |
| `EMA14_5` | Ema14\|5 | `EMA14\|5` | round |
| `EMA14_60` | Ema14\|60 | `EMA14\|60` | round |
| `EMA15` | Ema15 | `EMA15` | round |
| `EMA150` | Ema150 | `EMA150` | round |
| `EMA150_1` | Ema150\|1 | `EMA150\|1` | round |
| `EMA150_120` | Ema150\|120 | `EMA150\|120` | round |
| `EMA150_15` | Ema150\|15 | `EMA150\|15` | round |
| `EMA150_1M` | Ema150\|1m | `EMA150\|1M` | round |
| `EMA150_1W` | Ema150\|1w | `EMA150\|1W` | round |
| `EMA150_240` | Ema150\|240 | `EMA150\|240` | round |
| `EMA150_30` | Ema150\|30 | `EMA150\|30` | round |
| `EMA150_5` | Ema150\|5 | `EMA150\|5` | round |
| `EMA150_60` | Ema150\|60 | `EMA150\|60` | round |
| `EMA15_1` | Ema15\|1 | `EMA15\|1` | round |
| `EMA15_120` | Ema15\|120 | `EMA15\|120` | round |
| `EMA15_15` | Ema15\|15 | `EMA15\|15` | round |
| `EMA15_1M` | Ema15\|1m | `EMA15\|1M` | round |
| `EMA15_1W` | Ema15\|1w | `EMA15\|1W` | round |
| `EMA15_240` | Ema15\|240 | `EMA15\|240` | round |
| `EMA15_30` | Ema15\|30 | `EMA15\|30` | round |
| `EMA15_5` | Ema15\|5 | `EMA15\|5` | round |
| `EMA15_60` | Ema15\|60 | `EMA15\|60` | round |
| `EMA2` | Ema2 | `EMA2` | round |
| `EMA200_1` | Ema200\|1 | `EMA200\|1` | round |
| `EMA200_120` | Ema200\|120 | `EMA200\|120` | round |
| `EMA200_15` | Ema200\|15 | `EMA200\|15` | round |
| `EMA200_1M` | Ema200\|1m | `EMA200\|1M` | round |
| `EMA200_1W` | Ema200\|1w | `EMA200\|1W` | round |
| `EMA200_240` | Ema200\|240 | `EMA200\|240` | round |
| `EMA200_30` | Ema200\|30 | `EMA200\|30` | round |
| `EMA200_5` | Ema200\|5 | `EMA200\|5` | round |
| `EMA200_60` | Ema200\|60 | `EMA200\|60` | round |
| `EMA20_1` | Ema20\|1 | `EMA20\|1` | round |
| `EMA20_120` | Ema20\|120 | `EMA20\|120` | round |
| `EMA20_15` | Ema20\|15 | `EMA20\|15` | round |
| `EMA20_1M` | Ema20\|1m | `EMA20\|1M` | round |
| `EMA20_1W` | Ema20\|1w | `EMA20\|1W` | round |
| `EMA20_240` | Ema20\|240 | `EMA20\|240` | round |
| `EMA20_30` | Ema20\|30 | `EMA20\|30` | round |
| `EMA20_5` | Ema20\|5 | `EMA20\|5` | round |
| `EMA20_60` | Ema20\|60 | `EMA20\|60` | round |
| `EMA21` | Ema21 | `EMA21` | round |
| `EMA21_1` | Ema21\|1 | `EMA21\|1` | round |
| `EMA21_120` | Ema21\|120 | `EMA21\|120` | round |
| `EMA21_15` | Ema21\|15 | `EMA21\|15` | round |
| `EMA21_1M` | Ema21\|1m | `EMA21\|1M` | round |
| `EMA21_1W` | Ema21\|1w | `EMA21\|1W` | round |
| `EMA21_240` | Ema21\|240 | `EMA21\|240` | round |
| `EMA21_30` | Ema21\|30 | `EMA21\|30` | round |
| `EMA21_5` | Ema21\|5 | `EMA21\|5` | round |
| `EMA21_60` | Ema21\|60 | `EMA21\|60` | round |
| `EMA25` | Ema25 | `EMA25` | round |
| `EMA250` | Ema250 | `EMA250` | round |
| `EMA250_1` | Ema250\|1 | `EMA250\|1` | round |
| `EMA250_120` | Ema250\|120 | `EMA250\|120` | round |
| `EMA250_15` | Ema250\|15 | `EMA250\|15` | round |
| `EMA250_1M` | Ema250\|1m | `EMA250\|1M` | round |
| `EMA250_1W` | Ema250\|1w | `EMA250\|1W` | round |
| `EMA250_240` | Ema250\|240 | `EMA250\|240` | round |
| `EMA250_30` | Ema250\|30 | `EMA250\|30` | round |
| `EMA250_5` | Ema250\|5 | `EMA250\|5` | round |
| `EMA250_60` | Ema250\|60 | `EMA250\|60` | round |
| `EMA25_1` | Ema25\|1 | `EMA25\|1` | round |
| `EMA25_120` | Ema25\|120 | `EMA25\|120` | round |
| `EMA25_15` | Ema25\|15 | `EMA25\|15` | round |
| `EMA25_1M` | Ema25\|1m | `EMA25\|1M` | round |
| `EMA25_1W` | Ema25\|1w | `EMA25\|1W` | round |
| `EMA25_240` | Ema25\|240 | `EMA25\|240` | round |
| `EMA25_30` | Ema25\|30 | `EMA25\|30` | round |
| `EMA25_5` | Ema25\|5 | `EMA25\|5` | round |
| `EMA25_60` | Ema25\|60 | `EMA25\|60` | round |
| `EMA26` | Ema26 | `EMA26` | round |
| `EMA26_1` | Ema26\|1 | `EMA26\|1` | round |
| `EMA26_120` | Ema26\|120 | `EMA26\|120` | round |
| `EMA26_15` | Ema26\|15 | `EMA26\|15` | round |
| `EMA26_1M` | Ema26\|1m | `EMA26\|1M` | round |
| `EMA26_1W` | Ema26\|1w | `EMA26\|1W` | round |
| `EMA26_240` | Ema26\|240 | `EMA26\|240` | round |
| `EMA26_30` | Ema26\|30 | `EMA26\|30` | round |
| `EMA26_5` | Ema26\|5 | `EMA26\|5` | round |
| `EMA26_60` | Ema26\|60 | `EMA26\|60` | round |
| `EMA2_1` | Ema2\|1 | `EMA2\|1` | round |
| `EMA2_120` | Ema2\|120 | `EMA2\|120` | round |
| `EMA2_15` | Ema2\|15 | `EMA2\|15` | round |
| `EMA2_1M` | Ema2\|1m | `EMA2\|1M` | round |
| `EMA2_1W` | Ema2\|1w | `EMA2\|1W` | round |
| `EMA2_240` | Ema2\|240 | `EMA2\|240` | round |
| `EMA2_30` | Ema2\|30 | `EMA2\|30` | round |
| `EMA2_5` | Ema2\|5 | `EMA2\|5` | round |
| `EMA2_60` | Ema2\|60 | `EMA2\|60` | round |
| `EMA3` | Ema3 | `EMA3` | round |
| `EMA300` | Ema300 | `EMA300` | round |
| `EMA300_1` | Ema300\|1 | `EMA300\|1` | round |
| `EMA300_120` | Ema300\|120 | `EMA300\|120` | round |
| `EMA300_15` | Ema300\|15 | `EMA300\|15` | round |
| `EMA300_1M` | Ema300\|1m | `EMA300\|1M` | round |
| `EMA300_1W` | Ema300\|1w | `EMA300\|1W` | round |
| `EMA300_240` | Ema300\|240 | `EMA300\|240` | round |
| `EMA300_30` | Ema300\|30 | `EMA300\|30` | round |
| `EMA300_5` | Ema300\|5 | `EMA300\|5` | round |
| `EMA300_60` | Ema300\|60 | `EMA300\|60` | round |
| `EMA30_1` | Ema30\|1 | `EMA30\|1` | round |
| `EMA30_120` | Ema30\|120 | `EMA30\|120` | round |
| `EMA30_15` | Ema30\|15 | `EMA30\|15` | round |
| `EMA30_1M` | Ema30\|1m | `EMA30\|1M` | round |
| `EMA30_1W` | Ema30\|1w | `EMA30\|1W` | round |
| `EMA30_240` | Ema30\|240 | `EMA30\|240` | round |
| `EMA30_30` | Ema30\|30 | `EMA30\|30` | round |
| `EMA30_5` | Ema30\|5 | `EMA30\|5` | round |
| `EMA30_60` | Ema30\|60 | `EMA30\|60` | round |
| `EMA34` | Ema34 | `EMA34` | round |
| `EMA34_1` | Ema34\|1 | `EMA34\|1` | round |
| `EMA34_120` | Ema34\|120 | `EMA34\|120` | round |
| `EMA34_15` | Ema34\|15 | `EMA34\|15` | round |
| `EMA34_1M` | Ema34\|1m | `EMA34\|1M` | round |
| `EMA34_1W` | Ema34\|1w | `EMA34\|1W` | round |
| `EMA34_240` | Ema34\|240 | `EMA34\|240` | round |
| `EMA34_30` | Ema34\|30 | `EMA34\|30` | round |
| `EMA34_5` | Ema34\|5 | `EMA34\|5` | round |
| `EMA34_60` | Ema34\|60 | `EMA34\|60` | round |
| `EMA3_1` | Ema3\|1 | `EMA3\|1` | round |
| `EMA3_120` | Ema3\|120 | `EMA3\|120` | round |
| `EMA3_15` | Ema3\|15 | `EMA3\|15` | round |
| `EMA3_1M` | Ema3\|1m | `EMA3\|1M` | round |
| `EMA3_1W` | Ema3\|1w | `EMA3\|1W` | round |
| `EMA3_240` | Ema3\|240 | `EMA3\|240` | round |
| `EMA3_30` | Ema3\|30 | `EMA3\|30` | round |
| `EMA3_5` | Ema3\|5 | `EMA3\|5` | round |
| `EMA3_60` | Ema3\|60 | `EMA3\|60` | round |
| `EMA40` | Ema40 | `EMA40` | round |
| `EMA40_1` | Ema40\|1 | `EMA40\|1` | round |
| `EMA40_120` | Ema40\|120 | `EMA40\|120` | round |
| `EMA40_15` | Ema40\|15 | `EMA40\|15` | round |
| `EMA40_1M` | Ema40\|1m | `EMA40\|1M` | round |
| `EMA40_1W` | Ema40\|1w | `EMA40\|1W` | round |
| `EMA40_240` | Ema40\|240 | `EMA40\|240` | round |
| `EMA40_30` | Ema40\|30 | `EMA40\|30` | round |
| `EMA40_5` | Ema40\|5 | `EMA40\|5` | round |
| `EMA40_60` | Ema40\|60 | `EMA40\|60` | round |
| `EMA50_1` | Ema50\|1 | `EMA50\|1` | round |
| `EMA50_120` | Ema50\|120 | `EMA50\|120` | round |
| `EMA50_15` | Ema50\|15 | `EMA50\|15` | round |
| `EMA50_1M` | Ema50\|1m | `EMA50\|1M` | round |
| `EMA50_1W` | Ema50\|1w | `EMA50\|1W` | round |
| `EMA50_240` | Ema50\|240 | `EMA50\|240` | round |
| `EMA50_30` | Ema50\|30 | `EMA50\|30` | round |
| `EMA50_5` | Ema50\|5 | `EMA50\|5` | round |
| `EMA50_60` | Ema50\|60 | `EMA50\|60` | round |
| `EMA55` | Ema55 | `EMA55` | round |
| `EMA55_1` | Ema55\|1 | `EMA55\|1` | round |
| `EMA55_120` | Ema55\|120 | `EMA55\|120` | round |
| `EMA55_15` | Ema55\|15 | `EMA55\|15` | round |
| `EMA55_1M` | Ema55\|1m | `EMA55\|1M` | round |
| `EMA55_1W` | Ema55\|1w | `EMA55\|1W` | round |
| `EMA55_240` | Ema55\|240 | `EMA55\|240` | round |
| `EMA55_30` | Ema55\|30 | `EMA55\|30` | round |
| `EMA55_5` | Ema55\|5 | `EMA55\|5` | round |
| `EMA55_60` | Ema55\|60 | `EMA55\|60` | round |
| `EMA5_1` | Ema5\|1 | `EMA5\|1` | round |
| `EMA5_120` | Ema5\|120 | `EMA5\|120` | round |
| `EMA5_15` | Ema5\|15 | `EMA5\|15` | round |
| `EMA5_1M` | Ema5\|1m | `EMA5\|1M` | round |
| `EMA5_1W` | Ema5\|1w | `EMA5\|1W` | round |
| `EMA5_240` | Ema5\|240 | `EMA5\|240` | round |
| `EMA5_30` | Ema5\|30 | `EMA5\|30` | round |
| `EMA5_5` | Ema5\|5 | `EMA5\|5` | round |
| `EMA5_60` | Ema5\|60 | `EMA5\|60` | round |
| `EMA6` | Ema6 | `EMA6` | round |
| `EMA60` | Ema60 | `EMA60` | round |
| `EMA60_1` | Ema60\|1 | `EMA60\|1` | round |
| `EMA60_120` | Ema60\|120 | `EMA60\|120` | round |
| `EMA60_15` | Ema60\|15 | `EMA60\|15` | round |
| `EMA60_1M` | Ema60\|1m | `EMA60\|1M` | round |
| `EMA60_1W` | Ema60\|1w | `EMA60\|1W` | round |
| `EMA60_240` | Ema60\|240 | `EMA60\|240` | round |
| `EMA60_30` | Ema60\|30 | `EMA60\|30` | round |
| `EMA60_5` | Ema60\|5 | `EMA60\|5` | round |
| `EMA60_60` | Ema60\|60 | `EMA60\|60` | round |
| `EMA6_1` | Ema6\|1 | `EMA6\|1` | round |
| `EMA6_120` | Ema6\|120 | `EMA6\|120` | round |
| `EMA6_15` | Ema6\|15 | `EMA6\|15` | round |
| `EMA6_1M` | Ema6\|1m | `EMA6\|1M` | round |
| `EMA6_1W` | Ema6\|1w | `EMA6\|1W` | round |
| `EMA6_240` | Ema6\|240 | `EMA6\|240` | round |
| `EMA6_30` | Ema6\|30 | `EMA6\|30` | round |
| `EMA6_5` | Ema6\|5 | `EMA6\|5` | round |
| `EMA6_60` | Ema6\|60 | `EMA6\|60` | round |
| `EMA7` | Ema7 | `EMA7` | round |
| `EMA75` | Ema75 | `EMA75` | round |
| `EMA75_1` | Ema75\|1 | `EMA75\|1` | round |
| `EMA75_120` | Ema75\|120 | `EMA75\|120` | round |
| `EMA75_15` | Ema75\|15 | `EMA75\|15` | round |
| `EMA75_1M` | Ema75\|1m | `EMA75\|1M` | round |
| `EMA75_1W` | Ema75\|1w | `EMA75\|1W` | round |
| `EMA75_240` | Ema75\|240 | `EMA75\|240` | round |
| `EMA75_30` | Ema75\|30 | `EMA75\|30` | round |
| `EMA75_5` | Ema75\|5 | `EMA75\|5` | round |
| `EMA75_60` | Ema75\|60 | `EMA75\|60` | round |
| `EMA7_1` | Ema7\|1 | `EMA7\|1` | round |
| `EMA7_120` | Ema7\|120 | `EMA7\|120` | round |
| `EMA7_15` | Ema7\|15 | `EMA7\|15` | round |
| `EMA7_1M` | Ema7\|1m | `EMA7\|1M` | round |
| `EMA7_1W` | Ema7\|1w | `EMA7\|1W` | round |
| `EMA7_240` | Ema7\|240 | `EMA7\|240` | round |
| `EMA7_30` | Ema7\|30 | `EMA7\|30` | round |
| `EMA7_5` | Ema7\|5 | `EMA7\|5` | round |
| `EMA7_60` | Ema7\|60 | `EMA7\|60` | round |
| `EMA8` | Ema8 | `EMA8` | round |
| `EMA89` | Ema89 | `EMA89` | round |
| `EMA89_1` | Ema89\|1 | `EMA89\|1` | round |
| `EMA89_120` | Ema89\|120 | `EMA89\|120` | round |
| `EMA89_15` | Ema89\|15 | `EMA89\|15` | round |
| `EMA89_1M` | Ema89\|1m | `EMA89\|1M` | round |
| `EMA89_1W` | Ema89\|1w | `EMA89\|1W` | round |
| `EMA89_240` | Ema89\|240 | `EMA89\|240` | round |
| `EMA89_30` | Ema89\|30 | `EMA89\|30` | round |
| `EMA89_5` | Ema89\|5 | `EMA89\|5` | round |
| `EMA89_60` | Ema89\|60 | `EMA89\|60` | round |
| `EMA8_1` | Ema8\|1 | `EMA8\|1` | round |
| `EMA8_120` | Ema8\|120 | `EMA8\|120` | round |
| `EMA8_15` | Ema8\|15 | `EMA8\|15` | round |
| `EMA8_1M` | Ema8\|1m | `EMA8\|1M` | round |
| `EMA8_1W` | Ema8\|1w | `EMA8\|1W` | round |
| `EMA8_240` | Ema8\|240 | `EMA8\|240` | round |
| `EMA8_30` | Ema8\|30 | `EMA8\|30` | round |
| `EMA8_5` | Ema8\|5 | `EMA8\|5` | round |
| `EMA8_60` | Ema8\|60 | `EMA8\|60` | round |
| `EMA9` | Ema9 | `EMA9` | round |
| `EMA9_1` | Ema9\|1 | `EMA9\|1` | round |
| `EMA9_120` | Ema9\|120 | `EMA9\|120` | round |
| `EMA9_15` | Ema9\|15 | `EMA9\|15` | round |
| `EMA9_1M` | Ema9\|1m | `EMA9\|1M` | round |
| `EMA9_1W` | Ema9\|1w | `EMA9\|1W` | round |
| `EMA9_240` | Ema9\|240 | `EMA9\|240` | round |
| `EMA9_30` | Ema9\|30 | `EMA9\|30` | round |
| `EMA9_5` | Ema9\|5 | `EMA9\|5` | round |
| `EMA9_60` | Ema9\|60 | `EMA9\|60` | round |
| `EXPONENTIAL_MOVING_AVERAGE_10` | Exponential Moving Average (10) | `EMA10` | computed_recommendation |
| `EXPONENTIAL_MOVING_AVERAGE_100` | Exponential Moving Average (100) | `EMA100` | computed_recommendation |
| `EXPONENTIAL_MOVING_AVERAGE_20` | Exponential Moving Average (20) | `EMA20` | computed_recommendation |
| `EXPONENTIAL_MOVING_AVERAGE_200` | Exponential Moving Average (200) | `EMA200` | computed_recommendation |
| `EXPONENTIAL_MOVING_AVERAGE_30` | Exponential Moving Average (30) | `EMA30` | computed_recommendation |
| `EXPONENTIAL_MOVING_AVERAGE_5` | Exponential Moving Average (5) | `EMA5` | computed_recommendation |
| `EXPONENTIAL_MOVING_AVERAGE_50` | Exponential Moving Average (50) | `EMA50` | computed_recommendation |
| `HULLMA20` | Hullma20 | `HullMA20` | round |
| `HULLMA200` | Hullma200 | `HullMA200` | round |
| `HULLMA200_1` | Hullma200\|1 | `HullMA200\|1` | round |
| `HULLMA200_120` | Hullma200\|120 | `HullMA200\|120` | round |
| `HULLMA200_15` | Hullma200\|15 | `HullMA200\|15` | round |
| `HULLMA200_1M` | Hullma200\|1m | `HullMA200\|1M` | round |
| `HULLMA200_1W` | Hullma200\|1w | `HullMA200\|1W` | round |
| `HULLMA200_240` | Hullma200\|240 | `HullMA200\|240` | round |
| `HULLMA200_30` | Hullma200\|30 | `HullMA200\|30` | round |
| `HULLMA200_5` | Hullma200\|5 | `HullMA200\|5` | round |
| `HULLMA200_60` | Hullma200\|60 | `HullMA200\|60` | round |
| `HULLMA20_1` | Hullma20\|1 | `HullMA20\|1` | round |
| `HULLMA20_120` | Hullma20\|120 | `HullMA20\|120` | round |
| `HULLMA20_15` | Hullma20\|15 | `HullMA20\|15` | round |
| `HULLMA20_1M` | Hullma20\|1m | `HullMA20\|1M` | round |
| `HULLMA20_1W` | Hullma20\|1w | `HullMA20\|1W` | round |
| `HULLMA20_240` | Hullma20\|240 | `HullMA20\|240` | round |
| `HULLMA20_30` | Hullma20\|30 | `HullMA20\|30` | round |
| `HULLMA20_5` | Hullma20\|5 | `HullMA20\|5` | round |
| `HULLMA20_60` | Hullma20\|60 | `HullMA20\|60` | round |
| `HULLMA9_1` | Hullma9\|1 | `HullMA9\|1` | round |
| `HULLMA9_120` | Hullma9\|120 | `HullMA9\|120` | round |
| `HULLMA9_15` | Hullma9\|15 | `HullMA9\|15` | round |
| `HULLMA9_1M` | Hullma9\|1m | `HullMA9\|1M` | round |
| `HULLMA9_1W` | Hullma9\|1w | `HullMA9\|1W` | round |
| `HULLMA9_240` | Hullma9\|240 | `HullMA9\|240` | round |
| `HULLMA9_30` | Hullma9\|30 | `HullMA9\|30` | round |
| `HULLMA9_5` | Hullma9\|5 | `HullMA9\|5` | round |
| `HULLMA9_60` | Hullma9\|60 | `HullMA9\|60` | round |
| `HULL_MOVING_AVERAGE_9` | Hull Moving Average (9) | `HullMA9` | recommendation |
| `PIVOT_DM_P` | Pivot DM P | `Pivot.M.Demark.Middle` | round |
| `PIVOT_DM_R1` | Pivot DM R1 | `Pivot.M.Demark.R1` | round |
| `PIVOT_DM_S1` | Pivot DM S1 | `Pivot.M.Demark.S1` | round |
| `PIVOT_M_DEMARK_MIDDLE_1` | Pivot M Demark Middle\|1 | `Pivot.M.Demark.Middle\|1` | round |
| `PIVOT_M_DEMARK_MIDDLE_120` | Pivot M Demark Middle\|120 | `Pivot.M.Demark.Middle\|120` | round |
| `PIVOT_M_DEMARK_MIDDLE_15` | Pivot M Demark Middle\|15 | `Pivot.M.Demark.Middle\|15` | round |
| `PIVOT_M_DEMARK_MIDDLE_1M` | Pivot M Demark Middle\|1m | `Pivot.M.Demark.Middle\|1M` | round |
| `PIVOT_M_DEMARK_MIDDLE_1W` | Pivot M Demark Middle\|1w | `Pivot.M.Demark.Middle\|1W` | round |
| `PIVOT_M_DEMARK_MIDDLE_240` | Pivot M Demark Middle\|240 | `Pivot.M.Demark.Middle\|240` | round |
| `PIVOT_M_DEMARK_MIDDLE_30` | Pivot M Demark Middle\|30 | `Pivot.M.Demark.Middle\|30` | round |
| `PIVOT_M_DEMARK_MIDDLE_5` | Pivot M Demark Middle\|5 | `Pivot.M.Demark.Middle\|5` | round |
| `PIVOT_M_DEMARK_MIDDLE_60` | Pivot M Demark Middle\|60 | `Pivot.M.Demark.Middle\|60` | round |
| `PIVOT_M_DEMARK_R1_1` | Pivot M Demark R1\|1 | `Pivot.M.Demark.R1\|1` | round |
| `PIVOT_M_DEMARK_R1_120` | Pivot M Demark R1\|120 | `Pivot.M.Demark.R1\|120` | round |
| `PIVOT_M_DEMARK_R1_15` | Pivot M Demark R1\|15 | `Pivot.M.Demark.R1\|15` | round |
| `PIVOT_M_DEMARK_R1_1M` | Pivot M Demark R1\|1m | `Pivot.M.Demark.R1\|1M` | round |
| `PIVOT_M_DEMARK_R1_1W` | Pivot M Demark R1\|1w | `Pivot.M.Demark.R1\|1W` | round |
| `PIVOT_M_DEMARK_R1_240` | Pivot M Demark R1\|240 | `Pivot.M.Demark.R1\|240` | round |
| `PIVOT_M_DEMARK_R1_30` | Pivot M Demark R1\|30 | `Pivot.M.Demark.R1\|30` | round |
| `PIVOT_M_DEMARK_R1_5` | Pivot M Demark R1\|5 | `Pivot.M.Demark.R1\|5` | round |
| `PIVOT_M_DEMARK_R1_60` | Pivot M Demark R1\|60 | `Pivot.M.Demark.R1\|60` | round |
| `PIVOT_M_DEMARK_S1_1` | Pivot M Demark S1\|1 | `Pivot.M.Demark.S1\|1` | round |
| `PIVOT_M_DEMARK_S1_120` | Pivot M Demark S1\|120 | `Pivot.M.Demark.S1\|120` | round |
| `PIVOT_M_DEMARK_S1_15` | Pivot M Demark S1\|15 | `Pivot.M.Demark.S1\|15` | round |
| `PIVOT_M_DEMARK_S1_1M` | Pivot M Demark S1\|1m | `Pivot.M.Demark.S1\|1M` | round |
| `PIVOT_M_DEMARK_S1_1W` | Pivot M Demark S1\|1w | `Pivot.M.Demark.S1\|1W` | round |
| `PIVOT_M_DEMARK_S1_240` | Pivot M Demark S1\|240 | `Pivot.M.Demark.S1\|240` | round |
| `PIVOT_M_DEMARK_S1_30` | Pivot M Demark S1\|30 | `Pivot.M.Demark.S1\|30` | round |
| `PIVOT_M_DEMARK_S1_5` | Pivot M Demark S1\|5 | `Pivot.M.Demark.S1\|5` | round |
| `PIVOT_M_DEMARK_S1_60` | Pivot M Demark S1\|60 | `Pivot.M.Demark.S1\|60` | round |
| `PREMARKET_CHANGE` | Pre-market Change | `premarket_change_abs` | currency |
| `PREMARKET_CHANGE_FROM_OPEN` | Pre-market Change from Open | `premarket_change_from_open_abs` | round |
| `PREMARKET_CHANGE_FROM_OPEN_PERCENT` | Pre-market Change from Open % | `premarket_change_from_open` | percent |
| `PREMARKET_CHANGE_PERCENT` | Pre-market Change % | `premarket_change` | percent |
| `PREMARKET_CLOSE` | Pre-market Close | `premarket_close` | currency |
| `PREMARKET_GAP_PERCENT` | Pre-market Gap % | `premarket_gap` | percent |
| `PREMARKET_HIGH` | Pre-market High | `premarket_high` | currency |
| `PREMARKET_LOW` | Pre-market Low | `premarket_low` | currency |
| `PREMARKET_OPEN` | Pre-market Open | `premarket_open` | currency |
| `PREMARKET_TIME` | Premarket Time | `premarket_time` | date |
| `PREMARKET_VOLUME` | Pre-market Volume | `premarket_volume` | number_group |
| `REC_HULLMA9` | Rec Hullma9 | `Rec.HullMA9` | round |
| `REC_HULLMA9_1` | Rec Hullma9\|1 | `Rec.HullMA9\|1` | round |
| `REC_HULLMA9_120` | Rec Hullma9\|120 | `Rec.HullMA9\|120` | round |
| `REC_HULLMA9_15` | Rec Hullma9\|15 | `Rec.HullMA9\|15` | round |
| `REC_HULLMA9_1M` | Rec Hullma9\|1m | `Rec.HullMA9\|1M` | round |
| `REC_HULLMA9_1W` | Rec Hullma9\|1w | `Rec.HullMA9\|1W` | round |
| `REC_HULLMA9_240` | Rec Hullma9\|240 | `Rec.HullMA9\|240` | round |
| `REC_HULLMA9_30` | Rec Hullma9\|30 | `Rec.HullMA9\|30` | round |
| `REC_HULLMA9_5` | Rec Hullma9\|5 | `Rec.HullMA9\|5` | round |
| `REC_HULLMA9_60` | Rec Hullma9\|60 | `Rec.HullMA9\|60` | round |
| `REC_VWMA` | Rec VWMA | `Rec.VWMA` | round |
| `REC_VWMA_1` | Rec Vwma\|1 | `Rec.VWMA\|1` | round |
| `REC_VWMA_120` | Rec Vwma\|120 | `Rec.VWMA\|120` | round |
| `REC_VWMA_15` | Rec Vwma\|15 | `Rec.VWMA\|15` | round |
| `REC_VWMA_1M` | Rec Vwma\|1m | `Rec.VWMA\|1M` | round |
| `REC_VWMA_1W` | Rec Vwma\|1w | `Rec.VWMA\|1W` | round |
| `REC_VWMA_240` | Rec Vwma\|240 | `Rec.VWMA\|240` | round |
| `REC_VWMA_30` | Rec Vwma\|30 | `Rec.VWMA\|30` | round |
| `REC_VWMA_5` | Rec Vwma\|5 | `Rec.VWMA\|5` | round |
| `REC_VWMA_60` | Rec Vwma\|60 | `Rec.VWMA\|60` | round |
| `SIMPLE_MOVING_AVERAGE_10` | Simple Moving Average (10) | `SMA10` | computed_recommendation |
| `SIMPLE_MOVING_AVERAGE_100` | Simple Moving Average (100) | `SMA100` | computed_recommendation |
| `SIMPLE_MOVING_AVERAGE_20` | Simple Moving Average (20) | `SMA20` | computed_recommendation |
| `SIMPLE_MOVING_AVERAGE_200` | Simple Moving Average (200) | `SMA200` | computed_recommendation |
| `SIMPLE_MOVING_AVERAGE_30` | Simple Moving Average (30) | `SMA30` | computed_recommendation |
| `SIMPLE_MOVING_AVERAGE_5` | Simple Moving Average (5) | `SMA5` | computed_recommendation |
| `SIMPLE_MOVING_AVERAGE_50` | Simple Moving Average (50) | `SMA50` | computed_recommendation |
| `SMA100_1` | Sma100\|1 | `SMA100\|1` | round |
| `SMA100_120` | Sma100\|120 | `SMA100\|120` | round |
| `SMA100_15` | Sma100\|15 | `SMA100\|15` | round |
| `SMA100_1M` | Sma100\|1m | `SMA100\|1M` | round |
| `SMA100_1W` | Sma100\|1w | `SMA100\|1W` | round |
| `SMA100_240` | Sma100\|240 | `SMA100\|240` | round |
| `SMA100_30` | Sma100\|30 | `SMA100\|30` | round |
| `SMA100_5` | Sma100\|5 | `SMA100\|5` | round |
| `SMA100_60` | Sma100\|60 | `SMA100\|60` | round |
| `SMA10_1` | Sma10\|1 | `SMA10\|1` | round |
| `SMA10_120` | Sma10\|120 | `SMA10\|120` | round |
| `SMA10_15` | Sma10\|15 | `SMA10\|15` | round |
| `SMA10_1M` | Sma10\|1m | `SMA10\|1M` | round |
| `SMA10_1W` | Sma10\|1w | `SMA10\|1W` | round |
| `SMA10_240` | Sma10\|240 | `SMA10\|240` | round |
| `SMA10_30` | Sma10\|30 | `SMA10\|30` | round |
| `SMA10_5` | Sma10\|5 | `SMA10\|5` | round |
| `SMA10_60` | Sma10\|60 | `SMA10\|60` | round |
| `SMA12` | Sma12 | `SMA12` | round |
| `SMA120` | Sma120 | `SMA120` | round |
| `SMA120_1` | Sma120\|1 | `SMA120\|1` | round |
| `SMA120_120` | Sma120\|120 | `SMA120\|120` | round |
| `SMA120_15` | Sma120\|15 | `SMA120\|15` | round |
| `SMA120_1M` | Sma120\|1m | `SMA120\|1M` | round |
| `SMA120_1W` | Sma120\|1w | `SMA120\|1W` | round |
| `SMA120_240` | Sma120\|240 | `SMA120\|240` | round |
| `SMA120_30` | Sma120\|30 | `SMA120\|30` | round |
| `SMA120_5` | Sma120\|5 | `SMA120\|5` | round |
| `SMA120_60` | Sma120\|60 | `SMA120\|60` | round |
| `SMA12_1` | Sma12\|1 | `SMA12\|1` | round |
| `SMA12_120` | Sma12\|120 | `SMA12\|120` | round |
| `SMA12_15` | Sma12\|15 | `SMA12\|15` | round |
| `SMA12_1M` | Sma12\|1m | `SMA12\|1M` | round |
| `SMA12_1W` | Sma12\|1w | `SMA12\|1W` | round |
| `SMA12_240` | Sma12\|240 | `SMA12\|240` | round |
| `SMA12_30` | Sma12\|30 | `SMA12\|30` | round |
| `SMA12_5` | Sma12\|5 | `SMA12\|5` | round |
| `SMA12_60` | Sma12\|60 | `SMA12\|60` | round |
| `SMA13` | Sma13 | `SMA13` | round |
| `SMA13_1` | Sma13\|1 | `SMA13\|1` | round |
| `SMA13_120` | Sma13\|120 | `SMA13\|120` | round |
| `SMA13_15` | Sma13\|15 | `SMA13\|15` | round |
| `SMA13_1M` | Sma13\|1m | `SMA13\|1M` | round |
| `SMA13_1W` | Sma13\|1w | `SMA13\|1W` | round |
| `SMA13_240` | Sma13\|240 | `SMA13\|240` | round |
| `SMA13_30` | Sma13\|30 | `SMA13\|30` | round |
| `SMA13_5` | Sma13\|5 | `SMA13\|5` | round |
| `SMA13_60` | Sma13\|60 | `SMA13\|60` | round |
| `SMA14` | Sma14 | `SMA14` | round |
| `SMA144` | Sma144 | `SMA144` | round |
| `SMA144_1` | Sma144\|1 | `SMA144\|1` | round |
| `SMA144_120` | Sma144\|120 | `SMA144\|120` | round |
| `SMA144_15` | Sma144\|15 | `SMA144\|15` | round |
| `SMA144_1M` | Sma144\|1m | `SMA144\|1M` | round |
| `SMA144_1W` | Sma144\|1w | `SMA144\|1W` | round |
| `SMA144_240` | Sma144\|240 | `SMA144\|240` | round |
| `SMA144_30` | Sma144\|30 | `SMA144\|30` | round |
| `SMA144_5` | Sma144\|5 | `SMA144\|5` | round |
| `SMA144_60` | Sma144\|60 | `SMA144\|60` | round |
| `SMA14_1` | Sma14\|1 | `SMA14\|1` | round |
| `SMA14_120` | Sma14\|120 | `SMA14\|120` | round |
| `SMA14_15` | Sma14\|15 | `SMA14\|15` | round |
| `SMA14_1M` | Sma14\|1m | `SMA14\|1M` | round |
| `SMA14_1W` | Sma14\|1w | `SMA14\|1W` | round |
| `SMA14_240` | Sma14\|240 | `SMA14\|240` | round |
| `SMA14_30` | Sma14\|30 | `SMA14\|30` | round |
| `SMA14_5` | Sma14\|5 | `SMA14\|5` | round |
| `SMA14_60` | Sma14\|60 | `SMA14\|60` | round |
| `SMA15` | Sma15 | `SMA15` | round |
| `SMA150` | Sma150 | `SMA150` | round |
| `SMA150_1` | Sma150\|1 | `SMA150\|1` | round |
| `SMA150_120` | Sma150\|120 | `SMA150\|120` | round |
| `SMA150_15` | Sma150\|15 | `SMA150\|15` | round |
| `SMA150_1M` | Sma150\|1m | `SMA150\|1M` | round |
| `SMA150_1W` | Sma150\|1w | `SMA150\|1W` | round |
| `SMA150_240` | Sma150\|240 | `SMA150\|240` | round |
| `SMA150_30` | Sma150\|30 | `SMA150\|30` | round |
| `SMA150_5` | Sma150\|5 | `SMA150\|5` | round |
| `SMA150_60` | Sma150\|60 | `SMA150\|60` | round |
| `SMA15_1` | Sma15\|1 | `SMA15\|1` | round |
| `SMA15_120` | Sma15\|120 | `SMA15\|120` | round |
| `SMA15_15` | Sma15\|15 | `SMA15\|15` | round |
| `SMA15_1M` | Sma15\|1m | `SMA15\|1M` | round |
| `SMA15_1W` | Sma15\|1w | `SMA15\|1W` | round |
| `SMA15_240` | Sma15\|240 | `SMA15\|240` | round |
| `SMA15_30` | Sma15\|30 | `SMA15\|30` | round |
| `SMA15_5` | Sma15\|5 | `SMA15\|5` | round |
| `SMA15_60` | Sma15\|60 | `SMA15\|60` | round |
| `SMA2` | Sma2 | `SMA2` | round |
| `SMA200_1` | Sma200\|1 | `SMA200\|1` | round |
| `SMA200_120` | Sma200\|120 | `SMA200\|120` | round |
| `SMA200_15` | Sma200\|15 | `SMA200\|15` | round |
| `SMA200_1M` | Sma200\|1m | `SMA200\|1M` | round |
| `SMA200_1W` | Sma200\|1w | `SMA200\|1W` | round |
| `SMA200_240` | Sma200\|240 | `SMA200\|240` | round |
| `SMA200_30` | Sma200\|30 | `SMA200\|30` | round |
| `SMA200_5` | Sma200\|5 | `SMA200\|5` | round |
| `SMA200_60` | Sma200\|60 | `SMA200\|60` | round |
| `SMA20_1` | Sma20\|1 | `SMA20\|1` | round |
| `SMA20_120` | Sma20\|120 | `SMA20\|120` | round |
| `SMA20_15` | Sma20\|15 | `SMA20\|15` | round |
| `SMA20_1M` | Sma20\|1m | `SMA20\|1M` | round |
| `SMA20_1W` | Sma20\|1w | `SMA20\|1W` | round |
| `SMA20_240` | Sma20\|240 | `SMA20\|240` | round |
| `SMA20_30` | Sma20\|30 | `SMA20\|30` | round |
| `SMA20_5` | Sma20\|5 | `SMA20\|5` | round |
| `SMA20_60` | Sma20\|60 | `SMA20\|60` | round |
| `SMA21` | Sma21 | `SMA21` | round |
| `SMA21_1` | Sma21\|1 | `SMA21\|1` | round |
| `SMA21_120` | Sma21\|120 | `SMA21\|120` | round |
| `SMA21_15` | Sma21\|15 | `SMA21\|15` | round |
| `SMA21_1M` | Sma21\|1m | `SMA21\|1M` | round |
| `SMA21_1W` | Sma21\|1w | `SMA21\|1W` | round |
| `SMA21_240` | Sma21\|240 | `SMA21\|240` | round |
| `SMA21_30` | Sma21\|30 | `SMA21\|30` | round |
| `SMA21_5` | Sma21\|5 | `SMA21\|5` | round |
| `SMA21_60` | Sma21\|60 | `SMA21\|60` | round |
| `SMA25` | Sma25 | `SMA25` | round |
| `SMA250` | Sma250 | `SMA250` | round |
| `SMA250_1` | Sma250\|1 | `SMA250\|1` | round |
| `SMA250_120` | Sma250\|120 | `SMA250\|120` | round |
| `SMA250_15` | Sma250\|15 | `SMA250\|15` | round |
| `SMA250_1M` | Sma250\|1m | `SMA250\|1M` | round |
| `SMA250_1W` | Sma250\|1w | `SMA250\|1W` | round |
| `SMA250_240` | Sma250\|240 | `SMA250\|240` | round |
| `SMA250_30` | Sma250\|30 | `SMA250\|30` | round |
| `SMA250_5` | Sma250\|5 | `SMA250\|5` | round |
| `SMA250_60` | Sma250\|60 | `SMA250\|60` | round |
| `SMA25_1` | Sma25\|1 | `SMA25\|1` | round |
| `SMA25_120` | Sma25\|120 | `SMA25\|120` | round |
| `SMA25_15` | Sma25\|15 | `SMA25\|15` | round |
| `SMA25_1M` | Sma25\|1m | `SMA25\|1M` | round |
| `SMA25_1W` | Sma25\|1w | `SMA25\|1W` | round |
| `SMA25_240` | Sma25\|240 | `SMA25\|240` | round |
| `SMA25_30` | Sma25\|30 | `SMA25\|30` | round |
| `SMA25_5` | Sma25\|5 | `SMA25\|5` | round |
| `SMA25_60` | Sma25\|60 | `SMA25\|60` | round |
| `SMA26` | Sma26 | `SMA26` | round |
| `SMA26_1` | Sma26\|1 | `SMA26\|1` | round |
| `SMA26_120` | Sma26\|120 | `SMA26\|120` | round |
| `SMA26_15` | Sma26\|15 | `SMA26\|15` | round |
| `SMA26_1M` | Sma26\|1m | `SMA26\|1M` | round |
| `SMA26_1W` | Sma26\|1w | `SMA26\|1W` | round |
| `SMA26_240` | Sma26\|240 | `SMA26\|240` | round |
| `SMA26_30` | Sma26\|30 | `SMA26\|30` | round |
| `SMA26_5` | Sma26\|5 | `SMA26\|5` | round |
| `SMA26_60` | Sma26\|60 | `SMA26\|60` | round |
| `SMA2_1` | Sma2\|1 | `SMA2\|1` | round |
| `SMA2_120` | Sma2\|120 | `SMA2\|120` | round |
| `SMA2_15` | Sma2\|15 | `SMA2\|15` | round |
| `SMA2_1M` | Sma2\|1m | `SMA2\|1M` | round |
| `SMA2_1W` | Sma2\|1w | `SMA2\|1W` | round |
| `SMA2_240` | Sma2\|240 | `SMA2\|240` | round |
| `SMA2_30` | Sma2\|30 | `SMA2\|30` | round |
| `SMA2_5` | Sma2\|5 | `SMA2\|5` | round |
| `SMA2_60` | Sma2\|60 | `SMA2\|60` | round |
| `SMA3` | Sma3 | `SMA3` | round |
| `SMA300` | Sma300 | `SMA300` | round |
| `SMA300_1` | Sma300\|1 | `SMA300\|1` | round |
| `SMA300_120` | Sma300\|120 | `SMA300\|120` | round |
| `SMA300_15` | Sma300\|15 | `SMA300\|15` | round |
| `SMA300_1M` | Sma300\|1m | `SMA300\|1M` | round |
| `SMA300_1W` | Sma300\|1w | `SMA300\|1W` | round |
| `SMA300_240` | Sma300\|240 | `SMA300\|240` | round |
| `SMA300_30` | Sma300\|30 | `SMA300\|30` | round |
| `SMA300_5` | Sma300\|5 | `SMA300\|5` | round |
| `SMA300_60` | Sma300\|60 | `SMA300\|60` | round |
| `SMA30_1` | Sma30\|1 | `SMA30\|1` | round |
| `SMA30_120` | Sma30\|120 | `SMA30\|120` | round |
| `SMA30_15` | Sma30\|15 | `SMA30\|15` | round |
| `SMA30_1M` | Sma30\|1m | `SMA30\|1M` | round |
| `SMA30_1W` | Sma30\|1w | `SMA30\|1W` | round |
| `SMA30_240` | Sma30\|240 | `SMA30\|240` | round |
| `SMA30_30` | Sma30\|30 | `SMA30\|30` | round |
| `SMA30_5` | Sma30\|5 | `SMA30\|5` | round |
| `SMA30_60` | Sma30\|60 | `SMA30\|60` | round |
| `SMA34` | Sma34 | `SMA34` | round |
| `SMA34_1` | Sma34\|1 | `SMA34\|1` | round |
| `SMA34_120` | Sma34\|120 | `SMA34\|120` | round |
| `SMA34_15` | Sma34\|15 | `SMA34\|15` | round |
| `SMA34_1M` | Sma34\|1m | `SMA34\|1M` | round |
| `SMA34_1W` | Sma34\|1w | `SMA34\|1W` | round |
| `SMA34_240` | Sma34\|240 | `SMA34\|240` | round |
| `SMA34_30` | Sma34\|30 | `SMA34\|30` | round |
| `SMA34_5` | Sma34\|5 | `SMA34\|5` | round |
| `SMA34_60` | Sma34\|60 | `SMA34\|60` | round |
| `SMA3_1` | Sma3\|1 | `SMA3\|1` | round |
| `SMA3_120` | Sma3\|120 | `SMA3\|120` | round |
| `SMA3_15` | Sma3\|15 | `SMA3\|15` | round |
| `SMA3_1M` | Sma3\|1m | `SMA3\|1M` | round |
| `SMA3_1W` | Sma3\|1w | `SMA3\|1W` | round |
| `SMA3_240` | Sma3\|240 | `SMA3\|240` | round |
| `SMA3_30` | Sma3\|30 | `SMA3\|30` | round |
| `SMA3_5` | Sma3\|5 | `SMA3\|5` | round |
| `SMA3_60` | Sma3\|60 | `SMA3\|60` | round |
| `SMA40` | Sma40 | `SMA40` | round |
| `SMA40_1` | Sma40\|1 | `SMA40\|1` | round |
| `SMA40_120` | Sma40\|120 | `SMA40\|120` | round |
| `SMA40_15` | Sma40\|15 | `SMA40\|15` | round |
| `SMA40_1M` | Sma40\|1m | `SMA40\|1M` | round |
| `SMA40_1W` | Sma40\|1w | `SMA40\|1W` | round |
| `SMA40_240` | Sma40\|240 | `SMA40\|240` | round |
| `SMA40_30` | Sma40\|30 | `SMA40\|30` | round |
| `SMA40_5` | Sma40\|5 | `SMA40\|5` | round |
| `SMA40_60` | Sma40\|60 | `SMA40\|60` | round |
| `SMA50_1` | Sma50\|1 | `SMA50\|1` | round |
| `SMA50_120` | Sma50\|120 | `SMA50\|120` | round |
| `SMA50_15` | Sma50\|15 | `SMA50\|15` | round |
| `SMA50_1M` | Sma50\|1m | `SMA50\|1M` | round |
| `SMA50_1W` | Sma50\|1w | `SMA50\|1W` | round |
| `SMA50_240` | Sma50\|240 | `SMA50\|240` | round |
| `SMA50_30` | Sma50\|30 | `SMA50\|30` | round |
| `SMA50_5` | Sma50\|5 | `SMA50\|5` | round |
| `SMA50_60` | Sma50\|60 | `SMA50\|60` | round |
| `SMA55` | Sma55 | `SMA55` | round |
| `SMA55_1` | Sma55\|1 | `SMA55\|1` | round |
| `SMA55_120` | Sma55\|120 | `SMA55\|120` | round |
| `SMA55_15` | Sma55\|15 | `SMA55\|15` | round |
| `SMA55_1M` | Sma55\|1m | `SMA55\|1M` | round |
| `SMA55_1W` | Sma55\|1w | `SMA55\|1W` | round |
| `SMA55_240` | Sma55\|240 | `SMA55\|240` | round |
| `SMA55_30` | Sma55\|30 | `SMA55\|30` | round |
| `SMA55_5` | Sma55\|5 | `SMA55\|5` | round |
| `SMA55_60` | Sma55\|60 | `SMA55\|60` | round |
| `SMA5_1` | Sma5\|1 | `SMA5\|1` | round |
| `SMA5_120` | Sma5\|120 | `SMA5\|120` | round |
| `SMA5_15` | Sma5\|15 | `SMA5\|15` | round |
| `SMA5_1M` | Sma5\|1m | `SMA5\|1M` | round |
| `SMA5_1W` | Sma5\|1w | `SMA5\|1W` | round |
| `SMA5_240` | Sma5\|240 | `SMA5\|240` | round |
| `SMA5_30` | Sma5\|30 | `SMA5\|30` | round |
| `SMA5_5` | Sma5\|5 | `SMA5\|5` | round |
| `SMA5_60` | Sma5\|60 | `SMA5\|60` | round |
| `SMA6` | Sma6 | `SMA6` | round |
| `SMA60` | Sma60 | `SMA60` | round |
| `SMA60_1` | Sma60\|1 | `SMA60\|1` | round |
| `SMA60_120` | Sma60\|120 | `SMA60\|120` | round |
| `SMA60_15` | Sma60\|15 | `SMA60\|15` | round |
| `SMA60_1M` | Sma60\|1m | `SMA60\|1M` | round |
| `SMA60_1W` | Sma60\|1w | `SMA60\|1W` | round |
| `SMA60_240` | Sma60\|240 | `SMA60\|240` | round |
| `SMA60_30` | Sma60\|30 | `SMA60\|30` | round |
| `SMA60_5` | Sma60\|5 | `SMA60\|5` | round |
| `SMA60_60` | Sma60\|60 | `SMA60\|60` | round |
| `SMA6_1` | Sma6\|1 | `SMA6\|1` | round |
| `SMA6_120` | Sma6\|120 | `SMA6\|120` | round |
| `SMA6_15` | Sma6\|15 | `SMA6\|15` | round |
| `SMA6_1M` | Sma6\|1m | `SMA6\|1M` | round |
| `SMA6_1W` | Sma6\|1w | `SMA6\|1W` | round |
| `SMA6_240` | Sma6\|240 | `SMA6\|240` | round |
| `SMA6_30` | Sma6\|30 | `SMA6\|30` | round |
| `SMA6_5` | Sma6\|5 | `SMA6\|5` | round |
| `SMA6_60` | Sma6\|60 | `SMA6\|60` | round |
| `SMA7` | Sma7 | `SMA7` | round |
| `SMA75` | Sma75 | `SMA75` | round |
| `SMA75_1` | Sma75\|1 | `SMA75\|1` | round |
| `SMA75_120` | Sma75\|120 | `SMA75\|120` | round |
| `SMA75_15` | Sma75\|15 | `SMA75\|15` | round |
| `SMA75_1M` | Sma75\|1m | `SMA75\|1M` | round |
| `SMA75_1W` | Sma75\|1w | `SMA75\|1W` | round |
| `SMA75_240` | Sma75\|240 | `SMA75\|240` | round |
| `SMA75_30` | Sma75\|30 | `SMA75\|30` | round |
| `SMA75_5` | Sma75\|5 | `SMA75\|5` | round |
| `SMA75_60` | Sma75\|60 | `SMA75\|60` | round |
| `SMA7_1` | Sma7\|1 | `SMA7\|1` | round |
| `SMA7_120` | Sma7\|120 | `SMA7\|120` | round |
| `SMA7_15` | Sma7\|15 | `SMA7\|15` | round |
| `SMA7_1M` | Sma7\|1m | `SMA7\|1M` | round |
| `SMA7_1W` | Sma7\|1w | `SMA7\|1W` | round |
| `SMA7_240` | Sma7\|240 | `SMA7\|240` | round |
| `SMA7_30` | Sma7\|30 | `SMA7\|30` | round |
| `SMA7_5` | Sma7\|5 | `SMA7\|5` | round |
| `SMA7_60` | Sma7\|60 | `SMA7\|60` | round |
| `SMA8` | Sma8 | `SMA8` | round |
| `SMA89` | Sma89 | `SMA89` | round |
| `SMA89_1` | Sma89\|1 | `SMA89\|1` | round |
| `SMA89_120` | Sma89\|120 | `SMA89\|120` | round |
| `SMA89_15` | Sma89\|15 | `SMA89\|15` | round |
| `SMA89_1M` | Sma89\|1m | `SMA89\|1M` | round |
| `SMA89_1W` | Sma89\|1w | `SMA89\|1W` | round |
| `SMA89_240` | Sma89\|240 | `SMA89\|240` | round |
| `SMA89_30` | Sma89\|30 | `SMA89\|30` | round |
| `SMA89_5` | Sma89\|5 | `SMA89\|5` | round |
| `SMA89_60` | Sma89\|60 | `SMA89\|60` | round |
| `SMA8_1` | Sma8\|1 | `SMA8\|1` | round |
| `SMA8_120` | Sma8\|120 | `SMA8\|120` | round |
| `SMA8_15` | Sma8\|15 | `SMA8\|15` | round |
| `SMA8_1M` | Sma8\|1m | `SMA8\|1M` | round |
| `SMA8_1W` | Sma8\|1w | `SMA8\|1W` | round |
| `SMA8_240` | Sma8\|240 | `SMA8\|240` | round |
| `SMA8_30` | Sma8\|30 | `SMA8\|30` | round |
| `SMA8_5` | Sma8\|5 | `SMA8\|5` | round |
| `SMA8_60` | Sma8\|60 | `SMA8\|60` | round |
| `SMA9` | Sma9 | `SMA9` | round |
| `SMA9_1` | Sma9\|1 | `SMA9\|1` | round |
| `SMA9_120` | Sma9\|120 | `SMA9\|120` | round |
| `SMA9_15` | Sma9\|15 | `SMA9\|15` | round |
| `SMA9_1M` | Sma9\|1m | `SMA9\|1M` | round |
| `SMA9_1W` | Sma9\|1w | `SMA9\|1W` | round |
| `SMA9_240` | Sma9\|240 | `SMA9\|240` | round |
| `SMA9_30` | Sma9\|30 | `SMA9\|30` | round |
| `SMA9_5` | Sma9\|5 | `SMA9\|5` | round |
| `SMA9_60` | Sma9\|60 | `SMA9\|60` | round |
| `VOLUME_WEIGHTED_MOVING_AVERAGE_20` | Volume Weighted Moving Average (20) | `VWMA` | recommendation |
| `VWMA_1` | Vwma\|1 | `VWMA\|1` | round |
| `VWMA_120` | Vwma\|120 | `VWMA\|120` | round |
| `VWMA_15` | Vwma\|15 | `VWMA\|15` | round |
| `VWMA_1M` | Vwma\|1m | `VWMA\|1M` | round |
| `VWMA_1W` | Vwma\|1w | `VWMA\|1W` | round |
| `VWMA_240` | Vwma\|240 | `VWMA\|240` | round |
| `VWMA_30` | Vwma\|30 | `VWMA\|30` | round |
| `VWMA_5` | Vwma\|5 | `VWMA\|5` | round |
| `VWMA_60` | Vwma\|60 | `VWMA\|60` | round |

## Oscillators

*672 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `AO_1` | Ao[1] | `AO[1]` | round |
| `AO_120` | Ao\|120 | `AO\|120` | round |
| `AO_15` | Ao\|15 | `AO\|15` | round |
| `AO_1M` | Ao\|1m | `AO\|1M` | round |
| `AO_1W` | Ao\|1w | `AO\|1W` | round |
| `AO_1_1` | Ao[1]\|1 | `AO[1]\|1` | round |
| `AO_1_120` | Ao[1]\|120 | `AO[1]\|120` | round |
| `AO_1_15` | Ao[1]\|15 | `AO[1]\|15` | round |
| `AO_1_1M` | Ao[1]\|1m | `AO[1]\|1M` | round |
| `AO_1_1W` | Ao[1]\|1w | `AO[1]\|1W` | round |
| `AO_1_2` | Ao\|1 | `AO\|1` | round |
| `AO_1_240` | Ao[1]\|240 | `AO[1]\|240` | round |
| `AO_1_30` | Ao[1]\|30 | `AO[1]\|30` | round |
| `AO_1_5` | Ao[1]\|5 | `AO[1]\|5` | round |
| `AO_1_60` | Ao[1]\|60 | `AO[1]\|60` | round |
| `AO_2` | Ao[2] | `AO[2]` | round |
| `AO_240` | Ao\|240 | `AO\|240` | round |
| `AO_2_1` | Ao[2]\|1 | `AO[2]\|1` | round |
| `AO_2_120` | Ao[2]\|120 | `AO[2]\|120` | round |
| `AO_2_15` | Ao[2]\|15 | `AO[2]\|15` | round |
| `AO_2_1M` | Ao[2]\|1m | `AO[2]\|1M` | round |
| `AO_2_1W` | Ao[2]\|1w | `AO[2]\|1W` | round |
| `AO_2_240` | Ao[2]\|240 | `AO[2]\|240` | round |
| `AO_2_30` | Ao[2]\|30 | `AO[2]\|30` | round |
| `AO_2_5` | Ao[2]\|5 | `AO[2]\|5` | round |
| `AO_2_60` | Ao[2]\|60 | `AO[2]\|60` | round |
| `AO_30` | Ao\|30 | `AO\|30` | round |
| `AO_5` | Ao\|5 | `AO\|5` | round |
| `AO_60` | Ao\|60 | `AO\|60` | round |
| `AWESOME_OSCILLATOR` | Awesome Oscillator | `AO` | computed_recommendation |
| `BBPOWER_1` | Bbpower\|1 | `BBPower\|1` | round |
| `BBPOWER_120` | Bbpower\|120 | `BBPower\|120` | round |
| `BBPOWER_15` | Bbpower\|15 | `BBPower\|15` | round |
| `BBPOWER_1M` | Bbpower\|1m | `BBPower\|1M` | round |
| `BBPOWER_1W` | Bbpower\|1w | `BBPower\|1W` | round |
| `BBPOWER_240` | Bbpower\|240 | `BBPower\|240` | round |
| `BBPOWER_30` | Bbpower\|30 | `BBPower\|30` | round |
| `BBPOWER_5` | Bbpower\|5 | `BBPower\|5` | round |
| `BBPOWER_60` | Bbpower\|60 | `BBPower\|60` | round |
| `BULL_BEAR_POWER` | Bull Bear Power | `BBPower` | recommendation |
| `CCI20_1` | Cci20[1] | `CCI20[1]` | round |
| `CCI20_120` | Cci20\|120 | `CCI20\|120` | round |
| `CCI20_15` | Cci20\|15 | `CCI20\|15` | round |
| `CCI20_1M` | Cci20\|1m | `CCI20\|1M` | round |
| `CCI20_1W` | Cci20\|1w | `CCI20\|1W` | round |
| `CCI20_1_1` | Cci20[1]\|1 | `CCI20[1]\|1` | round |
| `CCI20_1_120` | Cci20[1]\|120 | `CCI20[1]\|120` | round |
| `CCI20_1_15` | Cci20[1]\|15 | `CCI20[1]\|15` | round |
| `CCI20_1_1M` | Cci20[1]\|1m | `CCI20[1]\|1M` | round |
| `CCI20_1_1W` | Cci20[1]\|1w | `CCI20[1]\|1W` | round |
| `CCI20_1_2` | Cci20\|1 | `CCI20\|1` | round |
| `CCI20_1_240` | Cci20[1]\|240 | `CCI20[1]\|240` | round |
| `CCI20_1_30` | Cci20[1]\|30 | `CCI20[1]\|30` | round |
| `CCI20_1_5` | Cci20[1]\|5 | `CCI20[1]\|5` | round |
| `CCI20_1_60` | Cci20[1]\|60 | `CCI20[1]\|60` | round |
| `CCI20_240` | Cci20\|240 | `CCI20\|240` | round |
| `CCI20_30` | Cci20\|30 | `CCI20\|30` | round |
| `CCI20_5` | Cci20\|5 | `CCI20\|5` | round |
| `CCI20_60` | Cci20\|60 | `CCI20\|60` | round |
| `COMMODITY_CHANNEL_INDEX_20` | Commodity Channel Index (20) | `CCI20` | computed_recommendation |
| `CONTINUOUS_DIVIDEND_GROWTH` | Continuous Dividend Growth | `continuous_dividend_growth` | round |
| `CONTINUOUS_DIVIDEND_PAYOUT` | Continuous Dividend Payout | `continuous_dividend_payout` | round |
| `MOMENTUM_10` | Momentum (10) | `Mom` | computed_recommendation |
| `MOM_1` | Mom\|1 | `Mom\|1` | round |
| `MOM_120` | Mom\|120 | `Mom\|120` | round |
| `MOM_14` | Mom 14 | `Mom_14` | round |
| `MOM_14_1` | Mom 14[1] | `Mom_14[1]` | round |
| `MOM_14_120` | Mom 14\|120 | `Mom_14\|120` | round |
| `MOM_14_15` | Mom 14\|15 | `Mom_14\|15` | round |
| `MOM_14_1M` | Mom 14\|1m | `Mom_14\|1M` | round |
| `MOM_14_1W` | Mom 14\|1w | `Mom_14\|1W` | round |
| `MOM_14_1_1` | Mom 14[1]\|1 | `Mom_14[1]\|1` | round |
| `MOM_14_1_120` | Mom 14[1]\|120 | `Mom_14[1]\|120` | round |
| `MOM_14_1_15` | Mom 14[1]\|15 | `Mom_14[1]\|15` | round |
| `MOM_14_1_1M` | Mom 14[1]\|1m | `Mom_14[1]\|1M` | round |
| `MOM_14_1_1W` | Mom 14[1]\|1w | `Mom_14[1]\|1W` | round |
| `MOM_14_1_2` | Mom 14\|1 | `Mom_14\|1` | round |
| `MOM_14_1_240` | Mom 14[1]\|240 | `Mom_14[1]\|240` | round |
| `MOM_14_1_30` | Mom 14[1]\|30 | `Mom_14[1]\|30` | round |
| `MOM_14_1_5` | Mom 14[1]\|5 | `Mom_14[1]\|5` | round |
| `MOM_14_1_60` | Mom 14[1]\|60 | `Mom_14[1]\|60` | round |
| `MOM_14_240` | Mom 14\|240 | `Mom_14\|240` | round |
| `MOM_14_30` | Mom 14\|30 | `Mom_14\|30` | round |
| `MOM_14_5` | Mom 14\|5 | `Mom_14\|5` | round |
| `MOM_14_60` | Mom 14\|60 | `Mom_14\|60` | round |
| `MOM_15` | Mom\|15 | `Mom\|15` | round |
| `MOM_1M` | Mom\|1m | `Mom\|1M` | round |
| `MOM_1W` | Mom\|1w | `Mom\|1W` | round |
| `MOM_1_1` | Mom[1]\|1 | `Mom[1]\|1` | round |
| `MOM_1_120` | Mom[1]\|120 | `Mom[1]\|120` | round |
| `MOM_1_15` | Mom[1]\|15 | `Mom[1]\|15` | round |
| `MOM_1_1M` | Mom[1]\|1m | `Mom[1]\|1M` | round |
| `MOM_1_1W` | Mom[1]\|1w | `Mom[1]\|1W` | round |
| `MOM_1_2` | Mom[1] | `Mom[1]` | round |
| `MOM_1_240` | Mom[1]\|240 | `Mom[1]\|240` | round |
| `MOM_1_30` | Mom[1]\|30 | `Mom[1]\|30` | round |
| `MOM_1_5` | Mom[1]\|5 | `Mom[1]\|5` | round |
| `MOM_1_60` | Mom[1]\|60 | `Mom[1]\|60` | round |
| `MOM_240` | Mom\|240 | `Mom\|240` | round |
| `MOM_30` | Mom\|30 | `Mom\|30` | round |
| `MOM_5` | Mom\|5 | `Mom\|5` | round |
| `MOM_60` | Mom\|60 | `Mom\|60` | round |
| `PIVOT_FIBONACCI_P` | Pivot Fibonacci P | `Pivot.M.Fibonacci.Middle` | round |
| `PIVOT_FIBONACCI_R1` | Pivot Fibonacci R1 | `Pivot.M.Fibonacci.R1` | round |
| `PIVOT_FIBONACCI_R2` | Pivot Fibonacci R2 | `Pivot.M.Fibonacci.R2` | round |
| `PIVOT_FIBONACCI_R3` | Pivot Fibonacci R3 | `Pivot.M.Fibonacci.R3` | round |
| `PIVOT_FIBONACCI_S1` | Pivot Fibonacci S1 | `Pivot.M.Fibonacci.S1` | round |
| `PIVOT_FIBONACCI_S2` | Pivot Fibonacci S2 | `Pivot.M.Fibonacci.S2` | round |
| `PIVOT_FIBONACCI_S3` | Pivot Fibonacci S3 | `Pivot.M.Fibonacci.S3` | round |
| `PIVOT_M_FIBONACCI_MIDDLE_1` | Pivot M Fibonacci Middle\|1 | `Pivot.M.Fibonacci.Middle\|1` | round |
| `PIVOT_M_FIBONACCI_MIDDLE_120` | Pivot M Fibonacci Middle\|120 | `Pivot.M.Fibonacci.Middle\|120` | round |
| `PIVOT_M_FIBONACCI_MIDDLE_15` | Pivot M Fibonacci Middle\|15 | `Pivot.M.Fibonacci.Middle\|15` | round |
| `PIVOT_M_FIBONACCI_MIDDLE_1M` | Pivot M Fibonacci Middle\|1m | `Pivot.M.Fibonacci.Middle\|1M` | round |
| `PIVOT_M_FIBONACCI_MIDDLE_1W` | Pivot M Fibonacci Middle\|1w | `Pivot.M.Fibonacci.Middle\|1W` | round |
| `PIVOT_M_FIBONACCI_MIDDLE_240` | Pivot M Fibonacci Middle\|240 | `Pivot.M.Fibonacci.Middle\|240` | round |
| `PIVOT_M_FIBONACCI_MIDDLE_30` | Pivot M Fibonacci Middle\|30 | `Pivot.M.Fibonacci.Middle\|30` | round |
| `PIVOT_M_FIBONACCI_MIDDLE_5` | Pivot M Fibonacci Middle\|5 | `Pivot.M.Fibonacci.Middle\|5` | round |
| `PIVOT_M_FIBONACCI_MIDDLE_60` | Pivot M Fibonacci Middle\|60 | `Pivot.M.Fibonacci.Middle\|60` | round |
| `PIVOT_M_FIBONACCI_R1_1` | Pivot M Fibonacci R1\|1 | `Pivot.M.Fibonacci.R1\|1` | round |
| `PIVOT_M_FIBONACCI_R1_120` | Pivot M Fibonacci R1\|120 | `Pivot.M.Fibonacci.R1\|120` | round |
| `PIVOT_M_FIBONACCI_R1_15` | Pivot M Fibonacci R1\|15 | `Pivot.M.Fibonacci.R1\|15` | round |
| `PIVOT_M_FIBONACCI_R1_1M` | Pivot M Fibonacci R1\|1m | `Pivot.M.Fibonacci.R1\|1M` | round |
| `PIVOT_M_FIBONACCI_R1_1W` | Pivot M Fibonacci R1\|1w | `Pivot.M.Fibonacci.R1\|1W` | round |
| `PIVOT_M_FIBONACCI_R1_240` | Pivot M Fibonacci R1\|240 | `Pivot.M.Fibonacci.R1\|240` | round |
| `PIVOT_M_FIBONACCI_R1_30` | Pivot M Fibonacci R1\|30 | `Pivot.M.Fibonacci.R1\|30` | round |
| `PIVOT_M_FIBONACCI_R1_5` | Pivot M Fibonacci R1\|5 | `Pivot.M.Fibonacci.R1\|5` | round |
| `PIVOT_M_FIBONACCI_R1_60` | Pivot M Fibonacci R1\|60 | `Pivot.M.Fibonacci.R1\|60` | round |
| `PIVOT_M_FIBONACCI_R2_1` | Pivot M Fibonacci R2\|1 | `Pivot.M.Fibonacci.R2\|1` | round |
| `PIVOT_M_FIBONACCI_R2_120` | Pivot M Fibonacci R2\|120 | `Pivot.M.Fibonacci.R2\|120` | round |
| `PIVOT_M_FIBONACCI_R2_15` | Pivot M Fibonacci R2\|15 | `Pivot.M.Fibonacci.R2\|15` | round |
| `PIVOT_M_FIBONACCI_R2_1M` | Pivot M Fibonacci R2\|1m | `Pivot.M.Fibonacci.R2\|1M` | round |
| `PIVOT_M_FIBONACCI_R2_1W` | Pivot M Fibonacci R2\|1w | `Pivot.M.Fibonacci.R2\|1W` | round |
| `PIVOT_M_FIBONACCI_R2_240` | Pivot M Fibonacci R2\|240 | `Pivot.M.Fibonacci.R2\|240` | round |
| `PIVOT_M_FIBONACCI_R2_30` | Pivot M Fibonacci R2\|30 | `Pivot.M.Fibonacci.R2\|30` | round |
| `PIVOT_M_FIBONACCI_R2_5` | Pivot M Fibonacci R2\|5 | `Pivot.M.Fibonacci.R2\|5` | round |
| `PIVOT_M_FIBONACCI_R2_60` | Pivot M Fibonacci R2\|60 | `Pivot.M.Fibonacci.R2\|60` | round |
| `PIVOT_M_FIBONACCI_R3_1` | Pivot M Fibonacci R3\|1 | `Pivot.M.Fibonacci.R3\|1` | round |
| `PIVOT_M_FIBONACCI_R3_120` | Pivot M Fibonacci R3\|120 | `Pivot.M.Fibonacci.R3\|120` | round |
| `PIVOT_M_FIBONACCI_R3_15` | Pivot M Fibonacci R3\|15 | `Pivot.M.Fibonacci.R3\|15` | round |
| `PIVOT_M_FIBONACCI_R3_1M` | Pivot M Fibonacci R3\|1m | `Pivot.M.Fibonacci.R3\|1M` | round |
| `PIVOT_M_FIBONACCI_R3_1W` | Pivot M Fibonacci R3\|1w | `Pivot.M.Fibonacci.R3\|1W` | round |
| `PIVOT_M_FIBONACCI_R3_240` | Pivot M Fibonacci R3\|240 | `Pivot.M.Fibonacci.R3\|240` | round |
| `PIVOT_M_FIBONACCI_R3_30` | Pivot M Fibonacci R3\|30 | `Pivot.M.Fibonacci.R3\|30` | round |
| `PIVOT_M_FIBONACCI_R3_5` | Pivot M Fibonacci R3\|5 | `Pivot.M.Fibonacci.R3\|5` | round |
| `PIVOT_M_FIBONACCI_R3_60` | Pivot M Fibonacci R3\|60 | `Pivot.M.Fibonacci.R3\|60` | round |
| `PIVOT_M_FIBONACCI_S1_1` | Pivot M Fibonacci S1\|1 | `Pivot.M.Fibonacci.S1\|1` | round |
| `PIVOT_M_FIBONACCI_S1_120` | Pivot M Fibonacci S1\|120 | `Pivot.M.Fibonacci.S1\|120` | round |
| `PIVOT_M_FIBONACCI_S1_15` | Pivot M Fibonacci S1\|15 | `Pivot.M.Fibonacci.S1\|15` | round |
| `PIVOT_M_FIBONACCI_S1_1M` | Pivot M Fibonacci S1\|1m | `Pivot.M.Fibonacci.S1\|1M` | round |
| `PIVOT_M_FIBONACCI_S1_1W` | Pivot M Fibonacci S1\|1w | `Pivot.M.Fibonacci.S1\|1W` | round |
| `PIVOT_M_FIBONACCI_S1_240` | Pivot M Fibonacci S1\|240 | `Pivot.M.Fibonacci.S1\|240` | round |
| `PIVOT_M_FIBONACCI_S1_30` | Pivot M Fibonacci S1\|30 | `Pivot.M.Fibonacci.S1\|30` | round |
| `PIVOT_M_FIBONACCI_S1_5` | Pivot M Fibonacci S1\|5 | `Pivot.M.Fibonacci.S1\|5` | round |
| `PIVOT_M_FIBONACCI_S1_60` | Pivot M Fibonacci S1\|60 | `Pivot.M.Fibonacci.S1\|60` | round |
| `PIVOT_M_FIBONACCI_S2_1` | Pivot M Fibonacci S2\|1 | `Pivot.M.Fibonacci.S2\|1` | round |
| `PIVOT_M_FIBONACCI_S2_120` | Pivot M Fibonacci S2\|120 | `Pivot.M.Fibonacci.S2\|120` | round |
| `PIVOT_M_FIBONACCI_S2_15` | Pivot M Fibonacci S2\|15 | `Pivot.M.Fibonacci.S2\|15` | round |
| `PIVOT_M_FIBONACCI_S2_1M` | Pivot M Fibonacci S2\|1m | `Pivot.M.Fibonacci.S2\|1M` | round |
| `PIVOT_M_FIBONACCI_S2_1W` | Pivot M Fibonacci S2\|1w | `Pivot.M.Fibonacci.S2\|1W` | round |
| `PIVOT_M_FIBONACCI_S2_240` | Pivot M Fibonacci S2\|240 | `Pivot.M.Fibonacci.S2\|240` | round |
| `PIVOT_M_FIBONACCI_S2_30` | Pivot M Fibonacci S2\|30 | `Pivot.M.Fibonacci.S2\|30` | round |
| `PIVOT_M_FIBONACCI_S2_5` | Pivot M Fibonacci S2\|5 | `Pivot.M.Fibonacci.S2\|5` | round |
| `PIVOT_M_FIBONACCI_S2_60` | Pivot M Fibonacci S2\|60 | `Pivot.M.Fibonacci.S2\|60` | round |
| `PIVOT_M_FIBONACCI_S3_1` | Pivot M Fibonacci S3\|1 | `Pivot.M.Fibonacci.S3\|1` | round |
| `PIVOT_M_FIBONACCI_S3_120` | Pivot M Fibonacci S3\|120 | `Pivot.M.Fibonacci.S3\|120` | round |
| `PIVOT_M_FIBONACCI_S3_15` | Pivot M Fibonacci S3\|15 | `Pivot.M.Fibonacci.S3\|15` | round |
| `PIVOT_M_FIBONACCI_S3_1M` | Pivot M Fibonacci S3\|1m | `Pivot.M.Fibonacci.S3\|1M` | round |
| `PIVOT_M_FIBONACCI_S3_1W` | Pivot M Fibonacci S3\|1w | `Pivot.M.Fibonacci.S3\|1W` | round |
| `PIVOT_M_FIBONACCI_S3_240` | Pivot M Fibonacci S3\|240 | `Pivot.M.Fibonacci.S3\|240` | round |
| `PIVOT_M_FIBONACCI_S3_30` | Pivot M Fibonacci S3\|30 | `Pivot.M.Fibonacci.S3\|30` | round |
| `PIVOT_M_FIBONACCI_S3_5` | Pivot M Fibonacci S3\|5 | `Pivot.M.Fibonacci.S3\|5` | round |
| `PIVOT_M_FIBONACCI_S3_60` | Pivot M Fibonacci S3\|60 | `Pivot.M.Fibonacci.S3\|60` | round |
| `RATE_OF_CHANGE_9` | Rate Of Change (9) | `ROC` | round |
| `REC_BBPOWER` | Rec Bbpower | `Rec.BBPower` | round |
| `REC_BBPOWER_1` | Rec Bbpower\|1 | `Rec.BBPower\|1` | round |
| `REC_BBPOWER_120` | Rec Bbpower\|120 | `Rec.BBPower\|120` | round |
| `REC_BBPOWER_15` | Rec Bbpower\|15 | `Rec.BBPower\|15` | round |
| `REC_BBPOWER_1M` | Rec Bbpower\|1m | `Rec.BBPower\|1M` | round |
| `REC_BBPOWER_1W` | Rec Bbpower\|1w | `Rec.BBPower\|1W` | round |
| `REC_BBPOWER_240` | Rec Bbpower\|240 | `Rec.BBPower\|240` | round |
| `REC_BBPOWER_30` | Rec Bbpower\|30 | `Rec.BBPower\|30` | round |
| `REC_BBPOWER_5` | Rec Bbpower\|5 | `Rec.BBPower\|5` | round |
| `REC_BBPOWER_60` | Rec Bbpower\|60 | `Rec.BBPower\|60` | round |
| `REC_STOCH_RSI` | Rec Stoch RSI | `Rec.Stoch.RSI` | round |
| `REC_STOCH_RSI_1` | Rec Stoch Rsi\|1 | `Rec.Stoch.RSI\|1` | round |
| `REC_STOCH_RSI_120` | Rec Stoch Rsi\|120 | `Rec.Stoch.RSI\|120` | round |
| `REC_STOCH_RSI_15` | Rec Stoch Rsi\|15 | `Rec.Stoch.RSI\|15` | round |
| `REC_STOCH_RSI_1M` | Rec Stoch Rsi\|1m | `Rec.Stoch.RSI\|1M` | round |
| `REC_STOCH_RSI_1W` | Rec Stoch Rsi\|1w | `Rec.Stoch.RSI\|1W` | round |
| `REC_STOCH_RSI_240` | Rec Stoch Rsi\|240 | `Rec.Stoch.RSI\|240` | round |
| `REC_STOCH_RSI_30` | Rec Stoch Rsi\|30 | `Rec.Stoch.RSI\|30` | round |
| `REC_STOCH_RSI_5` | Rec Stoch Rsi\|5 | `Rec.Stoch.RSI\|5` | round |
| `REC_STOCH_RSI_60` | Rec Stoch Rsi\|60 | `Rec.Stoch.RSI\|60` | round |
| `REC_UO` | Rec UO | `Rec.UO` | round |
| `REC_UO_1` | Rec Uo\|1 | `Rec.UO\|1` | round |
| `REC_UO_120` | Rec Uo\|120 | `Rec.UO\|120` | round |
| `REC_UO_15` | Rec Uo\|15 | `Rec.UO\|15` | round |
| `REC_UO_1M` | Rec Uo\|1m | `Rec.UO\|1M` | round |
| `REC_UO_1W` | Rec Uo\|1w | `Rec.UO\|1W` | round |
| `REC_UO_240` | Rec Uo\|240 | `Rec.UO\|240` | round |
| `REC_UO_30` | Rec Uo\|30 | `Rec.UO\|30` | round |
| `REC_UO_5` | Rec Uo\|5 | `Rec.UO\|5` | round |
| `REC_UO_60` | Rec Uo\|60 | `Rec.UO\|60` | round |
| `RELATIVE_STRENGTH_INDEX_14` | Relative Strength Index (14) | `RSI` | computed_recommendation |
| `RELATIVE_STRENGTH_INDEX_7` | Relative Strength Index (7) | `RSI7` | computed_recommendation |
| `ROC_1` | Roc\|1 | `ROC\|1` | round |
| `ROC_120` | Roc\|120 | `ROC\|120` | round |
| `ROC_15` | Roc\|15 | `ROC\|15` | round |
| `ROC_1M` | Roc\|1m | `ROC\|1M` | round |
| `ROC_1W` | Roc\|1w | `ROC\|1W` | round |
| `ROC_240` | Roc\|240 | `ROC\|240` | round |
| `ROC_30` | Roc\|30 | `ROC\|30` | round |
| `ROC_5` | Roc\|5 | `ROC\|5` | round |
| `ROC_60` | Roc\|60 | `ROC\|60` | round |
| `RSI10` | Rsi10 | `RSI10` | round |
| `RSI10_1` | Rsi10\|1 | `RSI10\|1` | round |
| `RSI10_120` | Rsi10\|120 | `RSI10\|120` | round |
| `RSI10_15` | Rsi10\|15 | `RSI10\|15` | round |
| `RSI10_1M` | Rsi10\|1m | `RSI10\|1M` | round |
| `RSI10_1W` | Rsi10\|1w | `RSI10\|1W` | round |
| `RSI10_1_1` | Rsi10[1]\|1 | `RSI10[1]\|1` | round |
| `RSI10_1_120` | Rsi10[1]\|120 | `RSI10[1]\|120` | round |
| `RSI10_1_15` | Rsi10[1]\|15 | `RSI10[1]\|15` | round |
| `RSI10_1_1M` | Rsi10[1]\|1m | `RSI10[1]\|1M` | round |
| `RSI10_1_1W` | Rsi10[1]\|1w | `RSI10[1]\|1W` | round |
| `RSI10_1_2` | Rsi10[1] | `RSI10[1]` | round |
| `RSI10_1_240` | Rsi10[1]\|240 | `RSI10[1]\|240` | round |
| `RSI10_1_30` | Rsi10[1]\|30 | `RSI10[1]\|30` | round |
| `RSI10_1_5` | Rsi10[1]\|5 | `RSI10[1]\|5` | round |
| `RSI10_1_60` | Rsi10[1]\|60 | `RSI10[1]\|60` | round |
| `RSI10_240` | Rsi10\|240 | `RSI10\|240` | round |
| `RSI10_30` | Rsi10\|30 | `RSI10\|30` | round |
| `RSI10_5` | Rsi10\|5 | `RSI10\|5` | round |
| `RSI10_60` | Rsi10\|60 | `RSI10\|60` | round |
| `RSI2` | Rsi2 | `RSI2` | round |
| `RSI20` | Rsi20 | `RSI20` | round |
| `RSI20_1` | Rsi20\|1 | `RSI20\|1` | round |
| `RSI20_120` | Rsi20\|120 | `RSI20\|120` | round |
| `RSI20_15` | Rsi20\|15 | `RSI20\|15` | round |
| `RSI20_1M` | Rsi20\|1m | `RSI20\|1M` | round |
| `RSI20_1W` | Rsi20\|1w | `RSI20\|1W` | round |
| `RSI20_1_1` | Rsi20[1]\|1 | `RSI20[1]\|1` | round |
| `RSI20_1_120` | Rsi20[1]\|120 | `RSI20[1]\|120` | round |
| `RSI20_1_15` | Rsi20[1]\|15 | `RSI20[1]\|15` | round |
| `RSI20_1_1M` | Rsi20[1]\|1m | `RSI20[1]\|1M` | round |
| `RSI20_1_1W` | Rsi20[1]\|1w | `RSI20[1]\|1W` | round |
| `RSI20_1_2` | Rsi20[1] | `RSI20[1]` | round |
| `RSI20_1_240` | Rsi20[1]\|240 | `RSI20[1]\|240` | round |
| `RSI20_1_30` | Rsi20[1]\|30 | `RSI20[1]\|30` | round |
| `RSI20_1_5` | Rsi20[1]\|5 | `RSI20[1]\|5` | round |
| `RSI20_1_60` | Rsi20[1]\|60 | `RSI20[1]\|60` | round |
| `RSI20_240` | Rsi20\|240 | `RSI20\|240` | round |
| `RSI20_30` | Rsi20\|30 | `RSI20\|30` | round |
| `RSI20_5` | Rsi20\|5 | `RSI20\|5` | round |
| `RSI20_60` | Rsi20\|60 | `RSI20\|60` | round |
| `RSI21` | Rsi21 | `RSI21` | round |
| `RSI21_1` | Rsi21\|1 | `RSI21\|1` | round |
| `RSI21_120` | Rsi21\|120 | `RSI21\|120` | round |
| `RSI21_15` | Rsi21\|15 | `RSI21\|15` | round |
| `RSI21_1M` | Rsi21\|1m | `RSI21\|1M` | round |
| `RSI21_1W` | Rsi21\|1w | `RSI21\|1W` | round |
| `RSI21_1_1` | Rsi21[1]\|1 | `RSI21[1]\|1` | round |
| `RSI21_1_120` | Rsi21[1]\|120 | `RSI21[1]\|120` | round |
| `RSI21_1_15` | Rsi21[1]\|15 | `RSI21[1]\|15` | round |
| `RSI21_1_1M` | Rsi21[1]\|1m | `RSI21[1]\|1M` | round |
| `RSI21_1_1W` | Rsi21[1]\|1w | `RSI21[1]\|1W` | round |
| `RSI21_1_2` | Rsi21[1] | `RSI21[1]` | round |
| `RSI21_1_240` | Rsi21[1]\|240 | `RSI21[1]\|240` | round |
| `RSI21_1_30` | Rsi21[1]\|30 | `RSI21[1]\|30` | round |
| `RSI21_1_5` | Rsi21[1]\|5 | `RSI21[1]\|5` | round |
| `RSI21_1_60` | Rsi21[1]\|60 | `RSI21[1]\|60` | round |
| `RSI21_240` | Rsi21\|240 | `RSI21\|240` | round |
| `RSI21_30` | Rsi21\|30 | `RSI21\|30` | round |
| `RSI21_5` | Rsi21\|5 | `RSI21\|5` | round |
| `RSI21_60` | Rsi21\|60 | `RSI21\|60` | round |
| `RSI2_1` | Rsi2[1] | `RSI2[1]` | round |
| `RSI2_120` | Rsi2\|120 | `RSI2\|120` | round |
| `RSI2_15` | Rsi2\|15 | `RSI2\|15` | round |
| `RSI2_1M` | Rsi2\|1m | `RSI2\|1M` | round |
| `RSI2_1W` | Rsi2\|1w | `RSI2\|1W` | round |
| `RSI2_1_1` | Rsi2[1]\|1 | `RSI2[1]\|1` | round |
| `RSI2_1_120` | Rsi2[1]\|120 | `RSI2[1]\|120` | round |
| `RSI2_1_15` | Rsi2[1]\|15 | `RSI2[1]\|15` | round |
| `RSI2_1_1M` | Rsi2[1]\|1m | `RSI2[1]\|1M` | round |
| `RSI2_1_1W` | Rsi2[1]\|1w | `RSI2[1]\|1W` | round |
| `RSI2_1_2` | Rsi2\|1 | `RSI2\|1` | round |
| `RSI2_1_240` | Rsi2[1]\|240 | `RSI2[1]\|240` | round |
| `RSI2_1_30` | Rsi2[1]\|30 | `RSI2[1]\|30` | round |
| `RSI2_1_5` | Rsi2[1]\|5 | `RSI2[1]\|5` | round |
| `RSI2_1_60` | Rsi2[1]\|60 | `RSI2[1]\|60` | round |
| `RSI2_240` | Rsi2\|240 | `RSI2\|240` | round |
| `RSI2_30` | Rsi2\|30 | `RSI2\|30` | round |
| `RSI2_5` | Rsi2\|5 | `RSI2\|5` | round |
| `RSI2_60` | Rsi2\|60 | `RSI2\|60` | round |
| `RSI3` | Rsi3 | `RSI3` | round |
| `RSI30` | Rsi30 | `RSI30` | round |
| `RSI30_1` | Rsi30\|1 | `RSI30\|1` | round |
| `RSI30_120` | Rsi30\|120 | `RSI30\|120` | round |
| `RSI30_15` | Rsi30\|15 | `RSI30\|15` | round |
| `RSI30_1M` | Rsi30\|1m | `RSI30\|1M` | round |
| `RSI30_1W` | Rsi30\|1w | `RSI30\|1W` | round |
| `RSI30_1_1` | Rsi30[1]\|1 | `RSI30[1]\|1` | round |
| `RSI30_1_120` | Rsi30[1]\|120 | `RSI30[1]\|120` | round |
| `RSI30_1_15` | Rsi30[1]\|15 | `RSI30[1]\|15` | round |
| `RSI30_1_1M` | Rsi30[1]\|1m | `RSI30[1]\|1M` | round |
| `RSI30_1_1W` | Rsi30[1]\|1w | `RSI30[1]\|1W` | round |
| `RSI30_1_2` | Rsi30[1] | `RSI30[1]` | round |
| `RSI30_1_240` | Rsi30[1]\|240 | `RSI30[1]\|240` | round |
| `RSI30_1_30` | Rsi30[1]\|30 | `RSI30[1]\|30` | round |
| `RSI30_1_5` | Rsi30[1]\|5 | `RSI30[1]\|5` | round |
| `RSI30_1_60` | Rsi30[1]\|60 | `RSI30[1]\|60` | round |
| `RSI30_240` | Rsi30\|240 | `RSI30\|240` | round |
| `RSI30_30` | Rsi30\|30 | `RSI30\|30` | round |
| `RSI30_5` | Rsi30\|5 | `RSI30\|5` | round |
| `RSI30_60` | Rsi30\|60 | `RSI30\|60` | round |
| `RSI3_1` | Rsi3\|1 | `RSI3\|1` | round |
| `RSI3_120` | Rsi3\|120 | `RSI3\|120` | round |
| `RSI3_15` | Rsi3\|15 | `RSI3\|15` | round |
| `RSI3_1M` | Rsi3\|1m | `RSI3\|1M` | round |
| `RSI3_1W` | Rsi3\|1w | `RSI3\|1W` | round |
| `RSI3_1_1` | Rsi3[1]\|1 | `RSI3[1]\|1` | round |
| `RSI3_1_120` | Rsi3[1]\|120 | `RSI3[1]\|120` | round |
| `RSI3_1_15` | Rsi3[1]\|15 | `RSI3[1]\|15` | round |
| `RSI3_1_1M` | Rsi3[1]\|1m | `RSI3[1]\|1M` | round |
| `RSI3_1_1W` | Rsi3[1]\|1w | `RSI3[1]\|1W` | round |
| `RSI3_1_2` | Rsi3[1] | `RSI3[1]` | round |
| `RSI3_1_240` | Rsi3[1]\|240 | `RSI3[1]\|240` | round |
| `RSI3_1_30` | Rsi3[1]\|30 | `RSI3[1]\|30` | round |
| `RSI3_1_5` | Rsi3[1]\|5 | `RSI3[1]\|5` | round |
| `RSI3_1_60` | Rsi3[1]\|60 | `RSI3[1]\|60` | round |
| `RSI3_240` | Rsi3\|240 | `RSI3\|240` | round |
| `RSI3_30` | Rsi3\|30 | `RSI3\|30` | round |
| `RSI3_5` | Rsi3\|5 | `RSI3\|5` | round |
| `RSI3_60` | Rsi3\|60 | `RSI3\|60` | round |
| `RSI4` | Rsi4 | `RSI4` | round |
| `RSI4_1` | Rsi4\|1 | `RSI4\|1` | round |
| `RSI4_120` | Rsi4\|120 | `RSI4\|120` | round |
| `RSI4_15` | Rsi4\|15 | `RSI4\|15` | round |
| `RSI4_1M` | Rsi4\|1m | `RSI4\|1M` | round |
| `RSI4_1W` | Rsi4\|1w | `RSI4\|1W` | round |
| `RSI4_1_1` | Rsi4[1]\|1 | `RSI4[1]\|1` | round |
| `RSI4_1_120` | Rsi4[1]\|120 | `RSI4[1]\|120` | round |
| `RSI4_1_15` | Rsi4[1]\|15 | `RSI4[1]\|15` | round |
| `RSI4_1_1M` | Rsi4[1]\|1m | `RSI4[1]\|1M` | round |
| `RSI4_1_1W` | Rsi4[1]\|1w | `RSI4[1]\|1W` | round |
| `RSI4_1_2` | Rsi4[1] | `RSI4[1]` | round |
| `RSI4_1_240` | Rsi4[1]\|240 | `RSI4[1]\|240` | round |
| `RSI4_1_30` | Rsi4[1]\|30 | `RSI4[1]\|30` | round |
| `RSI4_1_5` | Rsi4[1]\|5 | `RSI4[1]\|5` | round |
| `RSI4_1_60` | Rsi4[1]\|60 | `RSI4[1]\|60` | round |
| `RSI4_240` | Rsi4\|240 | `RSI4\|240` | round |
| `RSI4_30` | Rsi4\|30 | `RSI4\|30` | round |
| `RSI4_5` | Rsi4\|5 | `RSI4\|5` | round |
| `RSI4_60` | Rsi4\|60 | `RSI4\|60` | round |
| `RSI5` | Rsi5 | `RSI5` | round |
| `RSI5_1` | Rsi5\|1 | `RSI5\|1` | round |
| `RSI5_120` | Rsi5\|120 | `RSI5\|120` | round |
| `RSI5_15` | Rsi5\|15 | `RSI5\|15` | round |
| `RSI5_1M` | Rsi5\|1m | `RSI5\|1M` | round |
| `RSI5_1W` | Rsi5\|1w | `RSI5\|1W` | round |
| `RSI5_1_1` | Rsi5[1]\|1 | `RSI5[1]\|1` | round |
| `RSI5_1_120` | Rsi5[1]\|120 | `RSI5[1]\|120` | round |
| `RSI5_1_15` | Rsi5[1]\|15 | `RSI5[1]\|15` | round |
| `RSI5_1_1M` | Rsi5[1]\|1m | `RSI5[1]\|1M` | round |
| `RSI5_1_1W` | Rsi5[1]\|1w | `RSI5[1]\|1W` | round |
| `RSI5_1_2` | Rsi5[1] | `RSI5[1]` | round |
| `RSI5_1_240` | Rsi5[1]\|240 | `RSI5[1]\|240` | round |
| `RSI5_1_30` | Rsi5[1]\|30 | `RSI5[1]\|30` | round |
| `RSI5_1_5` | Rsi5[1]\|5 | `RSI5[1]\|5` | round |
| `RSI5_1_60` | Rsi5[1]\|60 | `RSI5[1]\|60` | round |
| `RSI5_240` | Rsi5\|240 | `RSI5\|240` | round |
| `RSI5_30` | Rsi5\|30 | `RSI5\|30` | round |
| `RSI5_5` | Rsi5\|5 | `RSI5\|5` | round |
| `RSI5_60` | Rsi5\|60 | `RSI5\|60` | round |
| `RSI7_1` | Rsi7\|1 | `RSI7\|1` | round |
| `RSI7_120` | Rsi7\|120 | `RSI7\|120` | round |
| `RSI7_15` | Rsi7\|15 | `RSI7\|15` | round |
| `RSI7_1M` | Rsi7\|1m | `RSI7\|1M` | round |
| `RSI7_1W` | Rsi7\|1w | `RSI7\|1W` | round |
| `RSI7_1_1` | Rsi7[1]\|1 | `RSI7[1]\|1` | round |
| `RSI7_1_120` | Rsi7[1]\|120 | `RSI7[1]\|120` | round |
| `RSI7_1_15` | Rsi7[1]\|15 | `RSI7[1]\|15` | round |
| `RSI7_1_1M` | Rsi7[1]\|1m | `RSI7[1]\|1M` | round |
| `RSI7_1_1W` | Rsi7[1]\|1w | `RSI7[1]\|1W` | round |
| `RSI7_1_2` | Rsi7[1] | `RSI7[1]` | round |
| `RSI7_1_240` | Rsi7[1]\|240 | `RSI7[1]\|240` | round |
| `RSI7_1_30` | Rsi7[1]\|30 | `RSI7[1]\|30` | round |
| `RSI7_1_5` | Rsi7[1]\|5 | `RSI7[1]\|5` | round |
| `RSI7_1_60` | Rsi7[1]\|60 | `RSI7[1]\|60` | round |
| `RSI7_240` | Rsi7\|240 | `RSI7\|240` | round |
| `RSI7_30` | Rsi7\|30 | `RSI7\|30` | round |
| `RSI7_5` | Rsi7\|5 | `RSI7\|5` | round |
| `RSI7_60` | Rsi7\|60 | `RSI7\|60` | round |
| `RSI9` | Rsi9 | `RSI9` | round |
| `RSI9_1` | Rsi9[1] | `RSI9[1]` | round |
| `RSI9_120` | Rsi9\|120 | `RSI9\|120` | round |
| `RSI9_15` | Rsi9\|15 | `RSI9\|15` | round |
| `RSI9_1M` | Rsi9\|1m | `RSI9\|1M` | round |
| `RSI9_1W` | Rsi9\|1w | `RSI9\|1W` | round |
| `RSI9_1_1` | Rsi9[1]\|1 | `RSI9[1]\|1` | round |
| `RSI9_1_120` | Rsi9[1]\|120 | `RSI9[1]\|120` | round |
| `RSI9_1_15` | Rsi9[1]\|15 | `RSI9[1]\|15` | round |
| `RSI9_1_1M` | Rsi9[1]\|1m | `RSI9[1]\|1M` | round |
| `RSI9_1_1W` | Rsi9[1]\|1w | `RSI9[1]\|1W` | round |
| `RSI9_1_2` | Rsi9\|1 | `RSI9\|1` | round |
| `RSI9_1_240` | Rsi9[1]\|240 | `RSI9[1]\|240` | round |
| `RSI9_1_30` | Rsi9[1]\|30 | `RSI9[1]\|30` | round |
| `RSI9_1_5` | Rsi9[1]\|5 | `RSI9[1]\|5` | round |
| `RSI9_1_60` | Rsi9[1]\|60 | `RSI9[1]\|60` | round |
| `RSI9_240` | Rsi9\|240 | `RSI9\|240` | round |
| `RSI9_30` | Rsi9\|30 | `RSI9\|30` | round |
| `RSI9_5` | Rsi9\|5 | `RSI9\|5` | round |
| `RSI9_60` | Rsi9\|60 | `RSI9\|60` | round |
| `RSI_1` | Rsi\|1 | `RSI\|1` | round |
| `RSI_120` | Rsi\|120 | `RSI\|120` | round |
| `RSI_15` | Rsi\|15 | `RSI\|15` | round |
| `RSI_1M` | Rsi\|1m | `RSI\|1M` | round |
| `RSI_1W` | Rsi\|1w | `RSI\|1W` | round |
| `RSI_1_1` | Rsi[1]\|1 | `RSI[1]\|1` | round |
| `RSI_1_120` | Rsi[1]\|120 | `RSI[1]\|120` | round |
| `RSI_1_15` | Rsi[1]\|15 | `RSI[1]\|15` | round |
| `RSI_1_1M` | Rsi[1]\|1m | `RSI[1]\|1M` | round |
| `RSI_1_1W` | Rsi[1]\|1w | `RSI[1]\|1W` | round |
| `RSI_1_2` | Rsi[1] | `RSI[1]` | round |
| `RSI_1_240` | Rsi[1]\|240 | `RSI[1]\|240` | round |
| `RSI_1_30` | Rsi[1]\|30 | `RSI[1]\|30` | round |
| `RSI_1_5` | Rsi[1]\|5 | `RSI[1]\|5` | round |
| `RSI_1_60` | Rsi[1]\|60 | `RSI[1]\|60` | round |
| `RSI_240` | Rsi\|240 | `RSI\|240` | round |
| `RSI_30` | Rsi\|30 | `RSI\|30` | round |
| `RSI_5` | Rsi\|5 | `RSI\|5` | round |
| `RSI_60` | Rsi\|60 | `RSI\|60` | round |
| `STOCHASTIC_PERCENTD_14_3_3` | Stochastic %D (14, 3, 3) | `Stoch.D` | round |
| `STOCHASTIC_PERCENTK_14_3_3` | Stochastic %K (14, 3, 3) | `Stoch.K` | computed_recommendation |
| `STOCHASTIC_RSI_FAST_3_3_14_14` | Stochastic RSI Fast (3, 3, 14, 14) | `Stoch.RSI.K` | computed_recommendation |
| `STOCHASTIC_RSI_SLOW_3_3_14_14` | Stochastic RSI Slow (3, 3, 14, 14) | `Stoch.RSI.D` | round |
| `STOCH_D_1` | Stoch D[1] | `Stoch.D[1]` | round |
| `STOCH_D_120` | Stoch D\|120 | `Stoch.D\|120` | round |
| `STOCH_D_14_1_3` | Stoch D 14 1 3 | `Stoch.D_14_1_3` | round |
| `STOCH_D_14_1_3_1` | Stoch D 14 1 3[1] | `Stoch.D_14_1_3[1]` | round |
| `STOCH_D_14_1_3_120` | Stoch D 14 1 3\|120 | `Stoch.D_14_1_3\|120` | round |
| `STOCH_D_14_1_3_15` | Stoch D 14 1 3\|15 | `Stoch.D_14_1_3\|15` | round |
| `STOCH_D_14_1_3_1M` | Stoch D 14 1 3\|1m | `Stoch.D_14_1_3\|1M` | round |
| `STOCH_D_14_1_3_1W` | Stoch D 14 1 3\|1w | `Stoch.D_14_1_3\|1W` | round |
| `STOCH_D_14_1_3_1_1` | Stoch D 14 1 3[1]\|1 | `Stoch.D_14_1_3[1]\|1` | round |
| `STOCH_D_14_1_3_1_120` | Stoch D 14 1 3[1]\|120 | `Stoch.D_14_1_3[1]\|120` | round |
| `STOCH_D_14_1_3_1_15` | Stoch D 14 1 3[1]\|15 | `Stoch.D_14_1_3[1]\|15` | round |
| `STOCH_D_14_1_3_1_1M` | Stoch D 14 1 3[1]\|1m | `Stoch.D_14_1_3[1]\|1M` | round |
| `STOCH_D_14_1_3_1_1W` | Stoch D 14 1 3[1]\|1w | `Stoch.D_14_1_3[1]\|1W` | round |
| `STOCH_D_14_1_3_1_2` | Stoch D 14 1 3\|1 | `Stoch.D_14_1_3\|1` | round |
| `STOCH_D_14_1_3_1_240` | Stoch D 14 1 3[1]\|240 | `Stoch.D_14_1_3[1]\|240` | round |
| `STOCH_D_14_1_3_1_30` | Stoch D 14 1 3[1]\|30 | `Stoch.D_14_1_3[1]\|30` | round |
| `STOCH_D_14_1_3_1_5` | Stoch D 14 1 3[1]\|5 | `Stoch.D_14_1_3[1]\|5` | round |
| `STOCH_D_14_1_3_1_60` | Stoch D 14 1 3[1]\|60 | `Stoch.D_14_1_3[1]\|60` | round |
| `STOCH_D_14_1_3_240` | Stoch D 14 1 3\|240 | `Stoch.D_14_1_3\|240` | round |
| `STOCH_D_14_1_3_30` | Stoch D 14 1 3\|30 | `Stoch.D_14_1_3\|30` | round |
| `STOCH_D_14_1_3_5` | Stoch D 14 1 3\|5 | `Stoch.D_14_1_3\|5` | round |
| `STOCH_D_14_1_3_60` | Stoch D 14 1 3\|60 | `Stoch.D_14_1_3\|60` | round |
| `STOCH_D_15` | Stoch D\|15 | `Stoch.D\|15` | round |
| `STOCH_D_1M` | Stoch D\|1m | `Stoch.D\|1M` | round |
| `STOCH_D_1W` | Stoch D\|1w | `Stoch.D\|1W` | round |
| `STOCH_D_1_1` | Stoch D[1]\|1 | `Stoch.D[1]\|1` | round |
| `STOCH_D_1_120` | Stoch D[1]\|120 | `Stoch.D[1]\|120` | round |
| `STOCH_D_1_15` | Stoch D[1]\|15 | `Stoch.D[1]\|15` | round |
| `STOCH_D_1_1M` | Stoch D[1]\|1m | `Stoch.D[1]\|1M` | round |
| `STOCH_D_1_1W` | Stoch D[1]\|1w | `Stoch.D[1]\|1W` | round |
| `STOCH_D_1_2` | Stoch D\|1 | `Stoch.D\|1` | round |
| `STOCH_D_1_240` | Stoch D[1]\|240 | `Stoch.D[1]\|240` | round |
| `STOCH_D_1_30` | Stoch D[1]\|30 | `Stoch.D[1]\|30` | round |
| `STOCH_D_1_5` | Stoch D[1]\|5 | `Stoch.D[1]\|5` | round |
| `STOCH_D_1_60` | Stoch D[1]\|60 | `Stoch.D[1]\|60` | round |
| `STOCH_D_240` | Stoch D\|240 | `Stoch.D\|240` | round |
| `STOCH_D_30` | Stoch D\|30 | `Stoch.D\|30` | round |
| `STOCH_D_5` | Stoch D\|5 | `Stoch.D\|5` | round |
| `STOCH_D_5_3_3` | Stoch D 5 3 3 | `Stoch.D_5_3_3` | round |
| `STOCH_D_5_3_3_1` | Stoch D 5 3 3\|1 | `Stoch.D_5_3_3\|1` | round |
| `STOCH_D_5_3_3_120` | Stoch D 5 3 3\|120 | `Stoch.D_5_3_3\|120` | round |
| `STOCH_D_5_3_3_15` | Stoch D 5 3 3\|15 | `Stoch.D_5_3_3\|15` | round |
| `STOCH_D_5_3_3_1M` | Stoch D 5 3 3\|1m | `Stoch.D_5_3_3\|1M` | round |
| `STOCH_D_5_3_3_1W` | Stoch D 5 3 3\|1w | `Stoch.D_5_3_3\|1W` | round |
| `STOCH_D_5_3_3_1_1` | Stoch D 5 3 3[1]\|1 | `Stoch.D_5_3_3[1]\|1` | round |
| `STOCH_D_5_3_3_1_120` | Stoch D 5 3 3[1]\|120 | `Stoch.D_5_3_3[1]\|120` | round |
| `STOCH_D_5_3_3_1_15` | Stoch D 5 3 3[1]\|15 | `Stoch.D_5_3_3[1]\|15` | round |
| `STOCH_D_5_3_3_1_1M` | Stoch D 5 3 3[1]\|1m | `Stoch.D_5_3_3[1]\|1M` | round |
| `STOCH_D_5_3_3_1_1W` | Stoch D 5 3 3[1]\|1w | `Stoch.D_5_3_3[1]\|1W` | round |
| `STOCH_D_5_3_3_1_2` | Stoch D 5 3 3[1] | `Stoch.D_5_3_3[1]` | round |
| `STOCH_D_5_3_3_1_240` | Stoch D 5 3 3[1]\|240 | `Stoch.D_5_3_3[1]\|240` | round |
| `STOCH_D_5_3_3_1_30` | Stoch D 5 3 3[1]\|30 | `Stoch.D_5_3_3[1]\|30` | round |
| `STOCH_D_5_3_3_1_5` | Stoch D 5 3 3[1]\|5 | `Stoch.D_5_3_3[1]\|5` | round |
| `STOCH_D_5_3_3_1_60` | Stoch D 5 3 3[1]\|60 | `Stoch.D_5_3_3[1]\|60` | round |
| `STOCH_D_5_3_3_240` | Stoch D 5 3 3\|240 | `Stoch.D_5_3_3\|240` | round |
| `STOCH_D_5_3_3_30` | Stoch D 5 3 3\|30 | `Stoch.D_5_3_3\|30` | round |
| `STOCH_D_5_3_3_5` | Stoch D 5 3 3\|5 | `Stoch.D_5_3_3\|5` | round |
| `STOCH_D_5_3_3_60` | Stoch D 5 3 3\|60 | `Stoch.D_5_3_3\|60` | round |
| `STOCH_D_60` | Stoch D\|60 | `Stoch.D\|60` | round |
| `STOCH_D_6_3_3` | Stoch D 6 3 3 | `Stoch.D_6_3_3` | round |
| `STOCH_D_6_3_3_1` | Stoch D 6 3 3[1] | `Stoch.D_6_3_3[1]` | round |
| `STOCH_D_6_3_3_120` | Stoch D 6 3 3\|120 | `Stoch.D_6_3_3\|120` | round |
| `STOCH_D_6_3_3_15` | Stoch D 6 3 3\|15 | `Stoch.D_6_3_3\|15` | round |
| `STOCH_D_6_3_3_1M` | Stoch D 6 3 3\|1m | `Stoch.D_6_3_3\|1M` | round |
| `STOCH_D_6_3_3_1W` | Stoch D 6 3 3\|1w | `Stoch.D_6_3_3\|1W` | round |
| `STOCH_D_6_3_3_1_1` | Stoch D 6 3 3[1]\|1 | `Stoch.D_6_3_3[1]\|1` | round |
| `STOCH_D_6_3_3_1_120` | Stoch D 6 3 3[1]\|120 | `Stoch.D_6_3_3[1]\|120` | round |
| `STOCH_D_6_3_3_1_15` | Stoch D 6 3 3[1]\|15 | `Stoch.D_6_3_3[1]\|15` | round |
| `STOCH_D_6_3_3_1_1M` | Stoch D 6 3 3[1]\|1m | `Stoch.D_6_3_3[1]\|1M` | round |
| `STOCH_D_6_3_3_1_1W` | Stoch D 6 3 3[1]\|1w | `Stoch.D_6_3_3[1]\|1W` | round |
| `STOCH_D_6_3_3_1_2` | Stoch D 6 3 3\|1 | `Stoch.D_6_3_3\|1` | round |
| `STOCH_D_6_3_3_1_240` | Stoch D 6 3 3[1]\|240 | `Stoch.D_6_3_3[1]\|240` | round |
| `STOCH_D_6_3_3_1_30` | Stoch D 6 3 3[1]\|30 | `Stoch.D_6_3_3[1]\|30` | round |
| `STOCH_D_6_3_3_1_5` | Stoch D 6 3 3[1]\|5 | `Stoch.D_6_3_3[1]\|5` | round |
| `STOCH_D_6_3_3_1_60` | Stoch D 6 3 3[1]\|60 | `Stoch.D_6_3_3[1]\|60` | round |
| `STOCH_D_6_3_3_240` | Stoch D 6 3 3\|240 | `Stoch.D_6_3_3\|240` | round |
| `STOCH_D_6_3_3_30` | Stoch D 6 3 3\|30 | `Stoch.D_6_3_3\|30` | round |
| `STOCH_D_6_3_3_5` | Stoch D 6 3 3\|5 | `Stoch.D_6_3_3\|5` | round |
| `STOCH_D_6_3_3_60` | Stoch D 6 3 3\|60 | `Stoch.D_6_3_3\|60` | round |
| `STOCH_D_8_3_3` | Stoch D 8 3 3 | `Stoch.D_8_3_3` | round |
| `STOCH_D_8_3_3_1` | Stoch D 8 3 3[1] | `Stoch.D_8_3_3[1]` | round |
| `STOCH_D_8_3_3_120` | Stoch D 8 3 3\|120 | `Stoch.D_8_3_3\|120` | round |
| `STOCH_D_8_3_3_15` | Stoch D 8 3 3\|15 | `Stoch.D_8_3_3\|15` | round |
| `STOCH_D_8_3_3_1M` | Stoch D 8 3 3\|1m | `Stoch.D_8_3_3\|1M` | round |
| `STOCH_D_8_3_3_1W` | Stoch D 8 3 3\|1w | `Stoch.D_8_3_3\|1W` | round |
| `STOCH_D_8_3_3_1_1` | Stoch D 8 3 3[1]\|1 | `Stoch.D_8_3_3[1]\|1` | round |
| `STOCH_D_8_3_3_1_120` | Stoch D 8 3 3[1]\|120 | `Stoch.D_8_3_3[1]\|120` | round |
| `STOCH_D_8_3_3_1_15` | Stoch D 8 3 3[1]\|15 | `Stoch.D_8_3_3[1]\|15` | round |
| `STOCH_D_8_3_3_1_1M` | Stoch D 8 3 3[1]\|1m | `Stoch.D_8_3_3[1]\|1M` | round |
| `STOCH_D_8_3_3_1_1W` | Stoch D 8 3 3[1]\|1w | `Stoch.D_8_3_3[1]\|1W` | round |
| `STOCH_D_8_3_3_1_2` | Stoch D 8 3 3\|1 | `Stoch.D_8_3_3\|1` | round |
| `STOCH_D_8_3_3_1_240` | Stoch D 8 3 3[1]\|240 | `Stoch.D_8_3_3[1]\|240` | round |
| `STOCH_D_8_3_3_1_30` | Stoch D 8 3 3[1]\|30 | `Stoch.D_8_3_3[1]\|30` | round |
| `STOCH_D_8_3_3_1_5` | Stoch D 8 3 3[1]\|5 | `Stoch.D_8_3_3[1]\|5` | round |
| `STOCH_D_8_3_3_1_60` | Stoch D 8 3 3[1]\|60 | `Stoch.D_8_3_3[1]\|60` | round |
| `STOCH_D_8_3_3_240` | Stoch D 8 3 3\|240 | `Stoch.D_8_3_3\|240` | round |
| `STOCH_D_8_3_3_30` | Stoch D 8 3 3\|30 | `Stoch.D_8_3_3\|30` | round |
| `STOCH_D_8_3_3_5` | Stoch D 8 3 3\|5 | `Stoch.D_8_3_3\|5` | round |
| `STOCH_D_8_3_3_60` | Stoch D 8 3 3\|60 | `Stoch.D_8_3_3\|60` | round |
| `STOCH_K_1` | Stoch K[1] | `Stoch.K[1]` | round |
| `STOCH_K_120` | Stoch K\|120 | `Stoch.K\|120` | round |
| `STOCH_K_14_1_3` | Stoch K 14 1 3 | `Stoch.K_14_1_3` | round |
| `STOCH_K_14_1_3_1` | Stoch K 14 1 3\|1 | `Stoch.K_14_1_3\|1` | round |
| `STOCH_K_14_1_3_120` | Stoch K 14 1 3\|120 | `Stoch.K_14_1_3\|120` | round |
| `STOCH_K_14_1_3_15` | Stoch K 14 1 3\|15 | `Stoch.K_14_1_3\|15` | round |
| `STOCH_K_14_1_3_1M` | Stoch K 14 1 3\|1m | `Stoch.K_14_1_3\|1M` | round |
| `STOCH_K_14_1_3_1W` | Stoch K 14 1 3\|1w | `Stoch.K_14_1_3\|1W` | round |
| `STOCH_K_14_1_3_1_1` | Stoch K 14 1 3[1]\|1 | `Stoch.K_14_1_3[1]\|1` | round |
| `STOCH_K_14_1_3_1_120` | Stoch K 14 1 3[1]\|120 | `Stoch.K_14_1_3[1]\|120` | round |
| `STOCH_K_14_1_3_1_15` | Stoch K 14 1 3[1]\|15 | `Stoch.K_14_1_3[1]\|15` | round |
| `STOCH_K_14_1_3_1_1M` | Stoch K 14 1 3[1]\|1m | `Stoch.K_14_1_3[1]\|1M` | round |
| `STOCH_K_14_1_3_1_1W` | Stoch K 14 1 3[1]\|1w | `Stoch.K_14_1_3[1]\|1W` | round |
| `STOCH_K_14_1_3_1_2` | Stoch K 14 1 3[1] | `Stoch.K_14_1_3[1]` | round |
| `STOCH_K_14_1_3_1_240` | Stoch K 14 1 3[1]\|240 | `Stoch.K_14_1_3[1]\|240` | round |
| `STOCH_K_14_1_3_1_30` | Stoch K 14 1 3[1]\|30 | `Stoch.K_14_1_3[1]\|30` | round |
| `STOCH_K_14_1_3_1_5` | Stoch K 14 1 3[1]\|5 | `Stoch.K_14_1_3[1]\|5` | round |
| `STOCH_K_14_1_3_1_60` | Stoch K 14 1 3[1]\|60 | `Stoch.K_14_1_3[1]\|60` | round |
| `STOCH_K_14_1_3_240` | Stoch K 14 1 3\|240 | `Stoch.K_14_1_3\|240` | round |
| `STOCH_K_14_1_3_30` | Stoch K 14 1 3\|30 | `Stoch.K_14_1_3\|30` | round |
| `STOCH_K_14_1_3_5` | Stoch K 14 1 3\|5 | `Stoch.K_14_1_3\|5` | round |
| `STOCH_K_14_1_3_60` | Stoch K 14 1 3\|60 | `Stoch.K_14_1_3\|60` | round |
| `STOCH_K_15` | Stoch K\|15 | `Stoch.K\|15` | round |
| `STOCH_K_1M` | Stoch K\|1m | `Stoch.K\|1M` | round |
| `STOCH_K_1W` | Stoch K\|1w | `Stoch.K\|1W` | round |
| `STOCH_K_1_1` | Stoch K[1]\|1 | `Stoch.K[1]\|1` | round |
| `STOCH_K_1_120` | Stoch K[1]\|120 | `Stoch.K[1]\|120` | round |
| `STOCH_K_1_15` | Stoch K[1]\|15 | `Stoch.K[1]\|15` | round |
| `STOCH_K_1_1M` | Stoch K[1]\|1m | `Stoch.K[1]\|1M` | round |
| `STOCH_K_1_1W` | Stoch K[1]\|1w | `Stoch.K[1]\|1W` | round |
| `STOCH_K_1_2` | Stoch K\|1 | `Stoch.K\|1` | round |
| `STOCH_K_1_240` | Stoch K[1]\|240 | `Stoch.K[1]\|240` | round |
| `STOCH_K_1_30` | Stoch K[1]\|30 | `Stoch.K[1]\|30` | round |
| `STOCH_K_1_5` | Stoch K[1]\|5 | `Stoch.K[1]\|5` | round |
| `STOCH_K_1_60` | Stoch K[1]\|60 | `Stoch.K[1]\|60` | round |
| `STOCH_K_240` | Stoch K\|240 | `Stoch.K\|240` | round |
| `STOCH_K_30` | Stoch K\|30 | `Stoch.K\|30` | round |
| `STOCH_K_5` | Stoch K\|5 | `Stoch.K\|5` | round |
| `STOCH_K_5_3_3` | Stoch K 5 3 3 | `Stoch.K_5_3_3` | round |
| `STOCH_K_5_3_3_1` | Stoch K 5 3 3[1] | `Stoch.K_5_3_3[1]` | round |
| `STOCH_K_5_3_3_120` | Stoch K 5 3 3\|120 | `Stoch.K_5_3_3\|120` | round |
| `STOCH_K_5_3_3_15` | Stoch K 5 3 3\|15 | `Stoch.K_5_3_3\|15` | round |
| `STOCH_K_5_3_3_1M` | Stoch K 5 3 3\|1m | `Stoch.K_5_3_3\|1M` | round |
| `STOCH_K_5_3_3_1W` | Stoch K 5 3 3\|1w | `Stoch.K_5_3_3\|1W` | round |
| `STOCH_K_5_3_3_1_1` | Stoch K 5 3 3[1]\|1 | `Stoch.K_5_3_3[1]\|1` | round |
| `STOCH_K_5_3_3_1_120` | Stoch K 5 3 3[1]\|120 | `Stoch.K_5_3_3[1]\|120` | round |
| `STOCH_K_5_3_3_1_15` | Stoch K 5 3 3[1]\|15 | `Stoch.K_5_3_3[1]\|15` | round |
| `STOCH_K_5_3_3_1_1M` | Stoch K 5 3 3[1]\|1m | `Stoch.K_5_3_3[1]\|1M` | round |
| `STOCH_K_5_3_3_1_1W` | Stoch K 5 3 3[1]\|1w | `Stoch.K_5_3_3[1]\|1W` | round |
| `STOCH_K_5_3_3_1_2` | Stoch K 5 3 3\|1 | `Stoch.K_5_3_3\|1` | round |
| `STOCH_K_5_3_3_1_240` | Stoch K 5 3 3[1]\|240 | `Stoch.K_5_3_3[1]\|240` | round |
| `STOCH_K_5_3_3_1_30` | Stoch K 5 3 3[1]\|30 | `Stoch.K_5_3_3[1]\|30` | round |
| `STOCH_K_5_3_3_1_5` | Stoch K 5 3 3[1]\|5 | `Stoch.K_5_3_3[1]\|5` | round |
| `STOCH_K_5_3_3_1_60` | Stoch K 5 3 3[1]\|60 | `Stoch.K_5_3_3[1]\|60` | round |
| `STOCH_K_5_3_3_240` | Stoch K 5 3 3\|240 | `Stoch.K_5_3_3\|240` | round |
| `STOCH_K_5_3_3_30` | Stoch K 5 3 3\|30 | `Stoch.K_5_3_3\|30` | round |
| `STOCH_K_5_3_3_5` | Stoch K 5 3 3\|5 | `Stoch.K_5_3_3\|5` | round |
| `STOCH_K_5_3_3_60` | Stoch K 5 3 3\|60 | `Stoch.K_5_3_3\|60` | round |
| `STOCH_K_60` | Stoch K\|60 | `Stoch.K\|60` | round |
| `STOCH_K_6_3_3` | Stoch K 6 3 3 | `Stoch.K_6_3_3` | round |
| `STOCH_K_6_3_3_1` | Stoch K 6 3 3[1] | `Stoch.K_6_3_3[1]` | round |
| `STOCH_K_6_3_3_120` | Stoch K 6 3 3\|120 | `Stoch.K_6_3_3\|120` | round |
| `STOCH_K_6_3_3_15` | Stoch K 6 3 3\|15 | `Stoch.K_6_3_3\|15` | round |
| `STOCH_K_6_3_3_1M` | Stoch K 6 3 3\|1m | `Stoch.K_6_3_3\|1M` | round |
| `STOCH_K_6_3_3_1W` | Stoch K 6 3 3\|1w | `Stoch.K_6_3_3\|1W` | round |
| `STOCH_K_6_3_3_1_1` | Stoch K 6 3 3[1]\|1 | `Stoch.K_6_3_3[1]\|1` | round |
| `STOCH_K_6_3_3_1_120` | Stoch K 6 3 3[1]\|120 | `Stoch.K_6_3_3[1]\|120` | round |
| `STOCH_K_6_3_3_1_15` | Stoch K 6 3 3[1]\|15 | `Stoch.K_6_3_3[1]\|15` | round |
| `STOCH_K_6_3_3_1_1M` | Stoch K 6 3 3[1]\|1m | `Stoch.K_6_3_3[1]\|1M` | round |
| `STOCH_K_6_3_3_1_1W` | Stoch K 6 3 3[1]\|1w | `Stoch.K_6_3_3[1]\|1W` | round |
| `STOCH_K_6_3_3_1_2` | Stoch K 6 3 3\|1 | `Stoch.K_6_3_3\|1` | round |
| `STOCH_K_6_3_3_1_240` | Stoch K 6 3 3[1]\|240 | `Stoch.K_6_3_3[1]\|240` | round |
| `STOCH_K_6_3_3_1_30` | Stoch K 6 3 3[1]\|30 | `Stoch.K_6_3_3[1]\|30` | round |
| `STOCH_K_6_3_3_1_5` | Stoch K 6 3 3[1]\|5 | `Stoch.K_6_3_3[1]\|5` | round |
| `STOCH_K_6_3_3_1_60` | Stoch K 6 3 3[1]\|60 | `Stoch.K_6_3_3[1]\|60` | round |
| `STOCH_K_6_3_3_240` | Stoch K 6 3 3\|240 | `Stoch.K_6_3_3\|240` | round |
| `STOCH_K_6_3_3_30` | Stoch K 6 3 3\|30 | `Stoch.K_6_3_3\|30` | round |
| `STOCH_K_6_3_3_5` | Stoch K 6 3 3\|5 | `Stoch.K_6_3_3\|5` | round |
| `STOCH_K_6_3_3_60` | Stoch K 6 3 3\|60 | `Stoch.K_6_3_3\|60` | round |
| `STOCH_K_8_3_3` | Stoch K 8 3 3 | `Stoch.K_8_3_3` | round |
| `STOCH_K_8_3_3_1` | Stoch K 8 3 3\|1 | `Stoch.K_8_3_3\|1` | round |
| `STOCH_K_8_3_3_120` | Stoch K 8 3 3\|120 | `Stoch.K_8_3_3\|120` | round |
| `STOCH_K_8_3_3_15` | Stoch K 8 3 3\|15 | `Stoch.K_8_3_3\|15` | round |
| `STOCH_K_8_3_3_1M` | Stoch K 8 3 3\|1m | `Stoch.K_8_3_3\|1M` | round |
| `STOCH_K_8_3_3_1W` | Stoch K 8 3 3\|1w | `Stoch.K_8_3_3\|1W` | round |
| `STOCH_K_8_3_3_1_1` | Stoch K 8 3 3[1]\|1 | `Stoch.K_8_3_3[1]\|1` | round |
| `STOCH_K_8_3_3_1_120` | Stoch K 8 3 3[1]\|120 | `Stoch.K_8_3_3[1]\|120` | round |
| `STOCH_K_8_3_3_1_15` | Stoch K 8 3 3[1]\|15 | `Stoch.K_8_3_3[1]\|15` | round |
| `STOCH_K_8_3_3_1_1M` | Stoch K 8 3 3[1]\|1m | `Stoch.K_8_3_3[1]\|1M` | round |
| `STOCH_K_8_3_3_1_1W` | Stoch K 8 3 3[1]\|1w | `Stoch.K_8_3_3[1]\|1W` | round |
| `STOCH_K_8_3_3_1_2` | Stoch K 8 3 3[1] | `Stoch.K_8_3_3[1]` | round |
| `STOCH_K_8_3_3_1_240` | Stoch K 8 3 3[1]\|240 | `Stoch.K_8_3_3[1]\|240` | round |
| `STOCH_K_8_3_3_1_30` | Stoch K 8 3 3[1]\|30 | `Stoch.K_8_3_3[1]\|30` | round |
| `STOCH_K_8_3_3_1_5` | Stoch K 8 3 3[1]\|5 | `Stoch.K_8_3_3[1]\|5` | round |
| `STOCH_K_8_3_3_1_60` | Stoch K 8 3 3[1]\|60 | `Stoch.K_8_3_3[1]\|60` | round |
| `STOCH_K_8_3_3_240` | Stoch K 8 3 3\|240 | `Stoch.K_8_3_3\|240` | round |
| `STOCH_K_8_3_3_30` | Stoch K 8 3 3\|30 | `Stoch.K_8_3_3\|30` | round |
| `STOCH_K_8_3_3_5` | Stoch K 8 3 3\|5 | `Stoch.K_8_3_3\|5` | round |
| `STOCH_K_8_3_3_60` | Stoch K 8 3 3\|60 | `Stoch.K_8_3_3\|60` | round |
| `STOCH_RSI_D_1` | Stoch RSI D\|1 | `Stoch.RSI.D\|1` | round |
| `STOCH_RSI_D_120` | Stoch RSI D\|120 | `Stoch.RSI.D\|120` | round |
| `STOCH_RSI_D_15` | Stoch RSI D\|15 | `Stoch.RSI.D\|15` | round |
| `STOCH_RSI_D_1M` | Stoch RSI D\|1m | `Stoch.RSI.D\|1M` | round |
| `STOCH_RSI_D_1W` | Stoch RSI D\|1w | `Stoch.RSI.D\|1W` | round |
| `STOCH_RSI_D_240` | Stoch RSI D\|240 | `Stoch.RSI.D\|240` | round |
| `STOCH_RSI_D_30` | Stoch RSI D\|30 | `Stoch.RSI.D\|30` | round |
| `STOCH_RSI_D_5` | Stoch RSI D\|5 | `Stoch.RSI.D\|5` | round |
| `STOCH_RSI_D_60` | Stoch RSI D\|60 | `Stoch.RSI.D\|60` | round |
| `STOCH_RSI_K_1` | Stoch RSI K\|1 | `Stoch.RSI.K\|1` | round |
| `STOCH_RSI_K_120` | Stoch RSI K\|120 | `Stoch.RSI.K\|120` | round |
| `STOCH_RSI_K_15` | Stoch RSI K\|15 | `Stoch.RSI.K\|15` | round |
| `STOCH_RSI_K_1M` | Stoch RSI K\|1m | `Stoch.RSI.K\|1M` | round |
| `STOCH_RSI_K_1W` | Stoch RSI K\|1w | `Stoch.RSI.K\|1W` | round |
| `STOCH_RSI_K_240` | Stoch RSI K\|240 | `Stoch.RSI.K\|240` | round |
| `STOCH_RSI_K_30` | Stoch RSI K\|30 | `Stoch.RSI.K\|30` | round |
| `STOCH_RSI_K_5` | Stoch RSI K\|5 | `Stoch.RSI.K\|5` | round |
| `STOCH_RSI_K_60` | Stoch RSI K\|60 | `Stoch.RSI.K\|60` | round |
| `ULTIMATE_OSCILLATOR_7_14_28` | Ultimate Oscillator (7, 14, 28) | `UO` | recommendation |
| `UO_1` | Uo\|1 | `UO\|1` | round |
| `UO_120` | Uo\|120 | `UO\|120` | round |
| `UO_15` | Uo\|15 | `UO\|15` | round |
| `UO_1M` | Uo\|1m | `UO\|1M` | round |
| `UO_1W` | Uo\|1w | `UO\|1W` | round |
| `UO_240` | Uo\|240 | `UO\|240` | round |
| `UO_30` | Uo\|30 | `UO\|30` | round |
| `UO_5` | Uo\|5 | `UO\|5` | round |
| `UO_60` | Uo\|60 | `UO\|60` | round |
| `WILLIAMS_PERCENT_RANGE_14` | Williams Percent Range (14) | `W.R` | computed_recommendation |
| `W_R_1` | W R\|1 | `W.R\|1` | round |
| `W_R_120` | W R\|120 | `W.R\|120` | round |
| `W_R_15` | W R\|15 | `W.R\|15` | round |
| `W_R_1M` | W R\|1m | `W.R\|1M` | round |
| `W_R_1W` | W R\|1w | `W.R\|1W` | round |
| `W_R_240` | W R\|240 | `W.R\|240` | round |
| `W_R_30` | W R\|30 | `W.R\|30` | round |
| `W_R_5` | W R\|5 | `W.R\|5` | round |
| `W_R_60` | W R\|60 | `W.R\|60` | round |

## Trend Indicators

*400 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `ADX_1` | Adx\|1 | `ADX\|1` | round |
| `ADX_100` | ADX 100 | `ADX_100` | round |
| `ADX_100_1` | ADX 100\|1 | `ADX_100\|1` | round |
| `ADX_100_120` | ADX 100\|120 | `ADX_100\|120` | round |
| `ADX_100_15` | ADX 100\|15 | `ADX_100\|15` | round |
| `ADX_100_1M` | ADX 100\|1m | `ADX_100\|1M` | round |
| `ADX_100_1W` | ADX 100\|1w | `ADX_100\|1W` | round |
| `ADX_100_240` | ADX 100\|240 | `ADX_100\|240` | round |
| `ADX_100_30` | ADX 100\|30 | `ADX_100\|30` | round |
| `ADX_100_5` | ADX 100\|5 | `ADX_100\|5` | round |
| `ADX_100_60` | ADX 100\|60 | `ADX_100\|60` | round |
| `ADX_120` | Adx\|120 | `ADX\|120` | round |
| `ADX_15` | Adx\|15 | `ADX\|15` | round |
| `ADX_1M` | Adx\|1m | `ADX\|1M` | round |
| `ADX_1W` | Adx\|1w | `ADX\|1W` | round |
| `ADX_20` | ADX 20 | `ADX_20` | round |
| `ADX_20_1` | ADX 20\|1 | `ADX_20\|1` | round |
| `ADX_20_120` | ADX 20\|120 | `ADX_20\|120` | round |
| `ADX_20_15` | ADX 20\|15 | `ADX_20\|15` | round |
| `ADX_20_1M` | ADX 20\|1m | `ADX_20\|1M` | round |
| `ADX_20_1W` | ADX 20\|1w | `ADX_20\|1W` | round |
| `ADX_20_240` | ADX 20\|240 | `ADX_20\|240` | round |
| `ADX_20_30` | ADX 20\|30 | `ADX_20\|30` | round |
| `ADX_20_5` | ADX 20\|5 | `ADX_20\|5` | round |
| `ADX_20_60` | ADX 20\|60 | `ADX_20\|60` | round |
| `ADX_240` | Adx\|240 | `ADX\|240` | round |
| `ADX_30` | Adx\|30 | `ADX\|30` | round |
| `ADX_5` | Adx\|5 | `ADX\|5` | round |
| `ADX_50` | ADX 50 | `ADX_50` | round |
| `ADX_50_1` | ADX 50\|1 | `ADX_50\|1` | round |
| `ADX_50_120` | ADX 50\|120 | `ADX_50\|120` | round |
| `ADX_50_15` | ADX 50\|15 | `ADX_50\|15` | round |
| `ADX_50_1M` | ADX 50\|1m | `ADX_50\|1M` | round |
| `ADX_50_1W` | ADX 50\|1w | `ADX_50\|1W` | round |
| `ADX_50_240` | ADX 50\|240 | `ADX_50\|240` | round |
| `ADX_50_30` | ADX 50\|30 | `ADX_50\|30` | round |
| `ADX_50_5` | ADX 50\|5 | `ADX_50\|5` | round |
| `ADX_50_60` | ADX 50\|60 | `ADX_50\|60` | round |
| `ADX_60` | Adx\|60 | `ADX\|60` | round |
| `ADX_9` | ADX 9 | `ADX_9` | round |
| `ADX_9_1` | ADX 9\|1 | `ADX_9\|1` | round |
| `ADX_9_120` | ADX 9\|120 | `ADX_9\|120` | round |
| `ADX_9_15` | ADX 9\|15 | `ADX_9\|15` | round |
| `ADX_9_1M` | ADX 9\|1m | `ADX_9\|1M` | round |
| `ADX_9_1W` | ADX 9\|1w | `ADX_9\|1W` | round |
| `ADX_9_240` | ADX 9\|240 | `ADX_9\|240` | round |
| `ADX_9_30` | ADX 9\|30 | `ADX_9\|30` | round |
| `ADX_9_5` | ADX 9\|5 | `ADX_9\|5` | round |
| `ADX_9_60` | ADX 9\|60 | `ADX_9\|60` | round |
| `ADX_DI_1` | Adx-di[1] | `ADX-DI[1]` | round |
| `ADX_DI_100` | Adx-di 100 | `ADX-DI_100` | round |
| `ADX_DI_100_1` | Adx-di 100[1] | `ADX-DI_100[1]` | round |
| `ADX_DI_100_120` | Adx-di 100\|120 | `ADX-DI_100\|120` | round |
| `ADX_DI_100_15` | Adx-di 100\|15 | `ADX-DI_100\|15` | round |
| `ADX_DI_100_1M` | Adx-di 100\|1m | `ADX-DI_100\|1M` | round |
| `ADX_DI_100_1W` | Adx-di 100\|1w | `ADX-DI_100\|1W` | round |
| `ADX_DI_100_1_1` | Adx-di 100[1]\|1 | `ADX-DI_100[1]\|1` | round |
| `ADX_DI_100_1_120` | Adx-di 100[1]\|120 | `ADX-DI_100[1]\|120` | round |
| `ADX_DI_100_1_15` | Adx-di 100[1]\|15 | `ADX-DI_100[1]\|15` | round |
| `ADX_DI_100_1_1M` | Adx-di 100[1]\|1m | `ADX-DI_100[1]\|1M` | round |
| `ADX_DI_100_1_1W` | Adx-di 100[1]\|1w | `ADX-DI_100[1]\|1W` | round |
| `ADX_DI_100_1_2` | Adx-di 100\|1 | `ADX-DI_100\|1` | round |
| `ADX_DI_100_1_240` | Adx-di 100[1]\|240 | `ADX-DI_100[1]\|240` | round |
| `ADX_DI_100_1_30` | Adx-di 100[1]\|30 | `ADX-DI_100[1]\|30` | round |
| `ADX_DI_100_1_5` | Adx-di 100[1]\|5 | `ADX-DI_100[1]\|5` | round |
| `ADX_DI_100_1_60` | Adx-di 100[1]\|60 | `ADX-DI_100[1]\|60` | round |
| `ADX_DI_100_240` | Adx-di 100\|240 | `ADX-DI_100\|240` | round |
| `ADX_DI_100_30` | Adx-di 100\|30 | `ADX-DI_100\|30` | round |
| `ADX_DI_100_5` | Adx-di 100\|5 | `ADX-DI_100\|5` | round |
| `ADX_DI_100_60` | Adx-di 100\|60 | `ADX-DI_100\|60` | round |
| `ADX_DI_120` | Adx-di\|120 | `ADX-DI\|120` | round |
| `ADX_DI_15` | Adx-di\|15 | `ADX-DI\|15` | round |
| `ADX_DI_1M` | Adx-di\|1m | `ADX-DI\|1M` | round |
| `ADX_DI_1W` | Adx-di\|1w | `ADX-DI\|1W` | round |
| `ADX_DI_1_1` | Adx-di[1]\|1 | `ADX-DI[1]\|1` | round |
| `ADX_DI_1_120` | Adx-di[1]\|120 | `ADX-DI[1]\|120` | round |
| `ADX_DI_1_15` | Adx-di[1]\|15 | `ADX-DI[1]\|15` | round |
| `ADX_DI_1_1M` | Adx-di[1]\|1m | `ADX-DI[1]\|1M` | round |
| `ADX_DI_1_1W` | Adx-di[1]\|1w | `ADX-DI[1]\|1W` | round |
| `ADX_DI_1_2` | Adx-di\|1 | `ADX-DI\|1` | round |
| `ADX_DI_1_240` | Adx-di[1]\|240 | `ADX-DI[1]\|240` | round |
| `ADX_DI_1_30` | Adx-di[1]\|30 | `ADX-DI[1]\|30` | round |
| `ADX_DI_1_5` | Adx-di[1]\|5 | `ADX-DI[1]\|5` | round |
| `ADX_DI_1_60` | Adx-di[1]\|60 | `ADX-DI[1]\|60` | round |
| `ADX_DI_20` | Adx-di 20 | `ADX-DI_20` | round |
| `ADX_DI_20_1` | Adx-di 20\|1 | `ADX-DI_20\|1` | round |
| `ADX_DI_20_120` | Adx-di 20\|120 | `ADX-DI_20\|120` | round |
| `ADX_DI_20_15` | Adx-di 20\|15 | `ADX-DI_20\|15` | round |
| `ADX_DI_20_1M` | Adx-di 20\|1m | `ADX-DI_20\|1M` | round |
| `ADX_DI_20_1W` | Adx-di 20\|1w | `ADX-DI_20\|1W` | round |
| `ADX_DI_20_1_1` | Adx-di 20[1]\|1 | `ADX-DI_20[1]\|1` | round |
| `ADX_DI_20_1_120` | Adx-di 20[1]\|120 | `ADX-DI_20[1]\|120` | round |
| `ADX_DI_20_1_15` | Adx-di 20[1]\|15 | `ADX-DI_20[1]\|15` | round |
| `ADX_DI_20_1_1M` | Adx-di 20[1]\|1m | `ADX-DI_20[1]\|1M` | round |
| `ADX_DI_20_1_1W` | Adx-di 20[1]\|1w | `ADX-DI_20[1]\|1W` | round |
| `ADX_DI_20_1_2` | Adx-di 20[1] | `ADX-DI_20[1]` | round |
| `ADX_DI_20_1_240` | Adx-di 20[1]\|240 | `ADX-DI_20[1]\|240` | round |
| `ADX_DI_20_1_30` | Adx-di 20[1]\|30 | `ADX-DI_20[1]\|30` | round |
| `ADX_DI_20_1_5` | Adx-di 20[1]\|5 | `ADX-DI_20[1]\|5` | round |
| `ADX_DI_20_1_60` | Adx-di 20[1]\|60 | `ADX-DI_20[1]\|60` | round |
| `ADX_DI_20_240` | Adx-di 20\|240 | `ADX-DI_20\|240` | round |
| `ADX_DI_20_30` | Adx-di 20\|30 | `ADX-DI_20\|30` | round |
| `ADX_DI_20_5` | Adx-di 20\|5 | `ADX-DI_20\|5` | round |
| `ADX_DI_20_60` | Adx-di 20\|60 | `ADX-DI_20\|60` | round |
| `ADX_DI_240` | Adx-di\|240 | `ADX-DI\|240` | round |
| `ADX_DI_30` | Adx-di\|30 | `ADX-DI\|30` | round |
| `ADX_DI_5` | Adx-di\|5 | `ADX-DI\|5` | round |
| `ADX_DI_50` | Adx-di 50 | `ADX-DI_50` | round |
| `ADX_DI_50_1` | Adx-di 50[1] | `ADX-DI_50[1]` | round |
| `ADX_DI_50_120` | Adx-di 50\|120 | `ADX-DI_50\|120` | round |
| `ADX_DI_50_15` | Adx-di 50\|15 | `ADX-DI_50\|15` | round |
| `ADX_DI_50_1M` | Adx-di 50\|1m | `ADX-DI_50\|1M` | round |
| `ADX_DI_50_1W` | Adx-di 50\|1w | `ADX-DI_50\|1W` | round |
| `ADX_DI_50_1_1` | Adx-di 50[1]\|1 | `ADX-DI_50[1]\|1` | round |
| `ADX_DI_50_1_120` | Adx-di 50[1]\|120 | `ADX-DI_50[1]\|120` | round |
| `ADX_DI_50_1_15` | Adx-di 50[1]\|15 | `ADX-DI_50[1]\|15` | round |
| `ADX_DI_50_1_1M` | Adx-di 50[1]\|1m | `ADX-DI_50[1]\|1M` | round |
| `ADX_DI_50_1_1W` | Adx-di 50[1]\|1w | `ADX-DI_50[1]\|1W` | round |
| `ADX_DI_50_1_2` | Adx-di 50\|1 | `ADX-DI_50\|1` | round |
| `ADX_DI_50_1_240` | Adx-di 50[1]\|240 | `ADX-DI_50[1]\|240` | round |
| `ADX_DI_50_1_30` | Adx-di 50[1]\|30 | `ADX-DI_50[1]\|30` | round |
| `ADX_DI_50_1_5` | Adx-di 50[1]\|5 | `ADX-DI_50[1]\|5` | round |
| `ADX_DI_50_1_60` | Adx-di 50[1]\|60 | `ADX-DI_50[1]\|60` | round |
| `ADX_DI_50_240` | Adx-di 50\|240 | `ADX-DI_50\|240` | round |
| `ADX_DI_50_30` | Adx-di 50\|30 | `ADX-DI_50\|30` | round |
| `ADX_DI_50_5` | Adx-di 50\|5 | `ADX-DI_50\|5` | round |
| `ADX_DI_50_60` | Adx-di 50\|60 | `ADX-DI_50\|60` | round |
| `ADX_DI_60` | Adx-di\|60 | `ADX-DI\|60` | round |
| `ADX_DI_9` | Adx-di 9 | `ADX-DI_9` | round |
| `ADX_DI_9_1` | Adx-di 9\|1 | `ADX-DI_9\|1` | round |
| `ADX_DI_9_120` | Adx-di 9\|120 | `ADX-DI_9\|120` | round |
| `ADX_DI_9_15` | Adx-di 9\|15 | `ADX-DI_9\|15` | round |
| `ADX_DI_9_1M` | Adx-di 9\|1m | `ADX-DI_9\|1M` | round |
| `ADX_DI_9_1W` | Adx-di 9\|1w | `ADX-DI_9\|1W` | round |
| `ADX_DI_9_1_1` | Adx-di 9[1]\|1 | `ADX-DI_9[1]\|1` | round |
| `ADX_DI_9_1_120` | Adx-di 9[1]\|120 | `ADX-DI_9[1]\|120` | round |
| `ADX_DI_9_1_15` | Adx-di 9[1]\|15 | `ADX-DI_9[1]\|15` | round |
| `ADX_DI_9_1_1M` | Adx-di 9[1]\|1m | `ADX-DI_9[1]\|1M` | round |
| `ADX_DI_9_1_1W` | Adx-di 9[1]\|1w | `ADX-DI_9[1]\|1W` | round |
| `ADX_DI_9_1_2` | Adx-di 9[1] | `ADX-DI_9[1]` | round |
| `ADX_DI_9_1_240` | Adx-di 9[1]\|240 | `ADX-DI_9[1]\|240` | round |
| `ADX_DI_9_1_30` | Adx-di 9[1]\|30 | `ADX-DI_9[1]\|30` | round |
| `ADX_DI_9_1_5` | Adx-di 9[1]\|5 | `ADX-DI_9[1]\|5` | round |
| `ADX_DI_9_1_60` | Adx-di 9[1]\|60 | `ADX-DI_9[1]\|60` | round |
| `ADX_DI_9_240` | Adx-di 9\|240 | `ADX-DI_9\|240` | round |
| `ADX_DI_9_30` | Adx-di 9\|30 | `ADX-DI_9\|30` | round |
| `ADX_DI_9_5` | Adx-di 9\|5 | `ADX-DI_9\|5` | round |
| `ADX_DI_9_60` | Adx-di 9\|60 | `ADX-DI_9\|60` | round |
| `ADX_PLUS_DI_1` | Adx+di[1] | `ADX+DI[1]` | round |
| `ADX_PLUS_DI_100` | Adx+di 100 | `ADX+DI_100` | round |
| `ADX_PLUS_DI_100_1` | Adx+di 100\|1 | `ADX+DI_100\|1` | round |
| `ADX_PLUS_DI_100_120` | Adx+di 100\|120 | `ADX+DI_100\|120` | round |
| `ADX_PLUS_DI_100_15` | Adx+di 100\|15 | `ADX+DI_100\|15` | round |
| `ADX_PLUS_DI_100_1M` | Adx+di 100\|1m | `ADX+DI_100\|1M` | round |
| `ADX_PLUS_DI_100_1W` | Adx+di 100\|1w | `ADX+DI_100\|1W` | round |
| `ADX_PLUS_DI_100_1_1` | Adx+di 100[1]\|1 | `ADX+DI_100[1]\|1` | round |
| `ADX_PLUS_DI_100_1_120` | Adx+di 100[1]\|120 | `ADX+DI_100[1]\|120` | round |
| `ADX_PLUS_DI_100_1_15` | Adx+di 100[1]\|15 | `ADX+DI_100[1]\|15` | round |
| `ADX_PLUS_DI_100_1_1M` | Adx+di 100[1]\|1m | `ADX+DI_100[1]\|1M` | round |
| `ADX_PLUS_DI_100_1_1W` | Adx+di 100[1]\|1w | `ADX+DI_100[1]\|1W` | round |
| `ADX_PLUS_DI_100_1_2` | Adx+di 100[1] | `ADX+DI_100[1]` | round |
| `ADX_PLUS_DI_100_1_240` | Adx+di 100[1]\|240 | `ADX+DI_100[1]\|240` | round |
| `ADX_PLUS_DI_100_1_30` | Adx+di 100[1]\|30 | `ADX+DI_100[1]\|30` | round |
| `ADX_PLUS_DI_100_1_5` | Adx+di 100[1]\|5 | `ADX+DI_100[1]\|5` | round |
| `ADX_PLUS_DI_100_1_60` | Adx+di 100[1]\|60 | `ADX+DI_100[1]\|60` | round |
| `ADX_PLUS_DI_100_240` | Adx+di 100\|240 | `ADX+DI_100\|240` | round |
| `ADX_PLUS_DI_100_30` | Adx+di 100\|30 | `ADX+DI_100\|30` | round |
| `ADX_PLUS_DI_100_5` | Adx+di 100\|5 | `ADX+DI_100\|5` | round |
| `ADX_PLUS_DI_100_60` | Adx+di 100\|60 | `ADX+DI_100\|60` | round |
| `ADX_PLUS_DI_120` | Adx+di\|120 | `ADX+DI\|120` | round |
| `ADX_PLUS_DI_15` | Adx+di\|15 | `ADX+DI\|15` | round |
| `ADX_PLUS_DI_1M` | Adx+di\|1m | `ADX+DI\|1M` | round |
| `ADX_PLUS_DI_1W` | Adx+di\|1w | `ADX+DI\|1W` | round |
| `ADX_PLUS_DI_1_1` | Adx+di[1]\|1 | `ADX+DI[1]\|1` | round |
| `ADX_PLUS_DI_1_120` | Adx+di[1]\|120 | `ADX+DI[1]\|120` | round |
| `ADX_PLUS_DI_1_15` | Adx+di[1]\|15 | `ADX+DI[1]\|15` | round |
| `ADX_PLUS_DI_1_1M` | Adx+di[1]\|1m | `ADX+DI[1]\|1M` | round |
| `ADX_PLUS_DI_1_1W` | Adx+di[1]\|1w | `ADX+DI[1]\|1W` | round |
| `ADX_PLUS_DI_1_2` | Adx+di\|1 | `ADX+DI\|1` | round |
| `ADX_PLUS_DI_1_240` | Adx+di[1]\|240 | `ADX+DI[1]\|240` | round |
| `ADX_PLUS_DI_1_30` | Adx+di[1]\|30 | `ADX+DI[1]\|30` | round |
| `ADX_PLUS_DI_1_5` | Adx+di[1]\|5 | `ADX+DI[1]\|5` | round |
| `ADX_PLUS_DI_1_60` | Adx+di[1]\|60 | `ADX+DI[1]\|60` | round |
| `ADX_PLUS_DI_20` | Adx+di 20 | `ADX+DI_20` | round |
| `ADX_PLUS_DI_20_1` | Adx+di 20[1] | `ADX+DI_20[1]` | round |
| `ADX_PLUS_DI_20_120` | Adx+di 20\|120 | `ADX+DI_20\|120` | round |
| `ADX_PLUS_DI_20_15` | Adx+di 20\|15 | `ADX+DI_20\|15` | round |
| `ADX_PLUS_DI_20_1M` | Adx+di 20\|1m | `ADX+DI_20\|1M` | round |
| `ADX_PLUS_DI_20_1W` | Adx+di 20\|1w | `ADX+DI_20\|1W` | round |
| `ADX_PLUS_DI_20_1_1` | Adx+di 20[1]\|1 | `ADX+DI_20[1]\|1` | round |
| `ADX_PLUS_DI_20_1_120` | Adx+di 20[1]\|120 | `ADX+DI_20[1]\|120` | round |
| `ADX_PLUS_DI_20_1_15` | Adx+di 20[1]\|15 | `ADX+DI_20[1]\|15` | round |
| `ADX_PLUS_DI_20_1_1M` | Adx+di 20[1]\|1m | `ADX+DI_20[1]\|1M` | round |
| `ADX_PLUS_DI_20_1_1W` | Adx+di 20[1]\|1w | `ADX+DI_20[1]\|1W` | round |
| `ADX_PLUS_DI_20_1_2` | Adx+di 20\|1 | `ADX+DI_20\|1` | round |
| `ADX_PLUS_DI_20_1_240` | Adx+di 20[1]\|240 | `ADX+DI_20[1]\|240` | round |
| `ADX_PLUS_DI_20_1_30` | Adx+di 20[1]\|30 | `ADX+DI_20[1]\|30` | round |
| `ADX_PLUS_DI_20_1_5` | Adx+di 20[1]\|5 | `ADX+DI_20[1]\|5` | round |
| `ADX_PLUS_DI_20_1_60` | Adx+di 20[1]\|60 | `ADX+DI_20[1]\|60` | round |
| `ADX_PLUS_DI_20_240` | Adx+di 20\|240 | `ADX+DI_20\|240` | round |
| `ADX_PLUS_DI_20_30` | Adx+di 20\|30 | `ADX+DI_20\|30` | round |
| `ADX_PLUS_DI_20_5` | Adx+di 20\|5 | `ADX+DI_20\|5` | round |
| `ADX_PLUS_DI_20_60` | Adx+di 20\|60 | `ADX+DI_20\|60` | round |
| `ADX_PLUS_DI_240` | Adx+di\|240 | `ADX+DI\|240` | round |
| `ADX_PLUS_DI_30` | Adx+di\|30 | `ADX+DI\|30` | round |
| `ADX_PLUS_DI_5` | Adx+di\|5 | `ADX+DI\|5` | round |
| `ADX_PLUS_DI_50` | Adx+di 50 | `ADX+DI_50` | round |
| `ADX_PLUS_DI_50_1` | Adx+di 50\|1 | `ADX+DI_50\|1` | round |
| `ADX_PLUS_DI_50_120` | Adx+di 50\|120 | `ADX+DI_50\|120` | round |
| `ADX_PLUS_DI_50_15` | Adx+di 50\|15 | `ADX+DI_50\|15` | round |
| `ADX_PLUS_DI_50_1M` | Adx+di 50\|1m | `ADX+DI_50\|1M` | round |
| `ADX_PLUS_DI_50_1W` | Adx+di 50\|1w | `ADX+DI_50\|1W` | round |
| `ADX_PLUS_DI_50_1_1` | Adx+di 50[1]\|1 | `ADX+DI_50[1]\|1` | round |
| `ADX_PLUS_DI_50_1_120` | Adx+di 50[1]\|120 | `ADX+DI_50[1]\|120` | round |
| `ADX_PLUS_DI_50_1_15` | Adx+di 50[1]\|15 | `ADX+DI_50[1]\|15` | round |
| `ADX_PLUS_DI_50_1_1M` | Adx+di 50[1]\|1m | `ADX+DI_50[1]\|1M` | round |
| `ADX_PLUS_DI_50_1_1W` | Adx+di 50[1]\|1w | `ADX+DI_50[1]\|1W` | round |
| `ADX_PLUS_DI_50_1_2` | Adx+di 50[1] | `ADX+DI_50[1]` | round |
| `ADX_PLUS_DI_50_1_240` | Adx+di 50[1]\|240 | `ADX+DI_50[1]\|240` | round |
| `ADX_PLUS_DI_50_1_30` | Adx+di 50[1]\|30 | `ADX+DI_50[1]\|30` | round |
| `ADX_PLUS_DI_50_1_5` | Adx+di 50[1]\|5 | `ADX+DI_50[1]\|5` | round |
| `ADX_PLUS_DI_50_1_60` | Adx+di 50[1]\|60 | `ADX+DI_50[1]\|60` | round |
| `ADX_PLUS_DI_50_240` | Adx+di 50\|240 | `ADX+DI_50\|240` | round |
| `ADX_PLUS_DI_50_30` | Adx+di 50\|30 | `ADX+DI_50\|30` | round |
| `ADX_PLUS_DI_50_5` | Adx+di 50\|5 | `ADX+DI_50\|5` | round |
| `ADX_PLUS_DI_50_60` | Adx+di 50\|60 | `ADX+DI_50\|60` | round |
| `ADX_PLUS_DI_60` | Adx+di\|60 | `ADX+DI\|60` | round |
| `ADX_PLUS_DI_9` | Adx+di 9 | `ADX+DI_9` | round |
| `ADX_PLUS_DI_9_1` | Adx+di 9[1] | `ADX+DI_9[1]` | round |
| `ADX_PLUS_DI_9_120` | Adx+di 9\|120 | `ADX+DI_9\|120` | round |
| `ADX_PLUS_DI_9_15` | Adx+di 9\|15 | `ADX+DI_9\|15` | round |
| `ADX_PLUS_DI_9_1M` | Adx+di 9\|1m | `ADX+DI_9\|1M` | round |
| `ADX_PLUS_DI_9_1W` | Adx+di 9\|1w | `ADX+DI_9\|1W` | round |
| `ADX_PLUS_DI_9_1_1` | Adx+di 9[1]\|1 | `ADX+DI_9[1]\|1` | round |
| `ADX_PLUS_DI_9_1_120` | Adx+di 9[1]\|120 | `ADX+DI_9[1]\|120` | round |
| `ADX_PLUS_DI_9_1_15` | Adx+di 9[1]\|15 | `ADX+DI_9[1]\|15` | round |
| `ADX_PLUS_DI_9_1_1M` | Adx+di 9[1]\|1m | `ADX+DI_9[1]\|1M` | round |
| `ADX_PLUS_DI_9_1_1W` | Adx+di 9[1]\|1w | `ADX+DI_9[1]\|1W` | round |
| `ADX_PLUS_DI_9_1_2` | Adx+di 9\|1 | `ADX+DI_9\|1` | round |
| `ADX_PLUS_DI_9_1_240` | Adx+di 9[1]\|240 | `ADX+DI_9[1]\|240` | round |
| `ADX_PLUS_DI_9_1_30` | Adx+di 9[1]\|30 | `ADX+DI_9[1]\|30` | round |
| `ADX_PLUS_DI_9_1_5` | Adx+di 9[1]\|5 | `ADX+DI_9[1]\|5` | round |
| `ADX_PLUS_DI_9_1_60` | Adx+di 9[1]\|60 | `ADX+DI_9[1]\|60` | round |
| `ADX_PLUS_DI_9_240` | Adx+di 9\|240 | `ADX+DI_9\|240` | round |
| `ADX_PLUS_DI_9_30` | Adx+di 9\|30 | `ADX+DI_9\|30` | round |
| `ADX_PLUS_DI_9_5` | Adx+di 9\|5 | `ADX+DI_9\|5` | round |
| `ADX_PLUS_DI_9_60` | Adx+di 9\|60 | `ADX+DI_9\|60` | round |
| `AROON_DOWN_1` | Aroon Down\|1 | `Aroon.Down\|1` | round |
| `AROON_DOWN_120` | Aroon Down\|120 | `Aroon.Down\|120` | round |
| `AROON_DOWN_14` | Aroon Down (14) | `Aroon.Down` | round |
| `AROON_DOWN_15` | Aroon Down\|15 | `Aroon.Down\|15` | round |
| `AROON_DOWN_1M` | Aroon Down\|1m | `Aroon.Down\|1M` | round |
| `AROON_DOWN_1W` | Aroon Down\|1w | `Aroon.Down\|1W` | round |
| `AROON_DOWN_240` | Aroon Down\|240 | `Aroon.Down\|240` | round |
| `AROON_DOWN_30` | Aroon Down\|30 | `Aroon.Down\|30` | round |
| `AROON_DOWN_5` | Aroon Down\|5 | `Aroon.Down\|5` | round |
| `AROON_DOWN_60` | Aroon Down\|60 | `Aroon.Down\|60` | round |
| `AROON_UP_1` | Aroon Up\|1 | `Aroon.Up\|1` | round |
| `AROON_UP_120` | Aroon Up\|120 | `Aroon.Up\|120` | round |
| `AROON_UP_14` | Aroon Up (14) | `Aroon.Up` | round |
| `AROON_UP_15` | Aroon Up\|15 | `Aroon.Up\|15` | round |
| `AROON_UP_1M` | Aroon Up\|1m | `Aroon.Up\|1M` | round |
| `AROON_UP_1W` | Aroon Up\|1w | `Aroon.Up\|1W` | round |
| `AROON_UP_240` | Aroon Up\|240 | `Aroon.Up\|240` | round |
| `AROON_UP_30` | Aroon Up\|30 | `Aroon.Up\|30` | round |
| `AROON_UP_5` | Aroon Up\|5 | `Aroon.Up\|5` | round |
| `AROON_UP_60` | Aroon Up\|60 | `Aroon.Up\|60` | round |
| `AVERAGE_DIRECTIONAL_INDEX_14` | Average Directional Index (14) | `ADX` | computed_recommendation |
| `ICHIMOKU_BASE_LINE_9_26_52_26` | Ichimoku Base Line (9, 26, 52, 26) | `Ichimoku.BLine` | computed_recommendation |
| `ICHIMOKU_BLINE_1` | Ichimoku Bline\|1 | `Ichimoku.BLine\|1` | round |
| `ICHIMOKU_BLINE_120` | Ichimoku Bline\|120 | `Ichimoku.BLine\|120` | round |
| `ICHIMOKU_BLINE_15` | Ichimoku Bline\|15 | `Ichimoku.BLine\|15` | round |
| `ICHIMOKU_BLINE_1M` | Ichimoku Bline\|1m | `Ichimoku.BLine\|1M` | round |
| `ICHIMOKU_BLINE_1W` | Ichimoku Bline\|1w | `Ichimoku.BLine\|1W` | round |
| `ICHIMOKU_BLINE_20_60_120_30` | Ichimoku Bline 20 60 120 30 | `Ichimoku.BLine_20_60_120_30` | round |
| `ICHIMOKU_BLINE_20_60_120_30_1` | Ichimoku Bline 20 60 120 30\|1 | `Ichimoku.BLine_20_60_120_30\|1` | round |
| `ICHIMOKU_BLINE_20_60_120_30_120` | Ichimoku Bline 20 60 120 30\|120 | `Ichimoku.BLine_20_60_120_30\|120` | round |
| `ICHIMOKU_BLINE_20_60_120_30_15` | Ichimoku Bline 20 60 120 30\|15 | `Ichimoku.BLine_20_60_120_30\|15` | round |
| `ICHIMOKU_BLINE_20_60_120_30_1M` | Ichimoku Bline 20 60 120 30\|1m | `Ichimoku.BLine_20_60_120_30\|1M` | round |
| `ICHIMOKU_BLINE_20_60_120_30_1W` | Ichimoku Bline 20 60 120 30\|1w | `Ichimoku.BLine_20_60_120_30\|1W` | round |
| `ICHIMOKU_BLINE_20_60_120_30_240` | Ichimoku Bline 20 60 120 30\|240 | `Ichimoku.BLine_20_60_120_30\|240` | round |
| `ICHIMOKU_BLINE_20_60_120_30_30` | Ichimoku Bline 20 60 120 30\|30 | `Ichimoku.BLine_20_60_120_30\|30` | round |
| `ICHIMOKU_BLINE_20_60_120_30_5` | Ichimoku Bline 20 60 120 30\|5 | `Ichimoku.BLine_20_60_120_30\|5` | round |
| `ICHIMOKU_BLINE_20_60_120_30_60` | Ichimoku Bline 20 60 120 30\|60 | `Ichimoku.BLine_20_60_120_30\|60` | round |
| `ICHIMOKU_BLINE_240` | Ichimoku Bline\|240 | `Ichimoku.BLine\|240` | round |
| `ICHIMOKU_BLINE_30` | Ichimoku Bline\|30 | `Ichimoku.BLine\|30` | round |
| `ICHIMOKU_BLINE_5` | Ichimoku Bline\|5 | `Ichimoku.BLine\|5` | round |
| `ICHIMOKU_BLINE_60` | Ichimoku Bline\|60 | `Ichimoku.BLine\|60` | round |
| `ICHIMOKU_CLINE_1` | Ichimoku Cline\|1 | `Ichimoku.CLine\|1` | round |
| `ICHIMOKU_CLINE_120` | Ichimoku Cline\|120 | `Ichimoku.CLine\|120` | round |
| `ICHIMOKU_CLINE_15` | Ichimoku Cline\|15 | `Ichimoku.CLine\|15` | round |
| `ICHIMOKU_CLINE_1M` | Ichimoku Cline\|1m | `Ichimoku.CLine\|1M` | round |
| `ICHIMOKU_CLINE_1W` | Ichimoku Cline\|1w | `Ichimoku.CLine\|1W` | round |
| `ICHIMOKU_CLINE_20_60_120_30` | Ichimoku Cline 20 60 120 30 | `Ichimoku.CLine_20_60_120_30` | round |
| `ICHIMOKU_CLINE_20_60_120_30_1` | Ichimoku Cline 20 60 120 30\|1 | `Ichimoku.CLine_20_60_120_30\|1` | round |
| `ICHIMOKU_CLINE_20_60_120_30_120` | Ichimoku Cline 20 60 120 30\|120 | `Ichimoku.CLine_20_60_120_30\|120` | round |
| `ICHIMOKU_CLINE_20_60_120_30_15` | Ichimoku Cline 20 60 120 30\|15 | `Ichimoku.CLine_20_60_120_30\|15` | round |
| `ICHIMOKU_CLINE_20_60_120_30_1M` | Ichimoku Cline 20 60 120 30\|1m | `Ichimoku.CLine_20_60_120_30\|1M` | round |
| `ICHIMOKU_CLINE_20_60_120_30_1W` | Ichimoku Cline 20 60 120 30\|1w | `Ichimoku.CLine_20_60_120_30\|1W` | round |
| `ICHIMOKU_CLINE_20_60_120_30_240` | Ichimoku Cline 20 60 120 30\|240 | `Ichimoku.CLine_20_60_120_30\|240` | round |
| `ICHIMOKU_CLINE_20_60_120_30_30` | Ichimoku Cline 20 60 120 30\|30 | `Ichimoku.CLine_20_60_120_30\|30` | round |
| `ICHIMOKU_CLINE_20_60_120_30_5` | Ichimoku Cline 20 60 120 30\|5 | `Ichimoku.CLine_20_60_120_30\|5` | round |
| `ICHIMOKU_CLINE_20_60_120_30_60` | Ichimoku Cline 20 60 120 30\|60 | `Ichimoku.CLine_20_60_120_30\|60` | round |
| `ICHIMOKU_CLINE_240` | Ichimoku Cline\|240 | `Ichimoku.CLine\|240` | round |
| `ICHIMOKU_CLINE_30` | Ichimoku Cline\|30 | `Ichimoku.CLine\|30` | round |
| `ICHIMOKU_CLINE_5` | Ichimoku Cline\|5 | `Ichimoku.CLine\|5` | round |
| `ICHIMOKU_CLINE_60` | Ichimoku Cline\|60 | `Ichimoku.CLine\|60` | round |
| `ICHIMOKU_CONVERSION_LINE_9_26_52_26` | Ichimoku Conversion Line (9, 26, 52, 26) | `Ichimoku.CLine` | round |
| `ICHIMOKU_LEAD1_1` | Ichimoku Lead1\|1 | `Ichimoku.Lead1\|1` | round |
| `ICHIMOKU_LEAD1_120` | Ichimoku Lead1\|120 | `Ichimoku.Lead1\|120` | round |
| `ICHIMOKU_LEAD1_15` | Ichimoku Lead1\|15 | `Ichimoku.Lead1\|15` | round |
| `ICHIMOKU_LEAD1_1M` | Ichimoku Lead1\|1m | `Ichimoku.Lead1\|1M` | round |
| `ICHIMOKU_LEAD1_1W` | Ichimoku Lead1\|1w | `Ichimoku.Lead1\|1W` | round |
| `ICHIMOKU_LEAD1_20_60_120_30` | Ichimoku Lead1 20 60 120 30 | `Ichimoku.Lead1_20_60_120_30` | round |
| `ICHIMOKU_LEAD1_20_60_120_30_1` | Ichimoku Lead1 20 60 120 30\|1 | `Ichimoku.Lead1_20_60_120_30\|1` | round |
| `ICHIMOKU_LEAD1_20_60_120_30_120` | Ichimoku Lead1 20 60 120 30\|120 | `Ichimoku.Lead1_20_60_120_30\|120` | round |
| `ICHIMOKU_LEAD1_20_60_120_30_15` | Ichimoku Lead1 20 60 120 30\|15 | `Ichimoku.Lead1_20_60_120_30\|15` | round |
| `ICHIMOKU_LEAD1_20_60_120_30_1M` | Ichimoku Lead1 20 60 120 30\|1m | `Ichimoku.Lead1_20_60_120_30\|1M` | round |
| `ICHIMOKU_LEAD1_20_60_120_30_1W` | Ichimoku Lead1 20 60 120 30\|1w | `Ichimoku.Lead1_20_60_120_30\|1W` | round |
| `ICHIMOKU_LEAD1_20_60_120_30_240` | Ichimoku Lead1 20 60 120 30\|240 | `Ichimoku.Lead1_20_60_120_30\|240` | round |
| `ICHIMOKU_LEAD1_20_60_120_30_30` | Ichimoku Lead1 20 60 120 30\|30 | `Ichimoku.Lead1_20_60_120_30\|30` | round |
| `ICHIMOKU_LEAD1_20_60_120_30_5` | Ichimoku Lead1 20 60 120 30\|5 | `Ichimoku.Lead1_20_60_120_30\|5` | round |
| `ICHIMOKU_LEAD1_20_60_120_30_60` | Ichimoku Lead1 20 60 120 30\|60 | `Ichimoku.Lead1_20_60_120_30\|60` | round |
| `ICHIMOKU_LEAD1_240` | Ichimoku Lead1\|240 | `Ichimoku.Lead1\|240` | round |
| `ICHIMOKU_LEAD1_30` | Ichimoku Lead1\|30 | `Ichimoku.Lead1\|30` | round |
| `ICHIMOKU_LEAD1_5` | Ichimoku Lead1\|5 | `Ichimoku.Lead1\|5` | round |
| `ICHIMOKU_LEAD1_60` | Ichimoku Lead1\|60 | `Ichimoku.Lead1\|60` | round |
| `ICHIMOKU_LEAD2_1` | Ichimoku Lead2\|1 | `Ichimoku.Lead2\|1` | round |
| `ICHIMOKU_LEAD2_120` | Ichimoku Lead2\|120 | `Ichimoku.Lead2\|120` | round |
| `ICHIMOKU_LEAD2_15` | Ichimoku Lead2\|15 | `Ichimoku.Lead2\|15` | round |
| `ICHIMOKU_LEAD2_1M` | Ichimoku Lead2\|1m | `Ichimoku.Lead2\|1M` | round |
| `ICHIMOKU_LEAD2_1W` | Ichimoku Lead2\|1w | `Ichimoku.Lead2\|1W` | round |
| `ICHIMOKU_LEAD2_20_60_120_30` | Ichimoku Lead2 20 60 120 30 | `Ichimoku.Lead2_20_60_120_30` | round |
| `ICHIMOKU_LEAD2_20_60_120_30_1` | Ichimoku Lead2 20 60 120 30\|1 | `Ichimoku.Lead2_20_60_120_30\|1` | round |
| `ICHIMOKU_LEAD2_20_60_120_30_120` | Ichimoku Lead2 20 60 120 30\|120 | `Ichimoku.Lead2_20_60_120_30\|120` | round |
| `ICHIMOKU_LEAD2_20_60_120_30_15` | Ichimoku Lead2 20 60 120 30\|15 | `Ichimoku.Lead2_20_60_120_30\|15` | round |
| `ICHIMOKU_LEAD2_20_60_120_30_1M` | Ichimoku Lead2 20 60 120 30\|1m | `Ichimoku.Lead2_20_60_120_30\|1M` | round |
| `ICHIMOKU_LEAD2_20_60_120_30_1W` | Ichimoku Lead2 20 60 120 30\|1w | `Ichimoku.Lead2_20_60_120_30\|1W` | round |
| `ICHIMOKU_LEAD2_20_60_120_30_240` | Ichimoku Lead2 20 60 120 30\|240 | `Ichimoku.Lead2_20_60_120_30\|240` | round |
| `ICHIMOKU_LEAD2_20_60_120_30_30` | Ichimoku Lead2 20 60 120 30\|30 | `Ichimoku.Lead2_20_60_120_30\|30` | round |
| `ICHIMOKU_LEAD2_20_60_120_30_5` | Ichimoku Lead2 20 60 120 30\|5 | `Ichimoku.Lead2_20_60_120_30\|5` | round |
| `ICHIMOKU_LEAD2_20_60_120_30_60` | Ichimoku Lead2 20 60 120 30\|60 | `Ichimoku.Lead2_20_60_120_30\|60` | round |
| `ICHIMOKU_LEAD2_240` | Ichimoku Lead2\|240 | `Ichimoku.Lead2\|240` | round |
| `ICHIMOKU_LEAD2_30` | Ichimoku Lead2\|30 | `Ichimoku.Lead2\|30` | round |
| `ICHIMOKU_LEAD2_5` | Ichimoku Lead2\|5 | `Ichimoku.Lead2\|5` | round |
| `ICHIMOKU_LEAD2_60` | Ichimoku Lead2\|60 | `Ichimoku.Lead2\|60` | round |
| `ICHIMOKU_LEADING_SPAN_A_9_26_52_26` | Ichimoku Leading Span A (9, 26, 52, 26) | `Ichimoku.Lead1` | float |
| `ICHIMOKU_LEADING_SPAN_B_9_26_52_26` | Ichimoku Leading Span B (9, 26, 52, 26) | `Ichimoku.Lead2` | float |
| `MACD_HIST` | MACD Hist | `MACD.hist` | round |
| `MACD_HIST_1` | MACD Hist\|1 | `MACD.hist\|1` | round |
| `MACD_HIST_120` | MACD Hist\|120 | `MACD.hist\|120` | round |
| `MACD_HIST_15` | MACD Hist\|15 | `MACD.hist\|15` | round |
| `MACD_HIST_1M` | MACD Hist\|1m | `MACD.hist\|1M` | round |
| `MACD_HIST_1W` | MACD Hist\|1w | `MACD.hist\|1W` | round |
| `MACD_HIST_240` | MACD Hist\|240 | `MACD.hist\|240` | round |
| `MACD_HIST_30` | MACD Hist\|30 | `MACD.hist\|30` | round |
| `MACD_HIST_5` | MACD Hist\|5 | `MACD.hist\|5` | round |
| `MACD_HIST_60` | MACD Hist\|60 | `MACD.hist\|60` | round |
| `MACD_LEVEL_12_26` | MACD Level (12, 26) | `MACD.macd` | computed_recommendation |
| `MACD_MACD_1` | MACD Macd\|1 | `MACD.macd\|1` | round |
| `MACD_MACD_120` | MACD Macd\|120 | `MACD.macd\|120` | round |
| `MACD_MACD_15` | MACD Macd\|15 | `MACD.macd\|15` | round |
| `MACD_MACD_1M` | MACD Macd\|1m | `MACD.macd\|1M` | round |
| `MACD_MACD_1W` | MACD Macd\|1w | `MACD.macd\|1W` | round |
| `MACD_MACD_240` | MACD Macd\|240 | `MACD.macd\|240` | round |
| `MACD_MACD_30` | MACD Macd\|30 | `MACD.macd\|30` | round |
| `MACD_MACD_5` | MACD Macd\|5 | `MACD.macd\|5` | round |
| `MACD_MACD_60` | MACD Macd\|60 | `MACD.macd\|60` | round |
| `MACD_SIGNAL_1` | MACD Signal\|1 | `MACD.signal\|1` | round |
| `MACD_SIGNAL_120` | MACD Signal\|120 | `MACD.signal\|120` | round |
| `MACD_SIGNAL_12_26` | MACD Signal (12, 26) | `MACD.signal` | float |
| `MACD_SIGNAL_15` | MACD Signal\|15 | `MACD.signal\|15` | round |
| `MACD_SIGNAL_1M` | MACD Signal\|1m | `MACD.signal\|1M` | round |
| `MACD_SIGNAL_1W` | MACD Signal\|1w | `MACD.signal\|1W` | round |
| `MACD_SIGNAL_240` | MACD Signal\|240 | `MACD.signal\|240` | round |
| `MACD_SIGNAL_30` | MACD Signal\|30 | `MACD.signal\|30` | round |
| `MACD_SIGNAL_5` | MACD Signal\|5 | `MACD.signal\|5` | round |
| `MACD_SIGNAL_60` | MACD Signal\|60 | `MACD.signal\|60` | round |
| `NEGATIVE_DIRECTIONAL_INDICATOR_14` | Negative Directional Indicator (14) | `ADX-DI` | round |
| `PARABOLIC_SAR` | Parabolic SAR | `P.SAR` | computed_recommendation |
| `POSITIVE_DIRECTIONAL_INDICATOR_14` | Positive Directional Indicator (14) | `ADX+DI` | round |
| `P_SAR_1` | P Sar\|1 | `P.SAR\|1` | round |
| `P_SAR_120` | P Sar\|120 | `P.SAR\|120` | round |
| `P_SAR_15` | P Sar\|15 | `P.SAR\|15` | round |
| `P_SAR_1M` | P Sar\|1m | `P.SAR\|1M` | round |
| `P_SAR_1W` | P Sar\|1w | `P.SAR\|1W` | round |
| `P_SAR_240` | P Sar\|240 | `P.SAR\|240` | round |
| `P_SAR_30` | P Sar\|30 | `P.SAR\|30` | round |
| `P_SAR_5` | P Sar\|5 | `P.SAR\|5` | round |
| `P_SAR_60` | P Sar\|60 | `P.SAR\|60` | round |
| `REC_ICHIMOKU` | Rec Ichimoku | `Rec.Ichimoku` | round |
| `REC_ICHIMOKU_1` | Rec Ichimoku\|1 | `Rec.Ichimoku\|1` | round |
| `REC_ICHIMOKU_120` | Rec Ichimoku\|120 | `Rec.Ichimoku\|120` | round |
| `REC_ICHIMOKU_15` | Rec Ichimoku\|15 | `Rec.Ichimoku\|15` | round |
| `REC_ICHIMOKU_1M` | Rec Ichimoku\|1m | `Rec.Ichimoku\|1M` | round |
| `REC_ICHIMOKU_1W` | Rec Ichimoku\|1w | `Rec.Ichimoku\|1W` | round |
| `REC_ICHIMOKU_240` | Rec Ichimoku\|240 | `Rec.Ichimoku\|240` | round |
| `REC_ICHIMOKU_30` | Rec Ichimoku\|30 | `Rec.Ichimoku\|30` | round |
| `REC_ICHIMOKU_5` | Rec Ichimoku\|5 | `Rec.Ichimoku\|5` | round |
| `REC_ICHIMOKU_60` | Rec Ichimoku\|60 | `Rec.Ichimoku\|60` | round |

## Volatility Indicators

*143 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `ATRP` | Average True Range % (14) | `ATRP` | percent |
| `ATRP_1` | Atrp\|1 | `ATRP\|1` | round |
| `ATRP_120` | Atrp\|120 | `ATRP\|120` | round |
| `ATRP_15` | Atrp\|15 | `ATRP\|15` | round |
| `ATRP_1M` | Atrp\|1m | `ATRP\|1M` | round |
| `ATRP_1W` | Atrp\|1w | `ATRP\|1W` | round |
| `ATRP_240` | Atrp\|240 | `ATRP\|240` | round |
| `ATRP_30` | Atrp\|30 | `ATRP\|30` | round |
| `ATRP_5` | Atrp\|5 | `ATRP\|5` | round |
| `ATRP_60` | Atrp\|60 | `ATRP\|60` | round |
| `ATR_1` | Atr\|1 | `ATR\|1` | round |
| `ATR_120` | Atr\|120 | `ATR\|120` | round |
| `ATR_15` | Atr\|15 | `ATR\|15` | round |
| `ATR_1M` | Atr\|1m | `ATR\|1M` | round |
| `ATR_1W` | Atr\|1w | `ATR\|1W` | round |
| `ATR_240` | Atr\|240 | `ATR\|240` | round |
| `ATR_30` | Atr\|30 | `ATR\|30` | round |
| `ATR_5` | Atr\|5 | `ATR\|5` | round |
| `ATR_60` | Atr\|60 | `ATR\|60` | round |
| `AVERAGE_TRUE_RANGE_14` | Average True Range (14) | `ATR` | float |
| `BB_BASIS` | BB Basis | `BB.basis` | round |
| `BB_BASIS_1` | BB Basis\|1 | `BB.basis\|1` | round |
| `BB_BASIS_120` | BB Basis\|120 | `BB.basis\|120` | round |
| `BB_BASIS_15` | BB Basis\|15 | `BB.basis\|15` | round |
| `BB_BASIS_1M` | BB Basis\|1m | `BB.basis\|1M` | round |
| `BB_BASIS_1W` | BB Basis\|1w | `BB.basis\|1W` | round |
| `BB_BASIS_240` | BB Basis\|240 | `BB.basis\|240` | round |
| `BB_BASIS_30` | BB Basis\|30 | `BB.basis\|30` | round |
| `BB_BASIS_5` | BB Basis\|5 | `BB.basis\|5` | round |
| `BB_BASIS_50` | BB Basis 50 | `BB.basis_50` | round |
| `BB_BASIS_50_1` | BB Basis 50\|1 | `BB.basis_50\|1` | round |
| `BB_BASIS_50_120` | BB Basis 50\|120 | `BB.basis_50\|120` | round |
| `BB_BASIS_50_15` | BB Basis 50\|15 | `BB.basis_50\|15` | round |
| `BB_BASIS_50_1M` | BB Basis 50\|1m | `BB.basis_50\|1M` | round |
| `BB_BASIS_50_1W` | BB Basis 50\|1w | `BB.basis_50\|1W` | round |
| `BB_BASIS_50_240` | BB Basis 50\|240 | `BB.basis_50\|240` | round |
| `BB_BASIS_50_30` | BB Basis 50\|30 | `BB.basis_50\|30` | round |
| `BB_BASIS_50_5` | BB Basis 50\|5 | `BB.basis_50\|5` | round |
| `BB_BASIS_50_60` | BB Basis 50\|60 | `BB.basis_50\|60` | round |
| `BB_BASIS_60` | BB Basis\|60 | `BB.basis\|60` | round |
| `BB_LOWER_1` | BB Lower\|1 | `BB.lower\|1` | round |
| `BB_LOWER_120` | BB Lower\|120 | `BB.lower\|120` | round |
| `BB_LOWER_15` | BB Lower\|15 | `BB.lower\|15` | round |
| `BB_LOWER_1M` | BB Lower\|1m | `BB.lower\|1M` | round |
| `BB_LOWER_1W` | BB Lower\|1w | `BB.lower\|1W` | round |
| `BB_LOWER_240` | BB Lower\|240 | `BB.lower\|240` | round |
| `BB_LOWER_30` | BB Lower\|30 | `BB.lower\|30` | round |
| `BB_LOWER_5` | BB Lower\|5 | `BB.lower\|5` | round |
| `BB_LOWER_50` | BB Lower 50 | `BB.lower_50` | round |
| `BB_LOWER_50_1` | BB Lower 50\|1 | `BB.lower_50\|1` | round |
| `BB_LOWER_50_120` | BB Lower 50\|120 | `BB.lower_50\|120` | round |
| `BB_LOWER_50_15` | BB Lower 50\|15 | `BB.lower_50\|15` | round |
| `BB_LOWER_50_1M` | BB Lower 50\|1m | `BB.lower_50\|1M` | round |
| `BB_LOWER_50_1W` | BB Lower 50\|1w | `BB.lower_50\|1W` | round |
| `BB_LOWER_50_240` | BB Lower 50\|240 | `BB.lower_50\|240` | round |
| `BB_LOWER_50_30` | BB Lower 50\|30 | `BB.lower_50\|30` | round |
| `BB_LOWER_50_5` | BB Lower 50\|5 | `BB.lower_50\|5` | round |
| `BB_LOWER_50_60` | BB Lower 50\|60 | `BB.lower_50\|60` | round |
| `BB_LOWER_60` | BB Lower\|60 | `BB.lower\|60` | round |
| `BB_UPPER_1` | BB Upper\|1 | `BB.upper\|1` | round |
| `BB_UPPER_120` | BB Upper\|120 | `BB.upper\|120` | round |
| `BB_UPPER_15` | BB Upper\|15 | `BB.upper\|15` | round |
| `BB_UPPER_1M` | BB Upper\|1m | `BB.upper\|1M` | round |
| `BB_UPPER_1W` | BB Upper\|1w | `BB.upper\|1W` | round |
| `BB_UPPER_240` | BB Upper\|240 | `BB.upper\|240` | round |
| `BB_UPPER_30` | BB Upper\|30 | `BB.upper\|30` | round |
| `BB_UPPER_5` | BB Upper\|5 | `BB.upper\|5` | round |
| `BB_UPPER_50` | BB Upper 50 | `BB.upper_50` | round |
| `BB_UPPER_50_1` | BB Upper 50\|1 | `BB.upper_50\|1` | round |
| `BB_UPPER_50_120` | BB Upper 50\|120 | `BB.upper_50\|120` | round |
| `BB_UPPER_50_15` | BB Upper 50\|15 | `BB.upper_50\|15` | round |
| `BB_UPPER_50_1M` | BB Upper 50\|1m | `BB.upper_50\|1M` | round |
| `BB_UPPER_50_1W` | BB Upper 50\|1w | `BB.upper_50\|1W` | round |
| `BB_UPPER_50_240` | BB Upper 50\|240 | `BB.upper_50\|240` | round |
| `BB_UPPER_50_30` | BB Upper 50\|30 | `BB.upper_50\|30` | round |
| `BB_UPPER_50_5` | BB Upper 50\|5 | `BB.upper_50\|5` | round |
| `BB_UPPER_50_60` | BB Upper 50\|60 | `BB.upper_50\|60` | round |
| `BB_UPPER_60` | BB Upper\|60 | `BB.upper\|60` | round |
| `BOLLINGER_LOWER_BAND_20` | Bollinger Lower Band (20) | `BB.lower` | computed_recommendation |
| `BOLLINGER_UPPER_BAND_20` | Bollinger Upper Band (20) | `BB.upper` | computed_recommendation |
| `DONCHCH20_LOWER_1` | Donchch20 Lower\|1 | `DonchCh20.Lower\|1` | round |
| `DONCHCH20_LOWER_120` | Donchch20 Lower\|120 | `DonchCh20.Lower\|120` | round |
| `DONCHCH20_LOWER_15` | Donchch20 Lower\|15 | `DonchCh20.Lower\|15` | round |
| `DONCHCH20_LOWER_1M` | Donchch20 Lower\|1m | `DonchCh20.Lower\|1M` | round |
| `DONCHCH20_LOWER_1W` | Donchch20 Lower\|1w | `DonchCh20.Lower\|1W` | round |
| `DONCHCH20_LOWER_240` | Donchch20 Lower\|240 | `DonchCh20.Lower\|240` | round |
| `DONCHCH20_LOWER_30` | Donchch20 Lower\|30 | `DonchCh20.Lower\|30` | round |
| `DONCHCH20_LOWER_5` | Donchch20 Lower\|5 | `DonchCh20.Lower\|5` | round |
| `DONCHCH20_LOWER_60` | Donchch20 Lower\|60 | `DonchCh20.Lower\|60` | round |
| `DONCHCH20_MIDDLE` | Donchch20 Middle | `DonchCh20.Middle` | round |
| `DONCHCH20_MIDDLE_1` | Donchch20 Middle\|1 | `DonchCh20.Middle\|1` | round |
| `DONCHCH20_MIDDLE_120` | Donchch20 Middle\|120 | `DonchCh20.Middle\|120` | round |
| `DONCHCH20_MIDDLE_15` | Donchch20 Middle\|15 | `DonchCh20.Middle\|15` | round |
| `DONCHCH20_MIDDLE_1M` | Donchch20 Middle\|1m | `DonchCh20.Middle\|1M` | round |
| `DONCHCH20_MIDDLE_1W` | Donchch20 Middle\|1w | `DonchCh20.Middle\|1W` | round |
| `DONCHCH20_MIDDLE_240` | Donchch20 Middle\|240 | `DonchCh20.Middle\|240` | round |
| `DONCHCH20_MIDDLE_30` | Donchch20 Middle\|30 | `DonchCh20.Middle\|30` | round |
| `DONCHCH20_MIDDLE_5` | Donchch20 Middle\|5 | `DonchCh20.Middle\|5` | round |
| `DONCHCH20_MIDDLE_60` | Donchch20 Middle\|60 | `DonchCh20.Middle\|60` | round |
| `DONCHCH20_UPPER_1` | Donchch20 Upper\|1 | `DonchCh20.Upper\|1` | round |
| `DONCHCH20_UPPER_120` | Donchch20 Upper\|120 | `DonchCh20.Upper\|120` | round |
| `DONCHCH20_UPPER_15` | Donchch20 Upper\|15 | `DonchCh20.Upper\|15` | round |
| `DONCHCH20_UPPER_1M` | Donchch20 Upper\|1m | `DonchCh20.Upper\|1M` | round |
| `DONCHCH20_UPPER_1W` | Donchch20 Upper\|1w | `DonchCh20.Upper\|1W` | round |
| `DONCHCH20_UPPER_240` | Donchch20 Upper\|240 | `DonchCh20.Upper\|240` | round |
| `DONCHCH20_UPPER_30` | Donchch20 Upper\|30 | `DonchCh20.Upper\|30` | round |
| `DONCHCH20_UPPER_5` | Donchch20 Upper\|5 | `DonchCh20.Upper\|5` | round |
| `DONCHCH20_UPPER_60` | Donchch20 Upper\|60 | `DonchCh20.Upper\|60` | round |
| `DONCHIAN_CHANNELS_LOWER_BAND_20` | Donchian Channels Lower Band (20) | `DonchCh20.Lower` | round |
| `DONCHIAN_CHANNELS_UPPER_BAND_20` | Donchian Channels Upper Band (20) | `DonchCh20.Upper` | round |
| `KELTNER_CHANNELS_LOWER_BAND_20` | Keltner Channels Lower Band (20) | `KltChnl.lower` | float |
| `KELTNER_CHANNELS_UPPER_BAND_20` | Keltner Channels Upper Band (20) | `KltChnl.upper` | float |
| `KLTCHNL_BASIS` | Kltchnl Basis | `KltChnl.basis` | round |
| `KLTCHNL_BASIS_1` | Kltchnl Basis\|1 | `KltChnl.basis\|1` | round |
| `KLTCHNL_BASIS_120` | Kltchnl Basis\|120 | `KltChnl.basis\|120` | round |
| `KLTCHNL_BASIS_15` | Kltchnl Basis\|15 | `KltChnl.basis\|15` | round |
| `KLTCHNL_BASIS_1M` | Kltchnl Basis\|1m | `KltChnl.basis\|1M` | round |
| `KLTCHNL_BASIS_1W` | Kltchnl Basis\|1w | `KltChnl.basis\|1W` | round |
| `KLTCHNL_BASIS_240` | Kltchnl Basis\|240 | `KltChnl.basis\|240` | round |
| `KLTCHNL_BASIS_30` | Kltchnl Basis\|30 | `KltChnl.basis\|30` | round |
| `KLTCHNL_BASIS_5` | Kltchnl Basis\|5 | `KltChnl.basis\|5` | round |
| `KLTCHNL_BASIS_60` | Kltchnl Basis\|60 | `KltChnl.basis\|60` | round |
| `KLTCHNL_LOWER_1` | Kltchnl Lower\|1 | `KltChnl.lower\|1` | round |
| `KLTCHNL_LOWER_120` | Kltchnl Lower\|120 | `KltChnl.lower\|120` | round |
| `KLTCHNL_LOWER_15` | Kltchnl Lower\|15 | `KltChnl.lower\|15` | round |
| `KLTCHNL_LOWER_1M` | Kltchnl Lower\|1m | `KltChnl.lower\|1M` | round |
| `KLTCHNL_LOWER_1W` | Kltchnl Lower\|1w | `KltChnl.lower\|1W` | round |
| `KLTCHNL_LOWER_240` | Kltchnl Lower\|240 | `KltChnl.lower\|240` | round |
| `KLTCHNL_LOWER_30` | Kltchnl Lower\|30 | `KltChnl.lower\|30` | round |
| `KLTCHNL_LOWER_5` | Kltchnl Lower\|5 | `KltChnl.lower\|5` | round |
| `KLTCHNL_LOWER_60` | Kltchnl Lower\|60 | `KltChnl.lower\|60` | round |
| `KLTCHNL_UPPER_1` | Kltchnl Upper\|1 | `KltChnl.upper\|1` | round |
| `KLTCHNL_UPPER_120` | Kltchnl Upper\|120 | `KltChnl.upper\|120` | round |
| `KLTCHNL_UPPER_15` | Kltchnl Upper\|15 | `KltChnl.upper\|15` | round |
| `KLTCHNL_UPPER_1M` | Kltchnl Upper\|1m | `KltChnl.upper\|1M` | round |
| `KLTCHNL_UPPER_1W` | Kltchnl Upper\|1w | `KltChnl.upper\|1W` | round |
| `KLTCHNL_UPPER_240` | Kltchnl Upper\|240 | `KltChnl.upper\|240` | round |
| `KLTCHNL_UPPER_30` | Kltchnl Upper\|30 | `KltChnl.upper\|30` | round |
| `KLTCHNL_UPPER_5` | Kltchnl Upper\|5 | `KltChnl.upper\|5` | round |
| `KLTCHNL_UPPER_60` | Kltchnl Upper\|60 | `KltChnl.upper\|60` | round |
| `VOLATILITY` | Volatility | `Volatility.D` | percent |
| `VOLATILITY_MONTH` | Volatility Month | `Volatility.M` | percent |
| `VOLATILITY_WEEK` | Volatility Week | `Volatility.W` | percent |

## Pivot Points

*210 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `PIVOT_CAMARILLA_P` | Pivot Camarilla P | `Pivot.M.Camarilla.Middle` | round |
| `PIVOT_CAMARILLA_R1` | Pivot Camarilla R1 | `Pivot.M.Camarilla.R1` | round |
| `PIVOT_CAMARILLA_R2` | Pivot Camarilla R2 | `Pivot.M.Camarilla.R2` | round |
| `PIVOT_CAMARILLA_R3` | Pivot Camarilla R3 | `Pivot.M.Camarilla.R3` | round |
| `PIVOT_CAMARILLA_S1` | Pivot Camarilla S1 | `Pivot.M.Camarilla.S1` | round |
| `PIVOT_CAMARILLA_S2` | Pivot Camarilla S2 | `Pivot.M.Camarilla.S2` | round |
| `PIVOT_CAMARILLA_S3` | Pivot Camarilla S3 | `Pivot.M.Camarilla.S3` | round |
| `PIVOT_CLASSIC_P` | Pivot Classic P | `Pivot.M.Classic.Middle` | round |
| `PIVOT_CLASSIC_R1` | Pivot Classic R1 | `Pivot.M.Classic.R1` | round |
| `PIVOT_CLASSIC_R2` | Pivot Classic R2 | `Pivot.M.Classic.R2` | round |
| `PIVOT_CLASSIC_R3` | Pivot Classic R3 | `Pivot.M.Classic.R3` | round |
| `PIVOT_CLASSIC_S1` | Pivot Classic S1 | `Pivot.M.Classic.S1` | round |
| `PIVOT_CLASSIC_S2` | Pivot Classic S2 | `Pivot.M.Classic.S2` | round |
| `PIVOT_CLASSIC_S3` | Pivot Classic S3 | `Pivot.M.Classic.S3` | round |
| `PIVOT_M_CAMARILLA_MIDDLE_1` | Pivot M Camarilla Middle\|1 | `Pivot.M.Camarilla.Middle\|1` | round |
| `PIVOT_M_CAMARILLA_MIDDLE_120` | Pivot M Camarilla Middle\|120 | `Pivot.M.Camarilla.Middle\|120` | round |
| `PIVOT_M_CAMARILLA_MIDDLE_15` | Pivot M Camarilla Middle\|15 | `Pivot.M.Camarilla.Middle\|15` | round |
| `PIVOT_M_CAMARILLA_MIDDLE_1M` | Pivot M Camarilla Middle\|1m | `Pivot.M.Camarilla.Middle\|1M` | round |
| `PIVOT_M_CAMARILLA_MIDDLE_1W` | Pivot M Camarilla Middle\|1w | `Pivot.M.Camarilla.Middle\|1W` | round |
| `PIVOT_M_CAMARILLA_MIDDLE_240` | Pivot M Camarilla Middle\|240 | `Pivot.M.Camarilla.Middle\|240` | round |
| `PIVOT_M_CAMARILLA_MIDDLE_30` | Pivot M Camarilla Middle\|30 | `Pivot.M.Camarilla.Middle\|30` | round |
| `PIVOT_M_CAMARILLA_MIDDLE_5` | Pivot M Camarilla Middle\|5 | `Pivot.M.Camarilla.Middle\|5` | round |
| `PIVOT_M_CAMARILLA_MIDDLE_60` | Pivot M Camarilla Middle\|60 | `Pivot.M.Camarilla.Middle\|60` | round |
| `PIVOT_M_CAMARILLA_R1_1` | Pivot M Camarilla R1\|1 | `Pivot.M.Camarilla.R1\|1` | round |
| `PIVOT_M_CAMARILLA_R1_120` | Pivot M Camarilla R1\|120 | `Pivot.M.Camarilla.R1\|120` | round |
| `PIVOT_M_CAMARILLA_R1_15` | Pivot M Camarilla R1\|15 | `Pivot.M.Camarilla.R1\|15` | round |
| `PIVOT_M_CAMARILLA_R1_1M` | Pivot M Camarilla R1\|1m | `Pivot.M.Camarilla.R1\|1M` | round |
| `PIVOT_M_CAMARILLA_R1_1W` | Pivot M Camarilla R1\|1w | `Pivot.M.Camarilla.R1\|1W` | round |
| `PIVOT_M_CAMARILLA_R1_240` | Pivot M Camarilla R1\|240 | `Pivot.M.Camarilla.R1\|240` | round |
| `PIVOT_M_CAMARILLA_R1_30` | Pivot M Camarilla R1\|30 | `Pivot.M.Camarilla.R1\|30` | round |
| `PIVOT_M_CAMARILLA_R1_5` | Pivot M Camarilla R1\|5 | `Pivot.M.Camarilla.R1\|5` | round |
| `PIVOT_M_CAMARILLA_R1_60` | Pivot M Camarilla R1\|60 | `Pivot.M.Camarilla.R1\|60` | round |
| `PIVOT_M_CAMARILLA_R2_1` | Pivot M Camarilla R2\|1 | `Pivot.M.Camarilla.R2\|1` | round |
| `PIVOT_M_CAMARILLA_R2_120` | Pivot M Camarilla R2\|120 | `Pivot.M.Camarilla.R2\|120` | round |
| `PIVOT_M_CAMARILLA_R2_15` | Pivot M Camarilla R2\|15 | `Pivot.M.Camarilla.R2\|15` | round |
| `PIVOT_M_CAMARILLA_R2_1M` | Pivot M Camarilla R2\|1m | `Pivot.M.Camarilla.R2\|1M` | round |
| `PIVOT_M_CAMARILLA_R2_1W` | Pivot M Camarilla R2\|1w | `Pivot.M.Camarilla.R2\|1W` | round |
| `PIVOT_M_CAMARILLA_R2_240` | Pivot M Camarilla R2\|240 | `Pivot.M.Camarilla.R2\|240` | round |
| `PIVOT_M_CAMARILLA_R2_30` | Pivot M Camarilla R2\|30 | `Pivot.M.Camarilla.R2\|30` | round |
| `PIVOT_M_CAMARILLA_R2_5` | Pivot M Camarilla R2\|5 | `Pivot.M.Camarilla.R2\|5` | round |
| `PIVOT_M_CAMARILLA_R2_60` | Pivot M Camarilla R2\|60 | `Pivot.M.Camarilla.R2\|60` | round |
| `PIVOT_M_CAMARILLA_R3_1` | Pivot M Camarilla R3\|1 | `Pivot.M.Camarilla.R3\|1` | round |
| `PIVOT_M_CAMARILLA_R3_120` | Pivot M Camarilla R3\|120 | `Pivot.M.Camarilla.R3\|120` | round |
| `PIVOT_M_CAMARILLA_R3_15` | Pivot M Camarilla R3\|15 | `Pivot.M.Camarilla.R3\|15` | round |
| `PIVOT_M_CAMARILLA_R3_1M` | Pivot M Camarilla R3\|1m | `Pivot.M.Camarilla.R3\|1M` | round |
| `PIVOT_M_CAMARILLA_R3_1W` | Pivot M Camarilla R3\|1w | `Pivot.M.Camarilla.R3\|1W` | round |
| `PIVOT_M_CAMARILLA_R3_240` | Pivot M Camarilla R3\|240 | `Pivot.M.Camarilla.R3\|240` | round |
| `PIVOT_M_CAMARILLA_R3_30` | Pivot M Camarilla R3\|30 | `Pivot.M.Camarilla.R3\|30` | round |
| `PIVOT_M_CAMARILLA_R3_5` | Pivot M Camarilla R3\|5 | `Pivot.M.Camarilla.R3\|5` | round |
| `PIVOT_M_CAMARILLA_R3_60` | Pivot M Camarilla R3\|60 | `Pivot.M.Camarilla.R3\|60` | round |
| `PIVOT_M_CAMARILLA_S1_1` | Pivot M Camarilla S1\|1 | `Pivot.M.Camarilla.S1\|1` | round |
| `PIVOT_M_CAMARILLA_S1_120` | Pivot M Camarilla S1\|120 | `Pivot.M.Camarilla.S1\|120` | round |
| `PIVOT_M_CAMARILLA_S1_15` | Pivot M Camarilla S1\|15 | `Pivot.M.Camarilla.S1\|15` | round |
| `PIVOT_M_CAMARILLA_S1_1M` | Pivot M Camarilla S1\|1m | `Pivot.M.Camarilla.S1\|1M` | round |
| `PIVOT_M_CAMARILLA_S1_1W` | Pivot M Camarilla S1\|1w | `Pivot.M.Camarilla.S1\|1W` | round |
| `PIVOT_M_CAMARILLA_S1_240` | Pivot M Camarilla S1\|240 | `Pivot.M.Camarilla.S1\|240` | round |
| `PIVOT_M_CAMARILLA_S1_30` | Pivot M Camarilla S1\|30 | `Pivot.M.Camarilla.S1\|30` | round |
| `PIVOT_M_CAMARILLA_S1_5` | Pivot M Camarilla S1\|5 | `Pivot.M.Camarilla.S1\|5` | round |
| `PIVOT_M_CAMARILLA_S1_60` | Pivot M Camarilla S1\|60 | `Pivot.M.Camarilla.S1\|60` | round |
| `PIVOT_M_CAMARILLA_S2_1` | Pivot M Camarilla S2\|1 | `Pivot.M.Camarilla.S2\|1` | round |
| `PIVOT_M_CAMARILLA_S2_120` | Pivot M Camarilla S2\|120 | `Pivot.M.Camarilla.S2\|120` | round |
| `PIVOT_M_CAMARILLA_S2_15` | Pivot M Camarilla S2\|15 | `Pivot.M.Camarilla.S2\|15` | round |
| `PIVOT_M_CAMARILLA_S2_1M` | Pivot M Camarilla S2\|1m | `Pivot.M.Camarilla.S2\|1M` | round |
| `PIVOT_M_CAMARILLA_S2_1W` | Pivot M Camarilla S2\|1w | `Pivot.M.Camarilla.S2\|1W` | round |
| `PIVOT_M_CAMARILLA_S2_240` | Pivot M Camarilla S2\|240 | `Pivot.M.Camarilla.S2\|240` | round |
| `PIVOT_M_CAMARILLA_S2_30` | Pivot M Camarilla S2\|30 | `Pivot.M.Camarilla.S2\|30` | round |
| `PIVOT_M_CAMARILLA_S2_5` | Pivot M Camarilla S2\|5 | `Pivot.M.Camarilla.S2\|5` | round |
| `PIVOT_M_CAMARILLA_S2_60` | Pivot M Camarilla S2\|60 | `Pivot.M.Camarilla.S2\|60` | round |
| `PIVOT_M_CAMARILLA_S3_1` | Pivot M Camarilla S3\|1 | `Pivot.M.Camarilla.S3\|1` | round |
| `PIVOT_M_CAMARILLA_S3_120` | Pivot M Camarilla S3\|120 | `Pivot.M.Camarilla.S3\|120` | round |
| `PIVOT_M_CAMARILLA_S3_15` | Pivot M Camarilla S3\|15 | `Pivot.M.Camarilla.S3\|15` | round |
| `PIVOT_M_CAMARILLA_S3_1M` | Pivot M Camarilla S3\|1m | `Pivot.M.Camarilla.S3\|1M` | round |
| `PIVOT_M_CAMARILLA_S3_1W` | Pivot M Camarilla S3\|1w | `Pivot.M.Camarilla.S3\|1W` | round |
| `PIVOT_M_CAMARILLA_S3_240` | Pivot M Camarilla S3\|240 | `Pivot.M.Camarilla.S3\|240` | round |
| `PIVOT_M_CAMARILLA_S3_30` | Pivot M Camarilla S3\|30 | `Pivot.M.Camarilla.S3\|30` | round |
| `PIVOT_M_CAMARILLA_S3_5` | Pivot M Camarilla S3\|5 | `Pivot.M.Camarilla.S3\|5` | round |
| `PIVOT_M_CAMARILLA_S3_60` | Pivot M Camarilla S3\|60 | `Pivot.M.Camarilla.S3\|60` | round |
| `PIVOT_M_CLASSIC_MIDDLE_1` | Pivot M Classic Middle\|1 | `Pivot.M.Classic.Middle\|1` | round |
| `PIVOT_M_CLASSIC_MIDDLE_120` | Pivot M Classic Middle\|120 | `Pivot.M.Classic.Middle\|120` | round |
| `PIVOT_M_CLASSIC_MIDDLE_15` | Pivot M Classic Middle\|15 | `Pivot.M.Classic.Middle\|15` | round |
| `PIVOT_M_CLASSIC_MIDDLE_1M` | Pivot M Classic Middle\|1m | `Pivot.M.Classic.Middle\|1M` | round |
| `PIVOT_M_CLASSIC_MIDDLE_1W` | Pivot M Classic Middle\|1w | `Pivot.M.Classic.Middle\|1W` | round |
| `PIVOT_M_CLASSIC_MIDDLE_240` | Pivot M Classic Middle\|240 | `Pivot.M.Classic.Middle\|240` | round |
| `PIVOT_M_CLASSIC_MIDDLE_30` | Pivot M Classic Middle\|30 | `Pivot.M.Classic.Middle\|30` | round |
| `PIVOT_M_CLASSIC_MIDDLE_5` | Pivot M Classic Middle\|5 | `Pivot.M.Classic.Middle\|5` | round |
| `PIVOT_M_CLASSIC_MIDDLE_60` | Pivot M Classic Middle\|60 | `Pivot.M.Classic.Middle\|60` | round |
| `PIVOT_M_CLASSIC_R1_1` | Pivot M Classic R1\|1 | `Pivot.M.Classic.R1\|1` | round |
| `PIVOT_M_CLASSIC_R1_120` | Pivot M Classic R1\|120 | `Pivot.M.Classic.R1\|120` | round |
| `PIVOT_M_CLASSIC_R1_15` | Pivot M Classic R1\|15 | `Pivot.M.Classic.R1\|15` | round |
| `PIVOT_M_CLASSIC_R1_1M` | Pivot M Classic R1\|1m | `Pivot.M.Classic.R1\|1M` | round |
| `PIVOT_M_CLASSIC_R1_1W` | Pivot M Classic R1\|1w | `Pivot.M.Classic.R1\|1W` | round |
| `PIVOT_M_CLASSIC_R1_240` | Pivot M Classic R1\|240 | `Pivot.M.Classic.R1\|240` | round |
| `PIVOT_M_CLASSIC_R1_30` | Pivot M Classic R1\|30 | `Pivot.M.Classic.R1\|30` | round |
| `PIVOT_M_CLASSIC_R1_5` | Pivot M Classic R1\|5 | `Pivot.M.Classic.R1\|5` | round |
| `PIVOT_M_CLASSIC_R1_60` | Pivot M Classic R1\|60 | `Pivot.M.Classic.R1\|60` | round |
| `PIVOT_M_CLASSIC_R2_1` | Pivot M Classic R2\|1 | `Pivot.M.Classic.R2\|1` | round |
| `PIVOT_M_CLASSIC_R2_120` | Pivot M Classic R2\|120 | `Pivot.M.Classic.R2\|120` | round |
| `PIVOT_M_CLASSIC_R2_15` | Pivot M Classic R2\|15 | `Pivot.M.Classic.R2\|15` | round |
| `PIVOT_M_CLASSIC_R2_1M` | Pivot M Classic R2\|1m | `Pivot.M.Classic.R2\|1M` | round |
| `PIVOT_M_CLASSIC_R2_1W` | Pivot M Classic R2\|1w | `Pivot.M.Classic.R2\|1W` | round |
| `PIVOT_M_CLASSIC_R2_240` | Pivot M Classic R2\|240 | `Pivot.M.Classic.R2\|240` | round |
| `PIVOT_M_CLASSIC_R2_30` | Pivot M Classic R2\|30 | `Pivot.M.Classic.R2\|30` | round |
| `PIVOT_M_CLASSIC_R2_5` | Pivot M Classic R2\|5 | `Pivot.M.Classic.R2\|5` | round |
| `PIVOT_M_CLASSIC_R2_60` | Pivot M Classic R2\|60 | `Pivot.M.Classic.R2\|60` | round |
| `PIVOT_M_CLASSIC_R3_1` | Pivot M Classic R3\|1 | `Pivot.M.Classic.R3\|1` | round |
| `PIVOT_M_CLASSIC_R3_120` | Pivot M Classic R3\|120 | `Pivot.M.Classic.R3\|120` | round |
| `PIVOT_M_CLASSIC_R3_15` | Pivot M Classic R3\|15 | `Pivot.M.Classic.R3\|15` | round |
| `PIVOT_M_CLASSIC_R3_1M` | Pivot M Classic R3\|1m | `Pivot.M.Classic.R3\|1M` | round |
| `PIVOT_M_CLASSIC_R3_1W` | Pivot M Classic R3\|1w | `Pivot.M.Classic.R3\|1W` | round |
| `PIVOT_M_CLASSIC_R3_240` | Pivot M Classic R3\|240 | `Pivot.M.Classic.R3\|240` | round |
| `PIVOT_M_CLASSIC_R3_30` | Pivot M Classic R3\|30 | `Pivot.M.Classic.R3\|30` | round |
| `PIVOT_M_CLASSIC_R3_5` | Pivot M Classic R3\|5 | `Pivot.M.Classic.R3\|5` | round |
| `PIVOT_M_CLASSIC_R3_60` | Pivot M Classic R3\|60 | `Pivot.M.Classic.R3\|60` | round |
| `PIVOT_M_CLASSIC_S1_1` | Pivot M Classic S1\|1 | `Pivot.M.Classic.S1\|1` | round |
| `PIVOT_M_CLASSIC_S1_120` | Pivot M Classic S1\|120 | `Pivot.M.Classic.S1\|120` | round |
| `PIVOT_M_CLASSIC_S1_15` | Pivot M Classic S1\|15 | `Pivot.M.Classic.S1\|15` | round |
| `PIVOT_M_CLASSIC_S1_1M` | Pivot M Classic S1\|1m | `Pivot.M.Classic.S1\|1M` | round |
| `PIVOT_M_CLASSIC_S1_1W` | Pivot M Classic S1\|1w | `Pivot.M.Classic.S1\|1W` | round |
| `PIVOT_M_CLASSIC_S1_240` | Pivot M Classic S1\|240 | `Pivot.M.Classic.S1\|240` | round |
| `PIVOT_M_CLASSIC_S1_30` | Pivot M Classic S1\|30 | `Pivot.M.Classic.S1\|30` | round |
| `PIVOT_M_CLASSIC_S1_5` | Pivot M Classic S1\|5 | `Pivot.M.Classic.S1\|5` | round |
| `PIVOT_M_CLASSIC_S1_60` | Pivot M Classic S1\|60 | `Pivot.M.Classic.S1\|60` | round |
| `PIVOT_M_CLASSIC_S2_1` | Pivot M Classic S2\|1 | `Pivot.M.Classic.S2\|1` | round |
| `PIVOT_M_CLASSIC_S2_120` | Pivot M Classic S2\|120 | `Pivot.M.Classic.S2\|120` | round |
| `PIVOT_M_CLASSIC_S2_15` | Pivot M Classic S2\|15 | `Pivot.M.Classic.S2\|15` | round |
| `PIVOT_M_CLASSIC_S2_1M` | Pivot M Classic S2\|1m | `Pivot.M.Classic.S2\|1M` | round |
| `PIVOT_M_CLASSIC_S2_1W` | Pivot M Classic S2\|1w | `Pivot.M.Classic.S2\|1W` | round |
| `PIVOT_M_CLASSIC_S2_240` | Pivot M Classic S2\|240 | `Pivot.M.Classic.S2\|240` | round |
| `PIVOT_M_CLASSIC_S2_30` | Pivot M Classic S2\|30 | `Pivot.M.Classic.S2\|30` | round |
| `PIVOT_M_CLASSIC_S2_5` | Pivot M Classic S2\|5 | `Pivot.M.Classic.S2\|5` | round |
| `PIVOT_M_CLASSIC_S2_60` | Pivot M Classic S2\|60 | `Pivot.M.Classic.S2\|60` | round |
| `PIVOT_M_CLASSIC_S3_1` | Pivot M Classic S3\|1 | `Pivot.M.Classic.S3\|1` | round |
| `PIVOT_M_CLASSIC_S3_120` | Pivot M Classic S3\|120 | `Pivot.M.Classic.S3\|120` | round |
| `PIVOT_M_CLASSIC_S3_15` | Pivot M Classic S3\|15 | `Pivot.M.Classic.S3\|15` | round |
| `PIVOT_M_CLASSIC_S3_1M` | Pivot M Classic S3\|1m | `Pivot.M.Classic.S3\|1M` | round |
| `PIVOT_M_CLASSIC_S3_1W` | Pivot M Classic S3\|1w | `Pivot.M.Classic.S3\|1W` | round |
| `PIVOT_M_CLASSIC_S3_240` | Pivot M Classic S3\|240 | `Pivot.M.Classic.S3\|240` | round |
| `PIVOT_M_CLASSIC_S3_30` | Pivot M Classic S3\|30 | `Pivot.M.Classic.S3\|30` | round |
| `PIVOT_M_CLASSIC_S3_5` | Pivot M Classic S3\|5 | `Pivot.M.Classic.S3\|5` | round |
| `PIVOT_M_CLASSIC_S3_60` | Pivot M Classic S3\|60 | `Pivot.M.Classic.S3\|60` | round |
| `PIVOT_M_WOODIE_MIDDLE_1` | Pivot M Woodie Middle\|1 | `Pivot.M.Woodie.Middle\|1` | round |
| `PIVOT_M_WOODIE_MIDDLE_120` | Pivot M Woodie Middle\|120 | `Pivot.M.Woodie.Middle\|120` | round |
| `PIVOT_M_WOODIE_MIDDLE_15` | Pivot M Woodie Middle\|15 | `Pivot.M.Woodie.Middle\|15` | round |
| `PIVOT_M_WOODIE_MIDDLE_1M` | Pivot M Woodie Middle\|1m | `Pivot.M.Woodie.Middle\|1M` | round |
| `PIVOT_M_WOODIE_MIDDLE_1W` | Pivot M Woodie Middle\|1w | `Pivot.M.Woodie.Middle\|1W` | round |
| `PIVOT_M_WOODIE_MIDDLE_240` | Pivot M Woodie Middle\|240 | `Pivot.M.Woodie.Middle\|240` | round |
| `PIVOT_M_WOODIE_MIDDLE_30` | Pivot M Woodie Middle\|30 | `Pivot.M.Woodie.Middle\|30` | round |
| `PIVOT_M_WOODIE_MIDDLE_5` | Pivot M Woodie Middle\|5 | `Pivot.M.Woodie.Middle\|5` | round |
| `PIVOT_M_WOODIE_MIDDLE_60` | Pivot M Woodie Middle\|60 | `Pivot.M.Woodie.Middle\|60` | round |
| `PIVOT_M_WOODIE_R1_1` | Pivot M Woodie R1\|1 | `Pivot.M.Woodie.R1\|1` | round |
| `PIVOT_M_WOODIE_R1_120` | Pivot M Woodie R1\|120 | `Pivot.M.Woodie.R1\|120` | round |
| `PIVOT_M_WOODIE_R1_15` | Pivot M Woodie R1\|15 | `Pivot.M.Woodie.R1\|15` | round |
| `PIVOT_M_WOODIE_R1_1M` | Pivot M Woodie R1\|1m | `Pivot.M.Woodie.R1\|1M` | round |
| `PIVOT_M_WOODIE_R1_1W` | Pivot M Woodie R1\|1w | `Pivot.M.Woodie.R1\|1W` | round |
| `PIVOT_M_WOODIE_R1_240` | Pivot M Woodie R1\|240 | `Pivot.M.Woodie.R1\|240` | round |
| `PIVOT_M_WOODIE_R1_30` | Pivot M Woodie R1\|30 | `Pivot.M.Woodie.R1\|30` | round |
| `PIVOT_M_WOODIE_R1_5` | Pivot M Woodie R1\|5 | `Pivot.M.Woodie.R1\|5` | round |
| `PIVOT_M_WOODIE_R1_60` | Pivot M Woodie R1\|60 | `Pivot.M.Woodie.R1\|60` | round |
| `PIVOT_M_WOODIE_R2_1` | Pivot M Woodie R2\|1 | `Pivot.M.Woodie.R2\|1` | round |
| `PIVOT_M_WOODIE_R2_120` | Pivot M Woodie R2\|120 | `Pivot.M.Woodie.R2\|120` | round |
| `PIVOT_M_WOODIE_R2_15` | Pivot M Woodie R2\|15 | `Pivot.M.Woodie.R2\|15` | round |
| `PIVOT_M_WOODIE_R2_1M` | Pivot M Woodie R2\|1m | `Pivot.M.Woodie.R2\|1M` | round |
| `PIVOT_M_WOODIE_R2_1W` | Pivot M Woodie R2\|1w | `Pivot.M.Woodie.R2\|1W` | round |
| `PIVOT_M_WOODIE_R2_240` | Pivot M Woodie R2\|240 | `Pivot.M.Woodie.R2\|240` | round |
| `PIVOT_M_WOODIE_R2_30` | Pivot M Woodie R2\|30 | `Pivot.M.Woodie.R2\|30` | round |
| `PIVOT_M_WOODIE_R2_5` | Pivot M Woodie R2\|5 | `Pivot.M.Woodie.R2\|5` | round |
| `PIVOT_M_WOODIE_R2_60` | Pivot M Woodie R2\|60 | `Pivot.M.Woodie.R2\|60` | round |
| `PIVOT_M_WOODIE_R3_1` | Pivot M Woodie R3\|1 | `Pivot.M.Woodie.R3\|1` | round |
| `PIVOT_M_WOODIE_R3_120` | Pivot M Woodie R3\|120 | `Pivot.M.Woodie.R3\|120` | round |
| `PIVOT_M_WOODIE_R3_15` | Pivot M Woodie R3\|15 | `Pivot.M.Woodie.R3\|15` | round |
| `PIVOT_M_WOODIE_R3_1M` | Pivot M Woodie R3\|1m | `Pivot.M.Woodie.R3\|1M` | round |
| `PIVOT_M_WOODIE_R3_1W` | Pivot M Woodie R3\|1w | `Pivot.M.Woodie.R3\|1W` | round |
| `PIVOT_M_WOODIE_R3_240` | Pivot M Woodie R3\|240 | `Pivot.M.Woodie.R3\|240` | round |
| `PIVOT_M_WOODIE_R3_30` | Pivot M Woodie R3\|30 | `Pivot.M.Woodie.R3\|30` | round |
| `PIVOT_M_WOODIE_R3_5` | Pivot M Woodie R3\|5 | `Pivot.M.Woodie.R3\|5` | round |
| `PIVOT_M_WOODIE_R3_60` | Pivot M Woodie R3\|60 | `Pivot.M.Woodie.R3\|60` | round |
| `PIVOT_M_WOODIE_S1_1` | Pivot M Woodie S1\|1 | `Pivot.M.Woodie.S1\|1` | round |
| `PIVOT_M_WOODIE_S1_120` | Pivot M Woodie S1\|120 | `Pivot.M.Woodie.S1\|120` | round |
| `PIVOT_M_WOODIE_S1_15` | Pivot M Woodie S1\|15 | `Pivot.M.Woodie.S1\|15` | round |
| `PIVOT_M_WOODIE_S1_1M` | Pivot M Woodie S1\|1m | `Pivot.M.Woodie.S1\|1M` | round |
| `PIVOT_M_WOODIE_S1_1W` | Pivot M Woodie S1\|1w | `Pivot.M.Woodie.S1\|1W` | round |
| `PIVOT_M_WOODIE_S1_240` | Pivot M Woodie S1\|240 | `Pivot.M.Woodie.S1\|240` | round |
| `PIVOT_M_WOODIE_S1_30` | Pivot M Woodie S1\|30 | `Pivot.M.Woodie.S1\|30` | round |
| `PIVOT_M_WOODIE_S1_5` | Pivot M Woodie S1\|5 | `Pivot.M.Woodie.S1\|5` | round |
| `PIVOT_M_WOODIE_S1_60` | Pivot M Woodie S1\|60 | `Pivot.M.Woodie.S1\|60` | round |
| `PIVOT_M_WOODIE_S2_1` | Pivot M Woodie S2\|1 | `Pivot.M.Woodie.S2\|1` | round |
| `PIVOT_M_WOODIE_S2_120` | Pivot M Woodie S2\|120 | `Pivot.M.Woodie.S2\|120` | round |
| `PIVOT_M_WOODIE_S2_15` | Pivot M Woodie S2\|15 | `Pivot.M.Woodie.S2\|15` | round |
| `PIVOT_M_WOODIE_S2_1M` | Pivot M Woodie S2\|1m | `Pivot.M.Woodie.S2\|1M` | round |
| `PIVOT_M_WOODIE_S2_1W` | Pivot M Woodie S2\|1w | `Pivot.M.Woodie.S2\|1W` | round |
| `PIVOT_M_WOODIE_S2_240` | Pivot M Woodie S2\|240 | `Pivot.M.Woodie.S2\|240` | round |
| `PIVOT_M_WOODIE_S2_30` | Pivot M Woodie S2\|30 | `Pivot.M.Woodie.S2\|30` | round |
| `PIVOT_M_WOODIE_S2_5` | Pivot M Woodie S2\|5 | `Pivot.M.Woodie.S2\|5` | round |
| `PIVOT_M_WOODIE_S2_60` | Pivot M Woodie S2\|60 | `Pivot.M.Woodie.S2\|60` | round |
| `PIVOT_M_WOODIE_S3_1` | Pivot M Woodie S3\|1 | `Pivot.M.Woodie.S3\|1` | round |
| `PIVOT_M_WOODIE_S3_120` | Pivot M Woodie S3\|120 | `Pivot.M.Woodie.S3\|120` | round |
| `PIVOT_M_WOODIE_S3_15` | Pivot M Woodie S3\|15 | `Pivot.M.Woodie.S3\|15` | round |
| `PIVOT_M_WOODIE_S3_1M` | Pivot M Woodie S3\|1m | `Pivot.M.Woodie.S3\|1M` | round |
| `PIVOT_M_WOODIE_S3_1W` | Pivot M Woodie S3\|1w | `Pivot.M.Woodie.S3\|1W` | round |
| `PIVOT_M_WOODIE_S3_240` | Pivot M Woodie S3\|240 | `Pivot.M.Woodie.S3\|240` | round |
| `PIVOT_M_WOODIE_S3_30` | Pivot M Woodie S3\|30 | `Pivot.M.Woodie.S3\|30` | round |
| `PIVOT_M_WOODIE_S3_5` | Pivot M Woodie S3\|5 | `Pivot.M.Woodie.S3\|5` | round |
| `PIVOT_M_WOODIE_S3_60` | Pivot M Woodie S3\|60 | `Pivot.M.Woodie.S3\|60` | round |
| `PIVOT_WOODIE_P` | Pivot Woodie P | `Pivot.M.Woodie.Middle` | round |
| `PIVOT_WOODIE_R1` | Pivot Woodie R1 | `Pivot.M.Woodie.R1` | round |
| `PIVOT_WOODIE_R2` | Pivot Woodie R2 | `Pivot.M.Woodie.R2` | round |
| `PIVOT_WOODIE_R3` | Pivot Woodie R3 | `Pivot.M.Woodie.R3` | round |
| `PIVOT_WOODIE_S1` | Pivot Woodie S1 | `Pivot.M.Woodie.S1` | round |
| `PIVOT_WOODIE_S2` | Pivot Woodie S2 | `Pivot.M.Woodie.S2` | round |
| `PIVOT_WOODIE_S3` | Pivot Woodie S3 | `Pivot.M.Woodie.S3` | round |

## Candlestick Patterns

*271 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `CANDLE_3BLACKCROWS` | Candle.3BlackCrows | `Candle.3BlackCrows` | bool |
| `CANDLE_3BLACKCROWS_1` | Candle 3blackcrows\|1 | `Candle.3BlackCrows\|1` | round |
| `CANDLE_3BLACKCROWS_120` | Candle 3blackcrows\|120 | `Candle.3BlackCrows\|120` | round |
| `CANDLE_3BLACKCROWS_15` | Candle 3blackcrows\|15 | `Candle.3BlackCrows\|15` | round |
| `CANDLE_3BLACKCROWS_1M` | Candle 3blackcrows\|1m | `Candle.3BlackCrows\|1M` | round |
| `CANDLE_3BLACKCROWS_1W` | Candle 3blackcrows\|1w | `Candle.3BlackCrows\|1W` | round |
| `CANDLE_3BLACKCROWS_240` | Candle 3blackcrows\|240 | `Candle.3BlackCrows\|240` | round |
| `CANDLE_3BLACKCROWS_30` | Candle 3blackcrows\|30 | `Candle.3BlackCrows\|30` | round |
| `CANDLE_3BLACKCROWS_5` | Candle 3blackcrows\|5 | `Candle.3BlackCrows\|5` | round |
| `CANDLE_3BLACKCROWS_60` | Candle 3blackcrows\|60 | `Candle.3BlackCrows\|60` | round |
| `CANDLE_3WHITESOLDIERS` | Candle.3WhiteSoldiers | `Candle.3WhiteSoldiers` | bool |
| `CANDLE_3WHITESOLDIERS_1` | Candle 3whitesoldiers\|1 | `Candle.3WhiteSoldiers\|1` | round |
| `CANDLE_3WHITESOLDIERS_120` | Candle 3whitesoldiers\|120 | `Candle.3WhiteSoldiers\|120` | round |
| `CANDLE_3WHITESOLDIERS_15` | Candle 3whitesoldiers\|15 | `Candle.3WhiteSoldiers\|15` | round |
| `CANDLE_3WHITESOLDIERS_1M` | Candle 3whitesoldiers\|1m | `Candle.3WhiteSoldiers\|1M` | round |
| `CANDLE_3WHITESOLDIERS_1W` | Candle 3whitesoldiers\|1w | `Candle.3WhiteSoldiers\|1W` | round |
| `CANDLE_3WHITESOLDIERS_240` | Candle 3whitesoldiers\|240 | `Candle.3WhiteSoldiers\|240` | round |
| `CANDLE_3WHITESOLDIERS_30` | Candle 3whitesoldiers\|30 | `Candle.3WhiteSoldiers\|30` | round |
| `CANDLE_3WHITESOLDIERS_5` | Candle 3whitesoldiers\|5 | `Candle.3WhiteSoldiers\|5` | round |
| `CANDLE_3WHITESOLDIERS_60` | Candle 3whitesoldiers\|60 | `Candle.3WhiteSoldiers\|60` | round |
| `CANDLE_ABANDONEDBABY_BEARISH` | Candle.AbandonedBaby.Bearish | `Candle.AbandonedBaby.Bearish` | bool |
| `CANDLE_ABANDONEDBABY_BEARISH_1` | Candle Abandonedbaby Bearish\|1 | `Candle.AbandonedBaby.Bearish\|1` | round |
| `CANDLE_ABANDONEDBABY_BEARISH_120` | Candle Abandonedbaby Bearish\|120 | `Candle.AbandonedBaby.Bearish\|120` | round |
| `CANDLE_ABANDONEDBABY_BEARISH_15` | Candle Abandonedbaby Bearish\|15 | `Candle.AbandonedBaby.Bearish\|15` | round |
| `CANDLE_ABANDONEDBABY_BEARISH_1M` | Candle Abandonedbaby Bearish\|1m | `Candle.AbandonedBaby.Bearish\|1M` | round |
| `CANDLE_ABANDONEDBABY_BEARISH_1W` | Candle Abandonedbaby Bearish\|1w | `Candle.AbandonedBaby.Bearish\|1W` | round |
| `CANDLE_ABANDONEDBABY_BEARISH_240` | Candle Abandonedbaby Bearish\|240 | `Candle.AbandonedBaby.Bearish\|240` | round |
| `CANDLE_ABANDONEDBABY_BEARISH_30` | Candle Abandonedbaby Bearish\|30 | `Candle.AbandonedBaby.Bearish\|30` | round |
| `CANDLE_ABANDONEDBABY_BEARISH_5` | Candle Abandonedbaby Bearish\|5 | `Candle.AbandonedBaby.Bearish\|5` | round |
| `CANDLE_ABANDONEDBABY_BEARISH_60` | Candle Abandonedbaby Bearish\|60 | `Candle.AbandonedBaby.Bearish\|60` | round |
| `CANDLE_ABANDONEDBABY_BULLISH` | Candle.AbandonedBaby.Bullish | `Candle.AbandonedBaby.Bullish` | bool |
| `CANDLE_ABANDONEDBABY_BULLISH_1` | Candle Abandonedbaby Bullish\|1 | `Candle.AbandonedBaby.Bullish\|1` | round |
| `CANDLE_ABANDONEDBABY_BULLISH_120` | Candle Abandonedbaby Bullish\|120 | `Candle.AbandonedBaby.Bullish\|120` | round |
| `CANDLE_ABANDONEDBABY_BULLISH_15` | Candle Abandonedbaby Bullish\|15 | `Candle.AbandonedBaby.Bullish\|15` | round |
| `CANDLE_ABANDONEDBABY_BULLISH_1M` | Candle Abandonedbaby Bullish\|1m | `Candle.AbandonedBaby.Bullish\|1M` | round |
| `CANDLE_ABANDONEDBABY_BULLISH_1W` | Candle Abandonedbaby Bullish\|1w | `Candle.AbandonedBaby.Bullish\|1W` | round |
| `CANDLE_ABANDONEDBABY_BULLISH_240` | Candle Abandonedbaby Bullish\|240 | `Candle.AbandonedBaby.Bullish\|240` | round |
| `CANDLE_ABANDONEDBABY_BULLISH_30` | Candle Abandonedbaby Bullish\|30 | `Candle.AbandonedBaby.Bullish\|30` | round |
| `CANDLE_ABANDONEDBABY_BULLISH_5` | Candle Abandonedbaby Bullish\|5 | `Candle.AbandonedBaby.Bullish\|5` | round |
| `CANDLE_ABANDONEDBABY_BULLISH_60` | Candle Abandonedbaby Bullish\|60 | `Candle.AbandonedBaby.Bullish\|60` | round |
| `CANDLE_DOJI` | Candle.Doji | `Candle.Doji` | bool |
| `CANDLE_DOJI_1` | Candle Doji\|1 | `Candle.Doji\|1` | round |
| `CANDLE_DOJI_120` | Candle Doji\|120 | `Candle.Doji\|120` | round |
| `CANDLE_DOJI_15` | Candle Doji\|15 | `Candle.Doji\|15` | round |
| `CANDLE_DOJI_1M` | Candle Doji\|1m | `Candle.Doji\|1M` | round |
| `CANDLE_DOJI_1W` | Candle Doji\|1w | `Candle.Doji\|1W` | round |
| `CANDLE_DOJI_240` | Candle Doji\|240 | `Candle.Doji\|240` | round |
| `CANDLE_DOJI_30` | Candle Doji\|30 | `Candle.Doji\|30` | round |
| `CANDLE_DOJI_5` | Candle Doji\|5 | `Candle.Doji\|5` | round |
| `CANDLE_DOJI_60` | Candle Doji\|60 | `Candle.Doji\|60` | round |
| `CANDLE_DOJI_DRAGONFLY` | Candle.Doji.Dragonfly | `Candle.Doji.Dragonfly` | bool |
| `CANDLE_DOJI_DRAGONFLY_1` | Candle Doji Dragonfly\|1 | `Candle.Doji.Dragonfly\|1` | round |
| `CANDLE_DOJI_DRAGONFLY_120` | Candle Doji Dragonfly\|120 | `Candle.Doji.Dragonfly\|120` | round |
| `CANDLE_DOJI_DRAGONFLY_15` | Candle Doji Dragonfly\|15 | `Candle.Doji.Dragonfly\|15` | round |
| `CANDLE_DOJI_DRAGONFLY_1M` | Candle Doji Dragonfly\|1m | `Candle.Doji.Dragonfly\|1M` | round |
| `CANDLE_DOJI_DRAGONFLY_1W` | Candle Doji Dragonfly\|1w | `Candle.Doji.Dragonfly\|1W` | round |
| `CANDLE_DOJI_DRAGONFLY_240` | Candle Doji Dragonfly\|240 | `Candle.Doji.Dragonfly\|240` | round |
| `CANDLE_DOJI_DRAGONFLY_30` | Candle Doji Dragonfly\|30 | `Candle.Doji.Dragonfly\|30` | round |
| `CANDLE_DOJI_DRAGONFLY_5` | Candle Doji Dragonfly\|5 | `Candle.Doji.Dragonfly\|5` | round |
| `CANDLE_DOJI_DRAGONFLY_60` | Candle Doji Dragonfly\|60 | `Candle.Doji.Dragonfly\|60` | round |
| `CANDLE_DOJI_GRAVESTONE` | Candle.Doji.Gravestone | `Candle.Doji.Gravestone` | bool |
| `CANDLE_DOJI_GRAVESTONE_1` | Candle Doji Gravestone\|1 | `Candle.Doji.Gravestone\|1` | round |
| `CANDLE_DOJI_GRAVESTONE_120` | Candle Doji Gravestone\|120 | `Candle.Doji.Gravestone\|120` | round |
| `CANDLE_DOJI_GRAVESTONE_15` | Candle Doji Gravestone\|15 | `Candle.Doji.Gravestone\|15` | round |
| `CANDLE_DOJI_GRAVESTONE_1M` | Candle Doji Gravestone\|1m | `Candle.Doji.Gravestone\|1M` | round |
| `CANDLE_DOJI_GRAVESTONE_1W` | Candle Doji Gravestone\|1w | `Candle.Doji.Gravestone\|1W` | round |
| `CANDLE_DOJI_GRAVESTONE_240` | Candle Doji Gravestone\|240 | `Candle.Doji.Gravestone\|240` | round |
| `CANDLE_DOJI_GRAVESTONE_30` | Candle Doji Gravestone\|30 | `Candle.Doji.Gravestone\|30` | round |
| `CANDLE_DOJI_GRAVESTONE_5` | Candle Doji Gravestone\|5 | `Candle.Doji.Gravestone\|5` | round |
| `CANDLE_DOJI_GRAVESTONE_60` | Candle Doji Gravestone\|60 | `Candle.Doji.Gravestone\|60` | round |
| `CANDLE_ENGULFING_BEARISH` | Candle.Engulfing.Bearish | `Candle.Engulfing.Bearish` | bool |
| `CANDLE_ENGULFING_BEARISH_1` | Candle Engulfing Bearish\|1 | `Candle.Engulfing.Bearish\|1` | round |
| `CANDLE_ENGULFING_BEARISH_120` | Candle Engulfing Bearish\|120 | `Candle.Engulfing.Bearish\|120` | round |
| `CANDLE_ENGULFING_BEARISH_15` | Candle Engulfing Bearish\|15 | `Candle.Engulfing.Bearish\|15` | round |
| `CANDLE_ENGULFING_BEARISH_1M` | Candle Engulfing Bearish\|1m | `Candle.Engulfing.Bearish\|1M` | round |
| `CANDLE_ENGULFING_BEARISH_1W` | Candle Engulfing Bearish\|1w | `Candle.Engulfing.Bearish\|1W` | round |
| `CANDLE_ENGULFING_BEARISH_240` | Candle Engulfing Bearish\|240 | `Candle.Engulfing.Bearish\|240` | round |
| `CANDLE_ENGULFING_BEARISH_30` | Candle Engulfing Bearish\|30 | `Candle.Engulfing.Bearish\|30` | round |
| `CANDLE_ENGULFING_BEARISH_5` | Candle Engulfing Bearish\|5 | `Candle.Engulfing.Bearish\|5` | round |
| `CANDLE_ENGULFING_BEARISH_60` | Candle Engulfing Bearish\|60 | `Candle.Engulfing.Bearish\|60` | round |
| `CANDLE_ENGULFING_BULLISH` | Candle.Engulfing.Bullish | `Candle.Engulfing.Bullish` | bool |
| `CANDLE_ENGULFING_BULLISH_1` | Candle Engulfing Bullish\|1 | `Candle.Engulfing.Bullish\|1` | round |
| `CANDLE_ENGULFING_BULLISH_120` | Candle Engulfing Bullish\|120 | `Candle.Engulfing.Bullish\|120` | round |
| `CANDLE_ENGULFING_BULLISH_15` | Candle Engulfing Bullish\|15 | `Candle.Engulfing.Bullish\|15` | round |
| `CANDLE_ENGULFING_BULLISH_1M` | Candle Engulfing Bullish\|1m | `Candle.Engulfing.Bullish\|1M` | round |
| `CANDLE_ENGULFING_BULLISH_1W` | Candle Engulfing Bullish\|1w | `Candle.Engulfing.Bullish\|1W` | round |
| `CANDLE_ENGULFING_BULLISH_240` | Candle Engulfing Bullish\|240 | `Candle.Engulfing.Bullish\|240` | round |
| `CANDLE_ENGULFING_BULLISH_30` | Candle Engulfing Bullish\|30 | `Candle.Engulfing.Bullish\|30` | round |
| `CANDLE_ENGULFING_BULLISH_5` | Candle Engulfing Bullish\|5 | `Candle.Engulfing.Bullish\|5` | round |
| `CANDLE_ENGULFING_BULLISH_60` | Candle Engulfing Bullish\|60 | `Candle.Engulfing.Bullish\|60` | round |
| `CANDLE_EVENINGSTAR` | Candle.EveningStar | `Candle.EveningStar` | bool |
| `CANDLE_EVENINGSTAR_1` | Candle Eveningstar\|1 | `Candle.EveningStar\|1` | round |
| `CANDLE_EVENINGSTAR_120` | Candle Eveningstar\|120 | `Candle.EveningStar\|120` | round |
| `CANDLE_EVENINGSTAR_15` | Candle Eveningstar\|15 | `Candle.EveningStar\|15` | round |
| `CANDLE_EVENINGSTAR_1M` | Candle Eveningstar\|1m | `Candle.EveningStar\|1M` | round |
| `CANDLE_EVENINGSTAR_1W` | Candle Eveningstar\|1w | `Candle.EveningStar\|1W` | round |
| `CANDLE_EVENINGSTAR_240` | Candle Eveningstar\|240 | `Candle.EveningStar\|240` | round |
| `CANDLE_EVENINGSTAR_30` | Candle Eveningstar\|30 | `Candle.EveningStar\|30` | round |
| `CANDLE_EVENINGSTAR_5` | Candle Eveningstar\|5 | `Candle.EveningStar\|5` | round |
| `CANDLE_EVENINGSTAR_60` | Candle Eveningstar\|60 | `Candle.EveningStar\|60` | round |
| `CANDLE_HAMMER` | Candle.Hammer | `Candle.Hammer` | bool |
| `CANDLE_HAMMER_1` | Candle Hammer\|1 | `Candle.Hammer\|1` | round |
| `CANDLE_HAMMER_120` | Candle Hammer\|120 | `Candle.Hammer\|120` | round |
| `CANDLE_HAMMER_15` | Candle Hammer\|15 | `Candle.Hammer\|15` | round |
| `CANDLE_HAMMER_1M` | Candle Hammer\|1m | `Candle.Hammer\|1M` | round |
| `CANDLE_HAMMER_1W` | Candle Hammer\|1w | `Candle.Hammer\|1W` | round |
| `CANDLE_HAMMER_240` | Candle Hammer\|240 | `Candle.Hammer\|240` | round |
| `CANDLE_HAMMER_30` | Candle Hammer\|30 | `Candle.Hammer\|30` | round |
| `CANDLE_HAMMER_5` | Candle Hammer\|5 | `Candle.Hammer\|5` | round |
| `CANDLE_HAMMER_60` | Candle Hammer\|60 | `Candle.Hammer\|60` | round |
| `CANDLE_HANGINGMAN` | Candle.HangingMan | `Candle.HangingMan` | bool |
| `CANDLE_HANGINGMAN_1` | Candle Hangingman\|1 | `Candle.HangingMan\|1` | round |
| `CANDLE_HANGINGMAN_120` | Candle Hangingman\|120 | `Candle.HangingMan\|120` | round |
| `CANDLE_HANGINGMAN_15` | Candle Hangingman\|15 | `Candle.HangingMan\|15` | round |
| `CANDLE_HANGINGMAN_1M` | Candle Hangingman\|1m | `Candle.HangingMan\|1M` | round |
| `CANDLE_HANGINGMAN_1W` | Candle Hangingman\|1w | `Candle.HangingMan\|1W` | round |
| `CANDLE_HANGINGMAN_240` | Candle Hangingman\|240 | `Candle.HangingMan\|240` | round |
| `CANDLE_HANGINGMAN_30` | Candle Hangingman\|30 | `Candle.HangingMan\|30` | round |
| `CANDLE_HANGINGMAN_5` | Candle Hangingman\|5 | `Candle.HangingMan\|5` | round |
| `CANDLE_HANGINGMAN_60` | Candle Hangingman\|60 | `Candle.HangingMan\|60` | round |
| `CANDLE_HARAMI_BEARISH` | Candle.Harami.Bearish | `Candle.Harami.Bearish` | bool |
| `CANDLE_HARAMI_BEARISH_1` | Candle Harami Bearish\|1 | `Candle.Harami.Bearish\|1` | round |
| `CANDLE_HARAMI_BEARISH_120` | Candle Harami Bearish\|120 | `Candle.Harami.Bearish\|120` | round |
| `CANDLE_HARAMI_BEARISH_15` | Candle Harami Bearish\|15 | `Candle.Harami.Bearish\|15` | round |
| `CANDLE_HARAMI_BEARISH_1M` | Candle Harami Bearish\|1m | `Candle.Harami.Bearish\|1M` | round |
| `CANDLE_HARAMI_BEARISH_1W` | Candle Harami Bearish\|1w | `Candle.Harami.Bearish\|1W` | round |
| `CANDLE_HARAMI_BEARISH_240` | Candle Harami Bearish\|240 | `Candle.Harami.Bearish\|240` | round |
| `CANDLE_HARAMI_BEARISH_30` | Candle Harami Bearish\|30 | `Candle.Harami.Bearish\|30` | round |
| `CANDLE_HARAMI_BEARISH_5` | Candle Harami Bearish\|5 | `Candle.Harami.Bearish\|5` | round |
| `CANDLE_HARAMI_BEARISH_60` | Candle Harami Bearish\|60 | `Candle.Harami.Bearish\|60` | round |
| `CANDLE_HARAMI_BULLISH` | Candle.Harami.Bullish | `Candle.Harami.Bullish` | bool |
| `CANDLE_HARAMI_BULLISH_1` | Candle Harami Bullish\|1 | `Candle.Harami.Bullish\|1` | round |
| `CANDLE_HARAMI_BULLISH_120` | Candle Harami Bullish\|120 | `Candle.Harami.Bullish\|120` | round |
| `CANDLE_HARAMI_BULLISH_15` | Candle Harami Bullish\|15 | `Candle.Harami.Bullish\|15` | round |
| `CANDLE_HARAMI_BULLISH_1M` | Candle Harami Bullish\|1m | `Candle.Harami.Bullish\|1M` | round |
| `CANDLE_HARAMI_BULLISH_1W` | Candle Harami Bullish\|1w | `Candle.Harami.Bullish\|1W` | round |
| `CANDLE_HARAMI_BULLISH_240` | Candle Harami Bullish\|240 | `Candle.Harami.Bullish\|240` | round |
| `CANDLE_HARAMI_BULLISH_30` | Candle Harami Bullish\|30 | `Candle.Harami.Bullish\|30` | round |
| `CANDLE_HARAMI_BULLISH_5` | Candle Harami Bullish\|5 | `Candle.Harami.Bullish\|5` | round |
| `CANDLE_HARAMI_BULLISH_60` | Candle Harami Bullish\|60 | `Candle.Harami.Bullish\|60` | round |
| `CANDLE_INVERTEDHAMMER` | Candle.InvertedHammer | `Candle.InvertedHammer` | bool |
| `CANDLE_INVERTEDHAMMER_1` | Candle Invertedhammer\|1 | `Candle.InvertedHammer\|1` | round |
| `CANDLE_INVERTEDHAMMER_120` | Candle Invertedhammer\|120 | `Candle.InvertedHammer\|120` | round |
| `CANDLE_INVERTEDHAMMER_15` | Candle Invertedhammer\|15 | `Candle.InvertedHammer\|15` | round |
| `CANDLE_INVERTEDHAMMER_1M` | Candle Invertedhammer\|1m | `Candle.InvertedHammer\|1M` | round |
| `CANDLE_INVERTEDHAMMER_1W` | Candle Invertedhammer\|1w | `Candle.InvertedHammer\|1W` | round |
| `CANDLE_INVERTEDHAMMER_240` | Candle Invertedhammer\|240 | `Candle.InvertedHammer\|240` | round |
| `CANDLE_INVERTEDHAMMER_30` | Candle Invertedhammer\|30 | `Candle.InvertedHammer\|30` | round |
| `CANDLE_INVERTEDHAMMER_5` | Candle Invertedhammer\|5 | `Candle.InvertedHammer\|5` | round |
| `CANDLE_INVERTEDHAMMER_60` | Candle Invertedhammer\|60 | `Candle.InvertedHammer\|60` | round |
| `CANDLE_KICKING_BEARISH` | Candle.Kicking.Bearish | `Candle.Kicking.Bearish` | bool |
| `CANDLE_KICKING_BEARISH_1` | Candle Kicking Bearish\|1 | `Candle.Kicking.Bearish\|1` | round |
| `CANDLE_KICKING_BEARISH_120` | Candle Kicking Bearish\|120 | `Candle.Kicking.Bearish\|120` | round |
| `CANDLE_KICKING_BEARISH_15` | Candle Kicking Bearish\|15 | `Candle.Kicking.Bearish\|15` | round |
| `CANDLE_KICKING_BEARISH_1M` | Candle Kicking Bearish\|1m | `Candle.Kicking.Bearish\|1M` | round |
| `CANDLE_KICKING_BEARISH_1W` | Candle Kicking Bearish\|1w | `Candle.Kicking.Bearish\|1W` | round |
| `CANDLE_KICKING_BEARISH_240` | Candle Kicking Bearish\|240 | `Candle.Kicking.Bearish\|240` | round |
| `CANDLE_KICKING_BEARISH_30` | Candle Kicking Bearish\|30 | `Candle.Kicking.Bearish\|30` | round |
| `CANDLE_KICKING_BEARISH_5` | Candle Kicking Bearish\|5 | `Candle.Kicking.Bearish\|5` | round |
| `CANDLE_KICKING_BEARISH_60` | Candle Kicking Bearish\|60 | `Candle.Kicking.Bearish\|60` | round |
| `CANDLE_KICKING_BULLISH` | Candle.Kicking.Bullish | `Candle.Kicking.Bullish` | bool |
| `CANDLE_KICKING_BULLISH_1` | Candle Kicking Bullish\|1 | `Candle.Kicking.Bullish\|1` | round |
| `CANDLE_KICKING_BULLISH_120` | Candle Kicking Bullish\|120 | `Candle.Kicking.Bullish\|120` | round |
| `CANDLE_KICKING_BULLISH_15` | Candle Kicking Bullish\|15 | `Candle.Kicking.Bullish\|15` | round |
| `CANDLE_KICKING_BULLISH_1M` | Candle Kicking Bullish\|1m | `Candle.Kicking.Bullish\|1M` | round |
| `CANDLE_KICKING_BULLISH_1W` | Candle Kicking Bullish\|1w | `Candle.Kicking.Bullish\|1W` | round |
| `CANDLE_KICKING_BULLISH_240` | Candle Kicking Bullish\|240 | `Candle.Kicking.Bullish\|240` | round |
| `CANDLE_KICKING_BULLISH_30` | Candle Kicking Bullish\|30 | `Candle.Kicking.Bullish\|30` | round |
| `CANDLE_KICKING_BULLISH_5` | Candle Kicking Bullish\|5 | `Candle.Kicking.Bullish\|5` | round |
| `CANDLE_KICKING_BULLISH_60` | Candle Kicking Bullish\|60 | `Candle.Kicking.Bullish\|60` | round |
| `CANDLE_LONGSHADOW_LOWER` | Candle.LongShadow.Lower | `Candle.LongShadow.Lower` | bool |
| `CANDLE_LONGSHADOW_LOWER_1` | Candle Longshadow Lower\|1 | `Candle.LongShadow.Lower\|1` | round |
| `CANDLE_LONGSHADOW_LOWER_120` | Candle Longshadow Lower\|120 | `Candle.LongShadow.Lower\|120` | round |
| `CANDLE_LONGSHADOW_LOWER_15` | Candle Longshadow Lower\|15 | `Candle.LongShadow.Lower\|15` | round |
| `CANDLE_LONGSHADOW_LOWER_1M` | Candle Longshadow Lower\|1m | `Candle.LongShadow.Lower\|1M` | round |
| `CANDLE_LONGSHADOW_LOWER_1W` | Candle Longshadow Lower\|1w | `Candle.LongShadow.Lower\|1W` | round |
| `CANDLE_LONGSHADOW_LOWER_240` | Candle Longshadow Lower\|240 | `Candle.LongShadow.Lower\|240` | round |
| `CANDLE_LONGSHADOW_LOWER_30` | Candle Longshadow Lower\|30 | `Candle.LongShadow.Lower\|30` | round |
| `CANDLE_LONGSHADOW_LOWER_5` | Candle Longshadow Lower\|5 | `Candle.LongShadow.Lower\|5` | round |
| `CANDLE_LONGSHADOW_LOWER_60` | Candle Longshadow Lower\|60 | `Candle.LongShadow.Lower\|60` | round |
| `CANDLE_LONGSHADOW_UPPER` | Candle.LongShadow.Upper | `Candle.LongShadow.Upper` | bool |
| `CANDLE_LONGSHADOW_UPPER_1` | Candle Longshadow Upper\|1 | `Candle.LongShadow.Upper\|1` | round |
| `CANDLE_LONGSHADOW_UPPER_120` | Candle Longshadow Upper\|120 | `Candle.LongShadow.Upper\|120` | round |
| `CANDLE_LONGSHADOW_UPPER_15` | Candle Longshadow Upper\|15 | `Candle.LongShadow.Upper\|15` | round |
| `CANDLE_LONGSHADOW_UPPER_1M` | Candle Longshadow Upper\|1m | `Candle.LongShadow.Upper\|1M` | round |
| `CANDLE_LONGSHADOW_UPPER_1W` | Candle Longshadow Upper\|1w | `Candle.LongShadow.Upper\|1W` | round |
| `CANDLE_LONGSHADOW_UPPER_240` | Candle Longshadow Upper\|240 | `Candle.LongShadow.Upper\|240` | round |
| `CANDLE_LONGSHADOW_UPPER_30` | Candle Longshadow Upper\|30 | `Candle.LongShadow.Upper\|30` | round |
| `CANDLE_LONGSHADOW_UPPER_5` | Candle Longshadow Upper\|5 | `Candle.LongShadow.Upper\|5` | round |
| `CANDLE_LONGSHADOW_UPPER_60` | Candle Longshadow Upper\|60 | `Candle.LongShadow.Upper\|60` | round |
| `CANDLE_MARUBOZU_BLACK` | Candle.Marubozu.Black | `Candle.Marubozu.Black` | bool |
| `CANDLE_MARUBOZU_BLACK_1` | Candle Marubozu Black\|1 | `Candle.Marubozu.Black\|1` | round |
| `CANDLE_MARUBOZU_BLACK_120` | Candle Marubozu Black\|120 | `Candle.Marubozu.Black\|120` | round |
| `CANDLE_MARUBOZU_BLACK_15` | Candle Marubozu Black\|15 | `Candle.Marubozu.Black\|15` | round |
| `CANDLE_MARUBOZU_BLACK_1M` | Candle Marubozu Black\|1m | `Candle.Marubozu.Black\|1M` | round |
| `CANDLE_MARUBOZU_BLACK_1W` | Candle Marubozu Black\|1w | `Candle.Marubozu.Black\|1W` | round |
| `CANDLE_MARUBOZU_BLACK_240` | Candle Marubozu Black\|240 | `Candle.Marubozu.Black\|240` | round |
| `CANDLE_MARUBOZU_BLACK_30` | Candle Marubozu Black\|30 | `Candle.Marubozu.Black\|30` | round |
| `CANDLE_MARUBOZU_BLACK_5` | Candle Marubozu Black\|5 | `Candle.Marubozu.Black\|5` | round |
| `CANDLE_MARUBOZU_BLACK_60` | Candle Marubozu Black\|60 | `Candle.Marubozu.Black\|60` | round |
| `CANDLE_MARUBOZU_WHITE` | Candle.Marubozu.White | `Candle.Marubozu.White` | bool |
| `CANDLE_MARUBOZU_WHITE_1` | Candle Marubozu White\|1 | `Candle.Marubozu.White\|1` | round |
| `CANDLE_MARUBOZU_WHITE_120` | Candle Marubozu White\|120 | `Candle.Marubozu.White\|120` | round |
| `CANDLE_MARUBOZU_WHITE_15` | Candle Marubozu White\|15 | `Candle.Marubozu.White\|15` | round |
| `CANDLE_MARUBOZU_WHITE_1M` | Candle Marubozu White\|1m | `Candle.Marubozu.White\|1M` | round |
| `CANDLE_MARUBOZU_WHITE_1W` | Candle Marubozu White\|1w | `Candle.Marubozu.White\|1W` | round |
| `CANDLE_MARUBOZU_WHITE_240` | Candle Marubozu White\|240 | `Candle.Marubozu.White\|240` | round |
| `CANDLE_MARUBOZU_WHITE_30` | Candle Marubozu White\|30 | `Candle.Marubozu.White\|30` | round |
| `CANDLE_MARUBOZU_WHITE_5` | Candle Marubozu White\|5 | `Candle.Marubozu.White\|5` | round |
| `CANDLE_MARUBOZU_WHITE_60` | Candle Marubozu White\|60 | `Candle.Marubozu.White\|60` | round |
| `CANDLE_MORNINGSTAR` | Candle.MorningStar | `Candle.MorningStar` | bool |
| `CANDLE_MORNINGSTAR_1` | Candle Morningstar\|1 | `Candle.MorningStar\|1` | round |
| `CANDLE_MORNINGSTAR_120` | Candle Morningstar\|120 | `Candle.MorningStar\|120` | round |
| `CANDLE_MORNINGSTAR_15` | Candle Morningstar\|15 | `Candle.MorningStar\|15` | round |
| `CANDLE_MORNINGSTAR_1M` | Candle Morningstar\|1m | `Candle.MorningStar\|1M` | round |
| `CANDLE_MORNINGSTAR_1W` | Candle Morningstar\|1w | `Candle.MorningStar\|1W` | round |
| `CANDLE_MORNINGSTAR_240` | Candle Morningstar\|240 | `Candle.MorningStar\|240` | round |
| `CANDLE_MORNINGSTAR_30` | Candle Morningstar\|30 | `Candle.MorningStar\|30` | round |
| `CANDLE_MORNINGSTAR_5` | Candle Morningstar\|5 | `Candle.MorningStar\|5` | round |
| `CANDLE_MORNINGSTAR_60` | Candle Morningstar\|60 | `Candle.MorningStar\|60` | round |
| `CANDLE_SHOOTINGSTAR` | Candle.ShootingStar | `Candle.ShootingStar` | bool |
| `CANDLE_SHOOTINGSTAR_1` | Candle Shootingstar\|1 | `Candle.ShootingStar\|1` | round |
| `CANDLE_SHOOTINGSTAR_120` | Candle Shootingstar\|120 | `Candle.ShootingStar\|120` | round |
| `CANDLE_SHOOTINGSTAR_15` | Candle Shootingstar\|15 | `Candle.ShootingStar\|15` | round |
| `CANDLE_SHOOTINGSTAR_1M` | Candle Shootingstar\|1m | `Candle.ShootingStar\|1M` | round |
| `CANDLE_SHOOTINGSTAR_1W` | Candle Shootingstar\|1w | `Candle.ShootingStar\|1W` | round |
| `CANDLE_SHOOTINGSTAR_240` | Candle Shootingstar\|240 | `Candle.ShootingStar\|240` | round |
| `CANDLE_SHOOTINGSTAR_30` | Candle Shootingstar\|30 | `Candle.ShootingStar\|30` | round |
| `CANDLE_SHOOTINGSTAR_5` | Candle Shootingstar\|5 | `Candle.ShootingStar\|5` | round |
| `CANDLE_SHOOTINGSTAR_60` | Candle Shootingstar\|60 | `Candle.ShootingStar\|60` | round |
| `CANDLE_SPINNINGTOP_BLACK` | Candle.SpinningTop.Black | `Candle.SpinningTop.Black` | bool |
| `CANDLE_SPINNINGTOP_BLACK_1` | Candle Spinningtop Black\|1 | `Candle.SpinningTop.Black\|1` | round |
| `CANDLE_SPINNINGTOP_BLACK_120` | Candle Spinningtop Black\|120 | `Candle.SpinningTop.Black\|120` | round |
| `CANDLE_SPINNINGTOP_BLACK_15` | Candle Spinningtop Black\|15 | `Candle.SpinningTop.Black\|15` | round |
| `CANDLE_SPINNINGTOP_BLACK_1M` | Candle Spinningtop Black\|1m | `Candle.SpinningTop.Black\|1M` | round |
| `CANDLE_SPINNINGTOP_BLACK_1W` | Candle Spinningtop Black\|1w | `Candle.SpinningTop.Black\|1W` | round |
| `CANDLE_SPINNINGTOP_BLACK_240` | Candle Spinningtop Black\|240 | `Candle.SpinningTop.Black\|240` | round |
| `CANDLE_SPINNINGTOP_BLACK_30` | Candle Spinningtop Black\|30 | `Candle.SpinningTop.Black\|30` | round |
| `CANDLE_SPINNINGTOP_BLACK_5` | Candle Spinningtop Black\|5 | `Candle.SpinningTop.Black\|5` | round |
| `CANDLE_SPINNINGTOP_BLACK_60` | Candle Spinningtop Black\|60 | `Candle.SpinningTop.Black\|60` | round |
| `CANDLE_SPINNINGTOP_WHITE` | Candle.SpinningTop.White | `Candle.SpinningTop.White` | bool |
| `CANDLE_SPINNINGTOP_WHITE_1` | Candle Spinningtop White\|1 | `Candle.SpinningTop.White\|1` | round |
| `CANDLE_SPINNINGTOP_WHITE_120` | Candle Spinningtop White\|120 | `Candle.SpinningTop.White\|120` | round |
| `CANDLE_SPINNINGTOP_WHITE_15` | Candle Spinningtop White\|15 | `Candle.SpinningTop.White\|15` | round |
| `CANDLE_SPINNINGTOP_WHITE_1M` | Candle Spinningtop White\|1m | `Candle.SpinningTop.White\|1M` | round |
| `CANDLE_SPINNINGTOP_WHITE_1W` | Candle Spinningtop White\|1w | `Candle.SpinningTop.White\|1W` | round |
| `CANDLE_SPINNINGTOP_WHITE_240` | Candle Spinningtop White\|240 | `Candle.SpinningTop.White\|240` | round |
| `CANDLE_SPINNINGTOP_WHITE_30` | Candle Spinningtop White\|30 | `Candle.SpinningTop.White\|30` | round |
| `CANDLE_SPINNINGTOP_WHITE_5` | Candle Spinningtop White\|5 | `Candle.SpinningTop.White\|5` | round |
| `CANDLE_SPINNINGTOP_WHITE_60` | Candle Spinningtop White\|60 | `Candle.SpinningTop.White\|60` | round |
| `CANDLE_TRISTAR_BEARISH` | Candle.TriStar.Bearish | `Candle.TriStar.Bearish` | bool |
| `CANDLE_TRISTAR_BEARISH_1` | Candle Tristar Bearish\|1 | `Candle.TriStar.Bearish\|1` | round |
| `CANDLE_TRISTAR_BEARISH_120` | Candle Tristar Bearish\|120 | `Candle.TriStar.Bearish\|120` | round |
| `CANDLE_TRISTAR_BEARISH_15` | Candle Tristar Bearish\|15 | `Candle.TriStar.Bearish\|15` | round |
| `CANDLE_TRISTAR_BEARISH_1M` | Candle Tristar Bearish\|1m | `Candle.TriStar.Bearish\|1M` | round |
| `CANDLE_TRISTAR_BEARISH_1W` | Candle Tristar Bearish\|1w | `Candle.TriStar.Bearish\|1W` | round |
| `CANDLE_TRISTAR_BEARISH_240` | Candle Tristar Bearish\|240 | `Candle.TriStar.Bearish\|240` | round |
| `CANDLE_TRISTAR_BEARISH_30` | Candle Tristar Bearish\|30 | `Candle.TriStar.Bearish\|30` | round |
| `CANDLE_TRISTAR_BEARISH_5` | Candle Tristar Bearish\|5 | `Candle.TriStar.Bearish\|5` | round |
| `CANDLE_TRISTAR_BEARISH_60` | Candle Tristar Bearish\|60 | `Candle.TriStar.Bearish\|60` | round |
| `CANDLE_TRISTAR_BULLISH` | Candle.TriStar.Bullish | `Candle.TriStar.Bullish` | bool |
| `CANDLE_TRISTAR_BULLISH_1` | Candle Tristar Bullish\|1 | `Candle.TriStar.Bullish\|1` | round |
| `CANDLE_TRISTAR_BULLISH_120` | Candle Tristar Bullish\|120 | `Candle.TriStar.Bullish\|120` | round |
| `CANDLE_TRISTAR_BULLISH_15` | Candle Tristar Bullish\|15 | `Candle.TriStar.Bullish\|15` | round |
| `CANDLE_TRISTAR_BULLISH_1M` | Candle Tristar Bullish\|1m | `Candle.TriStar.Bullish\|1M` | round |
| `CANDLE_TRISTAR_BULLISH_1W` | Candle Tristar Bullish\|1w | `Candle.TriStar.Bullish\|1W` | round |
| `CANDLE_TRISTAR_BULLISH_240` | Candle Tristar Bullish\|240 | `Candle.TriStar.Bullish\|240` | round |
| `CANDLE_TRISTAR_BULLISH_30` | Candle Tristar Bullish\|30 | `Candle.TriStar.Bullish\|30` | round |
| `CANDLE_TRISTAR_BULLISH_5` | Candle Tristar Bullish\|5 | `Candle.TriStar.Bullish\|5` | round |
| `CANDLE_TRISTAR_BULLISH_60` | Candle Tristar Bullish\|60 | `Candle.TriStar.Bullish\|60` | round |
| `PATTERN` | Pattern | `candlestick` | missing |

## Recommendations

*47 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `MOVING_AVERAGES_RATING` | Moving Averages Rating | `Recommend.MA` | rating |
| `OSCILLATORS_RATING` | Oscillators Rating | `Recommend.Other` | rating |
| `RECOMMENDATION_BUY` | Recommendation Buy | `recommendation_buy` | round |
| `RECOMMENDATION_HOLD` | Recommendation Hold | `recommendation_hold` | round |
| `RECOMMENDATION_MARK` | Analyst Rating | `recommendation_mark` | round |
| `RECOMMENDATION_OVER` | Recommendation Over | `recommendation_over` | round |
| `RECOMMENDATION_SELL` | Recommendation Sell | `recommendation_sell` | round |
| `RECOMMENDATION_TOTAL` | Recommendation Total | `recommendation_total` | round |
| `RECOMMENDATION_UNDER` | Recommendation Under | `recommendation_under` | round |
| `RECOMMEND_ALL_1` | Recommend All\|1 | `Recommend.All\|1` | round |
| `RECOMMEND_ALL_120` | Recommend All\|120 | `Recommend.All\|120` | round |
| `RECOMMEND_ALL_15` | Recommend All\|15 | `Recommend.All\|15` | round |
| `RECOMMEND_ALL_1M` | Recommend All\|1m | `Recommend.All\|1M` | round |
| `RECOMMEND_ALL_1W` | Recommend All\|1w | `Recommend.All\|1W` | round |
| `RECOMMEND_ALL_240` | Recommend All\|240 | `Recommend.All\|240` | round |
| `RECOMMEND_ALL_30` | Recommend All\|30 | `Recommend.All\|30` | round |
| `RECOMMEND_ALL_5` | Recommend All\|5 | `Recommend.All\|5` | round |
| `RECOMMEND_ALL_60` | Recommend All\|60 | `Recommend.All\|60` | round |
| `RECOMMEND_MA_1` | Recommend Ma\|1 | `Recommend.MA\|1` | round |
| `RECOMMEND_MA_120` | Recommend Ma\|120 | `Recommend.MA\|120` | round |
| `RECOMMEND_MA_15` | Recommend Ma\|15 | `Recommend.MA\|15` | round |
| `RECOMMEND_MA_1M` | Recommend Ma\|1m | `Recommend.MA\|1M` | round |
| `RECOMMEND_MA_1W` | Recommend Ma\|1w | `Recommend.MA\|1W` | round |
| `RECOMMEND_MA_240` | Recommend Ma\|240 | `Recommend.MA\|240` | round |
| `RECOMMEND_MA_30` | Recommend Ma\|30 | `Recommend.MA\|30` | round |
| `RECOMMEND_MA_5` | Recommend Ma\|5 | `Recommend.MA\|5` | round |
| `RECOMMEND_MA_60` | Recommend Ma\|60 | `Recommend.MA\|60` | round |
| `RECOMMEND_OTHER_1` | Recommend Other\|1 | `Recommend.Other\|1` | round |
| `RECOMMEND_OTHER_120` | Recommend Other\|120 | `Recommend.Other\|120` | round |
| `RECOMMEND_OTHER_15` | Recommend Other\|15 | `Recommend.Other\|15` | round |
| `RECOMMEND_OTHER_1M` | Recommend Other\|1m | `Recommend.Other\|1M` | round |
| `RECOMMEND_OTHER_1W` | Recommend Other\|1w | `Recommend.Other\|1W` | round |
| `RECOMMEND_OTHER_240` | Recommend Other\|240 | `Recommend.Other\|240` | round |
| `RECOMMEND_OTHER_30` | Recommend Other\|30 | `Recommend.Other\|30` | round |
| `RECOMMEND_OTHER_5` | Recommend Other\|5 | `Recommend.Other\|5` | round |
| `RECOMMEND_OTHER_60` | Recommend Other\|60 | `Recommend.Other\|60` | round |
| `REC_WR` | Rec Wr | `Rec.WR` | round |
| `REC_WR_1` | Rec Wr\|1 | `Rec.WR\|1` | round |
| `REC_WR_120` | Rec Wr\|120 | `Rec.WR\|120` | round |
| `REC_WR_15` | Rec Wr\|15 | `Rec.WR\|15` | round |
| `REC_WR_1M` | Rec Wr\|1m | `Rec.WR\|1M` | round |
| `REC_WR_1W` | Rec Wr\|1w | `Rec.WR\|1W` | round |
| `REC_WR_240` | Rec Wr\|240 | `Rec.WR\|240` | round |
| `REC_WR_30` | Rec Wr\|30 | `Rec.WR\|30` | round |
| `REC_WR_5` | Rec Wr\|5 | `Rec.WR\|5` | round |
| `REC_WR_60` | Rec Wr\|60 | `Rec.WR\|60` | round |
| `TECHNICAL_RATING` | Technical Rating | `Recommend.All` | rating |

## Valuation Ratios

*23 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `ENTERPRISE_VALUEEBITDA_TTM` | Enterprise Value/EBITDA (TTM) | `enterprise_value_ebitda_ttm` | round |
| `ENTERPRISE_VALUE_CURRENT` | Enterprise Value Current | `enterprise_value_current` | currency |
| `ENTERPRISE_VALUE_EBITDA_CURRENT` | Enterprise Value EBITDA Current | `enterprise_value_ebitda_current` | round |
| `ENTERPRISE_VALUE_MRQ` | Enterprise Value (MRQ) | `enterprise_value_fq` | currency |
| `ENTERPRISE_VALUE_TO_EBIT_TTM` | EV to EBIT (TTM) | `enterprise_value_to_ebit_ttm` | round |
| `ENTERPRISE_VALUE_TO_GROSS_PROFIT_TTM` | EV to Gross Profit (TTM) | `enterprise_value_to_gross_profit_ttm` | round |
| `ENTERPRISE_VALUE_TO_REVENUE_TTM` | EV to Revenue (TTM) | `enterprise_value_to_revenue_ttm` | round |
| `NCAVPS_RATIO_CURRENT` | Ncavps Ratio Current | `ncavps_ratio_current` | currency |
| `NCAVPS_RATIO_FH` | Ncavps Ratio Fh | `ncavps_ratio_fh` | currency |
| `NCAVPS_RATIO_FQ` | NCAV per Share (MRQ) | `ncavps_ratio_fq` | currency |
| `NCAVPS_RATIO_FY` | NCAV per Share (FY) | `ncavps_ratio_fy` | currency |
| `NEG_RESEARCH_AND_DEV_FH` | Neg Research and Dev Fh | `neg_research_and_dev_fh` | currency |
| `NEG_RESEARCH_AND_DEV_FQ` | Neg Research and Dev FQ | `neg_research_and_dev_fq` | currency |
| `NEG_RESEARCH_AND_DEV_FY` | Neg Research and Dev FY | `neg_research_and_dev_fy` | currency |
| `NEG_RESEARCH_AND_DEV_TTM` | Neg Research and Dev TTM | `neg_research_and_dev_ttm` | currency |
| `RESEARCH_AND_DEVELOPMENT_RATIO_FY` | Research & development Ratio (FY) | `research_and_dev_ratio_fy` | percent |
| `RESEARCH_AND_DEVELOPMENT_RATIO_TTM` | Research & development Ratio (TTM) | `research_and_dev_ratio_ttm` | percent |
| `RESEARCH_AND_DEV_FH` | Research and Dev Fh | `research_and_dev_fh` | currency |
| `RESEARCH_AND_DEV_FQ` | Research & Development (MRQ) | `research_and_dev_fq` | currency |
| `RESEARCH_AND_DEV_FY` | Research & Development (FY) | `research_and_dev_fy` | currency |
| `RESEARCH_AND_DEV_PER_EMPLOYEE_FY` | Research and Dev per Employee FY | `research_and_dev_per_employee_fy` | currency |
| `RESEARCH_AND_DEV_TTM` | Research and Dev TTM | `research_and_dev_ttm` | currency |
| `SUM_FOR_ENTERPRISE_VALUE` | Sum For Enterprise Value | `sum_for_enterprise_value` | currency |

## Profitability

*39 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `EBITDA_MARGIN_FY` | EBITDA Margin % (FY) | `ebitda_margin_fy` | percent |
| `EBITDA_MARGIN_TTM` | EBITDA Margin % (TTM) | `ebitda_margin_ttm` | percent |
| `GROSS_MARGIN_FY` | Gross Margin (FY) | `gross_profit_margin_fy` | percent |
| `GROSS_MARGIN_FY_2` | Gross Margin FY | `gross_margin_fy` | percent |
| `GROSS_MARGIN_PERCENT_TTM` | Gross Margin % (TTM) | `gross_margin_ttm` | percent |
| `GROSS_MARGIN_PERCENT_TTM_2` | Gross Margin Percent TTM | `gross_margin_percent_ttm` | percent |
| `GROSS_MARGIN_TTM` | Gross Margin (TTM) | `gross_margin` | percent |
| `NET_MARGIN` | Net Margin | `net_margin` | percent |
| `NET_MARGIN_FY` | Net Margin (FY) | `net_income_bef_disc_oper_margin_fy` | percent |
| `NET_MARGIN_FY_2` | Net Margin FY | `net_margin_fy` | percent |
| `NET_MARGIN_PERCENT_TTM` | Net Margin % (TTM) | `net_margin_ttm` | percent |
| `NET_MARGIN_TTM` | Net Margin (TTM) | `after_tax_margin` | percent |
| `OPERATING_MARGIN_FY` | Operating Margin (FY) | `oper_income_margin_fy` | percent |
| `OPERATING_MARGIN_FY_2` | Operating Margin FY | `operating_margin_fy` | percent |
| `OPERATING_MARGIN_PERCENT_TTM` | Operating Margin % (TTM) | `operating_margin_ttm` | percent |
| `OPERATING_MARGIN_TTM` | Operating Margin (TTM) | `operating_margin` | percent |
| `PRETAX_MARGIN_TTM` | Pretax Margin (TTM) | `pre_tax_margin` | percent |
| `PRE_TAX_MARGIN_TTM` | Pre Tax Margin TTM | `pre_tax_margin_ttm` | percent |
| `RETURN_ON_ASSETS_FQ` | Return on Assets % (MRQ) | `return_on_assets_fq` | percent |
| `RETURN_ON_ASSETS_FY` | Return on Assets FY | `return_on_assets_fy` | percent |
| `RETURN_ON_ASSETS_TTM` | Return on Assets (TTM) | `return_on_assets` | round |
| `RETURN_ON_CAPITAL_EMPLOYED_FQ` | Return on Capital Employed % (MRQ) | `return_on_capital_employed_fq` | percent |
| `RETURN_ON_CAPITAL_EMPLOYED_FY` | Return on Capital Employed FY | `return_on_capital_employed_fy` | percent |
| `RETURN_ON_COMMON_EQUITY_FY` | Return on Common Equity FY | `return_on_common_equity_fy` | percent |
| `RETURN_ON_COMMON_EQUITY_TTM` | Return on Common Equity % (TTM) | `return_on_common_equity_ttm` | percent |
| `RETURN_ON_EQUITY_ADJUST_TO_BOOK_FY` | Return on Equity Adjust to Book FY | `return_on_equity_adjust_to_book_fy` | percent |
| `RETURN_ON_EQUITY_ADJUST_TO_BOOK_TTM` | Return on Equity Adjust to Book TTM | `return_on_equity_adjust_to_book_ttm` | percent |
| `RETURN_ON_EQUITY_FQ` | Return on Equity % (MRQ) | `return_on_equity_fq` | percent |
| `RETURN_ON_EQUITY_FY` | Return on Equity FY | `return_on_equity_fy` | percent |
| `RETURN_ON_EQUITY_TTM` | Return on Equity (TTM) | `return_on_equity` | round |
| `RETURN_ON_INVESTED_CAPITAL_FQ` | Return on Invested Capital % (MRQ) | `return_on_invested_capital_fq` | percent |
| `RETURN_ON_INVESTED_CAPITAL_FY` | Return on Invested Capital FY | `return_on_invested_capital_fy` | percent |
| `RETURN_ON_INVESTED_CAPITAL_TTM` | Return on Invested Capital (TTM) | `return_on_invested_capital` | percent |
| `RETURN_ON_TANG_ASSETS_FQ` | Return on Tangible Assets % (MRQ) | `return_on_tang_assets_fq` | percent |
| `RETURN_ON_TANG_ASSETS_FY` | Return on Tangible Assets % (FY) | `return_on_tang_assets_fy` | percent |
| `RETURN_ON_TANG_EQUITY_FQ` | Return on Tangible Equity % (MRQ) | `return_on_tang_equity_fq` | percent |
| `RETURN_ON_TANG_EQUITY_FY` | Return on Tangible Equity % (FY) | `return_on_tang_equity_fy` | percent |
| `RETURN_ON_TOTAL_CAPITAL_FQ` | Return on Total Capital % (MRQ) | `return_on_total_capital_fq` | percent |
| `RETURN_ON_TOTAL_CAPITAL_FY` | Return on Total Capital FY | `return_on_total_capital_fy` | percent |

## Growth Metrics

*37 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `CAPITAL_EXPENDITURES_QOQ_GROWTH_FQ` | Capital Expenditures QOQ Growth FQ | `capital_expenditures_qoq_growth_fq` | percent |
| `CAPITAL_EXPENDITURES_YOY_GROWTH_FQ` | Capital Expenditures YOY Growth FQ | `capital_expenditures_yoy_growth_fq` | percent |
| `CAPITAL_EXPENDITURES_YOY_GROWTH_FY` | Capital Expenditures Growth % (YoY) | `capital_expenditures_yoy_growth_fy` | percent |
| `CAPITAL_EXPENDITURES_YOY_GROWTH_TTM` | Capital Expenditures YOY Growth TTM | `capital_expenditures_yoy_growth_ttm` | percent |
| `DIVIDENDS_PER_SHARE_ANNUAL_YOY_GROWTH` | Dividends per share (Annual YoY Growth) | `dps_common_stock_prim_issue_yoy_growth_fy` | percent |
| `EARNINGS_PER_SHARE_DILUTED_5Y_GROWTH_FY` | Earnings per Share Diluted 5y Growth FY | `earnings_per_share_diluted_5y_growth_fy` | percent |
| `EBITDA_ANNUAL_YOY_GROWTH` | EBITDA (Annual YoY Growth) | `ebitda_yoy_growth_fy` | percent |
| `EBITDA_QUARTERLY_QOQ_GROWTH` | EBITDA (Quarterly QoQ Growth) | `ebitda_qoq_growth_fq` | percent |
| `EBITDA_QUARTERLY_YOY_GROWTH` | EBITDA (Quarterly YoY Growth) | `ebitda_yoy_growth_fq` | percent |
| `EBITDA_TTM_YOY_GROWTH` | EBITDA (TTM YoY Growth) | `ebitda_yoy_growth_ttm` | percent |
| `EPS_DILUTED_ANNUAL_YOY_GROWTH` | EPS Diluted (Annual YoY Growth) | `earnings_per_share_diluted_yoy_growth_fy` | percent |
| `EPS_DILUTED_GROWTH_PERCENT_FQ` | EPS Diluted Growth Percent FQ | `eps_diluted_growth_percent_fq` | percent |
| `EPS_DILUTED_GROWTH_PERCENT_FY` | EPS Diluted Growth Percent FY | `eps_diluted_growth_percent_fy` | percent |
| `EPS_DILUTED_QUARTERLY_QOQ_GROWTH` | EPS Diluted (Quarterly QoQ Growth) | `earnings_per_share_diluted_qoq_growth_fq` | percent |
| `EPS_DILUTED_QUARTERLY_YOY_GROWTH` | EPS Diluted (Quarterly YoY Growth) | `earnings_per_share_diluted_yoy_growth_fq` | percent |
| `EPS_DILUTED_TTM_YOY_GROWTH` | EPS Diluted (TTM YoY Growth) | `earnings_per_share_diluted_yoy_growth_ttm` | percent |
| `GROSS_PROFIT_ANNUAL_YOY_GROWTH` | Gross Profit (Annual YoY Growth) | `gross_profit_yoy_growth_fy` | percent |
| `GROSS_PROFIT_QUARTERLY_QOQ_GROWTH` | Gross Profit (Quarterly QoQ Growth) | `gross_profit_qoq_growth_fq` | percent |
| `GROSS_PROFIT_QUARTERLY_YOY_GROWTH` | Gross Profit (Quarterly YoY Growth) | `gross_profit_yoy_growth_fq` | percent |
| `GROSS_PROFIT_TTM_YOY_GROWTH` | Gross Profit (TTM YoY Growth) | `gross_profit_yoy_growth_ttm` | percent |
| `NET_INCOME_ANNUAL_YOY_GROWTH` | Net Income (Annual YoY Growth) | `net_income_yoy_growth_fy` | percent |
| `NET_INCOME_QUARTERLY_QOQ_GROWTH` | Net Income (Quarterly QoQ Growth) | `net_income_qoq_growth_fq` | percent |
| `NET_INCOME_QUARTERLY_YOY_GROWTH` | Net Income (Quarterly YoY Growth) | `net_income_yoy_growth_fq` | percent |
| `NET_INCOME_TTM_YOY_GROWTH` | Net Income (TTM YoY Growth) | `net_income_yoy_growth_ttm` | percent |
| `REVENUE_ANNUAL_YOY_GROWTH` | Revenue (Annual YoY Growth) | `total_revenue_yoy_growth_fy` | percent |
| `REVENUE_QUARTERLY_QOQ_GROWTH` | Revenue (Quarterly QoQ Growth) | `total_revenue_qoq_growth_fq` | percent |
| `REVENUE_QUARTERLY_YOY_GROWTH` | Revenue (Quarterly YoY Growth) | `total_revenue_yoy_growth_fq` | percent |
| `REVENUE_TTM_YOY_GROWTH` | Revenue (TTM YoY Growth) | `total_revenue_yoy_growth_ttm` | percent |
| `SUSTAINABLE_GROWTH_RATE_FY` | Sustainable Growth Rate FY | `sustainable_growth_rate_fy` | percent |
| `SUSTAINABLE_GROWTH_RATE_TTM` | Sustainable Growth Rate (TTM) | `sustainable_growth_rate_ttm` | percent |
| `TOTAL_ASSETS_ANNUAL_YOY_GROWTH` | Total Assets (Annual YoY Growth) | `total_assets_yoy_growth_fy` | percent |
| `TOTAL_ASSETS_QUARTERLY_QOQ_GROWTH` | Total Assets (Quarterly QoQ Growth) | `total_assets_qoq_growth_fq` | percent |
| `TOTAL_ASSETS_QUARTERLY_YOY_GROWTH` | Total Assets (Quarterly YoY Growth) | `total_assets_yoy_growth_fq` | percent |
| `TOTAL_DEBT_ANNUAL_YOY_GROWTH` | Total Debt (Annual YoY Growth) | `total_debt_yoy_growth_fy` | percent |
| `TOTAL_DEBT_QUARTERLY_QOQ_GROWTH` | Total Debt (Quarterly QoQ Growth) | `total_debt_qoq_growth_fq` | percent |
| `TOTAL_DEBT_QUARTERLY_YOY_GROWTH` | Total Debt (Quarterly YoY Growth) | `total_debt_yoy_growth_fq` | percent |
| `TOTAL_REVENUE_5Y_GROWTH_FY` | Total Revenue 5y Growth FY | `total_revenue_5y_growth_fy` | percent |

## Dividends & Yield

*44 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `BUYBACK_YIELD` | Buyback Yield % | `buyback_yield` | percent |
| `CASH_DIVIDEND_COVERAGE_RATIO_FY` | Cash Dividend Coverage Ratio (FY) | `cash_dividend_coverage_ratio_fy` | round |
| `CASH_DIVIDEND_COVERAGE_RATIO_TTM` | Cash Dividend Coverage Ratio (TTM) | `cash_dividend_coverage_ratio_ttm` | round |
| `DIVIDENDS_FREQUENCY` | Dividends Frequency | `dividends_frequency` | text |
| `DIVIDENDS_PAID_FY` | Dividends Paid (FY) | `dividends_paid` | currency |
| `DIVIDENDS_PER_SHARE_MRQ` | Dividends per Share (MRQ) | `dividends_per_share_fq` | currency |
| `DIVIDENDS_YIELD` | Dividend Yield % | `dividends_yield` | percent |
| `DIVIDENDS_YIELD_CURRENT` | Dividend Yield % (Current) | `dividends_yield_current` | percent |
| `DIVIDENDS_YIELD_FQ` | Dividends Yield FQ | `dividends_yield_fq` | percent |
| `DIVIDENDS_YIELD_FY` | Dividends Yield FY | `dividends_yield_fy` | percent |
| `DIVIDEND_AMOUNT_RECENT` | Dividend Amount Recent | `dividend_amount_recent` | currency |
| `DIVIDEND_AMOUNT_UPCOMING` | Dividend Amount Upcoming | `dividend_amount_upcoming` | currency |
| `DIVIDEND_EX_DATE_RECENT` | Dividend Ex Date Recent | `dividend_ex_date_recent` | date |
| `DIVIDEND_EX_DATE_UPCOMING` | Dividend Ex Date Upcoming | `dividend_ex_date_upcoming` | date |
| `DIVIDEND_FREQUENCY_RECENT` | Dividend Frequency Recent | `dividend_frequency_recent` | text |
| `DIVIDEND_FREQUENCY_UPCOMING` | Dividend Frequency Upcoming | `dividend_frequency_upcoming` | text |
| `DIVIDEND_PAYMENT_DATE_RECENT` | Dividend Payment Date Recent | `dividend_payment_date_recent` | date |
| `DIVIDEND_PAYMENT_DATE_UPCOMING` | Dividend Payment Date Upcoming | `dividend_payment_date_upcoming` | date |
| `DIVIDEND_PAYOUT_RATIO_FY` | Dividend Payout Ratio FY | `dividend_payout_ratio_fy` | percent |
| `DIVIDEND_PAYOUT_RATIO_PERCENT_FQ` | Dividend Payout Ratio Percent FQ | `dividend_payout_ratio_percent_fq` | percent |
| `DIVIDEND_PAYOUT_RATIO_PERCENT_FY` | Dividend Payout Ratio Percent FY | `dividend_payout_ratio_percent_fy` | percent |
| `DIVIDEND_PAYOUT_RATIO_TTM` | Dividend Payout Ratio (TTM) | `dividend_payout_ratio_ttm` | percent |
| `DIVIDEND_TREATMENT` | Dividend Treatment | `dividend_treatment` | text |
| `DIVIDEND_YIELD_FORWARD` | Dividend Yield Forward | `dividend_yield_recent` | percent |
| `DIVIDEND_YIELD_UPCOMING` | Dividend Yield Upcoming | `dividend_yield_upcoming` | round |
| `EARNINGS_YIELD` | Earnings Yield % | `earnings_yield` | percent |
| `EXPECTED_ANNUAL_DIVIDENDS` | Expected Annual Dividends | `expected_annual_dividends` | round |
| `EX_DIVIDEND_DATE_RECENT` | Ex Dividend Date Recent | `ex_dividend_date_recent` | date |
| `EX_DIVIDEND_DATE_UPCOMING` | Ex Dividend Date Upcoming | `ex_dividend_date_upcoming` | date |
| `INDICATED_ANNUAL_DIVIDEND` | Indicated Annual Dividend | `indicated_annual_dividend` | currency |
| `NEG_TOTAL_CASH_DIVIDENDS_PAID_FH` | Neg Total Cash Dividends Paid Fh | `neg_total_cash_dividends_paid_fh` | currency |
| `NEG_TOTAL_CASH_DIVIDENDS_PAID_FQ` | Neg Total Cash Dividends Paid FQ | `neg_total_cash_dividends_paid_fq` | currency |
| `NEG_TOTAL_CASH_DIVIDENDS_PAID_FY` | Neg Total Cash Dividends Paid FY | `neg_total_cash_dividends_paid_fy` | currency |
| `NEG_TOTAL_CASH_DIVIDENDS_PAID_TTM` | Neg Total Cash Dividends Paid TTM | `neg_total_cash_dividends_paid_ttm` | currency |
| `NEXT_DIVIDEND_DATE` | Next Dividend Date | `next_dividend_date` | date |
| `PREFERRED_DIVIDENDS` | Preferred Dividends | `preferred_dividends` | round |
| `RATES_DIVIDEND_RECENT` | Rates Dividend Recent | `rates_dividend_recent` | text |
| `RATES_DIVIDEND_UPCOMING` | Rates Dividend Upcoming | `rates_dividend_upcoming` | text |
| `TOTAL_CASH_DIVIDENDS_PAID_FH` | Total Cash Dividends Paid Fh | `total_cash_dividends_paid_fh` | currency |
| `TOTAL_CASH_DIVIDENDS_PAID_FQ` | Total Cash Dividends Paid FQ | `total_cash_dividends_paid_fq` | currency |
| `TOTAL_CASH_DIVIDENDS_PAID_FY` | Total Cash Dividends Paid FY | `total_cash_dividends_paid_fy` | currency |
| `TOTAL_CASH_DIVIDENDS_PAID_TTM` | Total Cash Dividends Paid (TTM) | `total_cash_dividends_paid_ttm` | currency |
| `YIELD_RECENT` | Yield Recent | `yield_recent` | round |
| `YIELD_UPCOMING` | Yield Upcoming | `yield_upcoming` | round |

## Earnings & Income

*86 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `BASIC_EPS_FY` | Basic EPS (FY) | `basic_eps_net_income` | currency |
| `BASIC_EPS_TTM` | Basic EPS (TTM) | `earnings_per_share_basic_ttm` | currency |
| `EARNINGS_PER_SHARE_BASIC_CAGR_5Y` | Earnings per Share Basic Cagr 5y | `earnings_per_share_basic_cagr_5y` | percent |
| `EARNINGS_PER_SHARE_BASIC_FH` | Earnings per Share Basic Fh | `earnings_per_share_basic_fh` | currency |
| `EARNINGS_PER_SHARE_BASIC_FQ` | Earnings per Share Basic FQ | `earnings_per_share_basic_fq` | currency |
| `EARNINGS_PER_SHARE_BASIC_FY` | Earnings per Share Basic FY | `earnings_per_share_basic_fy` | currency |
| `EARNINGS_PER_SHARE_BASIC_FY_H` | Earnings per Share Basic FY H | `earnings_per_share_basic_fy_h` | round |
| `EARNINGS_PER_SHARE_BASIC_TTM` | EPS Basic (TTM) | `earnings_per_share_basic_ttm` | currency |
| `EARNINGS_PER_SHARE_DILUTED_FH` | Earnings per Share Diluted Fh | `earnings_per_share_diluted_fh` | currency |
| `EARNINGS_PER_SHARE_DILUTED_FQ` | Earnings per Share Diluted FQ | `earnings_per_share_diluted_fq` | currency |
| `EARNINGS_PER_SHARE_DILUTED_FQ_H` | Earnings per Share Diluted FQ H | `earnings_per_share_diluted_fq_h` | round |
| `EARNINGS_PER_SHARE_DILUTED_FY` | Earnings per Share Diluted FY | `earnings_per_share_diluted_fy` | currency |
| `EARNINGS_PER_SHARE_DILUTED_FY_H` | Earnings per Share Diluted FY H | `earnings_per_share_diluted_fy_h` | round |
| `EARNINGS_PER_SHARE_DILUTED_TTM_H` | Earnings per Share Diluted TTM H | `earnings_per_share_diluted_ttm_h` | round |
| `EARNINGS_PER_SHARE_FH` | Earnings per Share Fh | `earnings_per_share_fh` | currency |
| `EARNINGS_PER_SHARE_FORECAST_FQ` | Earnings per Share Forecast FQ | `earnings_per_share_forecast_fq` | currency |
| `EARNINGS_PER_SHARE_FORECAST_NEXT_FH` | Earnings per Share Forecast Next Fh | `earnings_per_share_forecast_next_fh` | currency |
| `EARNINGS_PER_SHARE_FORECAST_NEXT_FY` | Earnings per Share Forecast Next FY | `earnings_per_share_forecast_next_fy` | currency |
| `EARNINGS_PER_SHARE_FY` | Earnings per Share FY | `earnings_per_share_fy` | currency |
| `EARNINGS_PUBLICATION_TYPE_FQ` | Earnings Publication Type FQ | `earnings_publication_type_fq` | round |
| `EARNINGS_PUBLICATION_TYPE_NEXT_FQ` | Earnings Publication Type Next FQ | `earnings_publication_type_next_fq` | round |
| `EARNINGS_RELEASE_CALENDAR_DATE` | Earnings Release Calendar Date | `earnings_release_calendar_date` | date |
| `EARNINGS_RELEASE_NEXT_CALENDAR_DATE` | Earnings Release Next Calendar Date | `earnings_release_next_calendar_date` | date |
| `EARNINGS_RELEASE_NEXT_TIME` | Earnings Release Next Time | `earnings_release_next_time` | round |
| `EARNINGS_RELEASE_NEXT_TRADING_DATE_FQ` | Earnings Release Next Trading Date FQ | `earnings_release_next_trading_date_fq` | date |
| `EARNINGS_RELEASE_NEXT_TRADING_DATE_FY` | Earnings Release Next Trading Date FY | `earnings_release_next_trading_date_fy` | date |
| `EARNINGS_RELEASE_TIME` | Earnings Release Time | `earnings_release_time` | round |
| `EARNINGS_RELEASE_TRADING_DATE_FQ` | Earnings Release Trading Date FQ | `earnings_release_trading_date_fq` | date |
| `EARNINGS_RELEASE_TRADING_DATE_FY` | Earnings Release Trading Date FY | `earnings_release_trading_date_fy` | date |
| `EBITDA_FH` | EBITDA Fh | `ebitda_fh` | currency |
| `EBITDA_FQ` | EBITDA FQ | `ebitda_fq` | currency |
| `EBITDA_FQ_H` | EBITDA FQ H | `ebitda_fq_h` | round |
| `EBITDA_FY` | EBITDA FY | `ebitda_fy` | currency |
| `EBITDA_FY_H` | EBITDA FY H | `ebitda_fy_h` | round |
| `EBITDA_INTERST_COVER_FY` | EBITDA Interest Coverage (FY) | `ebitda_interst_cover_fy` | round |
| `EBITDA_INTERST_COVER_TTM` | EBITDA Interest Coverage (TTM) | `ebitda_interst_cover_ttm` | round |
| `EBITDA_LESS_CAPEX_INTERST_COVER_FY` | EBITDA Less CapEx Interest Coverage (FY) | `ebitda_less_capex_interst_cover_fy` | round |
| `EBITDA_LESS_CAPEX_INTERST_COVER_TTM` | EBITDA Less CapEx Interest Coverage (TTM) | `ebitda_less_capex_interst_cover_ttm` | round |
| `EBITDA_PER_EMPLOYEE_FY` | EBITDA per Employee (FY) | `ebitda_per_employee_fy` | currency |
| `EBITDA_PER_SHARE_CURRENT` | EBITDA per Share Current | `ebitda_per_share_current` | currency |
| `EBITDA_PER_SHARE_FH` | EBITDA per Share Fh | `ebitda_per_share_fh` | currency |
| `EBITDA_PER_SHARE_FQ` | EBITDA per Share FQ | `ebitda_per_share_fq` | currency |
| `EBITDA_PER_SHARE_FY` | EBITDA per Share FY | `ebitda_per_share_fy` | currency |
| `EBITDA_PER_SHARE_TTM` | EBITDA per Share (TTM) | `ebitda_per_share_ttm` | currency |
| `EBITDA_TTM` | EBITDA (TTM) | `ebitda` | currency |
| `EBITDA_TTM_2` | EBITDA TTM | `ebitda_ttm` | currency |
| `EBITDA_TTM_H` | EBITDA TTM H | `ebitda_ttm_h` | round |
| `EBIT_PER_SHARE_CURRENT` | EBIT per Share Current | `ebit_per_share_current` | currency |
| `EBIT_PER_SHARE_FH` | EBIT per Share Fh | `ebit_per_share_fh` | currency |
| `EBIT_PER_SHARE_FQ` | EBIT per Share FQ | `ebit_per_share_fq` | currency |
| `EBIT_PER_SHARE_FY` | EBIT per Share FY | `ebit_per_share_fy` | currency |
| `EBIT_PER_SHARE_TTM` | EBIT per Share (TTM) | `ebit_per_share_ttm` | currency |
| `EBIT_TTM` | EBIT TTM | `ebit_ttm` | currency |
| `EPS_DILUTED_FY` | EPS Diluted (FY) | `last_annual_eps` | currency |
| `EPS_DILUTED_MRQ` | EPS Diluted (MRQ) | `earnings_per_share_fq` | currency |
| `EPS_DILUTED_TTM` | EPS Diluted (TTM) | `earnings_per_share_diluted_ttm` | currency |
| `EPS_FORECAST_MRQ` | EPS Forecast (MRQ) | `earnings_per_share_forecast_next_fq` | currency |
| `EPS_SURPRISE_FQ` | EPS Surprise FQ | `eps_surprise_fq` | currency |
| `EPS_SURPRISE_PERCENT_FQ` | EPS Surprise Percent FQ | `eps_surprise_percent_fq` | percent |
| `GROSS_PROFIT_FH` | Gross Profit Fh | `gross_profit_fh` | currency |
| `GROSS_PROFIT_FQ_H` | Gross Profit FQ H | `gross_profit_fq_h` | round |
| `GROSS_PROFIT_FY` | Gross Profit (FY) | `gross_profit` | currency |
| `GROSS_PROFIT_FY_2` | Gross Profit FY | `gross_profit_fy` | currency |
| `GROSS_PROFIT_FY_H` | Gross Profit FY H | `gross_profit_fy_h` | round |
| `GROSS_PROFIT_MRQ` | Gross Profit (MRQ) | `gross_profit_fq` | currency |
| `GROSS_PROFIT_TTM` | Gross Profit TTM | `gross_profit_ttm` | currency |
| `GROSS_PROFIT_TTM_H` | Gross Profit TTM H | `gross_profit_ttm_h` | round |
| `NET_DEBT_TO_EBITDA_FQ` | Net Debt to EBITDA (MRQ) | `net_debt_to_ebitda_fq` | round |
| `NET_DEBT_TO_EBITDA_FY` | Net Debt to EBITDA FY | `net_debt_to_ebitda_fy` | round |
| `NET_INCOME_BEF_DISC_OPER_FY` | Net Income Bef Disc Oper FY | `net_income_bef_disc_oper_fy` | currency |
| `NET_INCOME_CAGR_5Y` | Net Income Cagr 5y | `net_income_cagr_5y` | percent |
| `NET_INCOME_FH` | Net Income Fh | `net_income_fh` | currency |
| `NET_INCOME_FQ` | Net Income FQ | `net_income_fq` | currency |
| `NET_INCOME_FQ_H` | Net Income FQ H | `net_income_fq_h` | round |
| `NET_INCOME_FY` | Net Income (FY) | `net_income` | currency |
| `NET_INCOME_FY_2` | Net Income FY | `net_income_fy` | currency |
| `NET_INCOME_FY_H` | Net Income FY H | `net_income_fy_h` | round |
| `NET_INCOME_PER_EMPLOYEE_FY` | Net Income per Employee (FY) | `net_income_per_employee_fy` | currency |
| `NET_INCOME_TTM` | Net Income TTM | `net_income_ttm` | currency |
| `NET_INCOME_TTM_H` | Net Income TTM H | `net_income_ttm_h` | round |
| `RATES_EARNINGS_FQ` | Rates Earnings FQ | `rates_earnings_fq` | text |
| `RATES_EARNINGS_NEXT_FQ` | Rates Earnings Next FQ | `rates_earnings_next_fq` | text |
| `RECENT_EARNINGS_DATE` | Recent Earnings Date | `earnings_release_date` | date |
| `TOTAL_DEBT_TO_EBITDA_FQ` | Total Debt to EBITDA FQ | `total_debt_to_ebitda_fq` | round |
| `TOTAL_DEBT_TO_EBITDA_FY` | Total Debt to EBITDA FY | `total_debt_to_ebitda_fy` | round |
| `UPCOMING_EARNINGS_DATE` | Upcoming Earnings Date | `earnings_release_next_date` | date |

## Revenue & Sales

*25 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `LAST_YEAR_REVENUE_FY` | Last Year Revenue (FY) | `last_annual_revenue` | currency |
| `REVENUE_FORECAST_FQ` | Revenue Estimate (MRQ) | `revenue_forecast_fq` | currency |
| `REVENUE_FORECAST_NEXT_FH` | Revenue Forecast Next Fh | `revenue_forecast_next_fh` | currency |
| `REVENUE_FORECAST_NEXT_FQ` | Revenue Forecast Next FQ | `revenue_forecast_next_fq` | currency |
| `REVENUE_FORECAST_NEXT_FY` | Revenue Forecast Next FY | `revenue_forecast_next_fy` | currency |
| `REVENUE_FQ` | Revenue FQ | `revenue_fq` | currency |
| `REVENUE_PER_EMPLOYEE_FY` | Revenue per Employee (FY) | `revenue_per_employee` | currency |
| `REVENUE_PER_EMPLOYEE_FY_2` | Revenue per Employee FY | `revenue_per_employee_fy` | currency |
| `REVENUE_PER_SHARE_CURRENT` | Revenue per Share Current | `revenue_per_share_current` | currency |
| `REVENUE_PER_SHARE_FH` | Revenue per Share Fh | `revenue_per_share_fh` | currency |
| `REVENUE_PER_SHARE_FQ` | Revenue per Share FQ | `revenue_per_share_fq` | currency |
| `REVENUE_PER_SHARE_FY` | Revenue per Share (FY) | `revenue_per_share_fy` | currency |
| `REVENUE_PER_SHARE_TTM` | Revenue per Share (TTM) | `revenue_per_share_ttm` | currency |
| `REVENUE_SURPRISE_FQ` | Revenue Surprise FQ | `revenue_surprise_fq` | currency |
| `REVENUE_SURPRISE_PERCENT_FQ` | Revenue Surprise Percent FQ | `revenue_surprise_percent_fq` | percent |
| `TOP_REVENUE_COUNTRY_CODE` | Top Revenue Country Code | `top_revenue_country_code` | text |
| `TOTAL_REVENUE_CAGR_5Y` | Total Revenue Cagr 5y | `total_revenue_cagr_5y` | percent |
| `TOTAL_REVENUE_FH` | Total Revenue Fh | `total_revenue_fh` | currency |
| `TOTAL_REVENUE_FQ` | Total Revenue FQ | `total_revenue_fq` | currency |
| `TOTAL_REVENUE_FQ_H` | Total Revenue FQ H | `total_revenue_fq_h` | round |
| `TOTAL_REVENUE_FY` | Total Revenue (FY) | `total_revenue` | currency |
| `TOTAL_REVENUE_FY_2` | Total Revenue FY | `total_revenue_fy` | currency |
| `TOTAL_REVENUE_FY_H` | Total Revenue FY H | `total_revenue_fy_h` | round |
| `TOTAL_REVENUE_TTM` | Total Revenue TTM | `total_revenue_ttm` | currency |
| `TOTAL_REVENUE_TTM_H` | Total Revenue TTM H | `total_revenue_ttm_h` | round |

## Balance Sheet

*103 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `BOOK_VALUE_PER_SHARE_CURRENT` | Book Value per Share Current | `book_value_per_share_current` | currency |
| `BOOK_VALUE_PER_SHARE_FH` | Book Value per Share Fh | `book_value_per_share_fh` | currency |
| `BOOK_VALUE_PER_SHARE_FQ` | Book Value per Share (MRQ) | `book_value_per_share_fq` | currency |
| `BOOK_VALUE_PER_SHARE_FY` | Book Value per Share FY | `book_value_per_share_fy` | currency |
| `CAPITAL_EXPENDITURES_FH` | Capital Expenditures Fh | `capital_expenditures_fh` | currency |
| `CAPITAL_EXPENDITURES_FQ` | Capital Expenditures (MRQ) | `capital_expenditures_fq` | currency |
| `CAPITAL_EXPENDITURES_FY` | Capital Expenditures (FY) | `capital_expenditures_fy` | currency |
| `CAPITAL_EXPENDITURES_TTM` | Capital Expenditures (TTM) | `capital_expenditures_ttm` | currency |
| `CAPITAL_EXPENDITURES_UNCHANGED_FQ_H` | Capital Expenditures Unchanged FQ H | `capital_expenditures_unchanged_fq_h` | round |
| `CAPITAL_EXPENDITURES_UNCHANGED_FY_H` | Capital Expenditures Unchanged FY H | `capital_expenditures_unchanged_fy_h` | round |
| `CAPITAL_EXPENDITURES_UNCHANGED_TTM_H` | Capital Expenditures Unchanged TTM H | `capital_expenditures_unchanged_ttm_h` | round |
| `CASH_AND_EQUIVALENTS_FY` | Cash & Equivalents (FY) | `cash_n_equivalents_fy` | currency |
| `CASH_AND_EQUIVALENTS_MRQ` | Cash & Equivalents (MRQ) | `cash_n_equivalents_fq` | currency |
| `CASH_AND_SHORT_TERM_INVESTMENTS_FY` | Cash and short term investments (FY) | `cash_n_short_term_invest_fy` | currency |
| `CASH_AND_SHORT_TERM_INVESTMENTS_MRQ` | Cash and short term investments (MRQ) | `cash_n_short_term_invest_fq` | currency |
| `CASH_F_FINANCING_ACTIVITIES_FH` | Cash f Financing Activities Fh | `cash_f_financing_activities_fh` | currency |
| `CASH_F_FINANCING_ACTIVITIES_FQ` | Cash f Financing Activities FQ | `cash_f_financing_activities_fq` | currency |
| `CASH_F_FINANCING_ACTIVITIES_FY` | Cash from Financing Activities (FY) | `cash_f_financing_activities_fy` | currency |
| `CASH_F_FINANCING_ACTIVITIES_TTM` | Cash from Financing Activities (TTM) | `cash_f_financing_activities_ttm` | currency |
| `CASH_F_INVESTING_ACTIVITIES_FH` | Cash f Investing Activities Fh | `cash_f_investing_activities_fh` | currency |
| `CASH_F_INVESTING_ACTIVITIES_FQ` | Cash f Investing Activities FQ | `cash_f_investing_activities_fq` | currency |
| `CASH_F_INVESTING_ACTIVITIES_FY` | Cash from Investing Activities (FY) | `cash_f_investing_activities_fy` | currency |
| `CASH_F_INVESTING_ACTIVITIES_TTM` | Cash from Investing Activities (TTM) | `cash_f_investing_activities_ttm` | currency |
| `CASH_F_OPERATING_ACTIVITIES_FH` | Cash f Operating Activities Fh | `cash_f_operating_activities_fh` | currency |
| `CASH_F_OPERATING_ACTIVITIES_FQ` | Cash f Operating Activities FQ | `cash_f_operating_activities_fq` | currency |
| `CASH_F_OPERATING_ACTIVITIES_FY` | Cash from Operating Activities (FY) | `cash_f_operating_activities_fy` | currency |
| `CASH_F_OPERATING_ACTIVITIES_TTM` | Cash from Operating Activities (TTM) | `cash_f_operating_activities_ttm` | currency |
| `CASH_N_SHORT_TERM_INVEST_TO_TOTAL_CURRENT_LIABILITIES_FQ` | Cash n Short Term Invest to Total Current Liabilities FQ | `cash_n_short_term_invest_to_total_current_liabilities_fq` | round |
| `CASH_N_SHORT_TERM_INVEST_TO_TOTAL_CURRENT_LIABILITIES_FY` | Cash Ratio (FY) | `cash_n_short_term_invest_to_total_current_liabilities_fy` | round |
| `CASH_N_SHORT_TERM_INVEST_TO_TOTAL_DEBT_FQ` | Cash to Debt Ratio (MRQ) | `cash_n_short_term_invest_to_total_debt_fq` | round |
| `CASH_N_SHORT_TERM_INVEST_TO_TOTAL_DEBT_FY` | Cash to Debt Ratio (FY) | `cash_n_short_term_invest_to_total_debt_fy` | round |
| `CASH_PER_SHARE_CURRENT` | Cash per Share Current | `cash_per_share_current` | currency |
| `CASH_PER_SHARE_FH` | Cash per Share Fh | `cash_per_share_fh` | currency |
| `CASH_PER_SHARE_FQ` | Cash per Share (MRQ) | `cash_per_share_fq` | currency |
| `CASH_PER_SHARE_FY` | Cash per Share FY | `cash_per_share_fy` | currency |
| `CASH_RATIO` | Cash Ratio | `cash_ratio` | round |
| `DEBT_TO_ASSETS` | Debt to Assets | `debt_to_assets` | round |
| `DEBT_TO_ASSET_FQ` | Debt to Assets (MRQ) | `debt_to_asset_fq` | percent |
| `DEBT_TO_ASSET_FY` | Debt to Assets (FY) | `debt_to_asset_fy` | percent |
| `DEBT_TO_EQUITY_FQ` | Debt to Equity FQ | `debt_to_equity_fq` | round |
| `DEBT_TO_EQUITY_FY` | Debt to Equity FY | `debt_to_equity_fy` | round |
| `DEBT_TO_EQUITY_RATIO_MRQ` | Debt to Equity Ratio (MRQ) | `debt_to_equity` | round |
| `DEBT_TO_REVENUE_FY` | Debt to Revenue FY | `debt_to_revenue_fy` | round |
| `DEBT_TO_REVENUE_TTM` | Debt to Revenue (TTM) | `debt_to_revenue_ttm` | round |
| `EFFECTIVE_INTEREST_RATE_ON_DEBT_FY` | Effective Interest Rate on Debt (FY) | `effective_interest_rate_on_debt_fy` | percent |
| `EFFECTIVE_INTEREST_RATE_ON_DEBT_TTM` | Effective Interest Rate on Debt (TTM) | `effective_interest_rate_on_debt_ttm` | percent |
| `FIXED_ASSETS_TURNOVER_FQ` | Fixed Assets Turnover FQ | `fixed_assets_turnover_fq` | round |
| `FIXED_ASSETS_TURNOVER_FY` | Fixed Assets Turnover (FY) | `fixed_assets_turnover_fy` | round |
| `LONG_TERM_CAPITAL` | Long Term Capital | `long_term_capital` | round |
| `LONG_TERM_DEBT_FQ` | Long Term Debt (MRQ) | `long_term_debt_fq` | currency |
| `LONG_TERM_DEBT_FY` | Long Term Debt (FY) | `long_term_debt_fy` | currency |
| `LONG_TERM_DEBT_TO_ASSETS_FQ` | Long Term Debt to Assets FQ | `long_term_debt_to_assets_fq` | round |
| `LONG_TERM_DEBT_TO_ASSETS_FY` | Long Term Debt to Assets FY | `long_term_debt_to_assets_fy` | round |
| `LONG_TERM_DEBT_TO_EQUITY_FQ` | Long Term Debt to Equity FQ | `long_term_debt_to_equity_fq` | round |
| `NEG_CAPITAL_EXPENDITURES_FH` | Neg Capital Expenditures Fh | `neg_capital_expenditures_fh` | currency |
| `NEG_CAPITAL_EXPENDITURES_FQ` | Neg Capital Expenditures FQ | `neg_capital_expenditures_fq` | currency |
| `NEG_CAPITAL_EXPENDITURES_FY` | Neg Capital Expenditures FY | `neg_capital_expenditures_fy` | currency |
| `NEG_CAPITAL_EXPENDITURES_TTM` | Neg Capital Expenditures TTM | `neg_capital_expenditures_ttm` | currency |
| `NET_DEBT_FQ` | Net Debt FQ | `net_debt_fq` | currency |
| `NET_DEBT_FY` | Net Debt FY | `net_debt_fy` | currency |
| `NET_DEBT_MRQ` | Net Debt (MRQ) | `net_debt` | currency |
| `RETURN_OF_INVESTED_CAPITAL_PERCENT_TTM` | Return of Invested Capital Percent TTM | `return_of_invested_capital_percent_ttm` | percent |
| `SHORT_TERM_DEBT_FQ` | Short Term Debt (MRQ) | `short_term_debt_fq` | currency |
| `SHORT_TERM_DEBT_FY` | Short Term Debt (FY) | `short_term_debt_fy` | currency |
| `SHRHLDRS_EQUITY_FQ` | Shrhldrs Equity FQ | `shrhldrs_equity_fq` | currency |
| `SHRHLDRS_EQUITY_FY` | Shrhldrs Equity FY | `shrhldrs_equity_fy` | currency |
| `SHRHLDRS_EQUITY_TO_TOTAL_ASSETS_FQ` | Equity to Assets (MRQ) | `shrhldrs_equity_to_total_assets_fq` | percent |
| `SHRHLDRS_EQUITY_TO_TOTAL_ASSETS_FY` | Equity to Assets (FY) | `shrhldrs_equity_to_total_assets_fy` | percent |
| `TOTAL_ASSETS_FQ` | Total Assets FQ | `total_assets_fq` | currency |
| `TOTAL_ASSETS_FQ_H` | Total Assets FQ H | `total_assets_fq_h` | round |
| `TOTAL_ASSETS_FY` | Total Assets FY | `total_assets_fy` | currency |
| `TOTAL_ASSETS_FY_H` | Total Assets FY H | `total_assets_fy_h` | round |
| `TOTAL_ASSETS_MRQ` | Total Assets (MRQ) | `total_assets` | currency |
| `TOTAL_ASSETS_PER_EMPLOYEE_FY` | Total Assets per Employee (FY) | `total_assets_per_employee_fy` | currency |
| `TOTAL_ASSETS_TO_EQUITY_FQ` | Total Assets to Equity FQ | `total_assets_to_equity_fq` | round |
| `TOTAL_ASSETS_TO_EQUITY_FY` | Total Assets to Equity FY | `total_assets_to_equity_fy` | round |
| `TOTAL_CAPITAL` | Total Capital | `total_capital` | round |
| `TOTAL_CURRENT_ASSETS_FQ` | Total Current Assets FQ | `total_current_assets_fq` | currency |
| `TOTAL_CURRENT_ASSETS_FY` | Total Current Assets FY | `total_current_assets_fy` | currency |
| `TOTAL_CURRENT_ASSETS_MRQ` | Total Current Assets (MRQ) | `total_current_assets` | currency |
| `TOTAL_CURRENT_LIABILITIES_FQ` | Total Current Liabilities (MRQ) | `total_current_liabilities_fq` | currency |
| `TOTAL_CURRENT_LIABILITIES_FY` | Total Current Liabilities FY | `total_current_liabilities_fy` | currency |
| `TOTAL_DEBT_FQ` | Total Debt FQ | `total_debt_fq` | currency |
| `TOTAL_DEBT_FQ_H` | Total Debt FQ H | `total_debt_fq_h` | round |
| `TOTAL_DEBT_FY` | Total Debt FY | `total_debt_fy` | currency |
| `TOTAL_DEBT_FY_H` | Total Debt FY H | `total_debt_fy_h` | round |
| `TOTAL_DEBT_MRQ` | Total Debt (MRQ) | `total_debt` | currency |
| `TOTAL_DEBT_PER_EMPLOYEE_FY` | Total Debt per Employee (FY) | `total_debt_per_employee_fy` | currency |
| `TOTAL_DEBT_PER_SHARE_CURRENT` | Total Debt per Share Current | `total_debt_per_share_current` | currency |
| `TOTAL_DEBT_PER_SHARE_FH` | Total Debt per Share Fh | `total_debt_per_share_fh` | currency |
| `TOTAL_DEBT_PER_SHARE_FQ` | Total Debt per Share (MRQ) | `total_debt_per_share_fq` | currency |
| `TOTAL_DEBT_PER_SHARE_FY` | Total Debt per Share FY | `total_debt_per_share_fy` | currency |
| `TOTAL_DEBT_TO_CAPITAL_FQ` | Total Debt to Capital (MRQ) | `total_debt_to_capital_fq` | percent |
| `TOTAL_DEBT_TO_CAPITAL_FY` | Total Debt to Capital (FY) | `total_debt_to_capital_fy` | percent |
| `TOTAL_EQUITY_FQ` | Total Equity (MRQ) | `total_equity_fq` | currency |
| `TOTAL_EQUITY_FY` | Total Equity (FY) | `total_equity_fy` | currency |
| `TOTAL_LIABILITIES_FY` | Total Liabilities (FY) | `total_liabilities_fy` | currency |
| `TOTAL_LIABILITIES_MRQ` | Total Liabilities (MRQ) | `total_liabilities_fq` | currency |
| `WORKING_CAPITAL_FQ` | Working Capital FQ | `working_capital_fq` | currency |
| `WORKING_CAPITAL_PER_SHARE_CURRENT` | Working Capital per Share Current | `working_capital_per_share_current` | currency |
| `WORKING_CAPITAL_PER_SHARE_FH` | Working Capital per Share Fh | `working_capital_per_share_fh` | currency |
| `WORKING_CAPITAL_PER_SHARE_FQ` | Working Capital per Share (MRQ) | `working_capital_per_share_fq` | currency |
| `WORKING_CAPITAL_PER_SHARE_FY` | Working Capital per Share FY | `working_capital_per_share_fy` | currency |

## Cash Flow

*5 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `CAPEX_PER_SHARE_CURRENT` | Capex per Share Current | `capex_per_share_current` | currency |
| `CAPEX_PER_SHARE_FH` | Capex per Share Fh | `capex_per_share_fh` | currency |
| `CAPEX_PER_SHARE_FQ` | Capex per Share FQ | `capex_per_share_fq` | currency |
| `CAPEX_PER_SHARE_FY` | Capex per Share FY | `capex_per_share_fy` | currency |
| `CAPEX_PER_SHARE_TTM` | CapEx per Share (TTM) | `capex_per_share_ttm` | currency |

## Shares & Market Cap

*16 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `DILUTED_SHARES_OUTSTANDING_FQ` | Diluted Shares Outstanding FQ | `diluted_shares_outstanding_fq` | currency |
| `FLOAT_SHARES_OUTSTANDING_CURRENT` | Float Shares Outstanding Current | `float_shares_outstanding_current` | round |
| `FLOAT_SHARES_PERCENT_CURRENT` | Free Float % | `float_shares_percent_current` | percent |
| `IPO_MARKET_CAP_USD` | IPO Market Cap Usd | `ipo_market_cap_usd` | round |
| `IPO_OFFERED_SHARES` | IPO Offered Shares | `ipo_offered_shares` | round |
| `IPO_OFFERED_SHARES_PRIMARY` | IPO Offered Shares Primary | `ipo_offered_shares_primary` | round |
| `IPO_OFFERED_SHARES_SECONDARY` | IPO Offered Shares Secondary | `ipo_offered_shares_secondary` | round |
| `IPO_SHARES_OUTSTANDING` | IPO Shares Outstanding | `ipo_shares_outstanding` | round |
| `MARKET_CAPITALIZATION` | Market Capitalization | `market_cap_basic` | currency |
| `MARKET_CAP_CALC` | Market Cap Calc | `market_cap_calc` | round |
| `SHARES_FLOAT` | Shares Float | `float_shares_outstanding` | number_group |
| `SHARES_OUTSTANDING` | Shares Outstanding | `shares_outstanding` | round |
| `TOTAL_SHARES_OUTSTANDING` | Total Shares Outstanding | `total_shares_outstanding_fundamental` | number_group |
| `TOTAL_SHARES_OUTSTANDING_CALCULATED` | Total Shares Outstanding Calculated | `total_shares_outstanding_calculated` | round |
| `TOTAL_SHARES_OUTSTANDING_CURRENT` | Total Shares Outstanding Current | `total_shares_outstanding_current` | round |
| `TOTAL_SHARES_OUTSTANDING_RAW` | Total Shares Outstanding (Raw) | `total_shares_outstanding` | round |

## Bond Data

*4 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `COUPON` | Coupon | `coupon` | round |
| `DAYS_TO_MATURITY` | Days to Maturity | `days_to_maturity` | round |
| `ISSUER` | Issuer | `issuer` | text |
| `MATURITY_DATE` | Maturity Date | `maturity_date` | date |

## Crypto Data

*2 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `CRYPTOASSET_INFO_DESCRIPTION` | Cryptoasset-info Description | `cryptoasset-info.description` | text |
| `CRYPTOASSET_INFO_ID` | Cryptoasset-info Id | `cryptoasset-info.id` | text |

## DEX Data

*3 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `INDEXES` | Index Membership | `indexes` | text |
| `INDEX_PRIORITY` | Index Priority | `index_priority` | round |
| `INDEX_PROVIDER` | Index Provider | `index_provider` | text |

## Time & Dates

*43 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `FIRST_BAR_TIME` | First Bar Time | `first_bar_time` | date |
| `IPO_ANNOUNCEMENT_DATE` | IPO Announcement Date | `ipo_announcement_date` | date |
| `IPO_OFFER_DATE` | IPO Offer Date | `ipo_offer_date` | date |
| `IPO_OFFER_TIME` | IPO Offer Time | `ipo_offer_time` | date |
| `LAST_BAR_UPDATE_TIME` | Last Bar Update Time | `last_bar_update_time` | round |
| `LAST_BAR_UPDATE_TIME_1` | Last Bar Update Time\|1 | `last_bar_update_time\|1` | round |
| `LAST_BAR_UPDATE_TIME_120` | Last Bar Update Time\|120 | `last_bar_update_time\|120` | round |
| `LAST_BAR_UPDATE_TIME_15` | Last Bar Update Time\|15 | `last_bar_update_time\|15` | round |
| `LAST_BAR_UPDATE_TIME_1M` | Last Bar Update Time\|1m | `last_bar_update_time\|1M` | round |
| `LAST_BAR_UPDATE_TIME_1W` | Last Bar Update Time\|1w | `last_bar_update_time\|1W` | round |
| `LAST_BAR_UPDATE_TIME_240` | Last Bar Update Time\|240 | `last_bar_update_time\|240` | round |
| `LAST_BAR_UPDATE_TIME_30` | Last Bar Update Time\|30 | `last_bar_update_time\|30` | round |
| `LAST_BAR_UPDATE_TIME_5` | Last Bar Update Time\|5 | `last_bar_update_time\|5` | round |
| `LAST_BAR_UPDATE_TIME_60` | Last Bar Update Time\|60 | `last_bar_update_time\|60` | round |
| `LAUNCH_DATE` | Launch Date | `launch_date` | date |
| `MOST_RECENT_QUARTER_DATE` | Most Recent Quarter Date | `most_recent_quarter_date` | date |
| `PAYMENT_DATE_RECENT` | Payment Date Recent | `payment_date_recent` | date |
| `PAYMENT_DATE_UPCOMING` | Payment Date Upcoming | `payment_date_upcoming` | date |
| `POSTMARKET_TIME` | Postmarket Time | `postmarket_time` | date |
| `RATES_TIME_SERIES` | Rates Time Series | `rates_time_series` | text |
| `TIME` | Time | `time` | date |
| `TIME_1` | Time\|1 | `time\|1` | date |
| `TIME_120` | Time\|120 | `time\|120` | date |
| `TIME_15` | Time\|15 | `time\|15` | date |
| `TIME_1M` | Time\|1m | `time\|1M` | date |
| `TIME_1W` | Time\|1w | `time\|1W` | date |
| `TIME_240` | Time\|240 | `time\|240` | date |
| `TIME_30` | Time\|30 | `time\|30` | date |
| `TIME_5` | Time\|5 | `time\|5` | date |
| `TIME_60` | Time\|60 | `time\|60` | date |
| `TIME_BUSINESS_DAY` | Time Business Day | `time_business_day` | round |
| `UPDATE_MODE` | Update Mode | `update_mode` | text |
| `UPDATE_MODE_1` | Update Mode\|1 | `update_mode\|1` | text |
| `UPDATE_MODE_120` | Update Mode\|120 | `update_mode\|120` | text |
| `UPDATE_MODE_15` | Update Mode\|15 | `update_mode\|15` | text |
| `UPDATE_MODE_1M` | Update Mode\|1m | `update_mode\|1M` | text |
| `UPDATE_MODE_1W` | Update Mode\|1w | `update_mode\|1W` | text |
| `UPDATE_MODE_240` | Update Mode\|240 | `update_mode\|240` | text |
| `UPDATE_MODE_30` | Update Mode\|30 | `update_mode\|30` | text |
| `UPDATE_MODE_5` | Update Mode\|5 | `update_mode\|5` | text |
| `UPDATE_MODE_60` | Update Mode\|60 | `update_mode\|60` | text |
| `UPDATE_TIME` | Update-time | `update-time` | round |
| `UPDATE_TIME_2` | Update Time | `update_time` | date |

## Other

*263 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `ACTIVELY_MANAGED` | Actively Managed | `actively_managed` | text |
| `ADRP` | Adrp | `ADRP` | round |
| `ADRP_1` | Adrp\|1 | `ADRP\|1` | round |
| `ADRP_120` | Adrp\|120 | `ADRP\|120` | round |
| `ADRP_15` | Adrp\|15 | `ADRP\|15` | round |
| `ADRP_1M` | Adrp\|1m | `ADRP\|1M` | round |
| `ADRP_1W` | Adrp\|1w | `ADRP\|1W` | round |
| `ADRP_240` | Adrp\|240 | `ADRP\|240` | round |
| `ADRP_30` | Adrp\|30 | `ADRP\|30` | round |
| `ADRP_5` | Adrp\|5 | `ADRP\|5` | round |
| `ADRP_60` | Adrp\|60 | `ADRP\|60` | round |
| `ADR_1` | Adr\|1 | `ADR\|1` | round |
| `ADR_120` | Adr\|120 | `ADR\|120` | round |
| `ADR_15` | Adr\|15 | `ADR\|15` | round |
| `ADR_1M` | Adr\|1m | `ADR\|1M` | round |
| `ADR_1W` | Adr\|1w | `ADR\|1W` | round |
| `ADR_240` | Adr\|240 | `ADR\|240` | round |
| `ADR_30` | Adr\|30 | `ADR\|30` | round |
| `ADR_5` | Adr\|5 | `ADR\|5` | round |
| `ADR_60` | Adr\|60 | `ADR\|60` | round |
| `ALTMAN_Z_SCORE_FY` | Altman Z Score FY | `altman_z_score_fy` | round |
| `ALTMAN_Z_SCORE_TTM` | Altman Z-Score (TTM) | `altman_z_score_ttm` | round |
| `AMOUNT_RECENT` | Amount Recent | `amount_recent` | currency |
| `AMOUNT_UPCOMING` | Amount Upcoming | `amount_upcoming` | currency |
| `ASSET_CLASS` | Asset Class | `asset_class` | text |
| `ASSET_TURNOVER_CURRENT` | Asset Turnover Current | `asset_turnover_current` | round |
| `ASSET_TURNOVER_FY` | Asset Turnover (FY) | `asset_turnover_fy` | round |
| `AUM` | Aum | `aum` | currency |
| `AVERAGE_DAY_RANGE_14` | Average Day Range (14) | `ADR` | float |
| `AVGVALUE_TRADED_10D` | Avgvalue Traded 10d | `AvgValue.Traded_10d` | round |
| `AVGVALUE_TRADED_30D` | Avgvalue Traded 30d | `AvgValue.Traded_30d` | round |
| `AVGVALUE_TRADED_60D` | Avgvalue Traded 60d | `AvgValue.Traded_60d` | round |
| `AVGVALUE_TRADED_90D` | Avgvalue Traded 90d | `AvgValue.Traded_90d` | round |
| `BARS_COUNT` | Bars Count | `bars_count` | round |
| `BARS_COUNT_1` | Bars Count\|1 | `bars_count\|1` | round |
| `BARS_COUNT_120` | Bars Count\|120 | `bars_count\|120` | round |
| `BARS_COUNT_15` | Bars Count\|15 | `bars_count\|15` | round |
| `BARS_COUNT_1M` | Bars Count\|1m | `bars_count\|1M` | round |
| `BARS_COUNT_1W` | Bars Count\|1w | `bars_count\|1W` | round |
| `BARS_COUNT_240` | Bars Count\|240 | `bars_count\|240` | round |
| `BARS_COUNT_30` | Bars Count\|30 | `bars_count\|30` | round |
| `BARS_COUNT_5` | Bars Count\|5 | `bars_count\|5` | round |
| `BARS_COUNT_60` | Bars Count\|60 | `bars_count\|60` | round |
| `BETA_3_YEAR` | Beta 3 Year | `beta_3_year` | round |
| `BETA_5_YEAR` | Beta 5 Year | `beta_5_year` | round |
| `BOOK_TANGIBLE_PER_SHARE_CURRENT` | Book Tangible per Share Current | `book_tangible_per_share_current` | currency |
| `BOOK_TANGIBLE_PER_SHARE_FH` | Book Tangible per Share Fh | `book_tangible_per_share_fh` | currency |
| `BOOK_TANGIBLE_PER_SHARE_FQ` | Tangible Book Value per Share (MRQ) | `book_tangible_per_share_fq` | currency |
| `BOOK_TANGIBLE_PER_SHARE_FY` | Book Tangible per Share FY | `book_tangible_per_share_fy` | currency |
| `BRAND` | Brand | `brand` | text |
| `CATEGORY` | Category | `category` | text |
| `CHANGE` | Change | `change_abs` | currency |
| `CHANGE_1` | Change\|1 | `change\|1` | percent |
| `CHANGE_120` | Change\|120 | `change\|120` | percent |
| `CHANGE_15` | Change\|15 | `change\|15` | percent |
| `CHANGE_15MIN` | Change 15m | `change_abs.15` | float |
| `CHANGE_15MIN_PERCENT` | Change 15m, % | `change.15` | percent |
| `CHANGE_1H` | Change 1h | `change_abs.60` | round |
| `CHANGE_1H_PERCENT` | Change 1h, % | `change.60` | percent |
| `CHANGE_1M` | Change 1M | `change_abs.1M` | round |
| `CHANGE_1MIN` | Change 1m | `change_abs.1` | float |
| `CHANGE_1MIN_PERCENT` | Change 1m, % | `change.1` | percent |
| `CHANGE_1M_2` | Change\|1m | `change\|1M` | percent |
| `CHANGE_1M_PERCENT` | Change 1M, % | `change.1M` | percent |
| `CHANGE_1W` | Change 1W | `change_abs.1W` | round |
| `CHANGE_1W_2` | Change\|1w | `change\|1W` | percent |
| `CHANGE_1W_PERCENT` | Change 1W, % | `change.1W` | percent |
| `CHANGE_240` | Change\|240 | `change\|240` | percent |
| `CHANGE_30` | Change\|30 | `change\|30` | percent |
| `CHANGE_4H` | Change 4h | `change_abs.240` | round |
| `CHANGE_4H_PERCENT` | Change 4h, % | `change.240` | percent |
| `CHANGE_5` | Change\|5 | `change\|5` | percent |
| `CHANGE_5MIN` | Change 5m | `change_abs.5` | round |
| `CHANGE_5MIN_PERCENT` | Change 5m, % | `change.5` | percent |
| `CHANGE_60` | Change\|60 | `change\|60` | percent |
| `CHANGE_ABS_1` | Change Abs\|1 | `change_abs\|1` | currency |
| `CHANGE_ABS_120` | Change Abs\|120 | `change_abs\|120` | currency |
| `CHANGE_ABS_15` | Change Abs\|15 | `change_abs\|15` | currency |
| `CHANGE_ABS_1M` | Change Abs\|1m | `change_abs\|1M` | currency |
| `CHANGE_ABS_1W` | Change Abs\|1w | `change_abs\|1W` | currency |
| `CHANGE_ABS_240` | Change Abs\|240 | `change_abs\|240` | currency |
| `CHANGE_ABS_30` | Change Abs\|30 | `change_abs\|30` | currency |
| `CHANGE_ABS_5` | Change Abs\|5 | `change_abs\|5` | currency |
| `CHANGE_ABS_60` | Change Abs\|60 | `change_abs\|60` | currency |
| `CHANGE_PERCENT` | Change % | `change` | percent |
| `CURRENT_RATIO_CURRENT` | Current Ratio Current | `current_ratio_current` | round |
| `CURRENT_RATIO_FQ` | Current Ratio (MRQ) | `current_ratio_fq` | round |
| `CURRENT_RATIO_FY` | Current Ratio FY | `current_ratio_fy` | round |
| `CURRENT_RATIO_MRQ` | Current Ratio (MRQ) | `current_ratio` | round |
| `CURRENT_SESSION` | Current Session | `current_session` | text |
| `CUSIP` | CUSIP | `cusip` | text |
| `DIVIDENDS_PER_SHARE_FY` | Dividends per Share (FY) | `dps_common_stock_prim_issue_fy` | currency |
| `DPS_COMMON_STOCK_PRIM_ISSUE_FH` | DPS Common Stock Prim Issue Fh | `dps_common_stock_prim_issue_fh` | currency |
| `DPS_COMMON_STOCK_PRIM_ISSUE_FQ` | DPS Common Stock Prim Issue FQ | `dps_common_stock_prim_issue_fq` | currency |
| `DPS_COMMON_STOCK_PRIM_ISSUE_FY_H` | DPS Common Stock Prim Issue FY H | `dps_common_stock_prim_issue_fy_h` | round |
| `DPS_COMMON_STOCK_PRIM_ISSUE_TTM` | DPS Common Stock Prim Issue TTM | `dps_common_stock_prim_issue_ttm` | currency |
| `ETF_HOLDINGS_COUNT` | Etf Holdings Count | `etf_holdings_count` | round |
| `EXPENSE_RATIO` | Expense Ratio | `expense_ratio` | round |
| `EXPIRATION` | Expiration | `expiration` | date |
| `FISCAL_PERIOD_CURRENT` | Fiscal Period Current | `fiscal_period_current` | text |
| `FISCAL_PERIOD_END_CURRENT` | Fiscal Period End Current | `fiscal_period_end_current` | date |
| `FISCAL_PERIOD_END_FH` | Fiscal Period End Fh | `fiscal_period_end_fh` | date |
| `FISCAL_PERIOD_END_FH_H` | Fiscal Period End Fh H | `fiscal_period_end_fh_h` | round |
| `FISCAL_PERIOD_END_FQ` | Fiscal Period End (MRQ) | `fiscal_period_end_fq` | date |
| `FISCAL_PERIOD_END_FY` | Fiscal Period End (FY) | `fiscal_period_end_fy` | date |
| `FISCAL_PERIOD_FY` | Fiscal Period (FY) | `fiscal_period_fy` | text |
| `FISCAL_PERIOD_FY_H` | Fiscal Period FY H | `fiscal_period_fy_h` | round |
| `FOCUS` | Focus | `focus` | text |
| `FRACTIONAL` | Fractional | `fractional` | text |
| `FREQUENCY_RECENT` | Frequency Recent | `frequency_recent` | text |
| `FREQUENCY_UPCOMING` | Frequency Upcoming | `frequency_upcoming` | text |
| `GOODWILL` | Goodwill | `goodwill` | currency |
| `GOODWILL_FQ` | Goodwill (MRQ) | `goodwill_fq` | currency |
| `GOODWILL_FY` | Goodwill (FY) | `goodwill_fy` | currency |
| `GRAHAM_NUMBERS_FY` | Graham's Number (FY) | `graham_numbers_fy` | currency |
| `GRAHAM_NUMBERS_TTM` | Graham's Number (TTM) | `graham_numbers_ttm` | currency |
| `HAS_IPO_DATA` | Has IPO Data | `has_ipo_data` | bool |
| `HAS_IPO_DETAILS_VISIBLE` | Has IPO Details Visible | `has_ipo_details_visible` | bool |
| `HOLDINGS_REGION` | Holdings Region | `holdings_region` | text |
| `HOLDS_DERIVATIVES_FLAG` | Holds Derivatives Flag | `holds_derivatives_flag` | text |
| `INDICATORS_BARS_COUNT` | Indicators Bars Count | `indicators_bars_count` | round |
| `INDICATORS_BARS_COUNT_1` | Indicators Bars Count\|1 | `indicators_bars_count\|1` | round |
| `INDICATORS_BARS_COUNT_120` | Indicators Bars Count\|120 | `indicators_bars_count\|120` | round |
| `INDICATORS_BARS_COUNT_15` | Indicators Bars Count\|15 | `indicators_bars_count\|15` | round |
| `INDICATORS_BARS_COUNT_1M` | Indicators Bars Count\|1m | `indicators_bars_count\|1M` | round |
| `INDICATORS_BARS_COUNT_1W` | Indicators Bars Count\|1w | `indicators_bars_count\|1W` | round |
| `INDICATORS_BARS_COUNT_240` | Indicators Bars Count\|240 | `indicators_bars_count\|240` | round |
| `INDICATORS_BARS_COUNT_30` | Indicators Bars Count\|30 | `indicators_bars_count\|30` | round |
| `INDICATORS_BARS_COUNT_5` | Indicators Bars Count\|5 | `indicators_bars_count\|5` | round |
| `INDICATORS_BARS_COUNT_60` | Indicators Bars Count\|60 | `indicators_bars_count\|60` | round |
| `INTERST_COVER_FY` | Interest Coverage (FY) | `interst_cover_fy` | round |
| `INTERST_COVER_TTM` | Interest Coverage (TTM) | `interst_cover_ttm` | round |
| `INVENT_TURNOVER_CURRENT` | Inventory Turnover (Current) | `invent_turnover_current` | round |
| `INVENT_TURNOVER_FY` | Inventory Turnover (FY) | `invent_turnover_fy` | round |
| `INVERSE_FLAG` | Inverse Flag | `inverse_flag` | round |
| `IPO_BLANK_CHECK_FLAG` | IPO Blank Check Flag | `ipo_blank_check_flag` | bool |
| `IPO_DEAL_AMOUNT_USD` | IPO Deal Amount Usd | `ipo_deal_amount_usd` | round |
| `ISIN` | ISIN | `isin` | text |
| `ISSUANCE_OF_STOCK_NET_TTM` | Issuance of Stock Net TTM | `issuance_of_stock_net_ttm` | currency |
| `IS_BLACKLISTED` | Is Blacklisted | `is_blacklisted` | bool |
| `IS_PRIMARY` | Is Primary | `is_primary` | bool |
| `IS_SHARIAH_COMPLIANT` | Is Shariah Compliant | `is_shariah_compliant` | bool |
| `K1_FORM` | K1 Form | `k1_form` | text |
| `KIND` | Kind | `kind` | text |
| `KIND_DELAY` | Kind-delay | `kind-delay` | round |
| `LAST_REPORT_FREQUENCY` | Last Report Frequency | `last_report_frequency` | round |
| `LEVERAGE` | Leverage | `leverage` | text |
| `LEVERAGED_FLAG` | Leveraged Flag | `leveraged_flag` | text |
| `LEVERAGE_RATIO` | Leverage Ratio | `leverage_ratio` | text |
| `MARKET` | Market | `market` | text |
| `MINMOV` | Minmov | `minmov` | round |
| `MINMOVE2` | Minmove2 | `minmove2` | round |
| `NAV` | Nav | `nav` | currency |
| `NAV_DISCOUNT_PREMIUM` | Nav Discount Premium | `nav_discount_premium` | round |
| `NAV_TOTAL_RETURN_1M` | Nav Total Return 1m | `nav_total_return.1M` | round |
| `NAV_TOTAL_RETURN_1Y` | Nav Total Return 1y | `nav_total_return.1Y` | round |
| `NAV_TOTAL_RETURN_3M` | Nav Total Return 3m | `nav_total_return.3M` | round |
| `NAV_TOTAL_RETURN_3Y` | Nav Total Return 3y | `nav_total_return.3Y` | round |
| `NAV_TOTAL_RETURN_5Y` | Nav Total Return 5y | `nav_total_return.5Y` | round |
| `NAV_TOTAL_RETURN_6M` | Nav Total Return 6m | `nav_total_return.6M` | round |
| `NAV_TOTAL_RETURN_YTD` | Nav Total Return Ytd | `nav_total_return.YTD` | round |
| `NICHE` | Niche | `niche` | text |
| `NUMBER_OF_EMPLOYEES` | Number of Employees | `number_of_employees` | number_group |
| `NUMBER_OF_EMPLOYEES_FY` | Number of Employees FY | `number_of_employees_fy` | round |
| `NUMBER_OF_SHAREHOLDERS` | Number of Shareholders | `number_of_shareholders` | number_group |
| `NUMBER_OF_SHAREHOLDERS_FY` | Number of Shareholders FY | `number_of_shareholders_fy` | round |
| `OPER_INCOME_FH` | Oper Income Fh | `oper_income_fh` | currency |
| `OPER_INCOME_FQ` | Oper Income FQ | `oper_income_fq` | currency |
| `OPER_INCOME_FY` | Operating Income (FY) | `oper_income_fy` | currency |
| `OPER_INCOME_PER_EMPLOYEE_FY` | Oper Income per Employee FY | `oper_income_per_employee_fy` | currency |
| `OPER_INCOME_TTM` | Operating Income (TTM) | `oper_income_ttm` | currency |
| `PIOTROSKI_F_SCORE_FY` | Piotroski f Score FY | `piotroski_f_score_fy` | round |
| `PIOTROSKI_F_SCORE_TTM` | Piotroski F-Score (TTM) | `piotroski_f_score_ttm` | round |
| `POSTMARKET_CHANGE` | Post-market Change | `postmarket_change_abs` | missing |
| `POSTMARKET_CHANGE_PERCENT` | Post-market Change % | `postmarket_change` | missing |
| `POST_CHANGE` | Post Change | `post_change` | percent |
| `POST_CHANGE_1` | Post Change\|1 | `post_change\|1` | percent |
| `POST_CHANGE_120` | Post Change\|120 | `post_change\|120` | percent |
| `POST_CHANGE_15` | Post Change\|15 | `post_change\|15` | percent |
| `POST_CHANGE_1M` | Post Change\|1m | `post_change\|1M` | percent |
| `POST_CHANGE_1W` | Post Change\|1w | `post_change\|1W` | percent |
| `POST_CHANGE_240` | Post Change\|240 | `post_change\|240` | percent |
| `POST_CHANGE_30` | Post Change\|30 | `post_change\|30` | percent |
| `POST_CHANGE_5` | Post Change\|5 | `post_change\|5` | percent |
| `POST_CHANGE_60` | Post Change\|60 | `post_change\|60` | percent |
| `PRE_CHANGE` | Pre Change | `pre_change` | percent |
| `PRE_CHANGE_1` | Pre Change\|1 | `pre_change\|1` | percent |
| `PRE_CHANGE_120` | Pre Change\|120 | `pre_change\|120` | percent |
| `PRE_CHANGE_15` | Pre Change\|15 | `pre_change\|15` | percent |
| `PRE_CHANGE_1M` | Pre Change\|1m | `pre_change\|1M` | percent |
| `PRE_CHANGE_1W` | Pre Change\|1w | `pre_change\|1W` | percent |
| `PRE_CHANGE_240` | Pre Change\|240 | `pre_change\|240` | percent |
| `PRE_CHANGE_30` | Pre Change\|30 | `pre_change\|30` | percent |
| `PRE_CHANGE_5` | Pre Change\|5 | `pre_change\|5` | percent |
| `PRE_CHANGE_60` | Pre Change\|60 | `pre_change\|60` | percent |
| `PRE_CHANGE_ABS` | Pre Change Abs | `pre_change_abs` | currency |
| `PRE_CHANGE_ABS_1` | Pre Change Abs\|1 | `pre_change_abs\|1` | currency |
| `PRE_CHANGE_ABS_120` | Pre Change Abs\|120 | `pre_change_abs\|120` | currency |
| `PRE_CHANGE_ABS_15` | Pre Change Abs\|15 | `pre_change_abs\|15` | currency |
| `PRE_CHANGE_ABS_1M` | Pre Change Abs\|1m | `pre_change_abs\|1M` | currency |
| `PRE_CHANGE_ABS_1W` | Pre Change Abs\|1w | `pre_change_abs\|1W` | currency |
| `PRE_CHANGE_ABS_240` | Pre Change Abs\|240 | `pre_change_abs\|240` | currency |
| `PRE_CHANGE_ABS_30` | Pre Change Abs\|30 | `pre_change_abs\|30` | currency |
| `PRE_CHANGE_ABS_5` | Pre Change Abs\|5 | `pre_change_abs\|5` | currency |
| `PRE_CHANGE_ABS_60` | Pre Change Abs\|60 | `pre_change_abs\|60` | currency |
| `PROVIDER_ID` | Provider-id | `provider-id` | text |
| `QUICK_RATIO_CURRENT` | Quick Ratio Current | `quick_ratio_current` | round |
| `QUICK_RATIO_FQ` | Quick Ratio (MRQ) | `quick_ratio_fq` | round |
| `QUICK_RATIO_FY` | Quick Ratio FY | `quick_ratio_fy` | round |
| `QUICK_RATIO_MRQ` | Quick Ratio (MRQ) | `quick_ratio` | round |
| `RATES_CF` | Rates Cf | `rates_cf` | text |
| `RATES_CURRENT` | Rates Current | `rates_current` | text |
| `RATES_FH` | Rates Fh | `rates_fh` | text |
| `RATES_FQ` | Rates FQ | `rates_fq` | text |
| `RATES_FY` | Rates FY | `rates_fy` | text |
| `RATES_MC` | Rates Mc | `rates_mc` | text |
| `RATES_PT` | Rates Pt | `rates_pt` | text |
| `RATES_TTM` | Rates TTM | `rates_ttm` | text |
| `RECEIVABLES_TURNOVER_FQ` | Receivables Turnover FQ | `receivables_turnover_fq` | round |
| `RECEIVABLES_TURNOVER_FY` | Receivables Turnover (FY) | `receivables_turnover_fy` | round |
| `RTC` | Rtc | `rtc` | currency |
| `SELECTION_CRITERIA` | Selection Criteria | `selection_criteria` | text |
| `SELLING_GENERAL_AND_ADMIN_EXPENSES_RATIO_FY` | Selling General & Admin expenses Ratio (FY) | `sell_gen_admin_exp_other_ratio_fy` | percent |
| `SELLING_GENERAL_AND_ADMIN_EXPENSES_RATIO_TTM` | Selling General & Admin expenses Ratio (TTM) | `sell_gen_admin_exp_other_ratio_ttm` | percent |
| `SELL_GEN_ADMIN_EXP_OTHER_FY` | Sell Gen Admin Exp Other FY | `sell_gen_admin_exp_other_fy` | currency |
| `SELL_GEN_ADMIN_EXP_OTHER_TTM` | Sell Gen Admin Exp Other TTM | `sell_gen_admin_exp_other_ttm` | currency |
| `SHARE_BUYBACK_RATIO_FQ` | Share Buyback Ratio % (MRQ) | `share_buyback_ratio_fq` | percent |
| `SHARE_BUYBACK_RATIO_FY` | Share Buyback Ratio % (FY) | `share_buyback_ratio_fy` | percent |
| `SLOAN_RATIO_FY` | Sloan Ratio FY | `sloan_ratio_fy` | percent |
| `SLOAN_RATIO_TTM` | Sloan Ratio % (TTM) | `sloan_ratio_ttm` | percent |
| `STRATEGY` | Strategy | `strategy` | text |
| `SUBMARKET` | Submarket | `submarket` | missing |
| `TOBIN_Q_RATIO_FQ` | Tobin's Q Ratio (MRQ) | `tobin_q_ratio_fq` | round |
| `TOBIN_Q_RATIO_FY` | Tobin's Q Ratio (FY) | `tobin_q_ratio_fy` | round |
| `TRANSPARENT_HOLDING_FLAG` | Transparent Holding Flag | `transparent_holding_flag` | text |
| `UCITS_COMPLIANT_FLAG` | Ucits Compliant Flag | `ucits_compliant_flag` | text |
| `VALUE_TRADED_1` | Value Traded\|1 | `Value.Traded\|1` | round |
| `VALUE_TRADED_120` | Value Traded\|120 | `Value.Traded\|120` | round |
| `VALUE_TRADED_15` | Value Traded\|15 | `Value.Traded\|15` | round |
| `VALUE_TRADED_1M` | Value Traded\|1m | `Value.Traded\|1M` | round |
| `VALUE_TRADED_1W` | Value Traded\|1w | `Value.Traded\|1W` | round |
| `VALUE_TRADED_240` | Value Traded\|240 | `Value.Traded\|240` | round |
| `VALUE_TRADED_30` | Value Traded\|30 | `Value.Traded\|30` | round |
| `VALUE_TRADED_5` | Value Traded\|5 | `Value.Traded\|5` | round |
| `VALUE_TRADED_60` | Value Traded\|60 | `Value.Traded\|60` | round |
| `VOLUMEXPRICE` | Volume*Price | `Value.Traded` | number_group |
| `VOLUME_WEIGHTED_AVERAGE_PRICE` | Volume Weighted Average Price | `VWAP` | float |
| `VWAP_1` | Vwap\|1 | `VWAP\|1` | round |
| `VWAP_120` | Vwap\|120 | `VWAP\|120` | round |
| `VWAP_15` | Vwap\|15 | `VWAP\|15` | round |
| `VWAP_1M` | Vwap\|1m | `VWAP\|1M` | round |
| `VWAP_1W` | Vwap\|1w | `VWAP\|1W` | round |
| `VWAP_240` | Vwap\|240 | `VWAP\|240` | round |
| `VWAP_30` | Vwap\|30 | `VWAP\|30` | round |
| `VWAP_5` | Vwap\|5 | `VWAP\|5` | round |
| `VWAP_60` | Vwap\|60 | `VWAP\|60` | round |
| `WEIGHTING_SCHEME` | Weighting Scheme | `weighting_scheme` | text |
| `WEIGHT_TOP_10` | Weight Top 10 | `weight_top_10` | percent |
| `WEIGHT_TOP_25` | Weight Top 25 | `weight_top_25` | percent |
| `WEIGHT_TOP_50` | Weight Top 50 | `weight_top_50` | percent |
| `YEAR_BETA_1` | 1-Year Beta | `beta_1_year` | round |
| `ZMIJEWSKI_SCORE_FY` | Zmijewski Score FY | `zmijewski_score_fy` | round |
| `ZMIJEWSKI_SCORE_TTM` | Zmijewski Score (TTM) | `zmijewski_score_ttm` | round |
