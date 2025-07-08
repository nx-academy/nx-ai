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
        with open("mock/summarized_article.json", "r") as f:
            mock = json.load(f)
            cleaned_article = GPTSummarizedArticle(FakeResponse(json.dumps(mock)))
        
            return cleaned_article
    
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
