import requests
import re
import os

from github import Github, Auth

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

from chromadb.config import Settings


CHROMA_DB_HOST = os.environ.get("CHROMA_DB_HOST")
CHROMA_DB_PORT = os.environ.get("CHROMA_DB_PORT")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


BASE_URL = "https://raw.githubusercontent.com/nx-academy/nx-academy.github.io/refs/heads/main/src/pages/cours"

# GitHub Config
auth = Auth.Token(GITHUB_TOKEN)

# OpenAI Config
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key=OPENAI_API_KEY)
llm = ChatOpenAI(model="gpt-4", temperature=0.7, openai_api_key=OPENAI_API_KEY)

# Chroma Config
db = Chroma(
    collection_name="my_first_quiz",
    embedding_function=embeddings,
    persist_directory="./chroma_store"
)


def create_quiz():
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 4})

    docs = retriever.get_relevant_documents("Génère un quiz sur ce chapitre")
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
    Tu es un générateur de quiz pédagogique.

    À partir du contenu suivant, génère 3 questions à choix multiples. 
    Chaque question doit avoir 4 propositions, dont une seule correcte. 

    Réponds au format JSON comme ceci :

    [
    {{
        "question": "...",
        "options": ["..."],
        "answer": "..."
    }}
    ]

    Voici le contenu :
    {context}
    """

    response = llm.predict(prompt)

    print(response)


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


def fetch_chapter():
    sample_url = f"{BASE_URL}/docker-et-docker-compose/chapitres/decouverte-docker.md"
    
    response = requests.get(sample_url)
    if response.status_code == 200:
        
        
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
            separators=["\n\n", "\n", ".", " "]
        )
        
        chunks = splitter.split_text(response.text)
        documents = [Document(page_content=chunk, metadata={}) for chunk in chunks]
        
        db.add_documents(documents)
        
        print(db._collection.count())
        
        
        # with open("decouverte-docker.md", "w", encoding="utf-8") as file:
        #     file.write(clean_md_for_rag(response.text))
            
        print(f"✅ File saved and downloaded as : {"decouverte-docker"}")
        
    else:
        print(f"❌ Error when downloading the file ({response.status_code}) : {sample_url}")



def main():
    print("====")
    print("====")
    print("====")


if __name__ == "__main__":
    main()
