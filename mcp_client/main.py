import hotpatch # this is a hotpatch module

import asyncio
import os

from openai import AsyncAzureOpenAI
from openai.types.responses import ResponseTextDeltaEvent
from agents import set_default_openai_client, set_tracing_disabled, Agent, Runner
from agents.mcp import MCPServerStdio, MCPServerSse, MCPServerStreamableHttp

from dotenv import load_dotenv

set_tracing_disabled(disabled=True) # Disable tracing
load_dotenv(override=True) # Load environment variables from .env file

async def main():
    # Initialize the OpenAI client with Azure OpenAI credentials
    async with AsyncAzureOpenAI(
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
        api_version=os.environ["AZURE_OPENAI_API_VERSION"],
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    ) as openai_client:
        set_default_openai_client(openai_client, use_for_tracing=False)

        async with MCPServerStdio(
            name="stdio_server",
            params={
                "command": "uv",
                "args": [
                    "--directory=../mcp_stdio",
                    "run",
                    "main.py"
                ],
            }
        ) as stdio_server, \
            MCPServerSse(
                name="sse_server",
                params={
                    "url":"http://localhost:8000/sse",
                }
            ) as sse_server, \
            MCPServerStreamableHttp(
                name="streamable_http_server",
                params={
                    "url":"http://localhost:9000/mcp",
                }
            ) as streamable_http_server:

            agent = Agent(
                name="Assistant",
                instructions="You are a helpful assistant.",
                mcp_servers=[stdio_server, sse_server, streamable_http_server],
                model=os.environ["AZURE_OPENAI_MODEL"],
            )

            question = "3+4=?"
            print(f"Q: {question}")
            result = Runner.run_streamed(agent, question)
            await print_streamed_response(result)

            question = "3×4=?"
            print(f"\n\nQ: {question}")
            result = Runner.run_streamed(agent, question)
            await print_streamed_response(result)

            question = "Greet! I'm Taro."
            print(f"\n\nQ: {question}")
            result = Runner.run_streamed(agent, question)
            await print_streamed_response(result)


async def print_streamed_response(result):
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)


if __name__ == "__main__":
    asyncio.run(main())

