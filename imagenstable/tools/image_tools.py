# image_tools.py
import os
import io
from typing import Type
from dotenv import load_dotenv
from PIL import Image
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

# Load environment variables
load_dotenv()

# Configure Stability AI
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

stability_api = client.StabilityInference(
    key=os.getenv("STABILITY_API_KEY"),
    verbose=True,
    engine="stable-diffusion-xl-1024-v1-0"
)

# Configure Google Gemini
from google.generativeai import configure, GenerativeModel
configure(api_key=os.getenv("GOOGLE_API_KEY"))
gemini_model = GenerativeModel('gemini-1.5-flash')

# Tool Schemas
class GenerateImageInput(BaseModel):
    """Input schema for image generation."""
    prompt: str = Field(..., description="Text prompt for image generation.")
    filename: str = Field(default="output.png", description="Output filename.")

class ValidateImageInput(BaseModel):
    """Input schema for image validation."""
    image_path: str = Field(..., description="Path to the image file.")
    original_prompt: str = Field(..., description="Original text prompt used for generation.")

# Tools Implementation
class GenerateImageTool(BaseTool):
    name: str = "Generate Image Tool"
    description: str = "Generates images using Stable Diffusion"
    args_schema: Type[BaseModel] = GenerateImageInput

    def _run(self, prompt: str, filename: str = "output.png") -> str:
        """Generate image using Stability AI API."""
        try:
            answers = stability_api.generate(
                prompt=prompt,
                steps=30,
                cfg_scale=8.0,
                width=1024,
                height=1024,
                samples=1,
                sampler=generation.SAMPLER_K_DPMPP_2M
            )
            
            for resp in answers:
                for artifact in resp.artifacts:
                    if artifact.finish_reason == generation.FILTER:
                        return "Error: Content violation detected"
                    if artifact.type == generation.ARTIFACT_IMAGE:
                        img = Image.open(io.BytesIO(artifact.binary))
                        img.save(filename)
                        return filename
            
            return "Error: No image generated"
        except Exception as e:
            return f"Generation Error: {str(e)}"

class ValidateImageTool(BaseTool):
    name: str = "Validate Image Tool"
    description: str = "Validates image matches prompt using Gemini AI"
    args_schema: Type[BaseModel] = ValidateImageInput

    def _run(self, image_path: str, original_prompt: str) -> str:
        """Validate image using Gemini Flash 1.5."""
        try:
            with open(image_path, "rb") as img_file:
                img_data = img_file.read()
            
            response = gemini_model.generate_content(
                [
                    f"STRICT VALIDATION: Does this image perfectly match the prompt? Respond only with 'YES' or 'NO'.\nPROMPT: {original_prompt}",
                    {"mime_type": "image/png", "data": img_data}
                ]
            )
            return response.text.strip().upper()
        except Exception as e:
            return f"Validation Error: {str(e)}"