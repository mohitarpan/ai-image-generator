import os
from dotenv import load_dotenv
from agents.input_collector import InputCollector
from agents.image_generator import ImageGenerator
import warnings

load_dotenv()

# Ensure output directories exist
os.makedirs("outputs/images", exist_ok=True)

# Disable all warnings
warnings.filterwarnings('ignore')

class ImageGenerationCrew:
    def __init__(self):
        self.max_iterations = int(os.getenv("MAX_ITERATIONS", 3))
        
    def setup_crew(self):
        # Initialize agents
        input_agent = InputCollector()
        generator_agent = ImageGenerator()
        
        return generator_agent, input_agent

    def run(self):
        try:
            generator, collector = self.setup_crew()
            
            # Get image requirements
            requirements = collector.collect_inputs()
            
            # Generate initial image
            prompt = self._build_prompt(requirements)
            image_path = generator.generate_image(prompt)
            
            if not image_path:
                print("\nError: Failed to generate image. Please check your Stability API key.")
                return
                
            print(f"\nImage generated: {image_path}")
            
            iteration = 0
            while iteration < self.max_iterations:
                user_input = input("\nAccept image? (Y/N): ").upper()
                
                if user_input == 'Y':
                    print("\nFinal image approved!")
                    break
                elif user_input == 'N':
                    feedback = input("Enter improvement requirements: ")
                    requirements['description'] += f". {feedback}"
                    prompt = self._build_prompt(requirements)
                    image_path = generator.generate_image(prompt)
                    if image_path:
                        print(f"\nNew image generated: {image_path}")
                    iteration += 1
                else:
                    print("Invalid input. Please enter Y/N")
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("\nPlease check your API key and try again.")
    
    def _build_prompt(self, requirements):
        # Build the main prompt
        prompt = f"{requirements['description']}, {requirements['style']}"
        
        # Add color preferences if specified
        if requirements['color_palette']:
            prompt += f", {requirements['color_palette']} colors"
        
        # Add required elements
        if requirements['required']:
            prompt += ", " + ", ".join(requirements['required'])
            
        # Add exclusions in a way that works with Stability AI
        if requirements['excluded']:
            prompt += ", without " + " or ".join(requirements['excluded'])
        
        return prompt

if __name__ == "__main__":
    ImageGenerationCrew().run()