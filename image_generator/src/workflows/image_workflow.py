# src/workflows/image_workflow.py
from crewai import Crew
from src.agents.prompt_engineer import PromptEngineer
from src.agents.creative_director import CreativeDirector
from src.agents.technical_validator import TechnicalValidator
from src.tasks.image_tasks import ImageTasks

class ImageWorkflow:
    def create_crew(self):
        # Initialize agents
        pe = PromptEngineer().create()
        cd = CreativeDirector().create()
        tv = TechnicalValidator().create()

        # Create tasks
        tasks = ImageTasks()
        task_list = [
            tasks.refine_prompt(pe, {}),
            tasks.add_artistic_direction(cd, {}),
            tasks.validate_prompt(tv, {})
        ]

        return Crew(
            agents=[pe, cd, tv],
            tasks=task_list,
            verbose=2,
            memory=True,
            process="sequential",
            full_output=True
        )