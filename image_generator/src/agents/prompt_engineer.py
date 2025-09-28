# src/agents/prompt_engineer.py
from crewai import Agent
from src.utils.config_loader import load_agent_config

class PromptEngineer:
    def __init__(self):
        self.config = load_agent_config('prompt_engineer')
        self.llm = genai.GenerativeModel(self.config['llm'])

    def create(self):
        return Agent(
            role=self.config['role'],
            goal=self.config['goal'],
            backstory=self.config['backstory'],
            verbose=self.config['verbose'],
            memory=self.config['memory'],
            tools=[]
        )