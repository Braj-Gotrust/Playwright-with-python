import re
import time
from itertools import count

import pytest
from playwright.sync_api import expect, Page

login_test_data = [("dpo.sgt@yopmail.com", "Test@123", "valid")]


@pytest.mark.parametrize("email,password,validity", login_test_data)
def test_ropa(email, password, validity, page: Page):
    page.goto("https://sandbox.gotrust.tech/home")

    # Login
    page.get_by_role("textbox", name="Username or email").fill(email)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Sign In").click()

    if validity == "valid":
        # Wait for dashboard load
        ccm_btn = page.locator("a span:has-text('Cookie Consent')").nth(0)
        expect(ccm_btn).to_be_visible(timeout=15000)

        # Click ccm button
        ccm_btn.click()
        ccm_btn.click()

        ccm_title = page.locator("h1:has-text('Cookie Consent Management')")
        expect(ccm_title).to_be_visible(timeout=15000)

        # click Banner Builder tab
        page.locator("button:has-text('Banner Builder')").click()

        # click Cookie Dictionary tab
        page.locator("button:has-text('Cookie Dictionary')").click()

        # click User Guide tab
        page.locator("button:has-text('User Guide')").click()

        # click Analytics tab
        page.locator("button:has-text('Analytics')").click()

        # click Consent Records tab
        page.locator("button:has-text('Consent Records')").click()

        # click Cookie Policy tab
        page.locator("button:has-text('Cookie Policy')").click()
        create_btn = page.locator("button:has-text('Create')")
        create_btn.click()


        domain_name = "HDFC BANK"
        select_domain_name(page, domain_name)
        next_btn = page.locator("button:has-text('Next')")
        next_btn.click()

        #page.get_by_placeholder("Enter cookie policy title").fill("title 3")
        input1 = page.get_by_placeholder("Enter cookie policy title")
        input1.focus()
        page.keyboard.insert_text("title 7")
        time.sleep(3)
        page.keyboard.press("Tab")
        page.keyboard.press("Enter")
        time.sleep(3)
        #page.locator("button:has-text('Select Regulation')").click()
        dropdown = page.locator("div[role='option']")
        dropdown.nth(0).click()
        page.locator("h2:has-text('1. Introduction')").click()
        page.keyboard.press("Enter")
        time.sleep(3)
        page.locator("button:has-text('Add cookie table')").click()
        time.sleep(3)
        add_cookie_table_confi_msg = page.get_by_text("Table added successfully")
        expect(add_cookie_table_confi_msg).to_be_visible(timeout=15000)

        save_btn = page.locator("button:has-text('Save')")
        save_btn.click()
        policy_create_confi_msg = page.get_by_text("Policy Created Successfully")
        expect(policy_create_confi_msg).to_be_visible(timeout=15000)
        time.sleep(3)

        cross_btn = page.locator("span:has-text('Close')")
        cross_btn.click()




        page.wait_for_timeout(5000)

def select_domain_name(page, domain_name: str):
    try:
        select_domain_txt = page.locator("button:has-text('Select Domain')")
        select_domain_txt.click()

        page.wait_for_selector("div[role='option']")

        page.locator("div[role='option']").filter(has_text=domain_name).first.click()

        print(f"Selected domain name : {domain_name}")

    except Exception as e:
        print(f"Exception while selecting domain name : {e}")
        raise

# def select_domain_name(page, domain_name:str ):
#     try:
#         select_domain_txt = page.locator("button:has-text('Select Domain')")
#         select_domain_txt.click()
#         dropdown = page.locator("div[role='option']")
#         count = dropdown.count()
#         print("\ndomain count :",count)
#         for i in range(count):
#             text = dropdown.nth(i).inner_text()
#             if text == domain_name:
#                 print("\ndomain name :", text)
#                 dropdown.nth(i).click()
#                 break
#     except Exception as e:
#         print(f"Exception while uploading logo: {e}")
#         raise





