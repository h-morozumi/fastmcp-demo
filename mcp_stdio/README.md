# mcp_stdio Project

The `mcp_stdio` project is part of the FastMCP demo, which showcases various functionalities related to standard input and output operations.

## Purpose

This project implements standard input/output functionalities that allow users to interact with the MCP Server through the command line. It serves as a demonstration of how to handle input and output in a Python environment.

## Usage

To test the `mcp_stdio` project using MCP Inspector, execute the following commands in your terminal:
```
.venv/Scripts/activate
fastmcp dev main.py
```

Once started, access [http://127.0.0.1:6274](http://127.0.0.1:6274).
```
(mcp-stdio) PS C:\Users\fastmcp-demo\mcp_stdio> fastmcp dev main.py
Starting MCP inspector...
🔍 MCP Inspector is up and running at http://127.0.0.1:6274 🚀
⚙️ Proxy server listening on port 6277
```

Press the Connect button to start the MCP server.

## Dependencies

This project requires Python 3.x. No additional libraries are needed for basic functionality. However, if you plan to extend the project, consider using libraries such as `argparse` for enhanced command-line argument parsing.

## Example

An example of how to use the `mcp_stdio` project can be found in the `main.py` file, which includes sample input and output operations.