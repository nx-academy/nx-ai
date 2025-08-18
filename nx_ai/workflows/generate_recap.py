import os

from nx_ai.openai_service.openai_api import summarize_article_with_gpt

def create_recap_folder():
    if not os.path.exists("nx_ai/recap_data"):
        os.makedirs("nx_ai/recap_data")


def generate_recap_beta(url: str, simulate: bool):
    article = summarize_article_with_gpt(url=url, simulate=simulate)
    
    print("====")
    print(article)
    print("====")
