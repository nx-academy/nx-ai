import os
from github import Github, Auth

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")


def create_pull_request_on_github(document_name: str):
    print("++++")
    print(document_name)
    print("++++")
