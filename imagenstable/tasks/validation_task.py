from crewai import Task

def create_validation_task():
    return Task(
        description=(
            "Validate generated image matches original prompt.\n"
            "If validation fails, provide specific reasons for mismatch."
        ),
        expected_output="Either 'VALIDATION_PASSED' or 'VALIDATION_FAILED' with issues list",
        context=[],
        output_file="validation_result.txt"
    )