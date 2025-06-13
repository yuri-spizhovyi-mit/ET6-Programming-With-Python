# scraping.py
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def get_article_links(base_url, max_links=5):
    """Scrape article links from BetterDwelling tag page"""
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Log all links found
    all_links = soup.find_all("a")
    print(f"🔎 Found {len(all_links)} total <a> tags")

    # Try common blog structure
    article_links = []
    for link in all_links:
        href = link.get("href")
        text = link.text.strip().lower()
        if href and "/202" in href and "housing" in text or "real estate" in text:
            article_links.append(href)
        if len(article_links) >= max_links:
            break

    print(f"✅ Filtered to {len(article_links)} housing-related article links")
    return article_links


def extract_article_data_bs(url):
    """Extract title and article text from a BetterDwelling article."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string.strip() if soup.title else "No Title"
        paragraphs = soup.find_all("p")
        content = "\n".join([p.get_text() for p in paragraphs if p.get_text().strip()])

        return {"url": url, "title": title, "content": content}

    except Exception as e:
        print(f"[ERROR] Failed to fetch {url}: {e}")
        return None


def collect_betterdwelling_articles(max_links=5):
    base_url = "https://betterdwelling.com/tag/canadian-real-estate/"
    article_links = get_article_links(base_url, max_links=max_links)

    print(f"🔍 Found {len(article_links)} article links")
    articles = []
    for url in article_links:
        print(f"📄 Scraping: {url}")
        article = extract_article_data_bs(url)
        if article:
            articles.append(article)
        time.sleep(1)  # Be nice to the server

    return pd.DataFrame(articles)
