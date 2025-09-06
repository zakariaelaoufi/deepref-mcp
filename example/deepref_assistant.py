import asyncio
import uuid
from agents import Agent, Runner, SQLiteSession
from agents.mcp import MCPServerStdio


async def build_agent() -> Agent:
    """Initialize and return a configured agent."""
    server = MCPServerStdio(
        params={
            "command": "uv",
            "args": ["run", "--with", "mcp", "mcp", "run", "src/server.py"],
        }
    )
    await server.connect()

    return Agent(
        name="DeepRef Copilot Assistant",
        instructions=(
            "You are a helpful assistant capable of reading from a variety of "
            "research paper databases (e.g., arXiv, PubMed, Semantic Scholar). "
            "Answer each question precisely."
        ),
        # model=,
        mcp_servers=[server],
    )


async def cli_interaction(agent: Agent) -> None:
    """Interactive CLI for querying the agent."""
    print("🔧 DeepRef Copilot Assistant — Ask me something (type 'exit' to quit):\n")

    session = SQLiteSession(
        f"conversation_{uuid.uuid4()}",
        "conversations.db"
    )

    loop = asyncio.get_event_loop()

    while True:
        try:
            query = await loop.run_in_executor(None, input, "> ")
        except (EOFError, KeyboardInterrupt):
            print("\n👋 Exiting gracefully...")
            break

        query = query.strip()
        if not query:
            continue
        if query.lower() in {"exit", "quit"}:
            break

        result = Runner.run(agent, query, session=session)
        print(result.final_output)


async def main() -> None:
    agent = await build_agent()
    await cli_interaction(agent)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n⚡ Program interrupted by user.")