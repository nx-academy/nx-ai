import sys
import os
import json

# Fix to make test work with import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from nx_ai.openai_service.gpt_models import GPTSummarizedArticle, FakeResponse


def test_gpt_summarized_article():
    with open("mock/summarized_article.json", "r") as f:
        mock = json.load(f)
        gpt_summarized_article = GPTSummarizedArticle(FakeResponse(json.dumps(mock), use_tool=True))
    
        assert gpt_summarized_article.data["author"] == "nx.academy"
        assert gpt_summarized_article.data["title_fr"] == "Présentation du registre Docker"
        assert "il aborde la sécurisation et la gestion des images" in gpt_summarized_article.data["article_summary"]
