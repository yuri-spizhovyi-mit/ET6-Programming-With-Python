import asyncio
import pandas as pd
import re
import uuid
import os
from datetime import datetime
from playwright.async_api import async_playwright

OUTPUT_CSV = "linkedin_raw_hidden_content.csv"
SEARCH_URL = "https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103644278%22%5D&keywords=data%20scientist&origin=FACETED_SEARCH"
NUM_PAGES = 1


def extract_text_from_html(html):
    return " | ".join(re.findall(r"<!---->(.*?)<!---->", html))


async def extract_experience(profile):
    try:
        exp_locator = profile.locator("span:has-text('Experience')").first
        section = await exp_locator.evaluate_handle("node => node.closest('section')")
        if not section:
            return {}, False

        html = await section.inner_html()
        # Find first experience block inside this section
        title = re.findall(r"aria-hidden=\"true\"><!---->(.*?)<!---->", html)
        company = re.findall(
            r"experience_company_logo.*?href=.*?><.*?><.*?><.*?><.*?><.*?><.*?>(.*?)<!---->",
            html,
            re.DOTALL,
        )
        dates = re.findall(r"\d{4}.*?Present|\d{4}", html)
        location = re.findall(r"\d{4}.*?<.*?>(.*?)<!---->", html)

        return {
            "Experience_1": title[0].strip() if title else "N/A",
            "Company_1": re.sub(r"·.*", "", company[0]).strip() if company else "N/A",
            "Date_1_start": dates[0] if dates else "N/A",
            "Date_1_end": dates[1] if len(dates) > 1 else "Present",
        }, True
    except:
        return {}, False


async def extract_education(profile):
    try:
        edu_locator = profile.locator("span:has-text('Education')").first
        section = await edu_locator.evaluate_handle("node => node.closest('section')")
        if not section:
            return {}, False

        html = await section.inner_html()
        school = re.findall(r"t-bold.*?><span.*?><!---->(.*?)<!---->", html)
        degree = re.findall(r"t-14 t-normal.*?><span.*?><!---->(.*?)<!---->", html)
        dates = re.findall(
            r"pvs-entity__caption-wrapper.*?><!---->(\d{4}) - (\d{4})<!---->", html
        )

        return {
            "Education_1": school[0].strip() if school else "N/A",
            "Degree": degree[0].split(",")[0].strip() if degree else "N/A",
            "Field": degree[0].split(",")[1].strip() if "," in degree[0] else "N/A",
            "Education_Start": dates[0][0] if dates else "N/A",
            "Education_End": dates[0][1] if dates else "N/A",
        }, True
    except:
        return {}, False


async def run():
    if os.path.exists(OUTPUT_CSV):
        df = pd.read_csv(OUTPUT_CSV)
    else:
        df = pd.DataFrame()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Manual login
        await page.goto("https://www.linkedin.com/login")
        print("🔐 Log in manually in the opened browser...")
        while True:
            if "feed" in page.url or "search/results" in page.url:
                break
            await asyncio.sleep(1)
        input("✅ Login complete. Press ENTER to start scraping...")

        await page.goto(SEARCH_URL, wait_until="domcontentloaded")

        for page_num in range(NUM_PAGES):
            print(f"\n🌍 Scraping search result page {page_num + 1}")
            await page.mouse.wheel(0, 5000)
            await page.wait_for_timeout(3000)

            profile_elements = await page.locator("a[href*='/in/']").all()
            profile_urls = list(
                {
                    await el.get_attribute("href")
                    for el in profile_elements
                    if await el.get_attribute("href")
                }
            )

            for url in profile_urls:
                print(f"➡️ Visiting profile: {url}")
                profile = await context.new_page()
                try:
                    await profile.goto(url, timeout=60000)
                    await profile.wait_for_timeout(3000)
                    await profile.wait_for_selector("h1", timeout=8000)

                    for _ in range(3):
                        await profile.mouse.wheel(0, 3000)
                        await profile.wait_for_timeout(1000)

                    name = await profile.locator("h1").first.text_content()
                    name = name.strip() if name else "N/A"

                    title_el = await profile.locator(
                        "div.text-body-medium.break-words"
                    ).first.text_content()
                    position = title_el.strip() if title_el else "N/A"

                    location_el = await profile.locator(
                        "span.text-body-small.inline.t-black--light.break-words"
                    ).first.text_content()
                    location = location_el.strip() if location_el else "N/A"

                    exp_data, _ = await extract_experience(profile)
                    edu_data, _ = await extract_education(profile)

                    df.loc[len(df)] = {
                        "linkedin_url": url,
                        "scrape_id": str(uuid.uuid4()),
                        "last_scrape": datetime.today().strftime("%Y-%m-%d"),
                        "Name": name,
                        "Position": position,
                        "Location": location,
                        **exp_data,
                        **edu_data,
                    }

                except Exception as e:
                    print(f"❌ Failed to scrape profile: {e}")
                finally:
                    await profile.close()

            try:
                next_button = page.locator(
                    "button.artdeco-pagination__button--next[aria-label='Next']"
                )
                if await next_button.is_visible() and await next_button.is_enabled():
                    await next_button.click()
                    await page.wait_for_load_state("domcontentloaded")
                    await page.wait_for_timeout(3000)
                else:
                    print("⚠️ No more pages.")
                    break
            except Exception as e:
                print(f"⚠️ Error navigating: {e}")
                break

        await browser.close()
        df.to_csv(OUTPUT_CSV, index=False)
        print(f"\n✅ Done! Appended data to {OUTPUT_CSV}")


if __name__ == "__main__":
    asyncio.run(run())
