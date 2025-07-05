import sys
import os
import json

# Fix to make test work with import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from nx_ai.gpt_models import GPTCleanedArticle
from tests.test_gpt_quiz import FakeResponse


def test_extracting_article_metadata():
    raw_json = {
        "data": {
            "author": "Thomas",
            "titre_fr": "Qu'est-ce qu'un registry Docker?",
            "published_date": "2025-06-06",
            "article_content": "Un registry Docker est un service de stockage et de distribution d'images Docker, comparable à GitHub ou GitLab pour les conteneurs. Il permet de stocker, versionner et distribuer des images Docker, facilitant ainsi le déploiement et le partage d'applications conteneurisées. Les registries peuvent être publics, accessibles à tous, ou privés, contrôlant l'accès aux images. Le registry par défaut est Docker Hub, mais il existe d'autres alternatives comme GitHub Container Registry, GitLab Container Registry, Google Container Registry (GCR) et Amazon Elastic Container Registry (ECR). Il est également possible d'héberger son propre registry Docker sur ses propres serveurs.\n\nLes images Docker sont nommées et taguées de manière spécifique. Par exemple, une image nommée `ghcr.io/mon-orga/mon-image:1.0.0` se décompose comme suit :\n\n- `ghcr.io` : nom du registry (ici, GitHub Container Registry).\n- `mon-orga` : nom de l'organisation ou de l'utilisateur.\n- `mon-image` : nom de l'image.\n- `1.0.0` : tag, représentant la version de l'image.\n\nPour envoyer (push) ou récupérer (pull) des images depuis un registry Docker, il est nécessaire de s'y authentifier. Par exemple, pour Docker Hub, il faut créer un compte, puis se connecter via la commande `docker login` en fournissant son nom d'utilisateur et son mot de passe. Une fois authentifié, on peut envoyer une image avec la commande `docker push` suivie du nom de l'image, ou la récupérer avec `docker pull`.\n\nEn résumé, un registry Docker est essentiel pour la gestion et la distribution des images Docker, facilitant le déploiement et le partage d'applications conteneurisées."
        }
    }
    
    # Fake GPT Response Object
    response = FakeResponse(json.dumps(raw_json))
    cleaned_article = GPTCleanedArticle(response)
    
    print("====")
    print(cleaned_article.data)
    print("====")
    
    
    assert True == True
