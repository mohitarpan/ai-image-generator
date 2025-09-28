import os
os.environ["CREWAI_TELEMETRY"] = "False" #Disable telemetry
from dotenv import load_dotenv
from crewai import Crew, Process
from langchain_community.llms import Ollama
from agents.query_understanding_agent import create_query_understanding_agent
from agents.prompt_engineering_agent import create_prompt_engineering_agent
from agents.image_generation_agent import create_image_generation_agent
from agents.validation_agent import create_validation_agent
from tasks.query_analysis_task import create_query_analysis_task
from tasks.prompt_creation_task import create_prompt_creation_task
from tasks.image_generation_task import create_image_generation_task
from tasks.validation_task import create_validation_task

ollama_llm = Ollama(model="openhermes")

class ImageGenerationCrew:
    def __init__(self):
        load_dotenv()
        # Test the connection to telemetry.crewai.com
        import requests
        try:
            response = requests.get('https://telemetry.crewai.com', verify=False)
            print(f"Connection successful: {response.status_code}")
        except Exception as e:
            print(f"Connection failed: {str(e)}")
        
        # Initialize agents
        self.query_agent = create_query_understanding_agent()
        self.prompt_agent = create_prompt_engineering_agent()
        self.image_agent = create_image_generation_agent()
        self.validation_agent = create_validation_agent()

        # Initialize tasks
        self.query_task = create_query_analysis_task()
        self.prompt_task = create_prompt_creation_task()
        self.image_task = create_image_generation_task()
        self.validation_task = create_validation_task()

        # Set up task relationships
        self.query_task.agent = self.query_agent
        self.prompt_task.agent = self.prompt_agent
        self.image_task.agent = self.image_agent
        self.validation_task.agent = self.validation_agent
        self.prompt_task.context = [self.query_task]
        self.image_task.context = [self.prompt_task]
        self.validation_task.context = [self.image_task, self.prompt_task]

    def assemble_crew(self):
        return Crew(
            agents=[
                self.query_agent,
                self.prompt_agent,
                self.image_agent,
                self.validation_agent
            ],
            tasks=[
                self.query_task,
                self.prompt_task,
                self.image_task,
                self.validation_task
            ],
            process=Process.sequential,
            verbose=True
        )

    def generate(self, query: str, max_retries: int = 3):
        current_query = query
        for attempt in range(max_retries):
            crew = self.assemble_crew()
            result = crew.kickoff(inputs={'query': current_query})
            
            if "VALIDATION_PASSED" in self.validation_task.output.result:
                return result
            
            # Handle failed validation
            print(f"Validation failed (attempt {attempt+1}/{max_retries})")
            current_query = f"Original query: {query}\nValidation feedback: {self.validation_task.output.result}"
        
        raise RuntimeError("Failed to generate satisfactory image after maximum retries")

if __name__ == "__main__":
    crew = ImageGenerationCrew()
    query = "A cyberpunk style marketplace on Mars with alien vendors and neon signs"
    try:
        result = crew.generate(query)
        print(f"\n✅ Generation successful!\nImage saved at: {result}")
    except Exception as e:
        print(f"\n Generation failed: {str(e)}")