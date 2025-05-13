import click


from nx_ai.github import write_content_from_github, create_pull_request_on_github
from nx_ai.openai import (
    create_document_with_chroma, 
    generate_quiz_from_gpt, 
    generate_summary_with_gpt)
from nx_ai.bot_test import run_bot
from nx_ai.scraper import scrape_article_from_internet


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
@click.option("--title", prompt="Title of the document", default="", help="Optional / Use it if you want to add a title to store in db")
@click.option("--author", prompt="Author of the document", default="", help="Optional / Use it if you want to add a document author to store in db")
@click.option("--url", prompt="URL of the document", default="", help="Optional / Use it if you want to store the URL where the document comes from, e.g. an online blog")
def create_document(location, name, title, author, url):
    """Read a local file, usually a md file, and store it as an embedded document with ChromaDB and GPT API."""
    create_document_with_chroma(location, name, title=title, author=author, url=url)


@cli.command()
@click.option("--name", prompt="Document name", help="Enter the document name you want to generate a quiz from")
def generate_quiz(name):
    """Retrieve a document stored in Chroma, then ask GPT to create a quiz, and store it as a json file once it's done."""
    generate_quiz_from_gpt(name)


@cli.command()
@click.option("--name", prompt="Document name", help="Enter the name of the document you want to create a Pull Request on GitHub from.")
def create_pull_request(name):
    """Retrieve the generated quiz json file, connect to NX GitHub org, commit the file, and create a PR on main"""
    create_pull_request_on_github(name)


@cli.command()
def run_discord_bot():
    run_bot()


@cli.command()
def scrape_article():
    articles = [
        {
            "url": "https://nx.academy/articles/profils-ia-developpeur/",
            "filename": "01-nx.txt"
        },
        {
            "url": "https://karlgroves.com/ai-is-the-future-of-accessibility/",
            "filename": "02-karlgroves.txt"
        },
        {
            "url": "https://www.cnet.com/tech/us-wants-judge-to-break-up-google-force-sale-of-chrome-heres-what-to-know/",
            "filename": "03-cnet.txt"
        },
    ]
    
    for article in articles:
        scrape_article_from_internet(article["url"], article["filename"])


@cli.command()
@click.option("--name", prompt="Document name", help="Enter the document name you want to generate a summary from")
def generate_summary(name):
    generate_summary_with_gpt(name)


if __name__ == "__main__":
    cli()
