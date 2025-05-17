# agent_hello.py

import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, OpenAIChatCompletionsModel

import asyncio

# Load API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Define the agent
async def my_first_agent():
    print("Initializing agent...")

    # Basic print for now (can be replaced with real agent logic later)
    print("🤖 Hello, world! This is your first OpenAI Agent.")

# To run the agent using uv script
def run_agent():
    asyncio.run(my_first_agent())
