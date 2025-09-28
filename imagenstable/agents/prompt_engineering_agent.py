from crewai import Agent


def create_prompt_engineering_agent():
    return Agent(
        role="Prompt Engineer",
        goal="Create detailed, unambiguous text-to-image prompts",
        backstory=(
            "Expert in translating abstract concepts into structured prompts. "
            "Skilled in including style, composition, and detail specifications."
        ),
        tools=[],
        verbose=True,
        allow_delegation=False
    )