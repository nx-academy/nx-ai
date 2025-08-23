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
        news_items = gpt_fetched_news.data["data"]
        
        assert len(news_items) == 3

        for item in news_items:
            assert "title" in item
            assert "content" in item
            assert "url" in item
            assert item["url"].startswith("http")

        assert "Lancement de GPT-5" in news_items[0]["title"]
        assert "mais certains enseignants pointent une complexité croissante" in news_items[2]["content"]
