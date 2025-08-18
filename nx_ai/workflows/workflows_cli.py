import click

from nx_ai.workflows.generate_quiz import generate_quiz_beta
from nx_ai.workflows.generate_recap import generate_recap_beta


@click.group()
def workflows_group():
    """Commands related to NX automation workflows."""
    pass


@workflows_group.command()
@click.option("--simulate", is_flag=True,
              help="Simulate the API Call to GPT / Costs no money")
def generate_quiz(simulate):
    """
    Generate a quiz from an article and open a PR on nx-academy.github.io
    """
    
    # For now, I keep the url of the article and its filename here. I'll see later to maybe save them in a local db.
    url = "https://nx.academy/drafts/artefact-github-actions/"
    filename = "artefact-github-actions"
    
    generate_quiz_beta(url, filename, simulate)


@workflows_group.command()
def generate_recap():
    """
    Generate an article recap as Markdown and open a PR on nx-academy.github.io
    """
    
    generate_recap_beta()
