import click

from nx_ai.discord_service.discord_api import run_discord_bot


@click.group()
def discord_group():
    """Set of commands related to Discord"""
    pass


@discord_group.command()
def run_bot():
    """Run NX Discord bot that allows to create News, fetch news, and more, directly from Discord"""
    run_discord_bot()
