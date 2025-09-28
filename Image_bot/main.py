from crew import ImageCrew
import datetime

def generate_image(query):
    crew = ImageCrew()
    result = crew.run(query)
    
    # Save image
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"output_{timestamp}.webp"
    result['image'].save(filename)
    
    print(f"Image saved as {filename}")
    print("Analysis Report:", result['analysis'])

if __name__ == "__main__":
    query = input("Enter your image concept: ")
    generate_image(query)