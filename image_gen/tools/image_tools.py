import requests
import os
from PIL import Image
import io

def generate_image(prompt: str) -> str:
    """Generate an image using Stable Diffusion API."""
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    headers = {"Authorization": f"Bearer {os.getenv('HF_API_KEY')}"}

    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    response.raise_for_status()

    # Save the generated image
    image = Image.open(io.BytesIO(response.content))
    image_path = "generated_image.jpg"
    image.save(image_path)

    return image_path

image_tool = {
    "name": "Image Generator",
    "func": generate_image,
    "description": "Generates images from text prompts using Stable Diffusion."
}
