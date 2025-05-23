# mcp_stream Project

The `mcp_stream` project is part of the FastMCP demo, which showcases various functionalities related to streaming data. This project implements streaming capabilities that allow for efficient data transfer and processing.

## Purpose

The primary purpose of the `mcp_stream` project is to demonstrate how to handle streaming data in the FastMCP framework. It serves as an example of how to implement and utilize streaming functionalities effectively.

## Usage

To run the `mcp_stream` project, execute the following command in your terminal:

1. Activate the virtual environment using venv:
   ```
   .venv/Scripts/activate
   ```
2. Run the main application using the command:
   ```
   uv run main.py
   ```
   or
   ```
   fastmcp run main.py --transport streamable-http --port 9000 
   ```

```
(mcp-stream) PS C:\Users\fastmcp-demo\mcp_stream> uv run main.py
[05/23/25 11:58:09] INFO     Starting MCP server 'My MCP Server Streamable HTTP' with transport 'streamable-http' on http://127.0.0.1:9000/mcp                  server.py:796
INFO:     Started server process [28588]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:9000 (Press CTRL+C to quit)
```

## Checking the Operation of MCP Server (Streamable HTTP) Using MCP Inspector

1. Open a new terminal.
2. Activate the virtual environment using venv.
   ```
   .venv/Scripts/activate
   ```
3. Run the following command to start MCP Inspector.
   ```
   fastmcp dev main.py
   ```
4. Access the URL.

   Once started, access [http://127.0.0.1:6274](http://127.0.0.1:6274).
   ```
   (mcp-stdio) PS C:\Users\fastmcp-demo\mcp_stream> fastmcp dev main.py
   Starting MCP inspector...
   🔍 MCP Inspector is up and running at http://127.0.0.1:6274 🚀
   ⚙️ Proxy server listening on port 6277
   ```
5. Input parameters in the input box and press the Connect button to start the MCP server.

   - Transport Type:
      - `Streamable HTTP` - Streamable HTTP
   - URL:
      - http://localhost:9000/mcp


## Example

Provide an example of how to use the streaming functionalities here, including any relevant code snippets or command-line instructions.

