import click


from nx_ai.github import write_content_from_github, create_pull_request_on_github
from nx_ai.openai import (
    create_document_with_chroma, 
    generate_quiz_from_gpt, 
    generate_summary_with_gpt)
from nx_ai.bot_test import run_bot
from nx_ai.scraper import scrape_article_from_internet


@click.group()
def cli():
    pass


@cli.command()
def generate_quiz_beta():
    """Generate a quiz with GPT from a raw markdown file and PR it to Astro repo"""
    # For now, I pass the url and the file name in raw data. I'll see later how to retrieve it from a file, command, and/or discord
    article_url = "https://raw.githubusercontent.com/nx-academy/nx-academy.github.io/refs/heads/main/src/pages/drafts/presentation-registry-docker.md"
    article_name = "presentation-registry-docker.md"
    
    # Retrieve the content from GitHub by scrapping it and store them locally
    write_content_from_github(article_url, article_name)
    
    # Create the doc
    create_document_with_chroma(
        f"nx_ai/courses_data/{article_name}",
        article_name[:-3]
    )
    
    # Generate the quiz
    generate_quiz_from_gpt(article_name[:-3])
    
    # PR it to GitHub
    print("Ready to PR it!")
    create_pull_request_on_github(article_name[:-3], "quiz")


@cli.command()
def generate_recap_beta():
    """Generate a summary of articles with GPT from a list of links, create a md friendly Astro file, and PR it to NX Astro repo"""
    # For now, I pass the list of articles here but I should be able to write it from a file.
    articles = [
        {
            "author": "NX Academy",
            "filename": "nx",
            "title": "Le Moine, le Vape Coder, le Debugger & le Learner",
            "url": "https://nx.academy/articles/profils-ia-developpeur/"
        },
        {
            "author": "Karl Groves",
            "filename": "karlgroves",
            "title": "AI is the future of accessibility",
            "url": "https://karlgroves.com/ai-is-the-future-of-accessibility/"
        },
        {
            "author": "NX Academy",
            "filename": "nx-academy-registry-docker",
            "title": "Qu’est-ce qu’un registry Docker?",
            "url": "https://nx.academy/drafts/presentation-registry-docker/"
        },
        {
            "author": "NX Academy",
            "filename": "nx-academy-registry-docker",
            "title": "Qu’est-ce qu’un registry Docker?",
            "url": "https://nx.academy/drafts/presentation-registry-docker/"
        }
    ]
    
    for article in articles:
        # Scrape the article (maybe I can store them locally first)
        scrape_article_from_internet(article["url"], article["filename"])
    
        # Create the doc
        create_document_with_chroma(
            f"nx_ai/articles_data/{article["filename"]}.txt",
            article["filename"],
            title=article["title"],
            author=article["author"], 
            url=article["url"]
        )
    
    # Generate and write Summary
    text = f"""---
layout: ../../layouts/BlogPostLayout.astro

title: Le Récap #2 - Mai 2025
description: Description à changer

imgAlt: rien
imgSrc: /images/articles/kiosque-journaux.webp

kind: Articles
author: Thomas
draft: false
publishedDate: 05/31/2025
---
    
    # Le récap #2 - Mai 2025

    <img src="/images/articles/kiosque-journaux.webp" alt="" style="aspect-ratio: 1792 / 1024; object-fit: cover; width: 100%; display: block; object-position: top" />

    <br>
    """
    for article in articles:
        print("Asking GPT API to make the summary")
        llm_summary = generate_summary_with_gpt(article["filename"])
        
        text += f"""
        ## {article["title"]}
        <small>{article["author"]}</small>
        
        {llm_summary}
        
        [Lire l'article]({article["url"]})
        
        <br>
        
        ---
        """
        
        print(f"""Successfully creating summary for article: {article["filename"]}""")
    with open(f"nx_ai/recap_data/test.md", "w", encoding="utf-8") as file:
        file.write(text)
        print("Successfully creating the file with all the summary")
    
    # PR the summary on GitHub
    create_pull_request_on_github("test", "recap")


@cli.command()
@click.option("--url", prompt="GitHub URL", help="Enter the full GitHub URL you'd like to fetch. Must be a raw format.")
@click.option("--name", prompt="Document name", help="The name of the document you'd like to create locally")
def scrape_github(url, name):
    """Retrieve a raw file from GitHub, clean it, and store it locally in the folder of your choice."""
    write_content_from_github(url, name)
    
    
@cli.command()
@click.option("--location", prompt="File location", help="Enter the path where the file you want to embed is located")
@click.option("--name", prompt="Document name", help="Enter the name of the document which will be used as metadata for ChromaDB")
@click.option("--title", prompt="Title of the document", default="", help="Optional / Use it if you want to add a title to store in db")
@click.option("--author", prompt="Author of the document", default="", help="Optional / Use it if you want to add a document author to store in db")
@click.option("--url", prompt="URL of the document", default="", help="Optional / Use it if you want to store the URL where the document comes from, e.g. an online blog")
def create_document(location, name, title, author, url):
    """Read a local file, usually a md file, and store it as an embedded document with ChromaDB and GPT API."""
    create_document_with_chroma(location, name, title=title, author=author, url=url)


# @TODO: I let that here for now, I'll probably create a subcommand to handle it later if I need it.
# @cli.command()
# @click.option("--name", prompt="Document name", help="Enter the document name you want to generate a quiz from")
# def generate_quiz(name):
#     """Retrieve a document stored in Chroma, then ask GPT to create a quiz, and store it as a json file once it's done."""
    # generate_quiz_from_gpt(name)


@cli.command()
@click.option("--name", prompt="Document name", help="Enter the name of the document you want to create a Pull Request on GitHub from.")
def create_pull_request(name):
    """Retrieve the generated quiz json file, connect to NX GitHub org, commit the file, and create a PR on main"""
    create_pull_request_on_github(name)


@cli.command()
def run_discord_bot():
    run_bot()


@cli.command()
def scrape_article():
    articles = [
        {
            "url": "https://nx.academy/articles/profils-ia-developpeur/",
            "filename": "01-nx.txt"
        },
        {
            "url": "https://karlgroves.com/ai-is-the-future-of-accessibility/",
            "filename": "02-karlgroves.txt"
        },
        {
            "url": "https://www.cnet.com/tech/us-wants-judge-to-break-up-google-force-sale-of-chrome-heres-what-to-know/",
            "filename": "03-cnet.txt"
        },
    ]
    
    for article in articles:
        scrape_article_from_internet(article["url"], article["filename"])


@cli.command()
@click.option("--name", prompt="Document name", help="Enter the document name you want to generate a summary from")
def generate_summary(name):
    generate_summary_with_gpt(name)


if __name__ == "__main__":
    cli()
