# Re-import required libraries after code execution state reset
from bs4 import BeautifulSoup
import pandas as pd
import os
import re
import uuid
from datetime import datetime


# Folder with LinkedIn profile HTML files (redefined path after reset)
html_dir = (
    "C:/Users/yspizhoviy/ET6-Programming-With-Python/linkedin/linkedin_html_profiles"
)
output_csv = "C:/Users/yspizhoviy/ET6-Programming-With-Python/linkedin/linkedin_raw_hidden_content.csv"

# Ensure the output CSV exists
if os.path.exists(output_csv):
    df_existing = pd.read_csv(output_csv)
else:
    df_existing = pd.DataFrame()


# Helper functions to extract specific fields
def extract_text(tag):
    if tag:
        return tag.get_text(strip=True)
    return "N/A"


def extract_from_spans(html, pattern):
    matches = re.findall(pattern, html)
    return matches[0].strip() if matches else "N/A"


# Extract detailed education and experience information from raw matches
def extract_education_details(matches):
    school = degree = field = start = end = "N/A"
    for text in matches:
        lower = text.lower()
        if any(k in lower for k in ["university", "college", "institute"]):
            school = text
        elif "degree" in lower or "bachelor" in lower or "master" in lower:
            degree = text
        elif any(
            k in lower
            for k in [
                "science",
                "engineering",
                "computer",
                "networking",
                "telecommunications",
            ]
        ):
            field = text
        elif re.match(r"^\d{4}\s*-\s*\d{4}$", text) or re.match(r"^\d{4}$", text):
            years = re.findall(r"\d{4}", text)
            if len(years) == 2:
                start, end = years
            elif len(years) == 1:
                start = years[0]
    return school, degree, field, start, end


def extract_experience_details(matches):
    position = company = start = end = "N/A"
    date_pattern = r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\s+\d{4}"
    date_range_pattern = re.compile(f"{date_pattern}\s*-\s*(Present|{date_pattern})")

    for i, text in enumerate(matches):
        if re.search(r"\bEngineer\b|\bDeveloper\b|\bManager\b|\bAnalyst\b", text):
            position = text
        elif "full-time" in text.lower():
            company = matches[i - 1] if i > 0 else "N/A"
        elif date_range_pattern.match(text):
            dates = re.findall(
                r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\s+\d{4}", text
            )
            if len(dates) >= 1:
                start = dates[0]
            if len(dates) == 2:
                end = dates[1]
            elif "present" in text.lower():
                end = "Present"
    return position, company, start, end


# Container for all parsed profile data
profile_data = []

# Parse each HTML file
for filename in os.listdir(html_dir):
    if not filename.endswith(".html"):
        continue

    file_path = os.path.join(html_dir, filename)
    with open(file_path, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    html = soup.prettify()
    matches = re.findall(r"<!---->(.*?)<!---->", html)

    name = extract_text(soup.find("h1"))
    position_el = soup.select_one("div.text-body-medium.break-words")
    position = extract_text(position_el)

    location_el = soup.select_one(
        "span.text-body-small.inline.t-black--light.break-words"
    )
    location = extract_text(location_el)

    # Extracted fields
    edu_school, edu_degree, edu_field, edu_start, edu_end = extract_education_details(
        matches
    )
    exp_position, exp_company, exp_start, exp_end = extract_experience_details(matches)

    profile_data.append(
        {
            "linkedin_url": "N/A",  # Placeholder since file has no URL
            "scrape_id": str(uuid.uuid4()),
            "last_scrape": datetime.today().strftime("%Y-%m-%d"),
            "Name": name,
            "Position": position,
            "Location": location,
            "Experience_1": exp_position,
            "Company_1": exp_company,
            "Date_1_start": exp_start,
            "Date_1_end": exp_end,
            "Education_1": edu_school,
            "Degree": edu_degree,
            "Field": edu_field,
            "Education_Start": edu_start,
            "Education_End": edu_end,
        }
    )

# Append to existing DataFrame and save
df_new = pd.DataFrame(profile_data)
df_combined = pd.concat([df_existing, df_new], ignore_index=True)
df_combined.to_csv(output_csv, index=False)


print(df_new)  # Simple output

# Or if you want to open in Excel or save locally:
df_new.to_csv("parsed_linkedin_output.csv", index=False)
