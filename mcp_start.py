from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name='calculator',
    host='0.0.0.0',
    port=8086
)



@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


if __name__ == '__main__':
    transport = 'stdio'
    if transport == 'stdio':
        mcp.run(transport='stdio')
    elif transport == 'sse':
        mcp.run(transport='sse')
    else:
        raise ValueError('unknown transport')