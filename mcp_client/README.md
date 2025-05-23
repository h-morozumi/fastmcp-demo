# mcp_client Project

The `mcp_client` project is a demo program of the MCP Client that calls the MCP Server from [Azure OpenAI Service](https://learn.microsoft.com/ja-jp/azure/ai-services/openai/overview). Using the [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/), it runs the MCP Server as an agent.

## Features

- Client-side implementation for FastMCP.
- Supports communication with the mcp_stdio, mcp_sse, and mcp_stream projects.

## Usage

1. Start the MCP Server (SSE). Open a new terminal and execute the following commands:
    ```
    cd ../mcp_sse
    .venv/Scripts/activate
    fastmcp run main.py --transport sse
    ```
2. Start the MCP Server (Streamable HTTP). Open a new terminal and execute the following commands:
    ```
    cd ../mcp_stream
    .venv/Scripts/activate
    fastmcp run main.py --transport streamable-http --port 9000
    ```
3. Create a .env file and set the environment variables.
4. Run the MCP Client:
    ```
    cd mcp_client
    .venv/Scripts/activate
    uv run main.py
    ```