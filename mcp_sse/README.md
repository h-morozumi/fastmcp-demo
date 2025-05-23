# mcp_sse Project

The `mcp_sse` project is part of the FastMCP demo, which implements server-sent events (SSE) functionalities. This allows the server to push real-time updates to the client over HTTP.

## Features

- Real-time data streaming from the server to the client.
- Simple and efficient implementation of SSE.
- Easy integration with other components of the FastMCP demo.

## Usage

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
   fastmcp run main.py --transport sse 
   ```

```
(mcp-sse) PS C:\Users\fastmcp-demo\mcp_sse> uv run main.py
[05/22/25 20:24:56] INFO     Starting MCP server 'My MCP Server SSE' with transport 'sse' on http://127.0.0.1:8000/sse
INFO:     Started server process [14388]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

## Checking the Operation of MCP Server (SSE) Using MCP Inspector

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
   (mcp-stdio) PS C:\Users\fastmcp-demo\mcp_sse> fastmcp dev main.py
   Starting MCP inspector...
   🔍 MCP Inspector is up and running at http://127.0.0.1:6274 🚀
   ⚙️ Proxy server listening on port 6277
   ```
5. Input parameters in the input box and press the Connect button to start the MCP server.

   - Transport Type:
      - `sse` - Server-Sent Events
   - URL:
      - http://localhost:8000/sse

## Example

Refer to the `main.py` file for an example implementation of the SSE functionalities.