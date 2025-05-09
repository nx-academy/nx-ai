import requests
from readability import Document
from bs4 import BeautifulSoup
from pathlib import Path


def scrape_article_from_internet(url, filename):
    print(f"📥 Récupération de : {url}")
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"❌ Échec du téléchargement ({response.status_code})")
        return
    
    doc = Document(response.text)
    title = doc.title()
    clean_html = doc.summary()
    
    soup = BeautifulSoup(clean_html, "html.parser")
    text = soup.get_text(separator="\n")
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n{text}")
        
    print(f"✅ Sauvegardé dans : {filename}\n")
