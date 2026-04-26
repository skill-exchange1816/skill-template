from src.main import example_skill

def test_example_skill():
    input_data = {"test": "data"}
    result = example_skill(input_data)
    assert result["status"] == "success"
    assert result["echo"] == input_data
