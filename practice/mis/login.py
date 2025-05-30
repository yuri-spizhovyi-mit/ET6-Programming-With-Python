from playwright.sync_api import sync_playwright


def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com/login")
        page.fill('input[name="email"]', "test@example.com")
        page.fill('input[name="password"]', "password123")
        page.click('button[type="submit"]')
        page.wait_for_url("https://example.com/dashboard")
        assert page.url == "https://example.com/dashboard"
        browser.close()


test_login()
