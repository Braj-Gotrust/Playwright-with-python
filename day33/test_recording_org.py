import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://sandbox.gotrust.tech/keycloak/realms/data-sec/protocol/openid-connect/auth?client_id=gt-web&redirect_uri=https%3A%2F%2Fsandbox.gotrust.tech%2Fhome&response_type=code&scope=openid+profile+email+offline_access&state=4cb54ff09312424995e73350d3e19c1c&code_challenge=Ht7ehRBqUHWEnva1bt6pBsy4mwGIG4ezMW6ZbSGMW4c&code_challenge_method=S256")
    page.get_by_role("textbox", name="Username or email").click()
    page.get_by_role("textbox", name="Username or email").fill("dpo.sgt@yopmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").press("CapsLock")
    page.get_by_role("textbox", name="Password").fill("T")
    page.get_by_role("textbox", name="Password").press("CapsLock")
    page.get_by_role("textbox", name="Password").fill("Test@123")
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("link", name="Ropa Registry").click()
    page.get_by_role("link", name="Ropa Registry").click()
    page.get_by_role("button", name="Processing Activity").click()
    page.get_by_role("textbox", name="e.g., Customer Registration").fill("ropa 1")
    page.get_by_role("textbox", name="Short explanation...").click()
    page.get_by_role("textbox", name="Short explanation...").fill("test")
    page.get_by_role("combobox").filter(has_text=re.compile(r"^Select legal entity$")).click()
    page.get_by_label("Appvin 4").get_by_text("Appvin 4").click()
    page.get_by_role("combobox").filter(has_text="Select department").click()
    page.get_by_label("department (Appvin 4)").get_by_text("department (Appvin 4)").click()
    page.get_by_role("button", name="Pick a date").click()
    page.get_by_role("button", name="Go to next month").click()
    page.get_by_role("button", name="Go to previous month").click()
    page.get_by_role("button", name="Go to next month").click()
    page.get_by_role("gridcell", name="25").click()
    page.get_by_role("combobox").filter(has_text="Select assignee").click()
    page.get_by_label("Braj Assignee (assignee)").get_by_text("Braj Assignee (assignee)").click()
    page.get_by_role("radio", name="Yes").click()
    page.get_by_role("button", name="Select reviewers for Level").click()
    page.get_by_label("Suggestions").get_by_text("Braj Reviewer (reviewer)").click()
    page.get_by_text("Do you want to add reviewer?Level 1YesNoBraj Reviewer (reviewer)Do you want to").click()
    page.get_by_role("button", name="Braj Reviewer (reviewer)").click()
    page.get_by_role("option", name="Close").click()
    page.locator("#next-level-0-yes").click()
    page.get_by_role("button", name="Select reviewers for Level").click()
    page.get_by_label("Suggestions").get_by_text("Nancy reviewer (reviewer)").click()
    page.get_by_role("option", name="Close").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
