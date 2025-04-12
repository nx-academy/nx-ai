import click


from nx_ai.github import fetch_chapter_from_github, create_pull_request_on_github
from nx_ai.openai import write_embedded_document


@click.group()
def cli():
    pass


@cli.command()
def fetch_chapter():
    fetch_chapter_from_github()
    
    
@cli.command()
def generate_quiz_from_gpt():
    print("Last part before release!")
    write_embedded_document()
    

@cli.command()
def create_pull_request():
    create_pull_request_on_github()


if __name__ == "__main__":
    cli()
