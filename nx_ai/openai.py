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


def create_document_with_chroma(file_location, document_name):
    try:
        with open(f"{file_location}", "r", encoding="utf-8") as file:
            file = file.read()
            
            engine = configure_engine()
            db = engine["db"]
                    
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=500,
                chunk_overlap=100,
                separators=["\n### ", "\n## ", "\n# ", "\n\n", "\n", ".", " "]
            )
            
            chunks = splitter.split_text(file)
            documents = [Document(page_content=chunk, metadata={"content": document_name}) for chunk in chunks]

            db.add_documents(documents)
            
    except FileNotFoundError:
        print(f"Unable to find the location {file_location} for the file named: {document_name}")
        

def generate_quiz_from_gpt():
    engine = configure_engine()
    db = engine["db"]
    llm = engine["llm"]

    results = db.get(where={"chapter": "decouverte-docker"})
    full_context = "\n\n".join(results["documents"])

    all_questions = []
    for i in range(3):
        print(f"📦 Generating questions bloc: {i + 1} / 5...")


        prompt = f"""
        Tu es un générateur de quiz pédagogique.

        À partir du contenu suivant, génère **1** question à choix multiples. 
        
        Chaque question doit avoir 4 propositions, dont une seule correcte et une explication pour la réponse correcte. L’explication ne doit pas dépasser 1 à 2 phrases.

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
            parsed = json.loads(response)
            if "data" in parsed and isinstance(parsed["data"], list):
                all_questions.extend(parsed["data"])
                print(f"✅ Bloc {i + 1} received.")
            else:
                print(f"⚠️ Bloc {i + 1} :unattended format")
        except:
            print(f"❌ Bloc {i + 1} :issues with JSON format. Failed to update all_questions list")
            print(response)
        
    
    full_quiz = { "data": all_questions }
    with open("nx_ai/quizzes_data/decouverte-docker.json", "w", encoding="utf-8") as file:
        json.dump(full_quiz, file, indent=4, ensure_ascii=False)

    print(f"\n✅ Quiz has been generated with ({len(all_questions)} questions)")
