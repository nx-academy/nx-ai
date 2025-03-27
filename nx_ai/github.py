import requests


BASE_URL = "https://raw.githubusercontent.com/nx-academy/nx-academy.github.io/refs/heads/main/src/pages/cours"


def fetch_chapter_from_github():
    sample_url = f"{BASE_URL}/docker-et-docker-compose/chapitres/decouverte-docker.md"
    
    response = requests.get(sample_url)
    
    if response.status_code == 200:
        with open("nx_ai/courses_data/decouverte-docker.md", "w", encoding="utf-8") as file:
            file.write(response.text)
