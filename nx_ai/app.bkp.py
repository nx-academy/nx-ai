
import os

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA




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
