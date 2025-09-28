from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import json
import re

def _parse_response(self, text):
    try:
        # Extract JSON from the response text
        json_match = re.search(r'\{.*\}', text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        else:
            raise ValueError("No JSON found in response")
            
    except Exception as e:
        print(f"Error parsing response: {str(e)}")
        return {
            'missing': [],
            'unwanted': [],
            'style_score': 0.0,
            'suggestions': ['Analysis failed']
        }

class ImageEvaluator(Agent):
    def __init__(self):
        llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
        
        super().__init__(
            role='Quality Assurance Analyst',
            goal='Ensure generated images match requirements',
            backstory="""Expert in visual analysis using AI models, skilled in 
            identifying discrepancies between requirements and generated content""",
            verbose=True,
            llm=llm
        )

    def evaluate_image(self, prompt, requirements):
        analysis = self.llm.invoke(
    f"""Analyze this image generation prompt against requirements:
    
    PROMPT: {prompt}
    REQUIREMENTS: {json.dumps(requirements, indent=2)}
    
    Return JSON format analysis with these EXACT keys:
    - "missing": list of missing required elements
    - "unwanted": list of present excluded elements
    - "style_score": 0-1 score for style match
    - "suggestions": list of improvement suggestions
    
    FORMAT EXAMPLE:
    ```json
    {{
        "missing": ["element1"],
        "unwanted": ["element2"],
        "style_score": 0.85,
        "suggestions": ["Suggestion 1", "Suggestion 2"]
    }}
    ```"""
)
        
        return self._parse_response(analysis.content)

    def _parse_response(self, text):
        # Add actual JSON parsing logic here
        return {
            'missing': ['mountain'],
            'unwanted': ['car'],
            'style_score': 0.85,
            'suggestions': ['Increase contrast', 'Add more details']
        }