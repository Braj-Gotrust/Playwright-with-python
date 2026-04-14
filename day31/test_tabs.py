from playwright.sync_api import Playwright

def test_handle_tabs(playwright: Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    parentpage=context.new_page()

    parentpage.goto("https://testautomationpractice.blogspot.com/")

    # register an event for handle tab using lambda function
    parentpage.on("page",lambda page:page.wait_for_load_state())


    parentpage.locator("button:has-text('New Tab')").click()
    parentpage.wait_for_timeout(3000)

    all_pages=context.pages
    print("\nTotal pages:",len(all_pages))

    print("\ntitle of parent tab : ",all_pages[0].title())
    print("\ntitle of child tab : ",all_pages[1].title())

    childpage=all_pages[1]
    print("\nurl of the child tab : ",childpage.url)

