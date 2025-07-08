import sys
import os
import json

# Fix to make test work with import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from nx_ai.openai_service.gpt_models import GPTGeneratedQuiz, FakeResponse


def test_gpt_generated_quiz():
    with open("mock/generated_quiz.json") as f:
        mock = json.load(f)
        gpt_generated_quiz = GPTGeneratedQuiz(FakeResponse(json.dumps(mock), use_tool=True))
        
        assert gpt_generated_quiz.data[0]["question"] == "Qu'est-ce qu'un registry Docker ?"
        assert gpt_generated_quiz.data[1]["answer"] == "Docker Hub"
