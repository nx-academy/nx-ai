import sys
import os

# Fix to make test work with import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from nx_ai.openai_service.gpt_models import GPTResponse, FakeResponse


def test_gpt_response():
    mock_text = "Hello, simulated World"
    mock_response = GPTResponse(FakeResponse(mock_text))

    assert mock_response.text == "Hello, simulated World"
