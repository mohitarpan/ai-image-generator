from crewai import Agent
from langchain_community.llms import Ollama

def create_query_understanding_agent():
    return Agent(
        role="Query Interpreter",
        goal="Accurately understand and clarify user's image generation request",
        backstory=(
            "Specializes in natural language processing and intent recognition. "
            "Expert in identifying ambiguous requirements and clarifying user needs."
        ),
        llm=Ollama(model="openhermes"),
        verbose=True,
        allow_delegation=False

    )