import click

from nx_ai.openai_service.openai_cli import openai_group
from nx_ai.github_service.github_cli import github_group


@click.group()
def cli():
    pass


cli.add_command(openai_group, name="openai")
cli.add_command(github_group, name="github")


if __name__ == "__main__":
    cli()
