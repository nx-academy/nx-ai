import sys
import os
import json

# Fix to make test work with import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from nx_ai.gpt_models import GPTGeneratedQuiz


class FakeResponse:
    def __init__(self, text):
        self.output = [None, FakeOutput(text)]


class FakeOutput:
    def __init__(self, text):
        self.content = [FakeText(text)]


class FakeText:
    def __init__(self, text):
        self.text = text


def test_quiz_parsing():
    raw_json = {
        "data": [
            {
                "question": "Qu'est-ce qu'un registry Docker ?",
                "options": [
                    "Un outil de gestion des conteneurs Docker",
                    "Un service de stockage et de distribution d'images Docker",
                    "Un environnement d'exécution pour les applications Docker",
                    "Un langage de programmation utilisé avec Docker"
                ],
                "answer": "Un service de stockage et de distribution d'images Docker",
                "explanation": "Un registry Docker est un service conçu pour stocker, versionner et distribuer des images Docker, similaire à GitHub pour le code source."
            },
            {
                "question": "Quel est le registry Docker par défaut ?",
                "options": [
                    "GitHub Container Registry",
                    "GitLab Container Registry",
                    "Docker Hub",
                    "Amazon ECR"
                ],
                "answer": "Docker Hub",
                "explanation": "Docker Hub est le registry Docker par défaut, utilisé pour stocker et partager des images Docker publiquement ou en privé."
            }
        ]
    }
    
    # Fake GPT Response Object
    response = FakeResponse(json.dumps(raw_json))
    quiz = GPTGeneratedQuiz(response)
    
    assert len(quiz.data) == 2
    assert quiz.data[0]["question"] == "Qu'est-ce qu'un registry Docker ?"
    assert quiz.data[1]["answer"] == "Docker Hub"
    