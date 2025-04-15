from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.schema import Document

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
    engine = configure_engine()
    db = engine["db"]

    with open("nx_ai/courses_data/decouverte-docker.md", "r", encoding="utf-8") as file:
        file = file.read()
        
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
            separators=["\n### ", "\n## ", "\n# ", "\n\n", "\n", ".", " "]
        )
        
        chunks = splitter.split_text(file)
        documents = [Document(page_content=chunk, metadata={"chapter": "decouverte-docker"}) for chunk in chunks]

        db.add_documents(documents)

        print("======")
        print(db._collection.count())
        print("======")
        

def get_embedded_documents():
    engine = configure_engine()
    db = engine["db"]

    results = db.get(where={"chapter": "decouverte-docker"})
    full_context = "\n\n".join(results["documents"])

    print("====")
    print(full_context)
    print("====")
