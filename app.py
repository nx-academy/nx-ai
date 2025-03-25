import requests
import re
import chromadb
import os
from github import Github, Auth
from langchain.text_splitter import RecursiveCharacterTextSplitter


CHROMA_DB_HOST = os.environ.get("CHROMA_DB_HOST")
CHROMA_DB_PORT = os.environ.get("CHROMA_DB_PORT")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


BASE_URL = "https://raw.githubusercontent.com/nx-academy/nx-academy.github.io/refs/heads/main/src/pages/cours"


auth = Auth.Token(GITHUB_TOKEN)


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


def open_pr():
    g = Github(auth=auth)
    
    repo = g.get_organization("nx-academy").get_repo("nx-academy.github.io")
    repo.create_pull(
        base="main",
        title="J'essaye d'ouvrir une PR",
        body="Un test d'ouverture de PR automatisé",
        head="content_math-data-science"
    )
        
    g.close()


def split_text_into_chuncks(content, chunk_size=500, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", " "]
    )
    
    return splitter.split_text(content)


def main():
    sample_url = f"{BASE_URL}/docker-et-docker-compose/chapitres/decouverte-docker.md"
    
    response = requests.get(sample_url)
    if response.status_code == 200:
        content = clean_md_for_rag(response.text)
        chunks = split_text_into_chuncks(content)
        
        print(chunks)
        
        # with open("decouverte-docker.md", "w", encoding="utf-8") as file:
        #     file.write(clean_md_for_rag(response.text))
            
        print(f"✅ File saved and downloaded as : {"decouverte-docker"}")
        
    else:
        print(f"❌ Error when downloading the file ({response.status_code}) : {sample_url}")
    

if __name__ == "__main__":
    main()
    
    # chroma_client = chromadb.HttpClient(host=CHROMA_DB_HOST, port=CHROMA_DB_PORT)
    # print(chroma_client.heartbeat())
