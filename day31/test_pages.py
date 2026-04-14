from playwright.sync_api import Page, Playwright, expect


def test_handle_popups(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")

    page.on("popup", lambda popup: popup.wait_for_load_state())

    page.locator("#PopUp").click()
    page.wait_for_timeout(3000)
    all_pages=context.pages
    print("\nTotal number of pages : ",len(all_pages))

    # capture url of the all popup pages
    for pw in all_pages:
        print("\npage url  : ",pw.url)
        title=pw.title()
        print("title  : ",title)
        if "Playwright" in title:
            pw.locator(".getStarted_Sjon").click()
            pw.wait_for_timeout(3000)
            expect(pw).to_have_title("Installation | Playwright")
            pw.close()  # close the playwright popup page
    page.wait_for_timeout(3000)
    context.close()
    browser.close()



