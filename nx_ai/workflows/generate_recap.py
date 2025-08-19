import os


from nx_ai.openai_service.openai_api import summarize_article_with_gpt
from nx_ai.github_service.github_api import create_pull_request_on_github


def create_recap_folder():
    if not os.path.exists("nx_ai/recap_data"):
        os.makedirs("nx_ai/recap_data")


def generate_recap_beta(urls: list[str], filename: str, simulate: bool):
    articles = []
    
    for url in urls:
        article = summarize_article_with_gpt(url=url, simulate=simulate)
        articles.append(article)
        
    recap_text = """---
layout: ../../layouts/BlogPostLayout.astro

title: "METTRE A JOUR | Le récap #3 - Juin 2025"
description: METTRE A JOUR

imgAlt: Un vendeur de journaux dans un kiosque parisien, pixel art
imgSrc: /images/articles/kiosque-journaux.webp

kind: Articles
author: Thomas
draft: false
publishedDate: METTRE A JOUR | 06/27/2025
---
    
# METTRE A JOUR | Le récap #3 - Juin 2025

<img src="/images/articles/kiosque-journaux.webp" alt="Un vendeur de journaux dans un kiosque parisien, pixel art" style="aspect-ratio: 1792 / 1024; object-fit: cover; width: 100%; display: block; object-position: top" />

<br>
"""
      
    for article in articles:
        recap_text += f"""## {article.data["title_fr"]}
<small>{article.data["author"]}</small>

{article.data["article_summary"]}

[Lire l'article](#)

<br>
        
---
"""

    create_recap_folder()
    with open(f"nx_ai/recap_data/{filename}.md", "w", encoding="utf-8") as file:
        file.write(recap_text)
        
    create_pull_request_on_github(filename=filename, type="recap")
