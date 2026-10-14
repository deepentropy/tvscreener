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
        }, names)

    def test_list_sectors_returns_tradingview_sectors(self):
        from tvscreener.field import Sector
        from tvscreener.mcp.server import list_sectors

        listed = {line.strip()[2:] for line in list_sectors().splitlines()[1:]}
        self.assertEqual({s.value for s in Sector if s is not Sector.ANY}, listed)
        self.assertNotIn("Healthcare", listed)


if __name__ == '__main__':
    unittest.main()
