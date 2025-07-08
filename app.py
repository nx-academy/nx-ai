import click


from nx_ai.github import write_content_from_github, create_pull_request_on_github
from nx_ai.openai import (
    create_document_with_chroma, 
    generate_quiz_from_gpt, 
    generate_summary_with_gpt)
from nx_ai.bot_test import run_bot
from nx_ai.scraper import scrape_article_from_internet

# from nx_ai.openai_cli import openai_group
from nx_ai.openai_service.openai_cli import openai_group


@click.group()
def cli():
    pass


@cli.command()
def generate_quiz():
    """New version of the generated quiz feature"""
    print("=====")
    print("=====")
    print("=====")


@cli.command()
def generate_quiz_beta():
    """Generate a quiz with GPT from a raw markdown file and PR it to Astro repo"""
    # For now, I pass the url and the file name in raw data. I'll see later how to retrieve it from a file, command, and/or discord
    article_url = "https://raw.githubusercontent.com/nx-academy/nx-academy.github.io/refs/heads/main/src/pages/drafts/optimisation-images-docker.md"
    article_name = "optimisation-images-docker.md"
    
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
            "author": "Alexander Opalic",
            "title": "No Server, No Database: Smarter Related Posts in Astro with `transformers.js`",
            "filename": "alexop.dev-astro-transformers",
            "url": "https://alexop.dev/posts/semantic-related-posts-astro-transformersjs/"
        },
        {
            "author": "WaspDev Blog",
            "title": "JavaScript's upcoming Temporal API and what problems it will solve",
            "filename": "temporal-api",
            "url": "https://waspdev.com/articles/2025-05-24/temporal-api"
        },
        {
            "author": "Courrier International",
            "title": "Enquête sur la chute de Builder.ai, l’entreprise d’IA qui a menti sur toute la ligne",
            "filename": "courrierinternational-builder-ai",
            "url": "https://www.courrierinternational.com/article/faillite-enquete-sur-la-chute-de-builder-ai-l-entreprise-d-ia-qui-a-menti-sur-toute-la-ligne_231696"
        },
        {
            "author": "Reuters",
            "filename": "Reuters-openai",
            "title": "OpenAI considers taking on Google with browser, the Information reports",
            "url": "https://www.reuters.com/technology/artificial-intelligence/openai-considers-taking-google-with-browser-information-reports-2024-11-21"
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

title: "Le récap #3 - June 2025"
description: Description à changer

imgAlt: Un vendeur de journaux dans un kiosque parisien, pixel art
imgSrc: /images/articles/kiosque-journaux.webp

kind: Articles
author: Thomas
draft: false
publishedDate: 06/27/2025
---
    
# Le récap #3 - June 2025

<img src="/images/articles/kiosque-journaux.webp" alt="Un vendeur de journaux dans un kiosque parisien, pixel art" style="aspect-ratio: 1792 / 1024; object-fit: cover; width: 100%; display: block; object-position: top" />

<br>
"""
    for article in articles:
        print("Asking GPT API to make the summary")
        llm_summary = generate_summary_with_gpt(article["filename"])
        
        text += f"""## {article["title"]}
<small>{article["author"]}</small>
        
{llm_summary}
        
[Lire l'article]({article["url"]})
        
<br>
        
---
"""
        
        print(f"""Successfully creating summary for article: {article["filename"]}""")
    with open(f"nx_ai/recap_data/le-recap-june-2025.md", "w", encoding="utf-8") as file:
        file.write(text)
        print("Successfully creating the file with all the summary")
    
    # PR the summary on GitHub
    create_pull_request_on_github("le-recap-june-2025", "recap")

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
@click.option("--type", prompt="Document type (Recap, quiz)", help="Enter the type of the document")
def create_pull_request(name, type):
    """Retrieve the generated quiz json file, connect to NX GitHub org, commit the file, and create a PR on main"""
    create_pull_request_on_github(name, type)


@cli.command()
def run_discord_bot():
    run_bot()


@cli.command()
def scrape_article():
    articles = [
        {
            "url": "https://www.reuters.com/technology/artificial-intelligence/openai-considers-taking-google-with-browser-information-reports-2024-11-21/",
            "filename": "reuteur-test.txt"
        }
    ]
    
    for article in articles:
        scrape_article_from_internet(article["url"], article["filename"])


@cli.command()
@click.option("--name", prompt="Document name", help="Enter the document name you want to generate a summary from")
def generate_summary(name):
    generate_summary_with_gpt(name)



cli.add_command(openai_group, name="openai")


if __name__ == "__main__":
    cli()
