import asyncio
import os

from libsql_client import create_client, Client


def _create_db_client() -> Client:
    turso_url = os.environ.get("TURSO_URL")
    turso_token = os.environ.get("TURSO_TOKEN")
    
    if turso_url is None or turso_token is None:
        raise ValueError("Please enter a valid turso url and/or a valid turso app token")
    
    return create_client(url=turso_url, auth_token=turso_token)


async def insert_news_in_db():
    client = _create_db_client()
    
    await client.execute(
        """
        INSERT INTO NewsFeed (title, content, slug, url, published)
        VALUES (?, ?, ?, ?, ?)
        """,
        [
            "Titre depuis ma CLI",
            "Contenu depuis ma CLI",
            "titre-depuis-cli",
            "https://nx.academy",
            "2025-08-21T19:00:00Z"
        ]
    )
    print("✅ News added in NewsFeed Table")
