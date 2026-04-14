from playwright.sync_api import Page, expect

# This is a run command :-  pytest day18-playwright/test_playwright.py -s -v --headed
# This is a browser command :-  pytest day18-playwright/test_playwright.py -s -v --headed --browser firefox
# THis is a two browser command :- pytest day18-playwright/test_playwright.py -s -v --headed --browser firefox --browser chromium
# This is a parallel execution command :- pytest day18-playwright/test_playwright.py -s -v --headed --numprocesses 2



def test_verifyPageUrl(page: Page):
    page.goto("https://www.flipkart.com/")   # passing url
    expect(page).to_have_url("https://www.flipkart.com/")  # expected url
    print("\nPage url or link url : ",page.url)

def test_verifyPageTitle(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")
    print("\nThis is my pate title : ",page.title)