import json
from openai import OpenAI

from nx_ai.openai_service.gpt_models import GPTResponse, FakeResponse, GPTSummarizedArticle


client = OpenAI()


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


def summarize_article_with_gpt(url, simulate):
    if simulate:
        raw_json = {
            "data": {
                "author": "nx.academy", 
                "title_fr": "Présentation du registre Docker", 
                "article_summary": "L'article explique le rôle du registre Docker, un service de stockage et de distribution d'images Docker. Il détaille les types de registres (Docker Hub, registres privés) et leur utilisation dans les workflows DevOps. Enfin, il aborde la sécurisation et la gestion des images pour optimiser les déploiements containerisés."
            }
        }
           
        cleaned_article = GPTSummarizedArticle(FakeResponse(json.dumps(raw_json)))
        
        print("====")
        print(cleaned_article)
        print("====")
        
        return
    
    response = client.responses.create(
        model="gpt-4.1-mini",
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
