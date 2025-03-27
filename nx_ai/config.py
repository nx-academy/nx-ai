import os


def get_config():
    GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

    if GITHUB_TOKEN is None:
        raise ValueError("Missing GITHUB_TOKEN env variable")
    
    if OPENAI_API_KEY is None:
        raise ValueError("Missing OPENAI_API_KEY env variable")
    
    return {
        "github_token": GITHUB_TOKEN,
        "openai_api_key": OPENAI_API_KEY
    }

