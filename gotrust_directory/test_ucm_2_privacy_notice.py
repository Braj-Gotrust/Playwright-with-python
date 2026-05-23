import re
import time
from itertools import count

import pytest
from playwright.sync_api import expect, Page

login_test_data = [("dpo.preprod@yopmail.com", "Test@123", "valid")]
#login_test_data = [("dpo.sgt@yopmail.com", "Test@123", "valid")]

# TEST DATA



@pytest.mark.parametrize("email,password,validity", login_test_data)
def test_ccm_1(email, password, validity, page: Page):
    page.goto("https://preprod.gotrust.tech/home")
    #page.goto("https://sandbox.gotrust.tech/home")

    # Login
    page.locator("#username").fill(email)
    page.locator("#password").fill(password)
    page.locator("button[type='submit']:has-text('Sign In'), input[type='submit'][value='Sign In']").click()

    if validity == "valid":
        # Wait for dashboard load
        task_overview_btn =page.locator("span:has-text('Task Overview')").nth(2)

        expect(task_overview_btn).to_be_visible(timeout=15000)


        task_overview_btn.click()
        task_overview_btn.click()

        # privacy policy title
        privacy_policy = page.locator("a:has-text('Privacy Notice')")
        expect(privacy_policy).to_be_visible(timeout=15000)

        # privacy policy tab
        privacy_policy.click()
        time.sleep(3)
        create_btn = page.locator("button:has-text('Create')")
        create_btn.click()

        # select legal entity
        legal_entity_name = "b2"
        select_legal_entity(page, legal_entity_name)
        select_txt = page.locator("span:has-text('Select')")
        select_txt.nth(0).click()
        dropdown = page.locator("div[role='option']")
        dropdown.nth(1).click()

        # privacy notice name
        privacy_notice_name = "privacy notice 2"
        privacy_policy_title = page.locator("input[placeholder='Enter Privacy Notice Title']")
        privacy_policy_title.fill(privacy_notice_name)

        # privacy notice text
        privacy_notice_description = page.locator(".tiptap")
        privacy_notice_description.fill("This Privacy Notice explains how personal information is collected, "
                                 "used, stored, and protected when users access or use the website, "
                                 "application, or services. It also outlines user rights, data security "
                                 "measures, and contact details for privacy-related concerns.")

        time.sleep(3)
        save_btn = page.locator("button:has-text('Save')")
        save_btn.click()

        privacy_notice_save_confi_msg = page.get_by_text("Privacy notice saved successfully")
        expect(privacy_notice_save_confi_msg).to_be_visible()




        time.sleep(5)

def select_legal_entity(page, legal_entity_name: str):
    try:
        select_txt = page.locator("span:has-text('Select')")
        select_txt.nth(0).click()
        page.wait_for_selector("[role='option']")
        dropdown = page.locator("div[role='option']")
        option = dropdown.filter(has_text=legal_entity_name)

        if option.is_visible():
            option.click()
        else:
            print(f" {legal_entity_name} not found, selecting Gotrust option")
            dropdown.nth(1).click()

    except Exception as e:
        print(f"Exception while selecting legal entity name: {e}")
        raise
