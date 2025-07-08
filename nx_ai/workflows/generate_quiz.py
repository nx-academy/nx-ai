from nx_ai.openai_service.openai_api import generate_quiz_with_gpt


def generate_quiz_beta(url: str):
    generated_quiz = generate_quiz_with_gpt(url, True)
    
    print("====")
    print(generated_quiz.data)
    print("====")
