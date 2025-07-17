import asyncio
import pandas as pd
from playwright.async_api import async_playwright

SEARCH_URL = "https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103644278%22%5D&keywords=data%20scientist&origin=FACETED_SEARCH"
NUM_PAGES = 2  # number of result pages to scrape


async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Step 1: Open LinkedIn login page
        await page.goto("https://www.linkedin.com/login")

        print("🔐 Log in manually in the opened browser.")

        # Wait for redirect to feed or search results
        while True:
            if "feed" in page.url or "search/results" in page.url:
                break
            await asyncio.sleep(1)

        input("✅ Login detected. Press ENTER to go to search results...")

        # Step 2: Go to the search page
        await page.goto(SEARCH_URL, wait_until="networkidle")

        all_profiles = []

        for page_num in range(NUM_PAGES):
            print(f"\n🌍 Processing Page {page_num + 1}")

            # Scroll to load lazy content
            await page.mouse.wheel(0, 5000)
            await page.wait_for_timeout(3000)

            # Get all profile links
            profile_elements = await page.locator("a[href*='/in/']").all()
            profile_urls = list(
                {await el.get_attribute("href") for el in profile_elements if el}
            )

            print(f"🔗 Found {len(profile_urls)} profile links")

            for url in profile_urls:
                print(f"➡️ Visiting: {url}")
                profile = await context.new_page()
                try:
                    await profile.goto(url, timeout=60000)
                    await profile.wait_for_timeout(3000)  # basic wait
                    await profile.wait_for_selector("h1", timeout=8000)

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

                    # Wait and extract experience
                    try:
                        await profile.wait_for_selector(
                            "section[id*='experience']", timeout=6000
                        )
                        exp_items = await profile.locator(
                            "section[id*='experience'] li"
                        ).all()
                        experience = " | ".join(
                            [
                                (await item.text_content()).strip().replace("\n", " ")
                                for item in exp_items[:3]
                            ]
                        )
                    except:
                        experience = "N/A"

                    # Wait and extract education
                    try:
                        await profile.wait_for_selector(
                            "section[id*='education']", timeout=6000
                        )
                        edu_items = await profile.locator(
                            "section[id*='education'] li"
                        ).all()
                        education = " | ".join(
                            [
                                (await item.text_content()).strip().replace("\n", " ")
                                for item in edu_items[:2]
                            ]
                        )
                    except:
                        education = "N/A"

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

            # Click the next button to go to the next page
            try:
                next_button = page.locator("button[aria-label='Next']")
                if await next_button.is_visible():
                    await next_button.click()
                    await page.wait_for_load_state("networkidle")
                else:
                    print("⚠️ No Next button found. Stopping.")
                    break
            except:
                print("❌ Error clicking next button.")
                break

        await browser.close()

        # Save results to CSV
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
