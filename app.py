import click


from nx_ai.github import fetch_chapter_from_github, create_pull_request_on_github


@click.group()
def cli():
    pass


@cli.command()
def fetch_chapter():
    fetch_chapter_from_github()
    

@cli.command()
def create_pull_request():
    create_pull_request_on_github()


if __name__ == "__main__":
    cli()
