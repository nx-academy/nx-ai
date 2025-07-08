import sys
import os
import json

# Fix to make test work with import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from nx_ai.openai_service.gpt_models import GPTGeneratedQuiz, FakeResponse


def test_gpt_generated_quiz():
    print("====")
    print("====")
    print("====")
    
    assert True == True
