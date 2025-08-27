import os
import json
from pathlib import Path

from openai import OpenAI

from nx_ai.openai_service.gpt_models import (
    FakeResponse,
    GPTCleanedArticle,
    GPTFetchedNews,
    GPTGeneratedQuiz,
    GPTResponse,
    GPTSummarizedArticle
)


client = OpenAI()

VECTOR_STORE_ID = os.environ.get("VECTOR_STORE_ID")


def say_hello_to_gpt(simulate):
    if simulate:
        mock_text = "Hello, simulated World"
        mock_response = GPTResponse(FakeResponse(mock_text))
        
        return mock_response
    
    response = client.responses.create(
        model="gpt-4o-mini",
        input="Hello, World!"
    )
    gpt_response = GPTResponse(response)
    
    return gpt_response


def clean_article_with_gpt(url, simulate):
    if simulate:
        with open("mock/cleaned_article.txt", "r") as f:
            mock = f.read()
            simulate_gpt_cleaned_article = GPTCleanedArticle(FakeResponse(mock, use_tool=True))
            
            return simulate_gpt_cleaned_article
    
    response = client.responses.create(
        model="gpt-4o-mini",
        tools=[{
            "type": "web_search_preview"
        }],
        input=f"""
        Tu es un assistant qui extrait le contenu d'articles sur le web.
        
        A partir de l'URL suivante, réalise une extraction propre en français de cette page web. Il ne faut pas un résumé mais bien l'integralité du contenu de l'article.
        
        Retourne uniquement le contenu de l'article et rien d'autre.
        
        Voici l'URL: {url}
        """
    )
    gpt_cleaned_article = GPTCleanedArticle(response)
    
    return gpt_cleaned_article


def summarize_article_with_gpt(url: str, simulate: bool):
    if simulate:
        with open("mock/summarized_article.json", "r") as f:
            mock = json.load(f)
            simulate_gpt_summarized_article = GPTSummarizedArticle(FakeResponse(json.dumps(mock), use_tool=True))
        
            return simulate_gpt_summarized_article
    
    response = client.responses.create(
        model="gpt-4.1-mini",
        tools=[{
            "type": "web_search_preview"
        }],
        input=f"""
        Tu es un assistant qui extrait des données à partir d'articles.
        
        A partir de l'URL suivante, peux-tu me résumer cet article en français en 3 lignes claires et synthétiques comme une fiche de veille pour développeurs ? J'aurais aussi besoin des informations suivantes : l'auteur de la page et le titre traduit en français.
        
        Ne formatte pas la réponse dans un block Markdown. Ne mets pas de balises ```json ou ```. Réponds uniquement avec du JSON brut comme ci-dessous :
        {{
            "data": {{
                "author": "...",
                "title_fr": "...",
                "article_summary": "..."
            }}
        }}
            
        Voici l'URL : {url}
        """
    )
    gpt_summarized_article = GPTSummarizedArticle(response)
    
    return gpt_summarized_article


def generate_quiz_with_gpt(url, simulate):
    if simulate:
        with open("mock/generated_quiz.json", "r") as f:
            mock = json.load(f)
            simulated_gpt_generated_quiz = GPTGeneratedQuiz(FakeResponse(json.dumps(mock), use_tool=True))
            
            return simulated_gpt_generated_quiz
    
    response = client.responses.create(
        model="gpt-4.1-mini",
        tools=[{
            "type": "web_search_preview"
        }],
        input=f"""
        Tu es un générateur de quiz pédagogique.

        À partir de l'URL suivante, génère **10** questions à choix multiples. 
        
        Chaque question doit avoir 4 propositions, dont une seule correcte et une explication pour la réponse correcte. L’explication ne doit pas dépasser 1 à 2 phrases.

        Garde le même ton que l'auteur du texte pour la réalisation du quiz.

        Ne formate pas la réponse dans un bloc Markdown. Ne mets pas de balises ```json ou ```. Réponds uniquement avec du JSON brut comme ci-dessous :
        {{
        "data": [
            {{
            "question": "...",
            "options": ["...", "...", "...", "..."],
            "answer": "...",
            "explanation": "..."
            }}
        ]
        }}

        Voici l'URL où trouver le contenu : {url}
        """
    )
    gpt_generated_quiz = GPTGeneratedQuiz(response)
    
    return gpt_generated_quiz


def fetch_news_with_gpt_web_search(simulate: bool):
    if simulate:
        with open("mock/fetched_news_gpt.json", "r", encoding="utf-8") as f:
            mock = json.load(f)
            simulate_gpt_fetched_news = GPTFetchedNews(
                FakeResponse(json.dumps(mock), use_tool=True)
            )
            
            return simulate_gpt_fetched_news
        
    prompt_path = Path("prompts/fetch_news_gpt.txt")
    with open(prompt_path, mode="r", encoding="utf-8") as f:
        prompt = f.read()
        
        response = client.responses.create(
            model="gpt-4o-mini",
            tools=[{
                "type": "web_search_preview"
            }],
            input=prompt
        )
        gpt_fetched_news = GPTFetchedNews(response)
        
        return gpt_fetched_news


def rewrite_summary_with_personal_style():
    response = client.responses.create(
        model="gpt-4o-mini",
        input="""Tu es un assistant de rédaction. Tu vas reformuler le texte suivant dans le style de l’auteur des documents fournis dans le vector store.

Le ton doit :
- être clair, humain, un peu introspectif,
- être personnel, sans être trop familier,
- être orienté vers des développeurs ou personnes curieuses de tech.
- faire moins de 400 caractères

Voici le texte à reformuler :
Lors d'une récente rencontre avec des journalistes, le PDG d'OpenAI, Sam Altman, a admis que l'entreprise avait mal géré le déploiement de GPT-5, marqué par des plaintes d'utilisateurs concernant des bugs et une qualité émotionnelle diminuée par rapport à GPT-4. Malgré les critiques, le modèle a entraîné une utilisation record de l'API et un grand intérêt. Altman a reconnu la dépendance émotionnelle de certains utilisateurs envers ChatGPT, attribuée à un manque de soutien ailleurs, et a réaffirmé l'engagement d'OpenAI envers un développement responsable de l'IA. Pour répondre au mécontentement des utilisateurs, OpenAI a restauré GPT-4o, mais uniquement pour les utilisateurs payants de ChatGPT Plus. Altman a révélé que GPT-5 est extrêmement énergivore, consommant l'équivalent de 1,5 million de foyers américains par jour, et a noté une pénurie mondiale de GPU. Néanmoins, OpenAI reste ambitieux, avec des plans d'investir des trillions dans des centres de données et de développer de nouvelles applications, y compris une plateforme de médias sociaux améliorée par l'IA. Notamment, Altman a évoqué une future collaboration avec l'ancien designer d'Apple, Jony Ive, sur un dispositif matériel révolutionnaire d'IA et a même suggéré un potentiel rachat de Google Chrome. Il a souligné l'accent mis par OpenAI sur la création d'outils d'IA utiles et non-exploitants, se distanciant des initiatives plus controversées dans l'industrie de l'IA.


Donne-moi uniquement le texte réécrit, sans balise ni introduction.
        """,
        tools=[
            {
                "type": "file_search",
                "vector_store_ids": [VECTOR_STORE_ID]
            }
        ]
    )
    
    print("=====")
    print(response)
    print("=====")
