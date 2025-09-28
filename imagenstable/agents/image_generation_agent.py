from crewai import Agent
from tools.image_tools import GenerateImageTool


def create_image_generation_agent():
    image_tool = GenerateImageTool()
    return Agent(
        role="Image Generator",
        goal="Generate high-quality images from text prompts",
        backstory=(
            "Specializes in using multiple AI models for image generation. "
            "Expert in optimizing model parameters for best results."
        ),
        tools=[image_tool],
        verbose=True,
        allow_delegation=False
    )