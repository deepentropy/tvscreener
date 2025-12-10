"""
Export tvscreener field and enum data to JavaScript for the code generator app.
Run this script to regenerate field-data.js when fields change.
"""
import json
import sys
from pathlib import Path

# Add parent to path to import tvscreener
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from tvscreener.field.stock import StockField
from tvscreener.field.crypto import CryptoField
from tvscreener.field.forex import ForexField
from tvscreener.field.bond import BondField
from tvscreener.field.futures import FuturesField
from tvscreener.field.coin import CoinField
from tvscreener.field import IndexSymbol
from tvscreener.filter import FilterOperator

# Screener configurations
SCREENERS = {
    "stock": {
        "name": "Stock Screener",
        "class": "StockScreener",
        "fieldClass": "StockField",
        "fieldEnum": StockField,
        "hasIndex": True,
        "hasMarket": True,
    },
    "crypto": {
        "name": "Crypto Screener",
        "class": "CryptoScreener",
        "fieldClass": "CryptoField",
        "fieldEnum": CryptoField,
        "hasIndex": False,
        "hasMarket": False,
    },
    "forex": {
        "name": "Forex Screener",
        "class": "ForexScreener",
        "fieldClass": "ForexField",
        "fieldEnum": ForexField,
        "hasIndex": False,
        "hasMarket": False,
    },
    "bond": {
        "name": "Bond Screener",
        "class": "BondScreener",
        "fieldClass": "BondField",
        "fieldEnum": BondField,
        "hasIndex": False,
        "hasMarket": True,
    },
    "futures": {
        "name": "Futures Screener",
        "class": "FuturesScreener",
        "fieldClass": "FuturesField",
        "fieldEnum": FuturesField,
        "hasIndex": False,
        "hasMarket": False,
    },
    "coin": {
        "name": "Coin Screener (CEX/DEX)",
        "class": "CoinScreener",
        "fieldClass": "CoinField",
        "fieldEnum": CoinField,
        "hasIndex": False,
        "hasMarket": False,
    },
}

