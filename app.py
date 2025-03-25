import requests
import re
import chromadb
import os
from github import Github


CHROMA_DB_HOST = os.environ.get("CHROMA_DB_HOST")
CHROMA_DB_PORT = os.environ.get("CHROMA_DB_PORT")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


BASE_URL = "https://raw.githubusercontent.com/nx-academy/nx-academy.github.io/refs/heads/main/src/pages/cours"


def clean_md_for_rag(content):
    # Removing YAML's Front Matter
    content = re.sub(r"^---.*?---\s*", "", content, flags=re.DOTALL)

    # Removing HTML tags (article, br, img, etc.)
    content = re.sub(r"<(br|/?article|img[^>]*)>", "", content)

    # Removing Markdown images
    content = re.sub(r"!\[.*?\]\(.*?\)", "", content)

    # Removing multiple empty lines
    content = re.sub(r"\n{2,}", "\n\n", content)

    # Removing trailing spaces
    content = re.sub(r"[ \t]+$", "", content, flags=re.MULTILINE)

    return content.strip()


def main():
    sample_url = f"{BASE_URL}/docker-et-docker-compose/chapitres/decouverte-docker.md"
    
    response = requests.get(sample_url)
    if response.status_code == 200:
        with open("decouverte-docker.md", "w", encoding="utf-8") as file:
            file.write(clean_md_for_rag(response.text))
            
        print(f"✅ File saved and downloaded as : {"decouverte-docker"}")
        
    else:
        print(f"❌ Error when downloading the file ({response.status_code}) : {sample_url}")
    

if __name__ == "__main__":
    # main()
    
    chroma_client = chromadb.HttpClient(host=CHROMA_DB_HOST, port=CHROMA_DB_PORT)
    print(chroma_client.heartbeat())
