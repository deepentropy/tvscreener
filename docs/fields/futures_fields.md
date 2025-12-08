# FuturesField Reference

Fields available for futures screening. Includes price data and technical indicators.

**Total Fields:** 393

## Table of Contents

- [Metadata](#metadata) (18 fields)
- [Price Data](#price-data) (50 fields)
- [Volume](#volume) (8 fields)
- [Performance](#performance) (11 fields)
- [Moving Averages](#moving-averages) (76 fields)
- [Oscillators](#oscillators) (67 fields)
- [Trend Indicators](#trend-indicators) (40 fields)
- [Volatility Indicators](#volatility-indicators) (17 fields)
- [Pivot Points](#pivot-points) (21 fields)
- [Candlestick Patterns](#candlestick-patterns) (27 fields)
- [Recommendations](#recommendations) (4 fields)
- [Dividends & Yield](#dividends--yield) (2 fields)
- [Earnings & Income](#earnings--income) (2 fields)
- [Bond Data](#bond-data) (3 fields)
- [Crypto Data](#crypto-data) (2 fields)
- [DEX Data](#dex-data) (1 fields)
- [Time & Dates](#time--dates) (8 fields)
- [Other](#other) (36 fields)

---

## Metadata

*18 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `ACTIVE_SYMBOL` | Active Symbol | `active_symbol` | float |
| `BASE_CURRENCY_KIND` | Base Currency Kind | `base_currency_kind` | text |
| `COUNTRY_CODE` | Country Code | `country_code` | text |
| `CURRENCY` | Currency | `currency` | text |
| `CURRENCY_ID` | Currency Id | `currency_id` | text |
| `CURRENCY_KIND` | Currency Kind | `currency_kind` | text |
| `DESCRIPTION` | Description | `description` | text |
| `EXCHANGE` | Exchange | `exchange` | percent |
| `FUNDAMENTAL_CURRENCY_CODE` | Fundamental Currency Code | `fundamental_currency_code` | text |
| `IS_SYMBOL_PRIMARY_LISTING` | Is Symbol Primary Listing | `is_symbol_primary_listing` | float |
| `LOGOID` | Logoid | `logoid` | text |
| `NAME` | Name | `name` | text |
| `SECTOR` | Sector | `sector` | text |
| `SOURCE_MINUS_LOGOID` | Source-Logoid | `source-logoid` | text |
| `SUBTYPE` | Subtype | `subtype` | text |
| `SYMBOL` | Symbol | `symbol` | float |
| `TYPE` | Type | `type` | text |
| `TYPESPECS` | Typespecs | `typespecs` | text |

## Price Data

*50 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `ALL_TIME_HIGH` | All Time High | `all_time_high` | date |
| `ALL_TIME_HIGH_DAY` | All Time High Day | `all_time_high_day` | date |
| `ALL_TIME_LOW` | All Time Low | `all_time_low` | date |
| `ALL_TIME_LOW_DAY` | All Time Low Day | `all_time_low_day` | date |
| `ALL_TIME_OPEN` | All Time Open | `all_time_open` | date |
| `CHAIKINMONEYFLOW` | Chaikinmoneyflow | `ChaikinMoneyFlow` | float |
| `CHANGE_FROM_OPEN` | Change From Open | `change_from_open` | percent |
| `CHANGE_FROM_OPEN_ABS` | Change From Open Abs | `change_from_open_abs` | percent |
| `CLOSE` | Close | `close` | float |
| `GAP` | Gap | `gap` | float |
| `GAP_DOWN` | Gap Down | `gap_down` | float |
| `GAP_DOWN_ABS` | Gap Down Abs | `gap_down_abs` | float |
| `GAP_UP` | Gap Up | `gap_up` | float |
| `GAP_UP_ABS` | Gap Up Abs | `gap_up_abs` | float |
| `HIGH` | High | `high` | float |
| `HIGH_1M` | High 1M | `High.1M` | float |
| `HIGH_1M_DATE` | High 1M Date | `High.1M.Date` | date |
| `HIGH_3M` | High 3M | `High.3M` | float |
| `HIGH_3M_DATE` | High 3M Date | `High.3M.Date` | date |
| `HIGH_5D` | High 5D | `High.5D` | float |
| `HIGH_6M` | High 6M | `High.6M` | float |
| `HIGH_6M_DATE` | High 6M Date | `High.6M.Date` | date |
| `HIGH_ALL` | High All | `High.All` | float |
| `HIGH_ALL_CALC` | High All Calc | `High.All.Calc` | float |
| `HIGH_ALL_CALC_DATE` | High All Calc Date | `High.All.Calc.Date` | date |
| `HIGH_ALL_DATE` | High All Date | `High.All.Date` | date |
| `LOW` | Low | `low` | float |
| `LOW_1M` | Low 1M | `Low.1M` | float |
| `LOW_1M_DATE` | Low 1M Date | `Low.1M.Date` | date |
| `LOW_3M` | Low 3M | `Low.3M` | float |
| `LOW_3M_DATE` | Low 3M Date | `Low.3M.Date` | date |
| `LOW_5D` | Low 5D | `Low.5D` | float |
| `LOW_6M` | Low 6M | `Low.6M` | float |
| `LOW_6M_DATE` | Low 6M Date | `Low.6M.Date` | date |
| `LOW_AFTER_HIGH_ALL` | Low After High All | `Low.After.High.All` | float |
| `LOW_AFTER_HIGH_ALL_CHANGE` | Low After High All Change | `low_after_high_all_change` | percent |
| `LOW_AFTER_HIGH_ALL_CHANGE_ABS` | Low After High All Change Abs | `low_after_high_all_change_abs` | percent |
| `LOW_ALL` | Low All | `Low.All` | float |
| `LOW_ALL_CALC` | Low All Calc | `Low.All.Calc` | float |
| `LOW_ALL_CALC_DATE` | Low All Calc Date | `Low.All.Calc.Date` | date |
| `LOW_ALL_DATE` | Low All Date | `Low.All.Date` | date |
| `MONEYFLOW` | Moneyflow | `MoneyFlow` | float |
| `OPEN` | Open | `open` | float |
| `OPEN_ALL_CALC` | Open All Calc | `Open.All.Calc` | float |
| `OPEN_INTEREST` | Open Interest | `open_interest` | float |
| `PRICESCALE` | Pricescale | `pricescale` | float |
| `PRICE_52_WEEK_HIGH` | Price 52 Week High | `price_52_week_high` | float |
| `PRICE_52_WEEK_HIGH_DATE` | Price 52 Week High Date | `price_52_week_high_date` | date |
| `PRICE_52_WEEK_LOW` | Price 52 Week Low | `price_52_week_low` | float |
| `PRICE_52_WEEK_LOW_DATE` | Price 52 Week Low Date | `price_52_week_low_date` | date |

## Volume

*8 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `AVERAGE_VOLUME_10D_CALC` | Average Volume 10D Calc | `average_volume_10d_calc` | number_group |
| `AVERAGE_VOLUME_30D_CALC` | Average Volume 30D Calc | `average_volume_30d_calc` | number_group |
| `AVERAGE_VOLUME_60D_CALC` | Average Volume 60D Calc | `average_volume_60d_calc` | number_group |
| `AVERAGE_VOLUME_90D_CALC` | Average Volume 90D Calc | `average_volume_90d_calc` | number_group |
| `RELATIVE_VOLUME_10D_CALC` | Relative Volume 10D Calc | `relative_volume_10d_calc` | number_group |
| `VOLUME` | Volume | `volume` | number_group |
| `VOLUME_CHANGE` | Volume Change | `volume_change` | percent |
| `VOLUME_CHANGE_ABS` | Volume Change Abs | `volume_change_abs` | percent |

## Performance

*11 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `PERF_10Y` | Perf 10Y | `Perf.10Y` | percent |
| `PERF_1M` | Perf 1M | `Perf.1M` | percent |
| `PERF_3M` | Perf 3M | `Perf.3M` | percent |
| `PERF_3Y` | Perf 3Y | `Perf.3Y` | percent |
| `PERF_5D` | Perf 5D | `Perf.5D` | percent |
| `PERF_5Y` | Perf 5Y | `Perf.5Y` | percent |
| `PERF_6M` | Perf 6M | `Perf.6M` | percent |
| `PERF_ALL` | Perf All | `Perf.All` | percent |
| `PERF_W` | Perf W | `Perf.W` | percent |
| `PERF_Y` | Perf Y | `Perf.Y` | percent |
| `PERF_YTD` | Perf YTD | `Perf.YTD` | percent |

## Moving Averages

*76 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `EMA10` | Ema10 | `EMA10` | float |
| `EMA100` | Ema100 | `EMA100` | float |
| `EMA12` | Ema12 | `EMA12` | float |
| `EMA120` | Ema120 | `EMA120` | float |
| `EMA13` | Ema13 | `EMA13` | float |
| `EMA14` | Ema14 | `EMA14` | float |
| `EMA144` | Ema144 | `EMA144` | float |
| `EMA15` | Ema15 | `EMA15` | float |
| `EMA150` | Ema150 | `EMA150` | float |
| `EMA2` | Ema2 | `EMA2` | float |
| `EMA20` | Ema20 | `EMA20` | float |
| `EMA200` | Ema200 | `EMA200` | float |
| `EMA21` | Ema21 | `EMA21` | float |
| `EMA25` | Ema25 | `EMA25` | float |
| `EMA250` | Ema250 | `EMA250` | float |
| `EMA26` | Ema26 | `EMA26` | float |
| `EMA3` | Ema3 | `EMA3` | float |
| `EMA30` | Ema30 | `EMA30` | float |
| `EMA300` | Ema300 | `EMA300` | float |
| `EMA34` | Ema34 | `EMA34` | float |
| `EMA40` | Ema40 | `EMA40` | float |
| `EMA5` | Ema5 | `EMA5` | float |
| `EMA50` | Ema50 | `EMA50` | float |
| `EMA55` | Ema55 | `EMA55` | float |
| `EMA6` | Ema6 | `EMA6` | float |
| `EMA60` | Ema60 | `EMA60` | float |
| `EMA7` | Ema7 | `EMA7` | float |
| `EMA75` | Ema75 | `EMA75` | float |
| `EMA8` | Ema8 | `EMA8` | float |
| `EMA89` | Ema89 | `EMA89` | float |
| `EMA9` | Ema9 | `EMA9` | float |
| `HULLMA20` | Hullma20 | `HullMA20` | float |
| `HULLMA200` | Hullma200 | `HullMA200` | float |
| `HULLMA9` | Hullma9 | `HullMA9` | float |
| `PIVOT_M_DEMARK_MIDDLE` | Pivot M Demark Middle | `Pivot.M.Demark.Middle` | float |
| `PIVOT_M_DEMARK_R1` | Pivot M Demark R1 | `Pivot.M.Demark.R1` | float |
| `PIVOT_M_DEMARK_S1` | Pivot M Demark S1 | `Pivot.M.Demark.S1` | float |
| `PREMARKET_CHANGE` | Premarket Change | `premarket_change` | percent |
| `PREMARKET_CHANGE_ABS` | Premarket Change Abs | `premarket_change_abs` | percent |
| `PREMARKET_CHANGE_FROM_OPEN` | Premarket Change From Open | `premarket_change_from_open` | percent |
| `PREMARKET_CHANGE_FROM_OPEN_ABS` | Premarket Change From Open Abs | `premarket_change_from_open_abs` | percent |
| `PREMARKET_GAP` | Premarket Gap | `premarket_gap` | float |
| `REC_HULLMA9` | Rec Hullma9 | `Rec.HullMA9` | rating |
| `REC_VWMA` | Rec VWMA | `Rec.VWMA` | rating |
| `SMA10` | Sma10 | `SMA10` | float |
| `SMA100` | Sma100 | `SMA100` | float |
| `SMA12` | Sma12 | `SMA12` | float |
| `SMA120` | Sma120 | `SMA120` | float |
| `SMA13` | Sma13 | `SMA13` | float |
| `SMA14` | Sma14 | `SMA14` | float |
| `SMA144` | Sma144 | `SMA144` | float |
| `SMA15` | Sma15 | `SMA15` | float |
| `SMA150` | Sma150 | `SMA150` | float |
| `SMA2` | Sma2 | `SMA2` | float |
| `SMA20` | Sma20 | `SMA20` | float |
| `SMA200` | Sma200 | `SMA200` | float |
| `SMA21` | Sma21 | `SMA21` | float |
| `SMA25` | Sma25 | `SMA25` | float |
| `SMA250` | Sma250 | `SMA250` | float |
| `SMA26` | Sma26 | `SMA26` | float |
| `SMA3` | Sma3 | `SMA3` | float |
| `SMA30` | Sma30 | `SMA30` | float |
| `SMA300` | Sma300 | `SMA300` | float |
| `SMA34` | Sma34 | `SMA34` | float |
| `SMA40` | Sma40 | `SMA40` | float |
| `SMA5` | Sma5 | `SMA5` | float |
| `SMA50` | Sma50 | `SMA50` | float |
| `SMA55` | Sma55 | `SMA55` | float |
| `SMA6` | Sma6 | `SMA6` | float |
| `SMA60` | Sma60 | `SMA60` | float |
| `SMA7` | Sma7 | `SMA7` | float |
| `SMA75` | Sma75 | `SMA75` | float |
| `SMA8` | Sma8 | `SMA8` | float |
| `SMA89` | Sma89 | `SMA89` | float |
| `SMA9` | Sma9 | `SMA9` | float |
| `VWMA` | VWMA | `VWMA` | float |

## Oscillators

*67 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `AO` | AO | `AO` | float |
| `AO_1` | AO[1] | `AO[1]` | float |
| `AO_2` | AO[2] | `AO[2]` | float |
| `BBPOWER` | Bbpower | `BBPower` | float |
| `CCI20` | Cci20 | `CCI20` | float |
| `CCI20_1` | Cci20[1] | `CCI20[1]` | float |
| `MOM` | Mom | `Mom` | float |
| `MOM_1` | Mom[1] | `Mom[1]` | float |
| `MOM_14` | Mom 14 | `Mom_14` | float |
| `MOM_14_1` | Mom 14[1] | `Mom_14[1]` | float |
| `PIVOT_M_FIBONACCI_MIDDLE` | Pivot M Fibonacci Middle | `Pivot.M.Fibonacci.Middle` | float |
| `PIVOT_M_FIBONACCI_R1` | Pivot M Fibonacci R1 | `Pivot.M.Fibonacci.R1` | float |
| `PIVOT_M_FIBONACCI_R2` | Pivot M Fibonacci R2 | `Pivot.M.Fibonacci.R2` | float |
| `PIVOT_M_FIBONACCI_R3` | Pivot M Fibonacci R3 | `Pivot.M.Fibonacci.R3` | float |
| `PIVOT_M_FIBONACCI_S1` | Pivot M Fibonacci S1 | `Pivot.M.Fibonacci.S1` | float |
| `PIVOT_M_FIBONACCI_S2` | Pivot M Fibonacci S2 | `Pivot.M.Fibonacci.S2` | float |
| `PIVOT_M_FIBONACCI_S3` | Pivot M Fibonacci S3 | `Pivot.M.Fibonacci.S3` | float |
| `REC_BBPOWER` | Rec Bbpower | `Rec.BBPower` | rating |
| `REC_STOCH_RSI` | Rec Stoch RSI | `Rec.Stoch.RSI` | rating |
| `REC_UO` | Rec UO | `Rec.UO` | rating |
| `ROC` | Roc | `ROC` | float |
| `RSI` | RSI | `RSI` | float |
| `RSI10` | Rsi10 | `RSI10` | float |
| `RSI10_1` | Rsi10[1] | `RSI10[1]` | float |
| `RSI2` | Rsi2 | `RSI2` | float |
| `RSI20` | Rsi20 | `RSI20` | float |
| `RSI20_1` | Rsi20[1] | `RSI20[1]` | float |
| `RSI21` | Rsi21 | `RSI21` | float |
| `RSI21_1` | Rsi21[1] | `RSI21[1]` | float |
| `RSI2_1` | Rsi2[1] | `RSI2[1]` | float |
| `RSI3` | Rsi3 | `RSI3` | float |
| `RSI30` | Rsi30 | `RSI30` | float |
| `RSI30_1` | Rsi30[1] | `RSI30[1]` | float |
| `RSI3_1` | Rsi3[1] | `RSI3[1]` | float |
| `RSI4` | Rsi4 | `RSI4` | float |
| `RSI4_1` | Rsi4[1] | `RSI4[1]` | float |
| `RSI5` | Rsi5 | `RSI5` | float |
| `RSI5_1` | Rsi5[1] | `RSI5[1]` | float |
| `RSI7` | Rsi7 | `RSI7` | float |
| `RSI7_1` | Rsi7[1] | `RSI7[1]` | float |
| `RSI9` | Rsi9 | `RSI9` | float |
| `RSI9_1` | Rsi9[1] | `RSI9[1]` | float |
| `RSI_1` | RSI[1] | `RSI[1]` | float |
| `STOCH_D` | Stoch D | `Stoch.D` | float |
| `STOCH_D_1` | Stoch D[1] | `Stoch.D[1]` | float |
| `STOCH_D_14_1_3` | Stoch D 14 1 3 | `Stoch.D_14_1_3` | float |
| `STOCH_D_14_1_3_1` | Stoch D 14 1 3[1] | `Stoch.D_14_1_3[1]` | float |
| `STOCH_D_5_3_3` | Stoch D 5 3 3 | `Stoch.D_5_3_3` | float |
| `STOCH_D_5_3_3_1` | Stoch D 5 3 3[1] | `Stoch.D_5_3_3[1]` | float |
| `STOCH_D_6_3_3` | Stoch D 6 3 3 | `Stoch.D_6_3_3` | float |
| `STOCH_D_6_3_3_1` | Stoch D 6 3 3[1] | `Stoch.D_6_3_3[1]` | float |
| `STOCH_D_8_3_3` | Stoch D 8 3 3 | `Stoch.D_8_3_3` | float |
| `STOCH_D_8_3_3_1` | Stoch D 8 3 3[1] | `Stoch.D_8_3_3[1]` | float |
| `STOCH_K` | Stoch K | `Stoch.K` | float |
| `STOCH_K_1` | Stoch K[1] | `Stoch.K[1]` | float |
| `STOCH_K_14_1_3` | Stoch K 14 1 3 | `Stoch.K_14_1_3` | float |
| `STOCH_K_14_1_3_1` | Stoch K 14 1 3[1] | `Stoch.K_14_1_3[1]` | float |
| `STOCH_K_5_3_3` | Stoch K 5 3 3 | `Stoch.K_5_3_3` | float |
| `STOCH_K_5_3_3_1` | Stoch K 5 3 3[1] | `Stoch.K_5_3_3[1]` | float |
| `STOCH_K_6_3_3` | Stoch K 6 3 3 | `Stoch.K_6_3_3` | float |
| `STOCH_K_6_3_3_1` | Stoch K 6 3 3[1] | `Stoch.K_6_3_3[1]` | float |
| `STOCH_K_8_3_3` | Stoch K 8 3 3 | `Stoch.K_8_3_3` | float |
| `STOCH_K_8_3_3_1` | Stoch K 8 3 3[1] | `Stoch.K_8_3_3[1]` | float |
| `STOCH_RSI_D` | Stoch RSI D | `Stoch.RSI.D` | float |
| `STOCH_RSI_K` | Stoch RSI K | `Stoch.RSI.K` | float |
| `UO` | UO | `UO` | float |
| `W_R` | W R | `W.R` | float |

## Trend Indicators

*40 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `ADX` | ADX | `ADX` | float |
| `ADX_100` | ADX 100 | `ADX_100` | float |
| `ADX_20` | ADX 20 | `ADX_20` | float |
| `ADX_50` | ADX 50 | `ADX_50` | float |
| `ADX_9` | ADX 9 | `ADX_9` | float |
| `ADX_MINUS_DI` | ADX-Di | `ADX-DI` | float |
| `ADX_MINUS_DI_1` | ADX-Di[1] | `ADX-DI[1]` | float |
| `ADX_MINUS_DI_100` | ADX-Di 100 | `ADX-DI_100` | float |
| `ADX_MINUS_DI_100_1` | ADX-Di 100[1] | `ADX-DI_100[1]` | float |
| `ADX_MINUS_DI_20` | ADX-Di 20 | `ADX-DI_20` | float |
| `ADX_MINUS_DI_20_1` | ADX-Di 20[1] | `ADX-DI_20[1]` | float |
| `ADX_MINUS_DI_50` | ADX-Di 50 | `ADX-DI_50` | float |
| `ADX_MINUS_DI_50_1` | ADX-Di 50[1] | `ADX-DI_50[1]` | float |
| `ADX_MINUS_DI_9` | ADX-Di 9 | `ADX-DI_9` | float |
| `ADX_MINUS_DI_9_1` | ADX-Di 9[1] | `ADX-DI_9[1]` | float |
| `ADX_PLUS_DI` | ADX+Di | `ADX+DI` | float |
| `ADX_PLUS_DI_1` | ADX+Di[1] | `ADX+DI[1]` | float |
| `ADX_PLUS_DI_100` | ADX+Di 100 | `ADX+DI_100` | float |
| `ADX_PLUS_DI_100_1` | ADX+Di 100[1] | `ADX+DI_100[1]` | float |
| `ADX_PLUS_DI_20` | ADX+Di 20 | `ADX+DI_20` | float |
| `ADX_PLUS_DI_20_1` | ADX+Di 20[1] | `ADX+DI_20[1]` | float |
| `ADX_PLUS_DI_50` | ADX+Di 50 | `ADX+DI_50` | float |
| `ADX_PLUS_DI_50_1` | ADX+Di 50[1] | `ADX+DI_50[1]` | float |
| `ADX_PLUS_DI_9` | ADX+Di 9 | `ADX+DI_9` | float |
| `ADX_PLUS_DI_9_1` | ADX+Di 9[1] | `ADX+DI_9[1]` | float |
| `AROON_DOWN` | Aroon Down | `Aroon.Down` | float |
| `AROON_UP` | Aroon Up | `Aroon.Up` | float |
| `ICHIMOKU_BLINE` | Ichimoku Bline | `Ichimoku.BLine` | float |
| `ICHIMOKU_BLINE_20_60_120_30` | Ichimoku Bline 20 60 120 30 | `Ichimoku.BLine_20_60_120_30` | float |
| `ICHIMOKU_CLINE` | Ichimoku Cline | `Ichimoku.CLine` | float |
| `ICHIMOKU_CLINE_20_60_120_30` | Ichimoku Cline 20 60 120 30 | `Ichimoku.CLine_20_60_120_30` | float |
| `ICHIMOKU_LEAD1` | Ichimoku Lead1 | `Ichimoku.Lead1` | float |
| `ICHIMOKU_LEAD1_20_60_120_30` | Ichimoku Lead1 20 60 120 30 | `Ichimoku.Lead1_20_60_120_30` | float |
| `ICHIMOKU_LEAD2` | Ichimoku Lead2 | `Ichimoku.Lead2` | float |
| `ICHIMOKU_LEAD2_20_60_120_30` | Ichimoku Lead2 20 60 120 30 | `Ichimoku.Lead2_20_60_120_30` | float |
| `MACD_HIST` | MACD Hist | `MACD.hist` | float |
| `MACD_MACD` | MACD MACD | `MACD.macd` | float |
| `MACD_SIGNAL` | MACD Signal | `MACD.signal` | float |
| `P_SAR` | P Sar | `P.SAR` | float |
| `REC_ICHIMOKU` | Rec Ichimoku | `Rec.Ichimoku` | rating |

## Volatility Indicators

*17 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `ATR` | ATR | `ATR` | float |
| `ATRP` | Atrp | `ATRP` | float |
| `BB_BASIS` | Bb Basis | `BB.basis` | float |
| `BB_BASIS_50` | Bb Basis 50 | `BB.basis_50` | float |
| `BB_LOWER` | Bb Lower | `BB.lower` | float |
| `BB_LOWER_50` | Bb Lower 50 | `BB.lower_50` | float |
| `BB_UPPER` | Bb Upper | `BB.upper` | float |
| `BB_UPPER_50` | Bb Upper 50 | `BB.upper_50` | float |
| `DONCHCH20_LOWER` | Donchch20 Lower | `DonchCh20.Lower` | float |
| `DONCHCH20_MIDDLE` | Donchch20 Middle | `DonchCh20.Middle` | float |
| `DONCHCH20_UPPER` | Donchch20 Upper | `DonchCh20.Upper` | float |
| `KLTCHNL_BASIS` | Kltchnl Basis | `KltChnl.basis` | float |
| `KLTCHNL_LOWER` | Kltchnl Lower | `KltChnl.lower` | float |
| `KLTCHNL_UPPER` | Kltchnl Upper | `KltChnl.upper` | float |
| `VOLATILITY_D` | Volatility D | `Volatility.D` | float |
| `VOLATILITY_M` | Volatility M | `Volatility.M` | float |
| `VOLATILITY_W` | Volatility W | `Volatility.W` | float |

## Pivot Points

*21 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `PIVOT_M_CAMARILLA_MIDDLE` | Pivot M Camarilla Middle | `Pivot.M.Camarilla.Middle` | float |
| `PIVOT_M_CAMARILLA_R1` | Pivot M Camarilla R1 | `Pivot.M.Camarilla.R1` | float |
| `PIVOT_M_CAMARILLA_R2` | Pivot M Camarilla R2 | `Pivot.M.Camarilla.R2` | float |
| `PIVOT_M_CAMARILLA_R3` | Pivot M Camarilla R3 | `Pivot.M.Camarilla.R3` | float |
| `PIVOT_M_CAMARILLA_S1` | Pivot M Camarilla S1 | `Pivot.M.Camarilla.S1` | float |
| `PIVOT_M_CAMARILLA_S2` | Pivot M Camarilla S2 | `Pivot.M.Camarilla.S2` | float |
| `PIVOT_M_CAMARILLA_S3` | Pivot M Camarilla S3 | `Pivot.M.Camarilla.S3` | float |
| `PIVOT_M_CLASSIC_MIDDLE` | Pivot M Classic Middle | `Pivot.M.Classic.Middle` | float |
| `PIVOT_M_CLASSIC_R1` | Pivot M Classic R1 | `Pivot.M.Classic.R1` | float |
| `PIVOT_M_CLASSIC_R2` | Pivot M Classic R2 | `Pivot.M.Classic.R2` | float |
| `PIVOT_M_CLASSIC_R3` | Pivot M Classic R3 | `Pivot.M.Classic.R3` | float |
| `PIVOT_M_CLASSIC_S1` | Pivot M Classic S1 | `Pivot.M.Classic.S1` | float |
| `PIVOT_M_CLASSIC_S2` | Pivot M Classic S2 | `Pivot.M.Classic.S2` | float |
| `PIVOT_M_CLASSIC_S3` | Pivot M Classic S3 | `Pivot.M.Classic.S3` | float |
| `PIVOT_M_WOODIE_MIDDLE` | Pivot M Woodie Middle | `Pivot.M.Woodie.Middle` | float |
| `PIVOT_M_WOODIE_R1` | Pivot M Woodie R1 | `Pivot.M.Woodie.R1` | float |
| `PIVOT_M_WOODIE_R2` | Pivot M Woodie R2 | `Pivot.M.Woodie.R2` | float |
| `PIVOT_M_WOODIE_R3` | Pivot M Woodie R3 | `Pivot.M.Woodie.R3` | float |
| `PIVOT_M_WOODIE_S1` | Pivot M Woodie S1 | `Pivot.M.Woodie.S1` | float |
| `PIVOT_M_WOODIE_S2` | Pivot M Woodie S2 | `Pivot.M.Woodie.S2` | float |
| `PIVOT_M_WOODIE_S3` | Pivot M Woodie S3 | `Pivot.M.Woodie.S3` | float |

## Candlestick Patterns

*27 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `CANDLE_3BLACKCROWS` | Candle 3Blackcrows | `Candle.3BlackCrows` | bool |
| `CANDLE_3WHITESOLDIERS` | Candle 3Whitesoldiers | `Candle.3WhiteSoldiers` | bool |
| `CANDLE_ABANDONEDBABY_BEARISH` | Candle Abandonedbaby Bearish | `Candle.AbandonedBaby.Bearish` | bool |
| `CANDLE_ABANDONEDBABY_BULLISH` | Candle Abandonedbaby Bullish | `Candle.AbandonedBaby.Bullish` | bool |
| `CANDLE_DOJI` | Candle Doji | `Candle.Doji` | bool |
| `CANDLE_DOJI_DRAGONFLY` | Candle Doji Dragonfly | `Candle.Doji.Dragonfly` | bool |
| `CANDLE_DOJI_GRAVESTONE` | Candle Doji Gravestone | `Candle.Doji.Gravestone` | bool |
| `CANDLE_ENGULFING_BEARISH` | Candle Engulfing Bearish | `Candle.Engulfing.Bearish` | bool |
| `CANDLE_ENGULFING_BULLISH` | Candle Engulfing Bullish | `Candle.Engulfing.Bullish` | bool |
| `CANDLE_EVENINGSTAR` | Candle Eveningstar | `Candle.EveningStar` | bool |
| `CANDLE_HAMMER` | Candle Hammer | `Candle.Hammer` | bool |
| `CANDLE_HANGINGMAN` | Candle Hangingman | `Candle.HangingMan` | bool |
| `CANDLE_HARAMI_BEARISH` | Candle Harami Bearish | `Candle.Harami.Bearish` | bool |
| `CANDLE_HARAMI_BULLISH` | Candle Harami Bullish | `Candle.Harami.Bullish` | bool |
| `CANDLE_INVERTEDHAMMER` | Candle Invertedhammer | `Candle.InvertedHammer` | bool |
| `CANDLE_KICKING_BEARISH` | Candle Kicking Bearish | `Candle.Kicking.Bearish` | bool |
| `CANDLE_KICKING_BULLISH` | Candle Kicking Bullish | `Candle.Kicking.Bullish` | bool |
| `CANDLE_LONGSHADOW_LOWER` | Candle Longshadow Lower | `Candle.LongShadow.Lower` | bool |
| `CANDLE_LONGSHADOW_UPPER` | Candle Longshadow Upper | `Candle.LongShadow.Upper` | bool |
| `CANDLE_MARUBOZU_BLACK` | Candle Marubozu Black | `Candle.Marubozu.Black` | bool |
| `CANDLE_MARUBOZU_WHITE` | Candle Marubozu White | `Candle.Marubozu.White` | bool |
| `CANDLE_MORNINGSTAR` | Candle Morningstar | `Candle.MorningStar` | bool |
| `CANDLE_SHOOTINGSTAR` | Candle Shootingstar | `Candle.ShootingStar` | bool |
| `CANDLE_SPINNINGTOP_BLACK` | Candle Spinningtop Black | `Candle.SpinningTop.Black` | bool |
| `CANDLE_SPINNINGTOP_WHITE` | Candle Spinningtop White | `Candle.SpinningTop.White` | bool |
| `CANDLE_TRISTAR_BEARISH` | Candle Tristar Bearish | `Candle.TriStar.Bearish` | bool |
| `CANDLE_TRISTAR_BULLISH` | Candle Tristar Bullish | `Candle.TriStar.Bullish` | bool |

## Recommendations

*4 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `RECOMMEND_ALL` | Recommend All | `Recommend.All` | rating |
| `RECOMMEND_MA` | Recommend Ma | `Recommend.MA` | rating |
| `RECOMMEND_OTHER` | Recommend Other | `Recommend.Other` | rating |
| `REC_WR` | Rec Wr | `Rec.WR` | rating |

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

*1 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `INDEXES` | Indexes | `indexes` | float |

## Time & Dates

*8 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `FIRST_BAR_TIME` | First Bar Time | `first_bar_time` | date |
| `LAST_BAR_UPDATE_TIME` | Last Bar Update Time | `last_bar_update_time` | date |
| `RATES_TIME_SERIES` | Rates Time Series | `rates_time_series` | date |
| `TIME` | Time | `time` | date |
| `TIME_BUSINESS_DAY` | Time Business Day | `time_business_day` | date |
| `UPDATE_MINUS_TIME` | Update-Time | `update-time` | date |
| `UPDATE_MODE` | Update Mode | `update_mode` | date |
| `UPDATE_TIME` | Update Time | `update_time` | date |

## Other

*36 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `ADR` | Adr | `ADR` | float |
| `ADRP` | Adrp | `ADRP` | float |
| `BARS_COUNT` | Bars Count | `bars_count` | float |
| `CHANGE` | Change | `change` | percent |
| `CHANGE_ABS` | Change Abs | `change_abs` | percent |
| `CURRENT_SESSION` | Current Session | `current_session` | float |
| `EXPIRATION` | Expiration | `expiration` | percent |
| `FRACTIONAL` | Fractional | `fractional` | float |
| `INDICATORS_BARS_COUNT` | Indicators Bars Count | `indicators_bars_count` | float |
| `IS_BLACKLISTED` | Is Blacklisted | `is_blacklisted` | float |
| `IS_PRIMARY` | Is Primary | `is_primary` | float |
| `IS_SHARIAH_COMPLIANT` | Is Shariah Compliant | `is_shariah_compliant` | float |
| `KIND` | Kind | `kind` | float |
| `KIND_MINUS_DELAY` | Kind-Delay | `kind-delay` | float |
| `MARKET` | Market | `market` | float |
| `MINMOV` | Minmov | `minmov` | float |
| `MINMOVE2` | Minmove2 | `minmove2` | float |
| `POPULARITY_RANK` | Popularity Rank | `popularity_rank` | float |
| `POSTMARKET_CHANGE` | Postmarket Change | `postmarket_change` | percent |
| `POSTMARKET_CHANGE_ABS` | Postmarket Change Abs | `postmarket_change_abs` | percent |
| `POST_CHANGE` | Post Change | `post_change` | percent |
| `PRE_CHANGE` | Pre Change | `pre_change` | percent |
| `PRE_CHANGE_ABS` | Pre Change Abs | `pre_change_abs` | percent |
| `PRODUCT` | Product | `product` | float |
| `PROVIDER_MINUS_ID` | Provider-Id | `provider-id` | float |
| `RATES_CF` | Rates Cf | `rates_cf` | float |
| `RATES_CURRENT` | Rates Current | `rates_current` | float |
| `RATES_FH` | Rates FH | `rates_fh` | float |
| `RATES_FQ` | Rates FQ | `rates_fq` | float |
| `RATES_FY` | Rates FY | `rates_fy` | float |
| `RATES_MC` | Rates Mc | `rates_mc` | float |
| `RATES_PT` | Rates Pt | `rates_pt` | float |
| `RATES_TTM` | Rates TTM | `rates_ttm` | float |
| `SUBMARKET` | Submarket | `submarket` | float |
| `VALUE_TRADED` | Value Traded | `Value.Traded` | float |
| `VWAP` | VWAP | `VWAP` | float |
