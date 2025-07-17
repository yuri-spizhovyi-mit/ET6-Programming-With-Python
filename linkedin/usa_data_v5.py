import asyncio
import pandas as pd
import re
from playwright.async_api import async_playwright

SEARCH_URL = "https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103644278%22%5D&keywords=data%20scientist&origin=FACETED_SEARCH"
NUM_PAGES = 2  # Number of search result pages to scrape


# 🧠 Utility: Extract all <!----> content from aria-hidden spans
async def extract_hidden_text(profile):
    try:
        spans = await profile.locator('span[aria-hidden="true"]').all()
        extracted = []
        for span in spans:
            html = await span.inner_html()
            matches = re.findall(r"<!---->(.*?)<!---->", html)
            for match in matches:
                cleaned = match.strip()
                if cleaned:
                    extracted.append(cleaned)
        return " | ".join(extracted)
    except Exception as e:
        print(f"⚠️ Error extracting hidden text: {e}")
        return "N/A"


async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Step 1: Manual Login
        await page.goto("https://www.linkedin.com/login")
        print("🔐 Log in manually in the opened browser...")

        while True:
            if "feed" in page.url or "search/results" in page.url:
                break
            await asyncio.sleep(1)

        input("✅ Login detected. Press ENTER to go to search results...")

        # Step 2: Retry loading search results
        for attempt in range(3):
            try:
                await page.goto(
                    SEARCH_URL, wait_until="domcontentloaded", timeout=60000
                )
                await page.wait_for_selector("a[href*='/in/']", timeout=10000)
                break
            except Exception as e:
                print(f"⚠️ Attempt {attempt + 1} failed to load search: {e}")
                await page.wait_for_timeout(3000)
        else:
            print("❌ Failed to load search page after 3 attempts.")
            return

        all_profiles = []

        for page_num in range(NUM_PAGES):
            print(f"\n🌍 Processing Page {page_num + 1}")
            await page.mouse.wheel(0, 5000)
            await page.wait_for_timeout(3000)

            # Collect profile URLs
            profile_elements = await page.locator("a[href*='/in/']").all()
            profile_urls = list(
                {
                    await el.get_attribute("href")
                    for el in profile_elements
                    if await el.get_attribute("href")
                }
            )

            print(f"🔗 Found {len(profile_urls)} profile links")

            for url in profile_urls:
                print(f"➡️ Visiting: {url}")
                profile = await context.new_page()
                try:
                    await profile.goto(url, timeout=60000)
                    await profile.wait_for_timeout(3000)
                    await profile.wait_for_selector("h1", timeout=8000)

                    # Scroll to load dynamic content
                    for _ in range(3):
                        await profile.mouse.wheel(0, 3000)
                        await profile.wait_for_timeout(1000)

                    # Extract visible name
                    try:
                        name = await profile.locator("h1").first.text_content() or "N/A"
                    except:
                        name = "N/A"

                    # Extract hidden content
                    raw_content = await extract_hidden_text(profile)

                    all_profiles.append(
                        {"Link": url, "Name": name.strip(), "Raw_Content": raw_content}
                    )

                except Exception as e:
                    print(f"❌ Failed to scrape {url}: {e}")
                await profile.close()

            # Go to next search result page
            try:
                next_button = page.locator(
                    "button.artdeco-pagination__button--next[aria-label='Next']"
                )
                if await next_button.is_visible() and await next_button.is_enabled():
                    await next_button.click()
                    await page.wait_for_load_state("domcontentloaded")
                    await page.wait_for_timeout(3000)
                else:
                    print("⚠️ 'Next' button is disabled — end of pagination.")
                    break
            except Exception as e:
                print(f"❌ Error clicking next button: {e}")
                break

        await browser.close()

        # Save results to CSV
        if all_profiles:
            df = pd.DataFrame(all_profiles)
            df.to_csv("linkedin_raw_hidden_content.csv", index=False)
            print(
                "\n✅ Scraping completed and saved to linkedin_raw_hidden_content.csv"
            )
        else:
            print("\n⚠️ No profiles were scraped.")


if __name__ == "__main__":
    asyncio.run(run())
