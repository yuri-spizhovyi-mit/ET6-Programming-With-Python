import asyncio
import pandas as pd
from playwright.async_api import async_playwright
import re
import os
import random
from datetime import datetime

# SEARCH_URL = "https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103644278%22%5D&keywords=frontend%20developer&origin=GLOBAL_SEARCH_HEADER"
SEARCH_URL = "https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103644278%22%5D&keywords=backend%20developer&origin=GLOBAL_SEARCH_HEADER&sid=VGf"
NUM_PAGES = 8
SAVE_DIR = "linkedin_html_profiles"
os.makedirs(SAVE_DIR, exist_ok=True)


def clean_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name.replace(" ", "_"))


async def extract_profiles_from_page(page, context, visited_links, all_profiles):
    await page.wait_for_selector("a[href*='/in/']", timeout=20000)
    await page.mouse.wheel(0, 20000)
    await asyncio.sleep(5)

    profile_urls = set()

    primary_links = await page.locator("a[href*='/in/']").all()
    for el in primary_links:
        href = await el.get_attribute("href")
        if href and "/in/" in href:
            profile_urls.add(href)

    if not profile_urls:
        print("⚠️ No <a> profile links found — using fallback method...")
        cards = await page.locator("div.entity-result__content").all()
        for card in cards:
            link_el = card.locator("a[href*='/in/']")
            if await link_el.count() > 0:
                href = await link_el.first.get_attribute("href")
                if href:
                    profile_urls.add(href)

    print(f"🔗 Found {len(profile_urls)} profile links")

    for url in profile_urls:
        if url in visited_links:
            continue
        visited_links.add(url)

        print(f"➡️ Visiting profile: {url}")
        profile = await context.new_page()
        try:
            await profile.goto(url, timeout=60000)
            await profile.wait_for_timeout(random.randint(3000, 6000))

            name_el = await profile.locator("h1").first.text_content()
            name = name_el.strip() if name_el else "unknown"
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_name = clean_filename(name or "unknown")[:30]
            file_name = f"{safe_name}_{timestamp}.html"
            file_path = os.path.join(SAVE_DIR, file_name)

            html_content = await profile.content()
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(html_content)

            print(f"✅ Saved: {file_name}")
            all_profiles.append({"Name": name, "Link": url, "Saved_HTML": file_name})

        except Exception as e:
            print(f"❌ Error scraping {url}: {e}")
        finally:
            await profile.close()


async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://www.linkedin.com/login")
        print("🔐 Please log in manually...")
        while True:
            if "feed" in page.url or "search/results" in page.url:
                break
            await asyncio.sleep(1)
        input("✅ Logged in. Press ENTER to proceed to search results...")

        await page.goto(SEARCH_URL, wait_until="networkidle")
        visited_links = set()
        all_profiles = []

        for page_num in range(NUM_PAGES):
            print(f"\n🌍 Scraping search result page {page_num + 1}...")
            await extract_profiles_from_page(page, context, visited_links, all_profiles)

            # Go to next page safely
            try:
                next_btn = page.locator(
                    "button.artdeco-pagination__button--next[aria-label='Next']"
                )
                if await next_btn.is_visible() and await next_btn.is_enabled():
                    old_url = page.url
                    await next_btn.click()

                    for _ in range(20):
                        if page.url != old_url:
                            break
                        await asyncio.sleep(1)
                    else:
                        print("❌ Pagination failed: URL did not change.")
                        break

                    await asyncio.sleep(3)  # Let new content load
                    await page.mouse.wheel(0, 10000)
                    await asyncio.sleep(3)
                else:
                    print("⚠️ Reached last page.")
                    break
            except Exception as e:
                print(f"⚠️ Pagination error: {e}")
                break

        await browser.close()

        if all_profiles:
            df = pd.DataFrame(all_profiles)
            df.to_csv("linkedin_profile_index.csv", index=False)
            print("\n📦 All profile HTMLs saved. Index: linkedin_profile_index.csv")
        else:
            print("⚠️ No profiles saved.")


if __name__ == "__main__":
    asyncio.run(run())
