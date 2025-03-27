import click


@click.group()
def cli():
    pass


@cli.command()
def say_hello():
    click.echo("Hello, World!")
    

@cli.command()
def fetch_chapter():
    pass


if __name__ == "__main__":
    cli()
