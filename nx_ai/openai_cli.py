import click
from openai import OpenAI

from nx_ai.gpt_models import (GPTResponse, GPTCleanedArticle, GPTSummarizedArticle, GPTGeneratedQuiz)


client = OpenAI()


MODEL = "gpt-4o-mini"


@click.group()
def openai_group():
    """Set of commands related to OpenAI"""
    pass


@openai_group.command()
def say_hello():
    """Say hello from openai group"""
    response = client.responses.create(
        model=MODEL,
        input="Hello ! This is a test"
    )
    gpt_response = GPTResponse(response)
    
    return gpt_response


@openai_group.command()
def clean_article():
    """Browse an article from the Web directly with GPT, clean it, and extract info from it"""
    response = client.responses.create(
        model=MODEL,
        tools=[{
            "type": "web_search_preview"
        }],
        input="""
            Peux-tu me faire une extraction propre de cette page web en français ? J'aimerais notamment que tu extrais :
            - Tout le texte de la page (pas un résumé)
            - L'auteur de la page
            - Le titre traduit en français
            - La date de publication
            
            Voici l'URL : https://nx.academy/fiches/presentation-registry-docker/
        """
    )
    gpt_cleaned_article = GPTCleanedArticle(response)
    
    return gpt_cleaned_article



@openai_group.command()
def summarize_article():
    """Send a url to GPT and ask it to summarize it in 3 lines"""
    print("Sending the request to GPT")
    response = client.responses.create(
        model=MODEL,
        tools=[{
            "type": "web_search_preview"
        }],
        input="Peux-tu me résumer cet article en français en 3 lignes claires et synthétiques comme une fiche de veille pour développeurs ? https://nx.academy/fiches/presentation-registry-docker/"
    )
    gpt_summarized_article = GPTSummarizedArticle(response)
    
    return gpt_summarized_article


@openai_group.command()
def generate_quiz():
    """Generate a quiz in JSON format"""
    print("Sending the request to GPT")
    response = client.responses.create(
        model=MODEL,
        tools=[{
            "type": "web_search_preview"
        }],
        input="""
        Tu es un générateur de quiz pédagogique.

        À partir de l'URL suivante, génère **1** question à choix multiples. 
        
        Chaque question doit avoir 4 propositions, dont une seule correcte et une explication pour la réponse correcte. L’explication ne doit pas dépasser 1 à 2 phrases.

        Garde le même ton que l'auteur du texte pour la réalisation du quiz.

        Ne formate pas la réponse dans un bloc Markdown. Ne mets pas de balises ```json ou ```.
        Réponds uniquement avec du JSON brut comme ci-dessous :
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

        Voici l'URL où trouver le contenu : https://nx.academy/fiches/presentation-registry-docker/
        """
    )
    gpt_generated_quiz = GPTGeneratedQuiz(response)
    
    print("=====")
    print(gpt_generated_quiz)
    print("=====")
