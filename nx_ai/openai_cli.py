import click
from openai import OpenAI


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
    
    print(response.output[0].content[0].text)


@openai_group.command()
def summarize_article():
    """Send a url to GPT and ask it to summarize it in 3 lines"""
    print("Sendin the request to GPT")
    response = client.responses.create(
        model=MODEL,
        tools=[{
            "type": "web_search_preview"
        }],
        input="Peux-tu me résumer cet article en français en 3 lignes claires et synthétiques comme une fiche de veille pour développeurs ? https://nx.academy/fiches/presentation-registry-docker/"
    )
    
    print("====")
    print(response.output[1].content[0].text)
    print("====")
