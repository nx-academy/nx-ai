import requests
from readability import Document
from bs4 import BeautifulSoup


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
    
    lines = [line.strip() for line in text.splitlines()]
    lines = [line for line in lines if line]  # supprimer les lignes vides
    body = "\n\n".join(lines)
    
    with open(f"nx_ai/articles_data/{filename}", "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n{body}")
        
    print(f"✅ Sauvegardé dans : {filename}\n")
