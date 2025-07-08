import click


@click.group()
def github_group():
    """Set of commands related to GitHub"""
    pass


@github_group.command()
def create_pr():
    """Create a Pull Request on repo nx-academy.github.io"""
    print("====")
    print("====")
    print("====")
