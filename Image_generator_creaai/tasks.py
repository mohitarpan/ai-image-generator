from crewai import Task

class ImageTasks:
    def enhance_prompt_task(self, agent, query):
        return Task(
            description=f"Enhance the user query: '{query}'",
            agent=agent,
            expected_output="A detailed paragraph describing visual elements, style, and composition.",
            output_file="enhanced_prompt.txt"
        )

    def generate_image_task(self, agent):
        return Task(
            description="Generate image based on enhanced description",
            agent=agent,
            expected_output="High-quality generated image saved as generated_image.jpg",
            output_file="generated_image.jpg"
        )