from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from tools.image_tools import image_tool
import os

class ImageAgents:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            temperature=0.7,
            google_api_key=os.getenv("GEMINI_API_KEY")
        )

    def prompt_engineer(self):
        return Agent(
            role="Prompt Expert",
            goal="Create perfect image generation prompts",
            backstory="Expert in crafting detailed prompts for AI image generation",
            llm=self.llm,
            verbose=True
        )

    def image_agent(self):
        return Agent(
            role="Image Generator",
            goal="Generate high quality images",
            backstory="Specialist in AI image generation",
            tools=[image_tool],
            llm=self.llm,
            verbose=True
        )