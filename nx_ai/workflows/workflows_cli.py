import click

from nx_ai.workflows.generate_quiz import generate_quiz_beta


@click.group()
def workflows_group():
    """Commands related to NX automation workflows."""
    pass


@workflows_group.command()
def generate_quiz():
    """
    Generate a quiz from an article and open a PR on nx-academy.github.io
    """
    url = "https://nx.academy/fiches/optimisation-images-docker/"
    filename = "optimisation-images-docker"
    
    generate_quiz_beta(url, filename)


@workflows_group.command()
def generate_recap():
    """
    Generate an article recap as Markdown and open a PR on nx-academy.github.io
    """
    print("====")
    print("====")
    print("====")
