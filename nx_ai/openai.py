import json

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
        

def generate_quiz_from_gpt():
    engine = configure_engine()
    db = engine["db"]
    llm = engine["llm"]

    results = db.get(where={"chapter": "decouverte-docker"})
    full_context = "\n\n".join(results["documents"])

    prompt = f"""
    Tu es un générateur de quiz pédagogique.

    À partir du contenu suivant, génère 10 question à choix multiples. 
    Chaque question doit avoir 4 propositions, dont une seule correcte et une explication pour la réponse correcte.

    Garde le même ton que l'auteur du texte pour la réalisation du quiz.

    Réponds au format JSON comme ceci :

    {{
      "data": [
        {{
          "question": "...",
          "options": ["...", "...", "...", "..."],
          "answer": "...",
          "explanation": "..."
        }}
      ]
    }}

    Voici le contenu :
    {full_context}
    """

    response = llm.predict(prompt)

    try:
        quiz = json.loads(response)
        with open("nx_ai/quizzes_data/decouverte-docker.json", "w", encoding="utf-8") as file:
            json.dump(quiz, file, indent=4, ensure_ascii=False)
            print("✅ The Quiz has been saved!")

    except json.JSONDecodeError:
        print("❌ Failing to decode quiz JSON file")
        print(response)
