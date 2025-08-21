import asyncio
import click

from nx_ai.turso_service.turso_api import insert_news_in_db


@click.group()
def turso_group():
    """Set of commands related to Turso DB"""
    pass


@turso_group.command()
def create_news():
    """Insert a News in NewsFeed table"""
    asyncio.run(insert_news_in_db())
