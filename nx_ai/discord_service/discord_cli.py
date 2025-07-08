import click


@click.group()
def discord_group():
    """Set of commands related to Discord"""
    pass


@discord_group.command()
def run_bot():
    print("Ok, let's go!")
