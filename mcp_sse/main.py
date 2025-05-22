from fastmcp import FastMCP

mcp = FastMCP("My MCP Server SSE")

# Adding a Tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiplies two numbers together."""
    return a * b

# Ruun the Server
if __name__ == "__main__":
    # This runs the server, defaulting to SSE
    mcp.run(transport="sse")
