from fastmcp import FastMCP

mcp = FastMCP("My MCP Server StdIO")

# Adding a Tool
@mcp.tool()
def greet(name: str) -> str:
    """Greets the user with the provided name."""
    return f"Hello, {name}!"

# Ruun the Server
if __name__ == "__main__":
    # This runs the server, defaulting to Standard I/O
    mcp.run()
