from crewai import Task

class DesignTask:
    def create(self, agent, query):
        return Task(
            description=f"""Create a detailed image generation prompt for: {query}
            Include these elements:
            1. Main subject with detailed description
            2. Color palette and lighting
            3. Artistic style (e.g., photorealistic, watercolor)
            4. Composition guidelines
            5. Special effects if needed""",
            expected_output="A well-structured prompt in markdown format",
            agent=agent
        )