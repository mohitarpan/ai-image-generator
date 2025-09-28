# main.py
from crewai import Crew
from dotenv import load_dotenv
from src.workflows.image_workflow import ImageWorkflow
from src.utils.image_generator import ImageGenerator
import argparse

load_dotenv()

def generate_image(prompt, style="realistic"):
    # Initialize workflow
    workflow = ImageWorkflow()
    crew = workflow.create_crew()
    
    # Execute crew
    result = crew.kickoff(inputs={
        'user_prompt': prompt,
        'style': style
    })
    
    # Generate final image
    generator = ImageGenerator()
    image = generator.generate(result['final_prompt'])
    image.save(f"outputs/images/{result['filename']}")
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='AI Image Generation Crew')
    parser.add_argument('prompt', type=str, help='Description of the image to generate')
    parser.add_argument('--style', type=str, default='realistic', 
                      choices=['realistic', 'anime', 'cyberpunk', 'painting'],
                      help='Art style for the image')
    args = parser.parse_args()
    
    result = generate_image(args.prompt, args.style)
    print(f"Image generated: outputs/images/{result['filename']}")