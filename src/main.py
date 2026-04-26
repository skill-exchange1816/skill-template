def example_skill(input_data: dict) -> dict:
    """
    An example AI skill that simply returns the input with a success flag.
    """
    return {
        "status": "success",
        "echo": input_data,
        "message": "Hello from the AI Skill Template!"
    }
