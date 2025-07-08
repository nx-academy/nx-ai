import requests
from readability import Document
from bs4 import BeautifulSoup


def scrape_website(url: str):
    print("====")
    print(url)
    print("====")
