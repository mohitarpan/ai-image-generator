from crewai import Task

def create_image_generation_task():
    return Task(
        description="Generate image using the provided prompt",
        expected_output="High-quality generated image file path",
        context=[],
        output_file="generated_image.txt"
    )