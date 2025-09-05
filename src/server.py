from mcp.server.fastmcp import FastMCP
from ..src.tools import search

mcp = FastMCP(
    name="Researcher MCP",
    instructions="",
    host="0.0.0.0",
    port=8085,
)


if __name__ == "__main__":
    mcp.run(transport='stdio')