from main import image_crew

def test_image_generation():
    test_cases = [
        "A cyberpunk laptop floating in space with neon lights",
        "A peaceful forest with glowing mushrooms at twilight",
        "A steampunk airship flying over a medieval city"
    ]
    
    for idx, query in enumerate(test_cases):
        print(f"\nTesting case {idx+1}: {query}")
        result = image_crew(query)
        print(f"Result: {result}")

if __name__ == "__main__":
    test_image_generation()