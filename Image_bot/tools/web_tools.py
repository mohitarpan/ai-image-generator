from crewai_tools import BaseTool
import requests
import os

class WebSearchTool(BaseTool):
    name = "Web Search"
    description = "Searches the web for reference images and information"

    def _run(self, query: str):
        url = "https://google.serper.dev/search"
        payload = {"q": query, "gl": "us"}
        headers = {
            "X-API-KEY": os.getenv("SERPER_API_KEY"),
            "Content-Type": "application/json"
        }
        response = requests.post(url, json=payload, headers=headers)
        return response.json().get("organic", [])[:3]  # Return top 3 results