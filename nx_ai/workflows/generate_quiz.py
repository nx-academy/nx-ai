import os
import json

from nx_ai.openai_service.openai_api import generate_quiz_with_gpt


def create_quiz_folder():
    if not os.path.exists("nx_ai/quizzes_data"):
        os.makedirs("nx_ai/quizzes_data")


def generate_quiz_beta(url: str, filename: str):
    generated_quiz = generate_quiz_with_gpt(url, True)
    
    create_quiz_folder()
    with open(f"nx_ai/quizzes_data/{filename}.json", "w", encoding="utf-8") as file:
        json.dump({"data": generated_quiz.data}, file, indent=4, ensure_ascii=False)
        
        
    
