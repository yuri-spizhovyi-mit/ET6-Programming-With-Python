import asyncio
import os
from playwright.async_api import async_playwright

SEARCH_URL = "https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103644278%22%5D&keywords=data%20scientist&origin=FACETED_SEARCH"
NUM_PAGES = 1  # or more

SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Login manually
        await page.goto("https://www.linkedin.com/login")
        print("🔐 Log in manually...")
        while True:
            if "feed" in page.url or "search/results" in page.url:
                break
            await asyncio.sleep(1)

        input("✅ Login detected. Press ENTER to go to search results...")

        # Load search results
        await page.goto(SEARCH_URL, wait_until="domcontentloaded", timeout=60000)
        await page.wait_for_selector("a[href*='/in/']", timeout=10000)

        for page_num in range(NUM_PAGES):
            print(f"\n🌍 Processing Search Page {page_num + 1}")
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
                print(f"📸 Visiting and capturing: {url}")
                profile = await context.new_page()
                try:
                    await profile.goto(url, timeout=60000)
                    await profile.wait_for_timeout(3000)
                    await profile.wait_for_selector("h1", timeout=8000)

                    # Scroll gradually
                    for _ in range(6):
                        await profile.mouse.wheel(0, 2000)
                        await profile.wait_for_timeout(1000)

                    # Use name or fallback ID in filename
                    try:
                        name = await profile.locator("h1").first.text_content()
                        safe_name = "".join(c for c in name if c.isalnum() or c in " _-").strip().replace(" ", "_")
                        filename = f"{safe_name}.png" if safe_name else f"profile_{hash(url)}.png"
                    except:
                        filename = f"profile_{hash(url)}.png"

                    path = os.path.join(SCREENSHOT_DIR, filename)
                    await profile.screenshot(path=path, full_page=True)
                    print(f"✅ Saved screenshot: {path}")

                except Exception as e:
                    print(f"❌ Failed to capture {url}: {e}")

                await profile.close()

            # Go to next page
            try:
                next_button = page.locator("button.artdeco-pagination__button--next[aria-label='Next']")
                if await next_button.is_visible() and await next_button.is_enabled():
                    await next_button.click()
                    await page.wait_for_load_state("domcontentloaded")
                    await page.wait_for_timeout(3000)
                else:
                    print("⚠️ 'Next' button is disabled.")
                    break
            except Exception as e:
                print(f"❌ Error on pagination: {e}")
                break

        await browser.close()
        print("\n🎯 Done capturing profile screenshots.")

if __name__ == "__main__":
    asyncio.run(run())
