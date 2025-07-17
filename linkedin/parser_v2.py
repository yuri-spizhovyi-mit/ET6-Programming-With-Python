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

    # Experience Section
    experience_1 = company_1 = date_1_start = date_1_end = "N/A"
    exp_header = soup.find("h2", class_="pvs-header__title")
    if exp_header and "Experience" in exp_header.text:
        exp_card = exp_header.find_parent().find_next(
            "div", class_="display-flex flex-column align-self-center flex-grow-1"
        )
        if exp_card:
            job_title = exp_card.select_one("div.t-bold span[aria-hidden='true']")
            experience_1 = extract_text(job_title)

            company = exp_card.select_one("span.t-14.t-normal span[aria-hidden='true']")
            if company:
                company_1 = re.sub(r"·.*", "", extract_text(company)).strip()

            date_match = exp_card.select(
                "span.t-14.t-normal.t-black--light span[aria-hidden='true']"
            )
            if len(date_match) >= 1:
                dates = re.findall(r"([A-Za-z]+ \\d{4})", date_match[0].text)
                if dates:
                    date_1_start = dates[0]
                    date_1_end = dates[1] if len(dates) > 1 else "Present"

    # Education Section
    education_1 = degree = field = education_start = education_end = "N/A"
    edu_header = soup.find("h2", class_="pvs-header__title")
    if edu_header and "Education" in edu_header.text:
        edu_card = edu_header.find_parent().find_next(
            "div", class_="display-flex flex-column align-self-center flex-grow-1"
        )
        if edu_card:
            school = edu_card.select_one("div.t-bold span[aria-hidden='true']")
            education_1 = extract_text(school)

            degree_field_el = edu_card.select_one(
                "span.t-14.t-normal span[aria-hidden='true']"
            )
            if degree_field_el:
                degree_field_text = extract_text(degree_field_el)
                if "," in degree_field_text:
                    degree, field = [x.strip() for x in degree_field_text.split(",", 1)]
                else:
                    degree = degree_field_text

            year_span = edu_card.select_one(
                "span.pvs-entity__caption-wrapper span[aria-hidden='true']"
            )
            if year_span:
                years = re.findall(r"(\\d{4})\\s*-\\s*(\\d{4})", year_span.text)
                if years:
                    education_start, education_end = years[0]

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
