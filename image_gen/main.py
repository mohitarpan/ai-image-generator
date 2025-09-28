from crewai import Crew, Task
from agents import ImageAgents
from dotenv import load_dotenv

load_dotenv()

def generate_image(query):
    agents = ImageAgents()
    
    prompt_expert = agents.prompt_engineer()
    image_generator = agents.image_agent()

    prompt_task = Task(
        description=f"Create an enhanced prompt for: {query}",
        agent=prompt_expert,
        expected_output="A detailed image description paragraph"
    )

    image_task = Task(
        description="Generate the actual image",
        agent=image_generator,
        expected_output="generated_image.jpg file path"
    )

    crew = Crew(
        agents=[prompt_expert, image_generator],
        tasks=[prompt_task, image_task],
        verbose=2
    )

    return crew.kickoff()

if __name__ == "__main__":
    user_input = input("Enter image description: ")
    result = generate_image(user_input)
    print(f"\nGenerated image saved at: {result}")