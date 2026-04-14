from playwright.sync_api import sync_playwright, expect, Playwright


def test_browser_context(playwright: Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page1=context.new_page()
    page2=context.new_page()

    page1.goto("https://playwright.dev/")
    page1.wait_for_timeout(3000)
    expect(page1).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")

    page2.goto("https://www.selenium.dev/")
    page2.wait_for_timeout(3000)
    expect(page2).to_have_title("Selenium")
