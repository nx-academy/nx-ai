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
