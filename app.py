import click


from nx_ai.github import write_content_from_github, create_pull_request_on_github
from nx_ai.openai import create_document_with_chroma, generate_quiz_from_gpt
from nx_ai.bot_test import run_bot
from nx_ai.medium import scrape_medium_article


@click.group()
def cli():
    pass


@cli.command()
@click.option("--url", prompt="GitHub URL", help="Enter the full GitHub URL you'd like to fetch. Must be a raw format.")
@click.option("--name", prompt="Document name", help="The name of the document you'd like to create locally")
def scrape_github(url, name):
    """Retrieve a raw file from GitHub, clean it, and store it locally in the folder of your choice."""
    write_content_from_github(url, name)
    
    
@cli.command()
@click.option("--location", prompt="File location", help="Enter the path where the file you want to embed is located")
@click.option("--name", prompt="Document name", help="Enter the name of the document which will be used as metadata for ChromaDB")
def create_document(location, name):
    """Read a local file, usually a md file, and store it as an embedded document with ChromaDB and GPT API."""
    create_document_with_chroma(location, name)


@cli.command()
def generate_quiz():
    generate_quiz_from_gpt()


@cli.command()
def create_pull_request():
    create_pull_request_on_github()


@cli.command()
def run_discord_bot():
    run_bot()


@cli.command()
def scrape_medium():
    scrape_medium_article()


if __name__ == "__main__":
    cli()
