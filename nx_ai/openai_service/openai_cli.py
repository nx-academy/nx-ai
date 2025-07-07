import click

from nx_ai.openai_service.openai_api import say_hello_to_gpt
 

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
