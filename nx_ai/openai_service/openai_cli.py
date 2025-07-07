import click

from nx_ai.openai_service.openai_api import say_hello_to_gpt, summarize_article_with_gpt
 

@click.group()
def openai_group():
    pass


@openai_group.command()
@click.option("--simulate", is_flag=True, 
              help="Simulate the API call by loading JSON file")
def say_hello(simulate):
    """Send Hello World to OpenAI"""
    gpt_response = say_hello_to_gpt(simulate)
    
    print(gpt_response)


@openai_group.command()
def summarize_article():
    """Generate a summary for an article and extract also the author and the title"""
    article_url = "https://nx.academy/fiches/presentation-registry-docker/"
    
    gpt_summarized_article = summarize_article_with_gpt(article_url)
    
    print("====")
    print(gpt_summarized_article.data)
    print("====")
