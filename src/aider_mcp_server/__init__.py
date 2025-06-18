"""
MCP server for Aider AI Code.
"""

# Apply patches to handle missing modules in Python 3.13
from aider_mcp_server.patches import apply_patches
apply_patches()

from aider_mcp_server.__main__ import main

__all__ = ["main"]
