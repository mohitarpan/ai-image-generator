from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from tools.prompt import enhance_prompt
import os


class ImageAgents:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            temperature=0.7,
            GEMINI_API_KEY=os.getenv("GOOGLE_API_KEY")

        )

    def prompt_engineer(self):
        return Agent(
            role="Prompt Engineering Expert",
            goal="Transform user queries into detailed, descriptive prompts",
            backstory=(
                "Expert in converting simple inputs into rich, descriptive prompts "
                "for image generation models. Specializes in adding relevant details "
                "and artistic elements."
            ),
            tools=[enhance_prompt],
            llm=self.llm,
            verbose=True
        )

    def image_generator(self):
        return Agent(
            role="Image Generation Specialist",
            goal="Generate high-quality images from text prompts",
            backstory=(
                "Skilled in AI image generation with expertise in visual composition "
                "and technical implementation of diffusion models."
            ),
            tools=[generate_image],
            llm=self.llm,
            verbose=True
        )