import os
from crewai import Crew
from agents import ImageAgents
from tasks import ImageTasks
from dotenv import load_dotenv

load_dotenv()

def image_crew(query):
    # Initialize components
    agents = ImageAgents()
    tasks = ImageTasks()

    # Create agents
    prompt_engineer = agents.prompt_engineer()
    image_generator = agents.image_generator()

    # Create tasks
    enhance_task = tasks.enhance_prompt_task(prompt_engineer, query)
    generate_task = tasks.generate_image_task(image_generator)

    # Assemble crew
    crew = Crew(
        agents=[prompt_engineer, image_generator],
        tasks=[enhance_task, generate_task],
        verbose=2
    )

    # Execute workflow
    result = crew.kickoff()
    return result

if __name__ == "__main__":
    user_query = input("Enter your image description: ")
    result = image_crew(user_query)
    print("\n\nGeneration Result:", result)