# Field categories based on common use patterns
FIELD_CATEGORIES = {
    "Metadata": [
        "NAME", "DESCRIPTION", "SYMBOL", "EXCHANGE", "SECTOR", "INDUSTRY",
        "COUNTRY", "TYPE", "SUBTYPE", "CURRENCY"
    ],
    "Price": [
        "PRICE", "OPEN", "HIGH", "LOW", "CLOSE", "PREMARKET_PRICE",
        "POSTMARKET_PRICE", "PREMARKET_CHANGE_PERCENT", "POSTMARKET_CHANGE_PERCENT",
        "PRICE_52_WEEK_HIGH", "PRICE_52_WEEK_LOW", "GAP_PERCENT", "BID", "ASK"
    ],
    "Change": [
        "CHANGE", "CHANGE_PERCENT", "CHANGE_FROM_OPEN", "CHANGE_FROM_OPEN_PERCENT",
        "CHANGE_1_HOUR", "CHANGE_4_HOUR", "CHANGE_24_HOUR"
    ],
    "Volume": [
        "VOLUME", "AVERAGE_VOLUME_10_DAY", "AVERAGE_VOLUME_30_DAY",
        "AVERAGE_VOLUME_60_DAY", "AVERAGE_VOLUME_90_DAY", "RELATIVE_VOLUME",
        "VOLUME_24H", "TOTAL_VALUE_TRADED"
    ],
    "Performance": [
        "PERFORMANCE_1_WEEK", "PERFORMANCE_1_MONTH", "PERFORMANCE_3_MONTH",
        "PERFORMANCE_6_MONTH", "PERFORMANCE_YEAR_TO_DATE", "PERFORMANCE_1_YEAR",
        "PERFORMANCE_5_YEAR", "PERFORMANCE_ALL_TIME",
        "HIGH_52_WEEK_PERFORMANCE", "LOW_52_WEEK_PERFORMANCE"
    ],
    "Valuation": [
        "MARKET_CAPITALIZATION", "ENTERPRISE_VALUE_FQ", "PE_RATIO_TTM",
        "PRICE_TO_BOOK_FY", "PRICE_TO_SALES_FY", "PRICE_TO_CASH_FLOW_TTM",
        "PRICE_EARNINGS_TO_GROWTH_TTM", "EV_TO_EBITDA_TTM", "EV_TO_REVENUE_TTM"
    ],
    "Dividends": [
        "DIVIDEND_YIELD_FY", "DIVIDENDS_PER_SHARE_FY", "PAYOUT_RATIO_TTM",
        "DIVIDEND_YIELD_RECENT", "DIVIDENDS_PAID_FY",
        "DPS_COMMON_STOCK_PRIMARY_ISSUE_GROWTH_FY", "COUPON"
    ],
    "Profitability": [
        "GROSS_MARGIN_TTM", "OPERATING_MARGIN_TTM", "NET_MARGIN_TTM",
        "RETURN_ON_EQUITY_TTM", "RETURN_ON_ASSETS_TTM", "RETURN_ON_INVESTED_CAPITAL_TTM",
        "FREE_CASH_FLOW_MARGIN_TTM"
    ],
    "Growth": [
        "REVENUE_GROWTH_TTM", "EARNINGS_PER_SHARE_DILUTED_GROWTH_TTM",
        "EARNINGS_PER_SHARE_GROWTH_FY", "REVENUE_GROWTH_FY"
    ],
    "Balance Sheet": [
        "TOTAL_DEBT_FY", "TOTAL_DEBT_TO_EQUITY_FY", "CURRENT_RATIO_FY",
        "QUICK_RATIO_FY", "DEBT_TO_ASSET_FY", "TOTAL_ASSETS_FY"
    ],
    "Earnings": [
        "EARNINGS_PER_SHARE_BASIC_TTM", "EARNINGS_PER_SHARE_DILUTED_TTM",
        "NET_INCOME_FY", "GROSS_PROFIT_FY", "OPERATING_INCOME_FY",
        "FREE_CASH_FLOW_TTM", "EARNINGS_RELEASE_DATE"
    ],
    "RSI": [
        "RELATIVE_STRENGTH_INDEX_7", "RELATIVE_STRENGTH_INDEX_14"
    ],
    "MACD": [
        "MACD_LEVEL_12_26", "MACD_SIGNAL_12_26_9", "MACD_HISTOGRAM_12_26_9"
    ],
    "Stochastic": [
        "STOCHASTIC_K_14_3_3", "STOCHASTIC_D_14_3_3",
        "STOCHASTIC_K_SLOW_14_3_3", "STOCHASTIC_D_SLOW_14_3_3"
    ],
    "Moving Averages": [
        "SIMPLE_MOVING_AVERAGE_5", "SIMPLE_MOVING_AVERAGE_10",
        "SIMPLE_MOVING_AVERAGE_20", "SIMPLE_MOVING_AVERAGE_50",
        "SIMPLE_MOVING_AVERAGE_100", "SIMPLE_MOVING_AVERAGE_200",
        "EXPONENTIAL_MOVING_AVERAGE_5", "EXPONENTIAL_MOVING_AVERAGE_10",
        "EXPONENTIAL_MOVING_AVERAGE_20", "EXPONENTIAL_MOVING_AVERAGE_50",
        "EXPONENTIAL_MOVING_AVERAGE_100", "EXPONENTIAL_MOVING_AVERAGE_200"
    ],
    "Other Oscillators": [
        "COMMODITY_CHANNEL_INDEX_20", "AVERAGE_DIRECTIONAL_INDEX_14",
        "AWESOME_OSCILLATOR", "MOMENTUM_10", "WILLIAMS_PERCENT_RANGE_14",
        "ULTIMATE_OSCILLATOR_7_14_28", "BULLS_BEARS_POWER"
    ],
    "Volatility": [
        "AVERAGE_TRUE_RANGE_14", "VOLATILITY_DAY", "VOLATILITY_WEEK",
        "VOLATILITY_MONTH", "BOLLINGER_UPPER_BAND_20", "BOLLINGER_LOWER_BAND_20"
    ],
    "Recommendations": [
        "RECOMMENDATION_MARK", "RECOMMENDATION_ALL", "RECOMMENDATION_MA",
        "RECOMMENDATION_OTHER"
    ],
    "Bond Specific": [
        "YIELD", "COUPON", "MATURITY_DATE", "RATING", "DURATION", "FACE_VALUE"
    ],
    "Crypto Specific": [
        "CIRCULATING_SUPPLY", "TOTAL_SUPPLY", "MAX_SUPPLY"
    ]
}


