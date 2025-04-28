## Import libraries & methods

import os
from dotenv import load_dotenv
import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_core import CancellationToken
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.ui import Console


## Setup an API connection
load_dotenv(override=True)
github_token = os.getenv('GITHUB_TOKEN')
model = os.getenv("GITHUB_MODEL", "gpt-4o") 

client = OpenAIChatCompletionClient(
    model=model,
    api_key=github_token,
    base_url="https://models.inference.ai.azure.com",
    temperature=0.2,
    presence_penalty=0.5
)


## Language tutor 
agent = AssistantAgent(
    name="thai_tutor",
    model_client=client,
    system_message="You are a Thai tutor. Help the user learn Thai." \
    "If the user uses a language other than Thai or English, respond with 'Apologies, I only understand English or Thai.'" \
    "Before giving a response to the user, you must first assess whether the user's query is allowed or not."\
    "The allowed topics are learning or understanding Thai." \
    "If the topic is allowed, reply with an answer as normal, otherwise, say 'Apologies, but this topic is not allowed.'"\
    "For example, if the user asks 'Can you help me with booking a flight to Bangkok?', respond with 'Apologies, but this topic is not allowed.'"\
    "If you're not sure about the correct answer to the user's query, reply with 'Apologies, I do not know.'",
    model_client_stream=True 
)


## Running tasks (user inputs)
async def main() -> None:
    await Console(agent.run_stream(task="Can you focus on pronounciation?",cancellation_token=CancellationToken()))
    await client.close() 


if __name__ == "__main__":
    asyncio.run(main())










