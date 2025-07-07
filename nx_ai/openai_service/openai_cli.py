import click

from nx_ai.openai_service.openai_api import say_hello_to_gpt
 

@click.group()
def openai_group():
    pass


@openai_group.command()
def say_hello():
    """Send Hello World to OpenAI"""
    response = say_hello_to_gpt()
    
    print("====")
    print(response)
    print("====")
