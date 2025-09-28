# src/tasks/image_tasks.py
from crewai import Task

class ImageTasks:
    def refine_prompt(self, agent, context):
        return Task(
            description=f"""Refine the user prompt: {context['user_prompt']}
            - Identify key elements
            - Clarify ambiguous terms
            - Add specific details""",
            agent=agent,
            expected_output="A structured JSON object with:\n- 'core_concept'\n- 'key_elements'\n- 'style_suggestions'",
            context=context,
            output_json=True
        )

    def add_artistic_direction(self, agent, context):
        return Task(
            description=f"""Enhance the refined prompt with {context['style']} style elements:
            - Color palette
            - Composition
            - Artistic techniques""",
            agent=agent,
            expected_output="A complete prompt with artistic direction in markdown format",
            context=context
        )

    def validate_prompt(self, agent, context):
        return Task(
            description="Validate the final prompt for technical feasibility and content safety",
            agent=agent,
            expected_output="Validation report with either 'Approved' or 'Revisions needed'",
            context=context,
            output_file="validation_report.txt"
        )