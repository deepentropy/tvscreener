# BondField Reference

Fields available for bond screening. Includes yield, coupon, maturity, and credit rating data.

**Total Fields:** 201

## Table of Contents

- [Metadata](#metadata) (28 fields)
- [Price Data](#price-data) (32 fields)
- [Volume](#volume) (3 fields)
- [Performance](#performance) (1 fields)
- [Moving Averages](#moving-averages) (6 fields)
- [Oscillators](#oscillators) (2 fields)
- [Dividends & Yield](#dividends--yield) (7 fields)
- [Earnings & Income](#earnings--income) (2 fields)
- [Bond Data](#bond-data) (41 fields)
- [Crypto Data](#crypto-data) (2 fields)
- [DEX Data](#dex-data) (2 fields)
- [Time & Dates](#time--dates) (15 fields)
- [Other](#other) (60 fields)

---

## Metadata

*28 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `ACTIVE_SYMBOL` | Active Symbol | `active_symbol` | float |
| `BASE_CURRENCY_KIND` | Base Currency Kind | `base_currency_kind` | text |
| `COUNTRY` | Country | `country` | text |
| `COUNTRY_CODE` | Country Code | `country_code` | text |
| `COUNTRY_CODE_FUND` | Country Code Fund | `country_code_fund` | text |
| `COUNTRY_FUND` | Country Fund | `country_fund` | text |
| `CREDIT_ENHANCEMENT_TYPE` | Credit Enhancement Type | `credit_enhancement_type` | text |
| `CURRENCY` | Currency | `currency` | text |
| `CURRENCY_ID` | Currency Id | `currency_id` | text |
| `CURRENCY_KIND` | Currency Kind | `currency_kind` | text |
| `DESCRIPTION` | Description | `description` | text |
| `DURATION_TYPE` | Duration Type | `duration_type` | percent |
| `EXCHANGE` | Exchange | `exchange` | percent |
| `FUNDAMENTAL_CURRENCY_CODE` | Fundamental Currency Code | `fundamental_currency_code` | text |
| `INDUSTRY` | Industry | `industry` | text |
| `IS_SYMBOL_PRIMARY_LISTING` | Is Symbol Primary Listing | `is_symbol_primary_listing` | float |
| `LOGOID` | Logoid | `logoid` | text |
| `NAME` | Name | `name` | text |
| `OFFER_TYPE` | Offer Type | `offer_type` | text |
| `PLACEMENT_TYPE` | Placement Type | `placement_type` | text |
| `PRINCIPAL_REDEMPTION_TYPE` | Principal Redemption Type | `principal_redemption_type` | text |
| `REDEMPTION_TYPE` | Redemption Type | `redemption_type` | text |
| `SECTOR` | Sector | `sector` | text |
| `SOURCE_MINUS_LOGOID` | Source-Logoid | `source-logoid` | text |
| `SUBTYPE` | Subtype | `subtype` | text |
| `SYMBOL` | Symbol | `symbol` | float |
| `TYPE` | Type | `type` | text |
| `TYPESPECS` | Typespecs | `typespecs` | text |

## Price Data

*32 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `ALL_TIME_HIGH` | All Time High | `all_time_high` | date |
| `ALL_TIME_HIGH_DAY` | All Time High Day | `all_time_high_day` | date |
| `ALL_TIME_LOW` | All Time Low | `all_time_low` | date |
| `ALL_TIME_LOW_DAY` | All Time Low Day | `all_time_low_day` | date |
| `ALL_TIME_OPEN` | All Time Open | `all_time_open` | date |
| `ASK` | Ask | `ask` | float |
| `ASK_NET` | Ask Net | `ask_net` | float |
| `ASK_PCT` | Ask Pct | `ask_pct` | percent |
| `BID` | Bid | `bid` | float |
| `BID_ASK_SPREAD_PCT` | Bid Ask Spread Pct | `bid_ask_spread_pct` | percent |
| `BID_NET` | Bid Net | `bid_net` | float |
| `BID_PCT` | Bid Pct | `bid_pct` | percent |
| `CALL_NEXT_PRICE` | Call Next Price | `call_next_price` | float |
| `CHANGE_FROM_OPEN` | Change From Open | `change_from_open` | percent |
| `CHANGE_FROM_OPEN_ABS` | Change From Open Abs | `change_from_open_abs` | percent |
| `CLOSE` | Close | `close` | float |
| `CLOSE_NET` | Close Net | `close_net` | float |
| `CLOSE_PCT` | Close Pct | `close_pct` | percent |
| `COUPON_EXDATE_GAP` | Coupon Exdate Gap | `coupon_exdate_gap` | date |
| `COUPON_EXDATE_GAP_SORT` | Coupon Exdate Gap Sort | `coupon_exdate_gap_sort` | date |
| `GAP` | Gap | `gap` | float |
| `GAP_DOWN` | Gap Down | `gap_down` | float |
| `GAP_DOWN_ABS` | Gap Down Abs | `gap_down_abs` | float |
| `GAP_UP` | Gap Up | `gap_up` | float |
| `GAP_UP_ABS` | Gap Up Abs | `gap_up_abs` | float |
| `HIGH` | High | `high` | float |
| `LAST_MINUS_PRICE_MINUS_UPDATE_MINUS_TIME` | Last-Price-Update-Time | `last-price-update-time` | date |
| `LOW` | Low | `low` | float |
| `OFFER_PRICE_PCT` | Offer Price Pct | `offer_price_pct` | percent |
| `OPEN` | Open | `open` | float |
| `PRICESCALE` | Pricescale | `pricescale` | float |
| `PUT_NEXT_PRICE` | Put Next Price | `put_next_price` | float |

## Volume

*3 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `VOLUME` | Volume | `volume` | number_group |
| `VOLUME_CHANGE` | Volume Change | `volume_change` | percent |
| `VOLUME_CHANGE_ABS` | Volume Change Abs | `volume_change_abs` | percent |

## Performance

*1 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `PERF_ALL` | Perf All | `Perf.All` | percent |

## Moving Averages

*6 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `PREMARKET_CHANGE` | Premarket Change | `premarket_change` | percent |
| `PREMARKET_CHANGE_ABS` | Premarket Change Abs | `premarket_change_abs` | percent |
| `PREMARKET_CHANGE_FROM_OPEN` | Premarket Change From Open | `premarket_change_from_open` | percent |
| `PREMARKET_CHANGE_FROM_OPEN_ABS` | Premarket Change From Open Abs | `premarket_change_from_open_abs` | percent |
| `PREMARKET_GAP` | Premarket Gap | `premarket_gap` | float |
| `PREMATURE_REDEMPTION` | Premature Redemption | `premature_redemption` | float |

## Oscillators

*2 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `CONVERSION_OPTION` | Conversion Option | `conversion_option` | float |
| `USE_OF_PROCEEDS` | Use Of Proceeds | `use_of_proceeds` | float |

## Dividends & Yield

*7 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `CURRENT_YIELD` | Current Yield | `current_yield` | percent |
| `RATES_DIVIDEND_RECENT` | Rates Dividend Recent | `rates_dividend_recent` | float |
| `RATES_DIVIDEND_UPCOMING` | Rates Dividend Upcoming | `rates_dividend_upcoming` | float |
| `YIELD_TO_CALL` | Yield To Call | `yield_to_call` | percent |
| `YIELD_TO_MATURITY` | Yield To Maturity | `yield_to_maturity` | percent |
| `YIELD_TO_PUT` | Yield To Put | `yield_to_put` | percent |
| `YIELD_TO_WORST` | Yield To Worst | `yield_to_worst` | percent |

## Earnings & Income

*2 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `RATES_EARNINGS_FQ` | Rates Earnings FQ | `rates_earnings_fq` | float |
| `RATES_EARNINGS_NEXT_FQ` | Rates Earnings Next FQ | `rates_earnings_next_fq` | float |

## Bond Data

*41 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `ACCRUED_COUPON_INTEREST` | Accrued Coupon Interest | `accrued_coupon_interest` | float |
| `BOND_AGENTS` | Bond Agents | `bond_agents` | float |
| `BOND_CURRENCY` | Bond Currency | `Bond.Currency` | text |
| `BOND_INVESTMENT_GRADE` | Bond Investment Grade | `bond_investment_grade` | float |
| `BOND_ISSUER_CR_PARENT` | Bond Issuer Cr Parent | `bond_issuer_cr_parent` | float |
| `BOND_ISSUER_CR_PARENT_STOCK_SYMBOL` | Bond Issuer Cr Parent Stock Symbol | `bond_issuer_cr_parent_stock_symbol` | float |
| `BOND_ISSUER_SNP_OUTLOOK_LT` | Bond Issuer S&P Outlook LT | `bond_issuer_snp_outlook_lt` | float |
| `BOND_ISSUER_SNP_OUTLOOK_ST` | Bond Issuer S&P Outlook ST | `bond_issuer_snp_outlook_st` | float |
| `BOND_ISSUER_SNP_RATING_LT` | Bond Issuer S&P Rating LT | `bond_issuer_snp_rating_lt` | float |
| `BOND_ISSUER_SNP_RATING_LT_H` | Bond Issuer S&P Rating LT H | `bond_issuer_snp_rating_lt_h` | float |
| `BOND_ISSUER_SNP_RATING_ST` | Bond Issuer S&P Rating ST | `bond_issuer_snp_rating_st` | float |
| `BOND_ISSUER_SNP_RATING_ST_H` | Bond Issuer S&P Rating ST H | `bond_issuer_snp_rating_st_h` | float |
| `BOND_ISSUER_STOCK_SYMBOL` | Bond Issuer Stock Symbol | `bond_issuer_stock_symbol` | float |
| `BOND_ISSUER_TYPE` | Bond Issuer Type | `bond_issuer_type` | text |
| `BOND_SNP_OUTLOOK_LT` | Bond S&P Outlook LT | `bond_snp_outlook_lt` | float |
| `BOND_SNP_RATING_LT` | Bond S&P Rating LT | `bond_snp_rating_lt` | float |
| `BOND_SNP_RATING_LT_H` | Bond S&P Rating LT H | `bond_snp_rating_lt_h` | float |
| `BOND_TYPE_GEN` | Bond Type Gen | `bond_type_gen` | text |
| `COUPON` | Coupon | `coupon` | float |
| `COUPON_CHANGE_TYPE` | Coupon Change Type | `coupon_change_type` | percent |
| `COUPON_CURRENCY` | Coupon Currency | `coupon_currency` | text |
| `COUPON_DATE_NEXT` | Coupon Date Next | `coupon_date_next` | date |
| `COUPON_DATE_PREV` | Coupon Date Prev | `coupon_date_prev` | date |
| `COUPON_DAYCOUNT_TYPE` | Coupon Daycount Type | `coupon_daycount_type` | text |
| `COUPON_FREQUENCY` | Coupon Frequency | `coupon_frequency` | float |
| `COUPON_LINK` | Coupon Link | `coupon_link` | float |
| `COUPON_NEXT_RESET_DATE` | Coupon Next Reset Date | `coupon_next_reset_date` | date |
| `COUPON_PMT_DATE_TYPE` | Coupon Pmt Date Type | `coupon_pmt_date_type` | text |
| `COUPON_RATE_CEILING` | Coupon Rate Ceiling | `coupon_rate_ceiling` | float |
| `COUPON_RATE_FLOOR` | Coupon Rate Floor | `coupon_rate_floor` | float |
| `COUPON_RESET_FREQUENCY` | Coupon Reset Frequency | `coupon_reset_frequency` | float |
| `COUPON_TYPE_CURRENT` | Coupon Type Current | `coupon_type_current` | text |
| `COUPON_TYPE_GENERAL` | Coupon Type General | `coupon_type_general` | text |
| `COUPON_UNDERLYING_INDEX` | Coupon Underlying Index | `coupon_underlying_index` | float |
| `CURRENT_COUPON` | Current Coupon | `current_coupon` | float |
| `DAYS_TO_MATURITY` | Days To Maturity | `days_to_maturity` | float |
| `MATURITY_DATE` | Maturity Date | `maturity_date` | date |
| `MATURITY_TYPE` | Maturity Type | `maturity_type` | text |
| `ORIGINAL_MATURITY` | Original Maturity | `original_maturity` | float |
| `TERM_MINUS_TO_MINUS_MATURITY` | Term-To-Maturity | `term-to-maturity` | float |
| `YEARS_TO_MATURITY` | Years To Maturity | `years_to_maturity` | float |

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

*15 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `BUS_DAY_CONV_METHOD` | Bus Day Conv Method | `bus_day_conv_method` | float |
| `CALL_NEXT_DATE` | Call Next Date | `call_next_date` | date |
| `DAILY_MINUS_BAR_TIME` | Daily-Bar Time | `daily-bar.time` | date |
| `ISSUE_DATE` | Issue Date | `issue_date` | date |
| `LAST_BAR_UPDATE_TIME` | Last Bar Update Time | `last_bar_update_time` | date |
| `MAKE_WHOLE_CALL_END_DATE` | Make Whole Call End Date | `make_whole_call_end_date` | date |
| `MAKE_WHOLE_CALL_START_DATE` | Make Whole Call Start Date | `make_whole_call_start_date` | date |
| `MINUTE_MINUS_BAR_TIME` | Minute-Bar Time | `minute-bar.time` | date |
| `OFFER_DATE` | Offer Date | `offer_date` | date |
| `PUT_NEXT_DATE` | Put Next Date | `put_next_date` | date |
| `RATES_TIME_SERIES` | Rates Time Series | `rates_time_series` | date |
| `TIME` | Time | `time` | date |
| `UPDATE_MINUS_TIME` | Update-Time | `update-time` | date |
| `UPDATE_MODE` | Update Mode | `update_mode` | date |
| `UPDATE_TIME` | Update Time | `update_time` | date |

## Other

*60 fields*

| Enum Name | Label | API Name | Format |
|-----------|-------|----------|--------|
| `AMOUNT_OUTSTANDING_RATIO` | Amount Outstanding Ratio | `amount_outstanding_ratio` | percent |
| `BARS_COUNT` | Bars Count | `bars_count` | float |
| `CALL_FREQUENCY` | Call Frequency | `call_frequency` | float |
| `CALL_OPTION` | Call Option | `call_option` | float |
| `CHANGE` | Change | `change` | percent |
| `CHANGE_ABS` | Change Abs | `change_abs` | percent |
| `COVENANT` | Covenant | `covenant` | float |
| `CREDIT_ENHANCEMENT_STATUS` | Credit Enhancement Status | `credit_enhancement_status` | float |
| `CURRENT_SESSION` | Current Session | `current_session` | float |
| `DENOM_INCREMENT` | Denom Increment | `denom_increment` | float |
| `DENOM_MIN` | Denom Min | `denom_min` | float |
| `EXPIRATION` | Expiration | `expiration` | percent |
| `FINAL_REDEMPTION_AMOUNT` | Final Redemption Amount | `final_redemption_amount` | float |
| `FOREX_PRIORITY` | Forex Priority | `forex_priority` | float |
| `FRACTIONAL` | Fractional | `fractional` | float |
| `INDICATORS_BARS_COUNT` | Indicators Bars Count | `indicators_bars_count` | float |
| `INFLATION_PROTECTION` | Inflation Protection | `inflation_protection` | float |
| `ISSUE_AMOUNT` | Issue Amount | `issue_amount` | float |
| `ISSUE_STATUS` | Issue Status | `issue_status` | float |
| `IS_BLACKLISTED` | Is Blacklisted | `is_blacklisted` | float |
| `IS_PRIMARY` | Is Primary | `is_primary` | float |
| `IS_SHARIAH_COMPLIANT` | Is Shariah Compliant | `is_shariah_compliant` | float |
| `KIND` | Kind | `kind` | float |
| `KIND_MINUS_DELAY` | Kind-Delay | `kind-delay` | float |
| `MAKE_WHOLE_CALL_OPTION` | Make Whole Call Option | `make_whole_call_option` | float |
| `MAKE_WHOLE_CALL_SPREAD` | Make Whole Call Spread | `make_whole_call_spread` | float |
| `MARKET` | Market | `market` | float |
| `MEASURE` | Measure | `measure` | float |
| `MINMOV` | Minmov | `minmov` | float |
| `MINMOVE2` | Minmove2 | `minmove2` | float |
| `NOMINAL_VALUE` | Nominal Value | `nominal_value` | float |
| `OUTSTANDING_AMOUNT` | Outstanding Amount | `outstanding_amount` | float |
| `OWNERSHIP_FORM` | Ownership Form | `ownership_form` | float |
| `PLEDGE_STATUS` | Pledge Status | `pledge_status` | float |
| `POISON_PUT_OPTION` | Poison Put Option | `poison_put_option` | float |
| `POPULARITY_RANK` | Popularity Rank | `popularity_rank` | float |
| `POSTMARKET_CHANGE` | Postmarket Change | `postmarket_change` | percent |
| `POSTMARKET_CHANGE_ABS` | Postmarket Change Abs | `postmarket_change_abs` | percent |
| `POST_CHANGE` | Post Change | `post_change` | percent |
| `PRE_CHANGE` | Pre Change | `pre_change` | percent |
| `PRE_CHANGE_ABS` | Pre Change Abs | `pre_change_abs` | percent |
| `PROVIDER_MINUS_ID` | Provider-Id | `provider-id` | float |
| `PUT_FREQUENCY` | Put Frequency | `put_frequency` | float |
| `PUT_OPTION` | Put Option | `put_option` | float |
| `RATES_CF` | Rates Cf | `rates_cf` | float |
| `RATES_CURRENT` | Rates Current | `rates_current` | float |
| `RATES_FH` | Rates FH | `rates_fh` | float |
| `RATES_FQ` | Rates FQ | `rates_fq` | float |
| `RATES_FY` | Rates FY | `rates_fy` | float |
| `RATES_MC` | Rates Mc | `rates_mc` | float |
| `RATES_PT` | Rates Pt | `rates_pt` | float |
| `RATES_TTM` | Rates TTM | `rates_ttm` | float |
| `REDEMPTIONS_H` | Redemptions H | `redemptions_h` | float |
| `REGION` | Region | `region` | float |
| `RTC` | Rtc | `rtc` | float |
| `SENIORITY_LEVEL` | Seniority Level | `seniority_level` | float |
| `SINKING_FUND` | Sinking Fund | `sinking_fund` | float |
| `SOCIAL_RESPONSIBILITY` | Social Responsibility | `social_responsibility` | float |
| `SUBMARKET` | Submarket | `submarket` | float |
| `VALUE_MINUS_UNIT_MINUS_ID` | Value-Unit-Id | `value-unit-id` | float |
