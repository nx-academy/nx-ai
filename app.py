import click


from nx_ai.github import fetch_chapter_from_github, create_pull_request_on_github
from nx_ai.openai import write_embedded_document, generate_quiz_from_gpt
from nx_ai.bot_test import run_bot


@click.group()
def cli():
    pass


@cli.command()
def fetch_chapter():
    fetch_chapter_from_github()

    
@cli.command()
def write_embedded_chapter():
    write_embedded_document()


@cli.command()
def generate_quiz():
    generate_quiz_from_gpt()


@cli.command()
def create_pull_request():
    create_pull_request_on_github()


@cli.command()
def run_discord_bot():
    run_bot()


if __name__ == "__main__":
    cli()
