import click


from nx_ai.github import fetch_chapter_from_github


@click.group()
def cli():
    pass


@cli.command()
def say_hello():
    click.echo("Hello, World!")
    

@cli.command()
def fetch_chapter():
    fetch_chapter_from_github()


if __name__ == "__main__":
    cli()
