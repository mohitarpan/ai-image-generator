import requests
import base64
from config import IMAGE_GENERATION_API_URL, API_KEY

class ImageGenerator:
    def run(self, prompt):
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Accept": "application/json",
        }

        # Use form-data for Stability AI
        payload = {
            "prompt": (None, prompt),
            "width": (None, "1024"),
            "height": (None, "1024")
        }

        response = requests.post(IMAGE_GENERATION_API_URL, headers=headers, files=payload)
        
        try:
            response_data = response.json()
        except requests.exceptions.JSONDecodeError:
            return f"Error: Response not in JSON format, Raw Response: {response.text}"

        print("Full API Response:", response_data)  # Debugging

        if "image" in response_data:
            # Decode Base64 Image Data
            image_data = base64.b64decode(response_data["image"])
            image_path = "generated_image.png"

            # Save Image Locally
            with open(image_path, "wb") as img_file:
                img_file.write(image_data)

            return f"Image saved locally: {image_path}"
        else:
            return f"Error: {response_data}"  # Return full error for debugging
