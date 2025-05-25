# run_scraper.py

import pandas as pd
from scraping import collect_betterdwelling_articles


def main():
    print("📡 Starting BetterDwelling article scraping...")

    # You can change this number to fetch more articles
    max_links = 10

    df = collect_betterdwelling_articles(max_links=max_links)

    if not df.empty:
        output_path = "../data/raw/betterdwelling_articles.csv"
        df.to_csv(output_path, index=False)
        print(f"✅ Done! Articles saved to {output_path}")
    else:
        print("⚠️ No articles were scraped.")


if __name__ == "__main__":
    main()
