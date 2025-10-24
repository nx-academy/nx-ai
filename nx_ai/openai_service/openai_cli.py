import click

from nx_ai.openai_service.openai_api import (
    clean_article_with_gpt, 
    fetch_news_with_gpt_web_search,
    generate_quiz_with_gpt,
    rewrite_summary_with_personal_style,
    say_hello_to_gpt,
    summarize_article_with_gpt)
 

@click.group()
def openai_group():
    """Set of commands related to OpenAI"""
    pass


@openai_group.command()
@click.option("--simulate", is_flag=True, 
              help="Simulate the API call by using a local text file")
def say_hello(simulate):
    """Send Hello World to OpenAI"""
    gpt_response = say_hello_to_gpt(simulate)
    
    print(gpt_response)

@openai_group.command()
@click.option("--simulate", is_flag=True, help="Simulate the API call by using a local text file")
def clean_article(simulate):
    """Browse an web article with GPT tool and keep only the text contents"""
    # For now, I keep the article URL here. I'll see later where to put it.
    article_url = "https://nx.academy/fiches/presentation-registry-docker/"
    
    gpt_cleaned_article = clean_article_with_gpt(article_url, simulate)
    
    print(gpt_cleaned_article.text)


@openai_group.command()
@click.option("--simulate", is_flag=True,
              help="Simulate the API call by loading a local JSON file")
def summarize_article(simulate):
    """Generate a summary for an article and extract also the author and the title"""
    # For now, I keep the article URL here. I'll see later where to put it.
    article_url = "https://nx.academy/fiches/presentation-registry-docker/"
    
    gpt_summarized_article = summarize_article_with_gpt(article_url, simulate)
    
    print(gpt_summarized_article.data)


@openai_group.command()
@click.option("--simulate", is_flag=True,
              help="Simulate the API call by loading a local JSON file")
def generate_quiz(simulate):
    """Generate a quiz in JSON Format from an article"""
    url = "https://nx.academy/fiches/presentation-registry-docker/"
    
    gpt_generated_quiz = generate_quiz_with_gpt(url, simulate)
    
    print(gpt_generated_quiz.data)


@openai_group.command()
@click.option("--simulate", is_flag=True,
              help="Simulate the API call by loading a local JSON file")
def fetch_news(simulate):
    """Use Bing Search to find news related to a specific topic"""
    gpt_fetched_news = fetch_news_with_gpt_web_search(simulate=simulate)
    
    print(gpt_fetched_news.data)


@openai_group.command()
@click.option("--simulate", is_flag=True,
              help="Simulate the API call by loading a local text file")
def style_summary(simulate):
    """(RAG) Rewrite the summary news with my personal style"""
    sample_raw_summary = "Lors d'une récente rencontre avec des journalistes, le PDG d'OpenAI, Sam Altman, a admis que l'entreprise avait mal géré le déploiement de GPT-5, marqué par des plaintes d'utilisateurs concernant des bugs et une qualité émotionnelle diminuée par rapport à GPT-4. Malgré les critiques, le modèle a entraîné une utilisation record de l'API et un grand intérêt. Altman a reconnu la dépendance émotionnelle de certains utilisateurs envers ChatGPT, attribuée à un manque de soutien ailleurs, et a réaffirmé l'engagement d'OpenAI envers un développement responsable de l'IA. Pour répondre au mécontentement des utilisateurs, OpenAI a restauré GPT-4o, mais uniquement pour les utilisateurs payants de ChatGPT Plus. Altman a révélé que GPT-5 est extrêmement énergivore, consommant l'équivalent de 1,5 million de foyers américains par jour, et a noté une pénurie mondiale de GPU. Néanmoins, OpenAI reste ambitieux, avec des plans d'investir des trillions dans des centres de données et de développer de nouvelles applications, y compris une plateforme de médias sociaux améliorée par l'IA. Notamment, Altman a évoqué une future collaboration avec l'ancien designer d'Apple, Jony Ive, sur un dispositif matériel révolutionnaire d'IA et a même suggéré un potentiel rachat de Google Chrome. Il a souligné l'accent mis par OpenAI sur la création d'outils d'IA utiles et non-exploitants, se distanciant des initiatives plus controversées dans l'industrie de l'IA."
    
    gpt_styled_summary = rewrite_summary_with_personal_style(simulate=simulate, raw_summary=sample_raw_summary)
    
    print(gpt_styled_summary)
