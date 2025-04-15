import requests
import os
from github import Github, Auth

from nx_ai.utils import clean_md_for_rag
from nx_ai.config import get_config


BASE_URL = "https://raw.githubusercontent.com/nx-academy/nx-academy.github.io/refs/heads/main/src/pages/cours"


auth = Auth.Token(get_config()["github_token"])


def create_course_folder():
    if not os.path.exists("nx_ai/courses_data"):
        os.makedirs("nx_ai/courses_data")


def fetch_chapter_from_github():
    sample_url = f"{BASE_URL}/docker-et-docker-compose/chapitres/decouverte-docker.md"
    
    response = requests.get(sample_url)
    
    if response.status_code == 200:
        create_course_folder()
        
        with open("nx_ai/courses_data/decouverte-docker.md", "w", encoding="utf-8") as file:
            file.write(clean_md_for_rag(response.text))


def create_pull_request_on_github():
    g = Github(auth=auth)
    
    repo = g.get_organization("nx-academy").get_repo("nx-academy.github.io")
    
    sb = repo.get_branch("main")
    repo.create_git_ref(ref=f"refs/heads/{"test-quiz"}", sha=sb.commit.sha)
    
    print(f"Successfully created branch test-quiz")
    
    
    with open("nx_ai/quiz_data/test.json", "r", encoding="utf-8") as f:
        content = f.read()
    
    repo.create_file(
        path="src/data/test.json",
        message="Ajout du quiz de test",
        content=content,
        branch="test-quiz"
    )
    
    print(f"Successfully commit test.json file")
    
    repo.create_pull(
        base="main",
        title="J'essaye d'ouvrir ma PR avec un fichier",
        body="Un test d'ouverture automatisé avec un fichier et une branche de base",
        head="test-quiz"
    )
    
    print(f"Successfully create the PR")
    
    g.close()
