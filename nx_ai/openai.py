from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain_community.vectorstores import Chroma

from nx_ai.config import get_config

openai_api_key = get_config()["openai_api_key"]


def configure_engine():
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key=openai_api_key)
    llm = ChatOpenAI(model="gpt-4", temperature=0.7, openai_api_key=openai_api_key)
    
    db = Chroma(
        collection_name="my_first_quiz",
        embedding_function=embeddings,
        persist_directory="./chroma_store"
    )
    
    return {
        "embeddings": embeddings,
        "llm": llm,
        "db": db
    }


def write_embedded_document():
    print("====")
    print("====")
    print("====")

