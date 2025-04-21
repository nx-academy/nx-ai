import requests
from pathlib import Path


def scrape_medium_article():
    test_url = "https://tdimnet.medium.com/the-monk-the-vape-coder-the-debugger-the-learner-24557b2dd8a5"

    output_dir = Path("nx_ai/recap_data/2025-04")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "01-medium.txt"

    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(test_url, headers=headers)
    html = response.text

    print("====")
    print(html)
    print("====")
