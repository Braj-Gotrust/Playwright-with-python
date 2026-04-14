from playwright.sync_api import sync_playwright, Page, expect

def test_statictable(page: Page):
    page.goto("https://preprod.gotrust.tech/data-mapping/ropa/ropa-management")
    page.wait_for_timeout(5000)