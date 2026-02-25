#!/usr/bin/env python3
"""
Forex Opportunity Screener Example

This example demonstrates how to use the ForexOpportunityScreener to find
trading opportunities across multiple forex pairs and timeframes.

Usage:
    python examples/forex_opportunity_screen.py

Requirements:
    pip install tvscreener[cli]
"""

from tvscreener.screeners.forex_opportunity import (
    ForexOpportunityScreener,
    ForexScreenerConfig,
    RatingFilter,
    RocFilter,
)


def main():
    config = ForexScreenerConfig(
        rating_filters=[
            RatingFilter("all", 0.1),
            RatingFilter("ma", 0.1),
            RatingFilter("oscillator", 0.1),
        ],
        roc_filter=RocFilter(min_roc=0),
    )

    scanner = ForexOpportunityScreener(
        pairs=["EURUSD", "GBPUSD", "USDJPY", "USDCHF", "USDCAD"],
        timeframes=["15", "60", "240"],
        config=config,
    )

    print("Scanning forex opportunities...")
    print(f"Configuration: {scanner}")
    print()

    scanner.print_summary()

    print("\nExporting to files...")
    scanner.to_csv("forex_opportunities.csv")
    scanner.to_json("forex_opportunities.json")
    print("Done!")


if __name__ == "__main__":
    main()
