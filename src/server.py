from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="Researcher MCP",
    instructions="",
    host="0.0.0.0",
    port=8085,
)

from tools.search import register_tools
register_tools(mcp)

if __name__ == "__main__":
    mcp.run(transport='stdio')