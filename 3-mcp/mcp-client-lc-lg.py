# Create server parameters for stdio connection
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
from dotenv import load_dotenv
import os
# For running asyncio
load_dotenv()
# model for agent
model = ChatOpenAI(model="gpt-4o")

# server parameters
server_params = {
    "count-r": {
        "transport": "sse",
        "url": "http://localhost:8000/sse"
    },
    "server-file-system": {
        "transport": "sse",
        "url": "http://localhost:8004/sse"
    },
    "task-manager": {
        "transport": "sse",
        "url": "http://localhost:8005/sse"
    }
}

# print(server_params)


async def main(query: str):
    client = MultiServerMCPClient(server_params)
    tools = await client.get_tools()
    agent = create_react_agent(model, tools)
    response = await agent.ainvoke({"messages": query})

    return response

query = """
    how many r characters found in the word 'characteristic' and write the output to 'count-r-output.txt' in the server file system,
    and create a new task 'Count R Characters' with the detail counting total number of r characters?
"""

if __name__ == "__main__":
    response = asyncio.run(main(query))
    print('------------')
    print(response)
