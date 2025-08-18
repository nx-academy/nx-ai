import os

from nx_ai.openai_service.openai_api import summarize_article_with_gpt

def create_recap_folder():
    if not os.path.exists("nx_ai/recap_data"):
        os.makedirs("nx_ai/recap_data")


def generate_recap_beta(urls: list[str], simulate: bool):
    articles = []
    
    for url in urls:
        article = summarize_article_with_gpt(url=url, simulate=simulate)
        articles.append(article)
        
        
    print("====")
    print(articles)
    print("====")
    
    create_recap_folder()
    
    
