import asyncio
import pandas as pd
from playwright.async_api import async_playwright

SEARCH_URL = "https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103644278%22%5D&keywords=data%20scientist&origin=FACETED_SEARCH"
NUM_PAGES = 2  # number of result pages to scrape


# 🧠 Utility: Extract list items following a header (like "Experience" or "Education")
async def extract_section_items(page, section_title, max_items=3):
    try:
        section_locator = page.locator(
            f"xpath=//h2[contains(@class, 'pvs-header__title')]"
            f"[.//span[text()='{section_title}']]/ancestor::div[contains(@class, 'pvs-header')]"
            f"/following-sibling::div//li[contains(@class, 'artdeco-list__item')]"
        )
        items = await section_locator.all()
        return (
            " | ".join(
                [
                    (await item.text_content()).strip().replace("\n", " ")
                    for item in items[:max_items]
                ]
            )
            if items
            else "N/A"
        )
    except Exception as e:
        print(f"⚠️ Error extracting {section_title}: {e}")
        return "N/A"


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

                    # Basic Info
                    try:
                        name = await profile.locator("h1").first.text_content() or "N/A"
                    except:
                        name = "N/A"

                    try:
                        position_block = profile.locator(
                            "div.text-body-medium.break-words"
                        )
                        position = await position_block.nth(0).text_content() or "N/A"
                    except:
                        position = "N/A"

                    try:
                        location_block = profile.locator(
                            "span.text-body-small.inline.t-black--light.break-words"
                        )
                        location = await location_block.nth(0).text_content() or "N/A"
                    except:
                        location = "N/A"

                    # ✅ Structured Data Extraction
                    experience = await extract_section_items(profile, "Experience")
                    education = await extract_section_items(profile, "Education")

                    all_profiles.append(
                        {
                            "Link": url,
                            "Name": name.strip(),
                            "Position": position.strip(),
                            "Country": location.strip(),
                            "Experience": experience,
                            "Education": education,
                        }
                    )

                except Exception as e:
                    print(f"❌ Failed to scrape {url}: {e}")

                await profile.close()

            # 🔄 Next page
            try:
                next_button = page.locator(
                    "button.artdeco-pagination__button--next[aria-label='Next']"
                )
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

        # 💾 Export results
        if all_profiles:
            df = pd.DataFrame(all_profiles)
            df.to_csv("linkedin_data_scientists_playwright.csv", index=False)
            print(
                "\n✅ Scraping completed and saved to linkedin_data_scientists_playwright.csv"
            )
        else:
            print("\n⚠️ No profiles were scraped.")


if __name__ == "__main__":
    asyncio.run(run())
