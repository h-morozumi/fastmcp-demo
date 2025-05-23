from fastmcp import FastMCP

mcp = FastMCP("My MCP Server Streamable HTTP")

# Adding a Tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


# Ruun the Server
if __name__ == "__main__":
    # This runs the server
    mcp.run(transport="streamable-http",port=9000)
