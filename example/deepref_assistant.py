import asyncio
import uuid
from agents import Agent, Runner, SQLiteSession
from openai.types.responses import ResponseTextDeltaEvent
from agents.mcp import MCPServerStdio
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set up and create the agent
async def build_agent():
    server = MCPServerStdio(
        params={
            "command": "uv",
            "args": ["run", "--with", "mcp", "mcp", "run", "src/server.py"]
        }
    )

    await server.connect()

    # Create and return the agent
    agent = Agent(
        name="DeepRef Copilot Assistant",
        instructions= "You are a helpful assistant capable of reading from a variety of research paper databases (e.g., arXiv, PubMed, Semantic Scholar). Answer each question precisely.",
        mcp_servers=[server],
    )

    return agent, server

# CLI interaction
async def cli_interaction(agent: Agent):
    print("🔧 Deepref Copilot Assistant — Ask me something (type 'exit' to quit):\n")

    random_uuid = uuid.uuid4()
    session = SQLiteSession(
        f"conversation_{random_uuid}",
        "conversations.db"
    )

    while True:
        query = input("> ")
        if query.strip().lower() in {"exit", "quit"}:
            break
        result = Runner.run_streamed(agent, query, session=session)
        if len(query.strip()) > 0:
            try:
                async for event in result.stream_events():
                    if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                        print(event.data.delta, end="", flush=True)
                        await asyncio.sleep(0.01)
                print()
            except asyncio.CancelledError:
                break

# Main entry point
async def main():
    agent, server = await build_agent()
    try:
        await cli_interaction(agent)
    finally:
        await server.cleanup()
        print("Server disconnected. Goodbye!")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting.")