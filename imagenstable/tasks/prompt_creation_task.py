from crewai import Task

def create_prompt_creation_task():
    return Task(
        description="Create optimized image generation prompt based on analyzed requirements",
        expected_output=(
            "Precisely structured text prompt including:\n"
            "- Subject description\n- Style specifications\n"
            "- Color scheme\n- Composition details\n- Special effects"
        ),
        context=[],
        output_file="generation_prompt.txt"
    )