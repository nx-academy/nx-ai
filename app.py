import click


from nx_ai.github import fetch_chapter_from_github, create_pull_request_on_github
from nx_ai.openai import write_embedded_document, get_embedded_documents


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
def get_embedded_chapter():
    get_embedded_documents()


@cli.command()
def create_pull_request():
    create_pull_request_on_github()


if __name__ == "__main__":
    cli()
