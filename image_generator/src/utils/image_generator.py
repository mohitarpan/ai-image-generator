# src/utils/image_generator.py
from diffusers import StableDiffusionPipeline
import torch
import hashlib
import datetime

class ImageGenerator:
    def __init__(self):
        self.model_name = "stabilityai/stable-diffusion-2-1"
        self.pipe = StableDiffusionPipeline.from_pretrained(
            self.model_name,
            torch_dtype=torch.float16
        ).to("cuda" if torch.cuda.is_available() else "cpu")

    def generate(self, prompt):
        result = self.pipe(
            prompt,
            num_inference_steps=50,
            guidance_scale=7.5
        )
        return result.images[0]

    def generate_filename(self, prompt):
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        hash_str = hashlib.md5(prompt.encode()).hexdigest()[:6]
        return f"image_{timestamp}_{hash_str}.png"