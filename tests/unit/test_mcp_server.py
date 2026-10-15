import asyncio
import unittest

try:
    import mcp  # noqa: F401
    HAS_MCP = True
except ImportError:
    HAS_MCP = False


@unittest.skipUnless(HAS_MCP, "mcp extra not installed")
class TestMCPServer(unittest.TestCase):

    def test_server_imports_and_registers_tools(self):
        # Import fails on mcp 2.x if the FastMCP/MCPServer fallback breaks (#60)
        from tvscreener.mcp import mcp as server

        self.assertEqual("tvscreener", server.name)
        tools = asyncio.run(server.list_tools())
        names = {tool.name for tool in tools}
        self.assertEqual({
            "discover_fields", "list_field_types", "custom_query",
            "search_stocks", "search_crypto", "search_forex",
            "get_top_movers", "list_sectors", "list_filter_operators",
            "get_calendar", "yield_curve", "symbol_data",
            "financials", "corporate_events", "seasonals", "quotes",
            "news", "company_documents", "earnings_calls", "read_text",
            "find_symbols", "peers", "forward_curve", "volatility_smile",
        }, names)

    def test_list_sectors_returns_tradingview_sectors(self):
        from tvscreener.field import Sector
        from tvscreener.mcp.server import list_sectors

        listed = {line.strip()[2:] for line in list_sectors().splitlines()[1:]}
        self.assertEqual({s.value for s in Sector if s is not Sector.ANY}, listed)
        self.assertNotIn("Healthcare", listed)



@unittest.skipUnless(HAS_MCP, "mcp extra not installed")
class TestMCPMarketDataTools(unittest.TestCase):

    def test_financials_in_millions_with_periods_as_columns(self):
        import pandas as pd
        from unittest.mock import patch
        from tvscreener.mcp import server

        df = pd.DataFrame({"period_end": [None, None], "Total revenue": [3e11, 4e11]}, index=["2024", "2025"])
        df.attrs["currency"] = "USD"
        with patch.object(server, "get_financials", return_value=df):
            text = server.financials("NASDAQ:AAPL", periods=1)
        self.assertIn("millions USD", text)
        self.assertIn("400,000", text)
        self.assertNotIn("2024", text)

    def test_read_text_routes_by_id(self):
        from unittest.mock import patch
        from tvscreener.mcp import server

        with patch.object(server, "get_document", return_value="transcript") as doc,                 patch.object(server, "get_article", return_value="x" * 50) as article:
            self.assertEqual("transcript", server.read_text("urn:transcripts:quartr.com:1"))
            self.assertIn("truncated, 50 characters", server.read_text("DJN_1:0", max_chars=10))
        doc.assert_called_once()
        article.assert_called_once_with("DJN_1:0")

    def test_yield_curve_single_country_or_matrix(self):
        import pandas as pd
        from unittest.mock import patch
        from tvscreener.mcp import server

        with patch.object(server, "get_yield_curve", return_value=pd.DataFrame({"tenor": ["10Y"]})) as curve,                 patch.object(server, "get_yield_matrix", return_value=pd.DataFrame({"10Y": [5.0]}, index=["US"])) as matrix:
            server.yield_curve("US")
            server.yield_curve("US, DE", tenors="2Y,10Y")
            server.yield_curve("ALL")
        curve.assert_called_once_with("US")
        self.assertEqual((["US", "DE"], ["2Y", "10Y"]), matrix.call_args_list[0].args)
        self.assertEqual((None, None), matrix.call_args_list[1].args)

    def test_economic_calendar_kind(self):
        import pandas as pd
        from unittest.mock import patch
        from tvscreener.mcp import server

        events = pd.DataFrame({"date": [1], "title": ["CPI"], "category": ["prce"], "source": ["BLS"],
                               "reference_date": [None], "id": ["1"]})
        with patch.object(server, "get_economic_calendar", return_value=events) as calendar:
            text = server.get_calendar("economic", "2026-10-15", countries="US,EU", importance="high")
        self.assertEqual({"countries": ["US", "EU"], "importance": "high"}, calendar.call_args.kwargs)
        self.assertIn("CPI", text)
        self.assertNotIn("BLS", text)

    def test_custom_query_reports_invalid_filters(self):
        from tvscreener.mcp.server import custom_query

        text = custom_query(filters='[{"field": "PRICE", "operator": ">", "value": 1}]')
        self.assertIn("Unknown filter keys ['operator']", text)
        self.assertIn("Unknown asset_type", custom_query(asset_type="stonks"))
        self.assertIn("Unknown field 'PRICX'", custom_query(fields="NAME,PRICX"))
        self.assertIn("Unknown sort_by field", custom_query(sort_by="NOT_A_FIELD_AT_ALL"))


if __name__ == '__main__':
    unittest.main()
