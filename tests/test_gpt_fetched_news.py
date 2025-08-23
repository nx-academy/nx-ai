import sys
import os
import json


# Fix to make test work with import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from nx_ai.openai_service.gpt_models import GPTFetchedNews, FakeResponse


def test_gpt_fetched_news():
    with open("mock/fetched_news_gpt.json", mode="r", encoding="utf-8") as f:
        mock = json.load(f)
        gpt_fetched_news = GPTFetchedNews(
            FakeResponse(json.dumps(mock), use_tool=True)
        )
        
        assert len(gpt_fetched_news.data["data"]) == 3
        
        first_mocked_news = gpt_fetched_news.data["data"][0]
        assert "Lancement de GPT-5" in first_mocked_news["title"]
        
        third_mocked_news = gpt_fetched_news.data["data"][2]
        assert "mais certains enseignants pointent une complexité croissante" in third_mocked_news["content"]
