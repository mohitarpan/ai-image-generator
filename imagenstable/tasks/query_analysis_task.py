from crewai import Task

def create_query_analysis_task():
    return Task(
        description="Analyze and clarify the user's request: '{query}'",
        expected_output=(
            "Detailed JSON structure containing:\n"
            "- Main subject\n- Style requirements\n- Color palette\n"
            "- Composition details\n- Any specific elements to include/exclude"
        ),
        output_file="query_analysis.json"
    )