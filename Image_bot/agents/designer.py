from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
import os

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

class ImageDesigner:
    def create(self):
        return Agent(
            role="Visual Concept Designer",
            goal="Create detailed image generation prompts",
            backstory="Expert in visual storytelling and prompt engineering",
            tools=[],  # From web_tools.py
            verbose=True,
            llm=llm,
            memory=True
        )