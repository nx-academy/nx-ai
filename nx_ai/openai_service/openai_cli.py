import click

from nx_ai.openai_service.openai_api import (
    clean_article_with_gpt, 
    fetch_news_with_gpt_web_search,
    generate_quiz_with_gpt,
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
