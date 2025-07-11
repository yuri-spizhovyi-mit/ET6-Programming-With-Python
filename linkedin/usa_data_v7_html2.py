import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import re
import os

SEARCH_URL = "https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103644278%22%5D&keywords=data%20scientist&origin=FACETED_SEARCH"
NUM_PAGES = 2  # Adjust to fetch more pages
SAVE_DIR = "linkedin_html_profiles"
os.makedirs(SAVE_DIR, exist_ok=True)

# Sanitize file name
def clean_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name.replace(" ", "_"))

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Step 1: Log in
        await page.goto("https://www.linkedin.com/login")
        print("🔐 Log in manually in the opened browser...")

        while True:
            if "feed" in page.url or "search/results" in page.url:
                break
            await asyncio.sleep(1)

        input("✅ Login detected. Press ENTER to go to search results...")

        # Step 2: Go to search results
        await page.goto(SEARCH_URL, wait_until="networkidle", timeout=60000)
        await page.wait_for_selector("a[href*='/in/']", timeout=10000)

        all_profiles = []

        for page_num in range(NUM_PAGES):
            print(f"\n🌍 Processing Page {page_num + 1}")
            await page.mouse.wheel(0, 5000)
            await page.wait_for_timeout(3000)

            profile_elements = await page.locator("a[href*='/in/']").all()
            profile_urls = list({
                await el.get_attribute("href")
                for el in profile_elements
                if await el.get_attribute("href")
            })

            print(f"🔗 Found {len(profile_urls)} profile links")

            for url in profile_urls:
                print(f"➡️ Visiting: {url}")
                profile = await context.new_page()
                try:
                    await profile.goto(url, timeout=60000)
                    await profile.wait_for_timeout(5000)

                    try:
                        name = await profile.locator("h1").first.text_content()
                        name = name.strip() if name else "N/A"
                    except:
                        name = "N/A"

                    try:
                        position_block = profile.locator("div.text-body-medium.break-words")
                        position = await position_block.nth(0).text_content()
                        position = position.strip() if position else "N/A"
                    except:
                        position = "N/A"

                    try:
                        location_block = profile.locator("span.text-body-small.inline.t-black--light.break-words")
                        location = await location_block.nth(0).text_content()
                        location = location.strip() if location else "N/A"
                    except:
                        location = "N/A"

                    # 🧾 Save raw HTML for future analysis
                    html_content = await profile.content()
                    file_name = f"{clean_filename(name or 'unknown')}.html"
                    file_path = os.path.join(SAVE_DIR, file_name)
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(html_content)
                    print(f"📝 Saved HTML to {file_path}")

                    all_profiles.append({
                        "Link": url,
                        "Name": name,
                        "Position": position,
                        "Country": location,
                        "Saved_HTML": file_path
                    })

                except Exception as e:
                    print(f"❌ Failed to scrape {url}: {e}")
                finally:
                    await profile.close()

            # 🔄 Next page
            try:
                next_button = page.locator("button.artdeco-pagination__button--next[aria-label='Next']")
                if await next_button.is_visible() and await next_button.is_enabled():
                    await next_button.click()
                    await page.wait_for_load_state("networkidle")
                    await page.wait_for_timeout(3000)
                else:
                    print("⚠️ 'Next' button is disabled — end of pagination.")
                    break
            except Exception as e:
                print(f"❌ Error clicking next button: {e}")
                break

        await browser.close()

        # 💾 Save index CSV
        if all_profiles:
            df = pd.DataFrame(all_profiles)
            df.to_csv("linkedin_index_with_html.csv", index=False)
            print("\n✅ All profiles saved. Index written to linkedin_index_with_html.csv")
        else:
            print("\n⚠️ No profiles were scraped.")

if __name__ == "__main__":
    asyncio.run(run())
