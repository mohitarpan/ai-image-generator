from flask import Flask, request, jsonify
from agents.idea_generator import IdeaGenerator
from agents.prompt_enhancer import PromptEnhancer
from agents.image_generator import ImageGenerator
from agents.user_interaction import UserInteraction

app = Flask(__name__)

# Initialize agents
idea_generator = IdeaGenerator()
prompt_enhancer = PromptEnhancer()
image_generator = ImageGenerator()
user_interaction = UserInteraction()

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.json  # Accept JSON request
        user_input = data.get("query")

        if not user_input:
            return jsonify({"error": "Missing 'query' in request"}), 400

        # Step-by-step processing
        prompt = idea_generator.run(user_input)
        enhanced_prompt = prompt_enhancer.run(prompt)
        image_url = image_generator.run(enhanced_prompt)
        response = user_interaction.run(image_url)

        return jsonify({"response": response, "image_url": image_url})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
