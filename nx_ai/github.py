import requests
from github import Github, Auth

from nx_ai.utils import clean_md_for_rag
from nx_ai.config import get_config


BASE_URL = "https://raw.githubusercontent.com/nx-academy/nx-academy.github.io/refs/heads/main/src/pages/cours"


auth = Auth.Token(get_config()["github_token"])


def fetch_chapter_from_github():
    sample_url = f"{BASE_URL}/docker-et-docker-compose/chapitres/decouverte-docker.md"
    
    response = requests.get(sample_url)
    
    if response.status_code == 200:
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
