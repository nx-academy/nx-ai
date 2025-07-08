import click

from nx_ai.github_service.github_api import create_pull_request_on_github


@click.group()
def github_group():
    """Set of commands related to GitHub"""
    pass


@github_group.command()
def create_pr():
    """Create a Pull Request on repo nx-academy.github.io"""
    filename = "optimisation-images-docker"
    create_pull_request_on_github(filename)
