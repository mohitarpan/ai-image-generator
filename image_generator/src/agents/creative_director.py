# src/agents/creative_director.py
from crewai import Agent
from crewai_tools import tool
from src.utils.config_loader import load_agent_config

class CreativeDirector:
    def __init__(self):
        self.config = load_agent_config('creative_director')

    @tool(name="Style Enhancer")
    def enhance_style(self, prompt: str, style: str) -> str:
        """Adds specific style elements to the prompt."""
        styles = {
            "realistic": "sharp focus, realistic textures, natural lighting",
            "photographic": "35mm lens, f/8 aperture, cinematic lighting",
            "artistic": "brush strokes, impressionist style, textured canvas"
        }
        return f"{prompt} ({styles.get(style, '')})"

    def create(self):
        return Agent(
            role=self.config['role'],
            goal=self.config['goal'],
            backstory=self.config['backstory'],
            verbose=self.config['verbose'],
            memory=self.config['memory'],
            tools=[self.enhance_style]
        )