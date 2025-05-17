from agents import Agent, Runner,AsyncOpenAI,set_default_openai_client,set_tracing_disabled,OpenAIChatCompletionsModel
from dotenv import load_dotenv
import os

load_dotenv()

gemeini_api_key=os.getenv("gemeini_api_key")

external_client = AsyncOpenAI(
    api_key = gemeini_api_key,
    base_url ="https://generativelanguage.googleapis.com/v1beta/openai/"
)
set_default_openai_client(external_client)
set_tracing_disabled(True)
model=OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

def main():
    agent= Agent(name="MoodMate", instructions="""
    You are MoodMate, a friendly and emotionally intelligent assistant.
    Your job is to help users reflect on their emotions and offer general tips for self-care.
    Be supportive, non-judgmental, and never offer medical advice.
    Use soft, comforting language and speak like a calm friend or life coach.
    Always end your response with a gentle question to encourage continued reflection.
    """,model=model)
    result=Runner.run_sync(
        agent,"I've been feeling anxious and low energy lately.",)
    
    print(result.final_output)
