import click

from nx_ai.openai_service.openai_cli import openai_group


@click.group()
def cli():
    pass


cli.add_command(openai_group, name="openai")


if __name__ == "__main__":
    cli()
