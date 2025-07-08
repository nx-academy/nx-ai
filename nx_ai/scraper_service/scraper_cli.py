import click

from nx_ai.scraper_service.scrape_website import scrape_website


@click.group()
def scraper_group():
    """NOT USED RIGHT NOW - Set of commands related to scrape features."""
    pass


@scraper_group.command()
def run():
    """Scrape a website and clean it"""
    url = "https://nx.academy"
    
    scrape_website(url)
