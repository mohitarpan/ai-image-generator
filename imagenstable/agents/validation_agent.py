from crewai import Agent
from tools.image_tools import ValidateImageTool

def create_validation_agent():
    validation_tool = ValidateImageTool()  # Create an instance of ValidateImageTool
    return Agent(
        role="Quality Validator",
        goal="Ensure generated images match the original prompt exactly",
        backstory=(
            "Detail-oriented quality assurance specialist with "
            "expertise in visual content validation."
        ),
        tools=[validation_tool],
        verbose=True,
        allow_delegation=False
    )