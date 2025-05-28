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


# @cli.command()
# @click.option("--name", prompt="Document name", help="Enter the document name you want to generate a quiz from")
# def generate_quiz(name):
#     """Retrieve a document stored in Chroma, then ask GPT to create a quiz, and store it as a json file once it's done."""
#     generate_quiz_from_gpt(name)


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


@cli.command()
def generate_quiz_beta():
    article_url = "https://raw.githubusercontent.com/nx-academy/nx-academy.github.io/refs/heads/main/src/pages/drafts/presentation-registry-docker.md"
    article_name = "presentation-registry-docker.md"
    
    # Retrieve the content from GitHub by scrapping it and store them locally
    write_content_from_github(article_url, article_name)
    
    # Create the doc
    create_document_with_chroma(
        f"nx_ai/courses_data/{article_name}",
        article_name[:-3]
    )
    


@cli.command()
def generate_recap():
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
            "author": "CNET",
            "filename": "cnet",
            "title": "US wants judge to break up google force sale of Chrome",
            "url": "https://www.cnet.com/tech/us-wants-judge-to-break-up-google-force-sale-of-chrome-heres-what-to-know/"
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
    text = f"""
    ---
    layout: ../../layouts/BlogPostLayout.astro

    title: "Titre à changer"
    description: Description à changer

    imgAlt: rien
    imgSrc: /misc/kiosque-journaux.png

    kind: Articles
    author: Thomas
    draft: false
    publishedDate: mois à préciser
    ---
    
    # Le récap #1 - Date à changer

    <img src="/misc/kiosque-journaux.png" alt="" style="aspect-ratio: 1792 / 1024; object-fit: cover; width: 100%; display: block; object-position: top" />

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
    print("Now ready to open a PR and enjoy life!")


if __name__ == "__main__":
    cli()
