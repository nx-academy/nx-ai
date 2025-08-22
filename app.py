import click

from nx_ai.discord_service.discord_cli import discord_group
from nx_ai.github_service.github_cli import github_group
from nx_ai.openai_service.openai_cli import openai_group
from nx_ai.turso_service.turso_cli import turso_group
from nx_ai.workflows.workflows_cli import workflows_group


@click.group()
def cli():
    pass


cli.add_command(discord_group, name="discord")
cli.add_command(github_group, name="github")
cli.add_command(openai_group, name="openai")
cli.add_command(turso_group, name="turso")
cli.add_command(workflows_group, name="workflows")


if __name__ == "__main__":
    cli()
