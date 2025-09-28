from crewai import Task

class EvaluationTasks:
    @staticmethod
    def quality_check(agent):
        return Task(
            description="""Analyze generated image for:
            1. Missing required elements
            2. Presence of excluded items
            3. Style compliance
            4. Color scheme accuracy""",
            agent=agent,
            expected_output="Detailed evaluation report with improvement points",
            output_file="outputs/reports/evaluation_report.json"
        )