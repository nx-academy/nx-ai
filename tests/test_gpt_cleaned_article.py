import sys
import os

# Fix to make test work with import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from nx_ai.openai_service.gpt_models import GPTCleanedArticle, FakeResponse


def test_gpt_cleaned_article():
    with open("mock/cleaned_article.txt", "r") as f:
        mock = f.read()
        gpt_cleaned_article = GPTCleanedArticle(FakeResponse(mock, use_tool=True))
        
        assert len(gpt_cleaned_article.text) > 100
        assert "Les images Docker sont nommées et taguées" in gpt_cleaned_article.text
        assert "Il est également possible d'héberger son propre" in gpt_cleaned_article.text
