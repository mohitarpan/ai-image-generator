import os
import sys
from typing import Optional
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
from datetime import datetime

class ImageGenerator:
    def __init__(self):
        try:
            self.api = client.StabilityInference(
                key=os.getenv('STABILITY_API_KEY'),
                engine="stable-diffusion-xl-1024-v1-0",
                verbose=True
            )
        except Exception as e:
            print(f"Critical Error: {str(e)}")
            sys.exit(1)

    def generate_image(self, prompt: str, negative_prompt: str = "") -> Optional[str]:
        try:
            # Ensure outputs/images directory exists
            os.makedirs("outputs/images", exist_ok=True)
            
            # Configure generation parameters
            answers = self.api.generate(
                prompt=prompt,
                cfg_scale=8.0,
                height=720,
                width=720,
                samples=1,
                steps=30,
                seed=0,
                style_preset="photographic"
            )
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            img_path = f"outputs/images/image_{timestamp}.png"
            
            for resp in answers:
                for artifact in resp.artifacts:
                    if artifact.finish_reason == generation.FILTER:
                        print("\nWarning: Your image was filtered by safety systems")
                        return None
                    if artifact.type == generation.ARTIFACT_IMAGE:
                        with open(img_path, "wb") as f:
                            f.write(artifact.binary)
                        return img_path
            return None
            
        except Exception as e:
            print(f"Generation Error: {str(e)}")
            return None