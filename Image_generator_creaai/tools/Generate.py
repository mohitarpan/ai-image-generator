import requests
import io
import os
from PIL import Image
from crewai import tool

@tool("image_generator")
def generate_image(prompt: str, output_path: str = "generated_image.jpg") -> str:
    """Generates image using Stable Diffusion model through Hugging Face API."""
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    headers = {"Authorization": f"Bearer {os.environ['HF_API_KEY']}"}
    
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    response.raise_for_status()
    
    image = Image.open(io.BytesIO(response.content))
    image.save(output_path)
    return f"Image generated and saved as {output_path}"