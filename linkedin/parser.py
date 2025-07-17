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

    name = extract_text(soup.find("h1"))
    position_el = soup.select_one("div.text-body-medium.break-words")
    position = extract_text(position_el)

    location_el = soup.select_one(
        "span.text-body-small.inline.t-black--light.break-words"
    )
    location = extract_text(location_el)

    # Experience
    exp_section = soup.find("span", string=re.compile("Experience", re.I))
    if exp_section:
        exp_container = exp_section.find_parent("section") or exp_section.find_parent()
        exp_html = exp_container.decode() if exp_container else ""
        experience_1 = extract_from_spans(
            exp_html, r'aria-hidden="true"><!---->(.*?)<!---->'
        )
        company_1 = extract_from_spans(
            exp_html, r'·\s*Full-time|aria-hidden="true"><!---->(.*?)<!---->'
        )
        dates = re.findall(r"(\w+\s+\d{4})", exp_html)
        date_1_start = dates[0] if dates else "N/A"
        date_1_end = dates[1] if len(dates) > 1 else "Present"
    else:
        experience_1 = company_1 = date_1_start = date_1_end = "N/A"

    # Education
    edu_section = soup.find("span", string=re.compile("Education", re.I))
    if edu_section:
        edu_container = edu_section.find_parent("section") or edu_section.find_parent()
        edu_html = edu_container.decode() if edu_container else ""
        education_1 = extract_from_spans(
            edu_html, r't-bold">.*?><span.*?><!---->(.*?)<!---->'
        )
        degree_field = re.findall(r'aria-hidden="true"><!---->(.*?)<!---->', edu_html)
        degree = degree_field[0].split(",")[0] if degree_field else "N/A"
        field = (
            degree_field[0].split(",")[1].strip()
            if degree_field and "," in degree_field[0]
            else "N/A"
        )
        years = re.findall(r"(\d{4})\s*-\s*(\d{4})", edu_html)
        education_start = years[0][0] if years else "N/A"
        education_end = years[0][1] if years else "N/A"
    else:
        education_1 = degree = field = education_start = education_end = "N/A"

    profile_data.append(
        {
            "linkedin_url": "N/A",  # Placeholder since file has no URL
            "scrape_id": str(uuid.uuid4()),
            "last_scrape": datetime.today().strftime("%Y-%m-%d"),
            "Name": name,
            "Position": position,
            "Location": location,
            "Experience_1": experience_1,
            "Company_1": company_1,
            "Date_1_start": date_1_start,
            "Date_1_end": date_1_end,
            "Education_1": education_1,
            "Degree": degree,
            "Field": field,
            "Education_Start": education_start,
            "Education_End": education_end,
        }
    )

# Append to existing DataFrame and save
df_new = pd.DataFrame(profile_data)
df_combined = pd.concat([df_existing, df_new], ignore_index=True)
df_combined.to_csv(output_csv, index=False)

import ace_tools as tools

tools.display_dataframe_to_user(name="Parsed LinkedIn Data", dataframe=df_new)
