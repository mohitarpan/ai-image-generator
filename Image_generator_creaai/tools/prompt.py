from crewai_tools.core.tool import tool

import google.generativeai as genai
import os

@tool("prompt_enhancer")
def enhance_prompt(query: str) -> str:
    """Enhance user's image description using Gemini Pro."""
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')
    
    response = model.generate_content(f"""
    Enhance this image description for better AI generation: "{query}"
    Return only the enhanced prompt, no additional text.
    """)
    
    return response.text