import asyncio
import uuid
from agents import Agent, Runner, SQLiteSession
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

    return agent

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
        if len(query.strip()) > 0:
            result = await Runner.run(agent, query,session=session)
            print(result.final_output)


# Main entry point
async def main():
    agent = await build_agent()
    await cli_interaction(agent)

if __name__ == "__main__":
    asyncio.run(main())