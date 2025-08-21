import click


@click.group()
def turso_group():
    """Set of commands related to Turso DB"""
    pass


@turso_group.command()
def create_news():
    """Insert a News in NewsFeed table"""
    print("+++")
    print("+++")
    print("+++")
