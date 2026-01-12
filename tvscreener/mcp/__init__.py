"""
MCP (Model Context Protocol) server for tvscreener.

This module provides an MCP server that exposes tvscreener functionality
to AI assistants like Claude.

Usage:
    # Run directly
    python -m tvscreener.mcp

    # Or use the CLI entry point (after installing with mcp extra)
    tvscreener-mcp

    # Register with Claude Code
    claude mcp add tvscreener -- tvscreener-mcp
"""

from .server import mcp, run

__all__ = ["mcp", "run"]