def get_field_category(field_name: str) -> str:
    """Get the category for a field based on its name."""
    for category, fields in FIELD_CATEGORIES.items():
        if field_name in fields:
            return category
    # Try to infer category from name patterns
    name_upper = field_name.upper()
    if "RSI" in name_upper or "RELATIVE_STRENGTH" in name_upper:
        return "RSI"
    if "MACD" in name_upper:
        return "MACD"
    if "STOCHASTIC" in name_upper:
        return "Stochastic"
    if "SMA" in name_upper or "SIMPLE_MOVING" in name_upper:
        return "Moving Averages"
    if "EMA" in name_upper or "EXPONENTIAL_MOVING" in name_upper:
        return "Moving Averages"
    if "VOLUME" in name_upper:
        return "Volume"
    if "MARGIN" in name_upper or "RETURN_ON" in name_upper:
        return "Profitability"
    if "DIVIDEND" in name_upper or "YIELD" in name_upper or "COUPON" in name_upper:
        return "Dividends"
    if "EARNINGS" in name_upper or "EPS" in name_upper or "INCOME" in name_upper:
        return "Earnings"
    if "DEBT" in name_upper or "ASSET" in name_upper or "RATIO" in name_upper:
        return "Balance Sheet"
    if "GROWTH" in name_upper:
        return "Growth"
    if "PERFORMANCE" in name_upper:
        return "Performance"
    if "PE_" in name_upper or "PRICE_TO" in name_upper or "MARKET_CAP" in name_upper or "EV_" in name_upper:
        return "Valuation"
    if "BOLLINGER" in name_upper or "ATR" in name_upper or "VOLATILITY" in name_upper:
        return "Volatility"
    if "RECOMMEND" in name_upper:
        return "Recommendations"
    if "SUPPLY" in name_upper:
        return "Crypto Specific"
    if "MATURITY" in name_upper or "RATING" in name_upper or "DURATION" in name_upper:
        return "Bond Specific"
    return "Other"


def export_fields(field_enum) -> list:
    """Export all field enum members with their metadata."""
    fields = []
    for field in field_enum:
        try:
            fields.append({
                "name": field.name,
                "label": field.label,
                "fieldName": field.field_name,
                "format": field.format,
                "interval": getattr(field, 'interval', False),
                "historical": getattr(field, 'historical', False),
                "category": get_field_category(field.name)
            })
        except Exception as e:
            print(f"Warning: Could not export {field.name}: {e}")
    return fields


def export_filter_operators() -> list:
    """Export FilterOperator enum values."""
    return [
        {"name": "ABOVE", "symbol": ">", "label": "Greater than"},
        {"name": "ABOVE_OR_EQUAL", "symbol": ">=", "label": "Greater or equal"},
        {"name": "BELOW", "symbol": "<", "label": "Less than"},
        {"name": "BELOW_OR_EQUAL", "symbol": "<=", "label": "Less or equal"},
        {"name": "EQUAL", "symbol": "==", "label": "Equals"},
        {"name": "NOT_EQUAL", "symbol": "!=", "label": "Not equals"},
        {"name": "BETWEEN", "symbol": "between", "label": "Between"},
        {"name": "ISIN", "symbol": "isin", "label": "In list"},
        {"name": "NOT_IN", "symbol": "not_in", "label": "Not in list"},
    ]


def export_index_symbols() -> list:
    """Export IndexSymbol enum values."""
    indices = []
    for idx in IndexSymbol:
        indices.append({
            "name": idx.name,
            "label": idx.label,
            "symbol": idx.symbol
        })
    return indices


def export_markets() -> list:
    """Export Market enum values."""
    return [
        {"name": "AMERICA", "label": "United States"},
        {"name": "UK", "label": "United Kingdom"},
        {"name": "GERMANY", "label": "Germany"},
        {"name": "FRANCE", "label": "France"},
        {"name": "JAPAN", "label": "Japan"},
        {"name": "CANADA", "label": "Canada"},
        {"name": "AUSTRALIA", "label": "Australia"},
        {"name": "INDIA", "label": "India"},
        {"name": "BRAZIL", "label": "Brazil"},
        {"name": "CHINA", "label": "China"},
        {"name": "HONG_KONG", "label": "Hong Kong"},
        {"name": "SWITZERLAND", "label": "Switzerland"},
        {"name": "ALL", "label": "All Markets"},
    ]


