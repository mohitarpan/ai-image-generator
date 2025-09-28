# src/agents/technical_validator.py
from crewai import Agent
from crewai_tools import tool
from src.utils.config_loader import load_agent_config

class TechnicalValidator:
    def __init__(self):
        self.config = load_agent_config('technical_validator')

    @tool(name="Prompt Safety Validator")
    def validate_prompt(self, prompt: str) -> str:
        """Validates prompts for content safety and technical constraints."""
        BLACKLIST = ["nudity", "violence", "hate speech", "illegal activities"]
        if any(word in prompt.lower() for word in BLACKLIST):
            return "REJECTED: Contains restricted content"
        if len(prompt) > 500:
            return "REJECTED: Prompt exceeds 500 characters"
        return "APPROVED"

    def create(self):
        return Agent(
            role=self.config['role'],
            goal=self.config['goal'],
            backstory=self.config['backstory'],
            verbose=self.config['verbose'],
            memory=self.config['memory'],
            tools=[self.validate_prompt]
        )

    def validate_prompt(self, prompt):
        BLACKLIST = ["nudity", "violence", "hate speech"]
        if any(word in prompt.lower() for word in BLACKLIST):
            return "Error: Prompt contains restricted content"
        if len(prompt) > 500:
            return "Error: Prompt too long (max 500 characters)"
        return "Prompt validated successfully"