# mcp_sse Project

The `mcp_sse` project is part of the FastMCP demo, which implements server-sent events (SSE) functionalities. This allows the server to push real-time updates to the client over HTTP.

## Features

- Real-time data streaming from the server to the client.
- Simple and efficient implementation of SSE.
- Easy integration with other components of the FastMCP demo.

## Usage

1. Ensure you have Python installed on your machine.
2. Navigate to the `mcp_sse` directory.
3. Run the main application using the command:
   ```
   python main.py
   ```
4. Access the SSE endpoint from your web browser or a client that supports SSE.

```
.venv/Scripts/activate
uv run main.py
     or
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



## Dependencies

- Flask (or any other web framework you choose to use for handling HTTP requests).
- Any other libraries required for your specific implementation.

## Example

Refer to the `main.py` file for an example implementation of the SSE functionalities.