from crewai import Task

class InputTasks:
    @staticmethod
    def collect_requirements(agent):
        return Task(
            description="Collect detailed image specifications from user",
            agent=agent,
            expected_output="Structured JSON with requirements and exclusions",
            output_file="outputs/reports/requirements.json"
        )
    
    @staticmethod
    def generate_image(agent):
        return Task(
            description="Generate image using Stability AI",
            agent=agent,
            expected_output="High-resolution PNG image file path",
            context=[]
        )