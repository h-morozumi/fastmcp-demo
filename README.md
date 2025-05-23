# FastMCP Demo

This repository is a demo project for FastMCP. Using FastMCP, it creates MCP Server and MCP Client. The MCP Server creates three demos: STDIO (Standard IO), SSE (Server-Sent Event), and Streamable HTTP.

[Model Context Protocol](https://modelcontextprotocol.io/introduction) 

## Requirements

- [Python 3.13 or higher](https://www.python.org/downloads/)
- [uv 0.6.16 or higher](https://docs.astral.sh/uv/getting-started/installation/)


## Sub-Projects

After checking out the repository, initialize each project by executing the following command:
```
uv sync
```
This will create a virtual environment and install the required dependencies for each sub-project.

### 1. mcp_stdio
- **Description**: Implements standard input/output MCP Server.
- **Location**: `mcp_stdio/`
- **Entry Point**: `main.py`
- **Documentation**: See `mcp_stdio/README.md` for details on usage and dependencies.

### 2. mcp_sse
- **Description**: Implements server-sent events (SSE) MCP Server.
- **Location**: `mcp_sse/`
- **Entry Point**: `main.py`
- **Documentation**: See `mcp_sse/README.md` for details on usage and dependencies.

### 3. mcp_stream
- **Description**: Implements Streamable HTTP MCP Server.
- **Location**: `mcp_stream/`
- **Entry Point**: `main.py`
- **Documentation**: See `mcp_stream/README.md` for details on usage and dependencies.

### 4. mcp_client
- **Description**: Implements client-side MCP Client.
- **Location**: `mcp_client/`
- **Entry Point**: `main.py`
- **Documentation**: See `mcp_client/README.md` for details on usage and dependencies.

## Running the Projects

To run any of the sub-projects, navigate to the respective directory and execute the `main.py` file. Ensure that you have all necessary dependencies installed as mentioned in each sub-project's README.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your feedback and contributions are welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
