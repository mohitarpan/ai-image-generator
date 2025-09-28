from crewai import Tool
from PIL import Image
import io
import requests
import os

class ImageGeneratorTool(Tool):
    name: str = "Image Generator"
    description: str = "Generates images using Stability AI's API"

    def _run(self, prompt: str) -> Image.Image:
        response = requests.post(
            "https://api.stability.ai/v2beta/stable-image/generate/core",
            headers={
                "Authorization": f"Bearer {os.getenv('STABILITY_KEY')}",
                "Accept": "image/*"
            },
            files={"none": ''},
            data={
                "prompt": prompt,
                "output_format": "webp",
                "model": "core",
                "aspect_ratio": "1:1"
            }
        )
        
        if response.status_code == 200:
            return Image.open(io.BytesIO(response.content))
        raise Exception(f"Image generation failed: {response.text}")

class ImageAnalysisTool(Tool):
    name: str = "Image Analyzer"
    description: str = "Analyzes generated images for quality and relevance"

    def _run(self, image: Image.Image):
        analysis = {
            "resolution": image.size,
            "mode": image.mode,
            "histogram": image.histogram(),
            "format": image.format
        }
        return analysis