def export_symbol_types() -> list:
    """Export SymbolType enum values."""
    return [
        {"name": "COMMON_STOCK", "label": "Common Stock"},
        {"name": "ETF", "label": "ETF"},
        {"name": "MUTUAL_FUND", "label": "Mutual Fund"},
        {"name": "REIT", "label": "REIT"},
        {"name": "PREFERRED_STOCK", "label": "Preferred Stock"},
        {"name": "DEPOSITORY_RECEIPT", "label": "Depository Receipt (ADR)"},
        {"name": "CLOSED_END_FUND", "label": "Closed-End Fund"},
    ]


def export_sectors() -> list:
    """Export sector values (as strings used in API)."""
    return [
        {"value": "Electronic Technology", "label": "Technology"},
        {"value": "Health Technology", "label": "Healthcare"},
        {"value": "Finance", "label": "Finance"},
        {"value": "Energy Minerals", "label": "Energy"},
        {"value": "Consumer Durables", "label": "Consumer Durables"},
        {"value": "Consumer Non-Durables", "label": "Consumer Staples"},
        {"value": "Consumer Services", "label": "Consumer Services"},
        {"value": "Commercial Services", "label": "Commercial Services"},
        {"value": "Industrial Services", "label": "Industrial Services"},
        {"value": "Producer Manufacturing", "label": "Industrials"},
        {"value": "Process Industries", "label": "Materials"},
        {"value": "Non-Energy Minerals", "label": "Mining"},
        {"value": "Utilities", "label": "Utilities"},
        {"value": "Transportation", "label": "Transportation"},
        {"value": "Distribution Services", "label": "Distribution"},
        {"value": "Retail Trade", "label": "Retail"},
        {"value": "Technology Services", "label": "Tech Services"},
        {"value": "Health Services", "label": "Health Services"},
        {"value": "Communications", "label": "Communications"},
        {"value": "Miscellaneous", "label": "Miscellaneous"},
    ]


def export_time_intervals() -> list:
    """Export available time intervals for technical indicators."""
    return [
        {"value": "1", "label": "1 minute"},
        {"value": "5", "label": "5 minutes"},
        {"value": "15", "label": "15 minutes"},
        {"value": "30", "label": "30 minutes"},
        {"value": "60", "label": "1 hour"},
        {"value": "120", "label": "2 hours"},
        {"value": "240", "label": "4 hours"},
        {"value": "1D", "label": "Daily"},
        {"value": "1W", "label": "Weekly"},
        {"value": "1M", "label": "Monthly"},
    ]


def main():
    """Export all data and write to JavaScript file."""
    print("Exporting tvscreener field data...")

    # Export fields for each screener
    screeners_data = {}
    for key, config in SCREENERS.items():
        fields = export_fields(config["fieldEnum"])
        screeners_data[key] = {
            "name": config["name"],
            "class": config["class"],
            "fieldClass": config["fieldClass"],
            "hasIndex": config["hasIndex"],
            "hasMarket": config["hasMarket"],
            "fields": fields,
            "fieldCount": len(fields)
        }
        print(f"  - {config['name']}: {len(fields)} fields")

    # Collect all data
    data = {
        "screeners": screeners_data,
        "operators": export_filter_operators(),
        "indices": export_index_symbols(),
        "markets": export_markets(),
        "symbolTypes": export_symbol_types(),
        "sectors": export_sectors(),
        "timeIntervals": export_time_intervals(),
        "categories": list(FIELD_CATEGORIES.keys()) + ["Other"]
    }

    print(f"  - Exported {len(data['indices'])} indices")

    # Write as JavaScript module
    output_path = Path(__file__).parent.parent / "js" / "field-data.js"

    js_content = f"""// Auto-generated by export_fields.py - DO NOT EDIT MANUALLY
// Run: python docs/scripts/export_fields.py

const FIELD_DATA = {json.dumps(data, indent=2)};

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {{
    module.exports = FIELD_DATA;
}}
"""

    output_path.write_text(js_content, encoding='utf-8')
    print(f"  - Written to {output_path}")
    print("Done!")


if __name__ == "__main__":
    main()
