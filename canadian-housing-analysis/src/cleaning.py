# cleaning.py

import pandas as pd
import re


def clean_article_text(text):
    """Cleans boilerplate and extra whitespace from article content."""
    # Remove newsletter or repeated site footers
    text = re.sub(
        r"Sign up for our.*?newsletter", "", text, flags=re.IGNORECASE | re.DOTALL
    )
    text = re.sub(r"Read More.*?\n", "", text, flags=re.IGNORECASE)

    # Normalize whitespace and newlines
    text = re.sub(r"\n+", "\n", text)
    text = re.sub(r"\s{2,}", " ", text)

    return text.strip()


def apply_cleaning(df):
    """Apply text cleaning to a DataFrame of articles."""
    df["cleaned_content"] = df["content"].apply(clean_article_text)
    return df
