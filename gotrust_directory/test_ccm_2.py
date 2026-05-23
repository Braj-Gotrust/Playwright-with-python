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

        # click banner builder tab
        page.locator("button:has-text('Banner Builder')").click()

        # domain details
        domain_name = "HDFC BANK"
        domain_url = "https://www.hdfc.bank.in/"
        cookie_policy_link = "https://www.hdfc.bank.in/privacy-policy"

        # Items per page
        page.locator(".lucide.lucide-chevron-down.size-4").click()
        dropdown = page.locator("div[role='option']")
        dropdown.nth(4).click()

        page.wait_for_timeout(1000)

        # select domain name
        all_domain_name = page.locator("tbody td:nth-child(1)")
        domain_count = all_domain_name.count()
        for i in range(domain_count):
            text = all_domain_name.nth(i).inner_text()
            if text == domain_name:
                all_domain_name.nth(i).click()
                break
        # select domain name confirmation
        select_domain_name_confi = page.locator("p:has-text('Cookie Configuration')")
        expect(select_domain_name_confi).to_be_visible(timeout=15000)

        # next button
        page.wait_for_timeout(1000)
        page.locator("button:has-text('Next')").click()
        page.wait_for_timeout(1000)
        # next button
        page.locator("button:has-text('Next')").click()
        page.wait_for_timeout(1000)
        # next button
        page.locator("button:has-text('Next')").click()
        page.wait_for_timeout(1000)

        # step 4 - User Consent Renewal
        page.get_by_label("User consent renewal in months:").click()
        dropdown = page.locator("div[role='option']")
        dropdown.nth(20).click()
        # next button
        page.locator("button:has-text('Next')").click()
        page.wait_for_timeout(1000)

        # step 5
        # upload logo
        file_path = "uploads/appvin-logo.png"

        print("\nupload trying...........")
        upload_logo(page, file_path)
        page.wait_for_timeout(1000)

        logo_upload_confi_msg = page.locator("img[alt='Uploaded Logo']")
        expect(logo_upload_confi_msg).to_have_attribute("src", re.compile(r"data:image"))
        print("\nupload successfully")

        # reset button
        page.locator("button:has-text('Reset Changes')").click()
        reset_confi_msg = page.locator("img[alt='Uploaded Logo']")
        expect(reset_confi_msg).to_have_attribute("src", "/assets/gotrustTitle_light.DIPQ8Yl4.svg")
        print("\nreset successfully")

        page.wait_for_timeout(1000)
        upload_logo(page, file_path)
        page.wait_for_timeout(1000)

        select_checkbox(page)
        page.wait_for_timeout(1000)
        page.locator("button[role='switch']").nth(2).click()
        page.wait_for_timeout(1000)
        page.locator("button[role='switch']").nth(4).click()
        page.wait_for_timeout(1000)
        page.locator("button[role='switch']").nth(5).click()
        page.wait_for_timeout(1000)
        page.locator("button[role='switch']").nth(6).click()
        # banner layout
        page.locator("img[alt='banner Wall']").click()
        page.wait_for_timeout(1000)
        page.locator("img[alt='banner Corner']").click()
        # mobile view
        page.locator("button[role='switch']").nth(0).click()
        page.wait_for_timeout(1000)

        page.locator("button:has-text('Next')").click()

        # select language
        page.wait_for_timeout(2000)
        page.locator("button[role='combobox']:nth-child(1)").click()
        dropdown = page.locator("div[role='option']")
        dropdown.filter(has_text="Dutch").click()
        #page.get_by_role("option", name="Dutch").click()
        page.wait_for_timeout(2000)
        page.locator("button:has-text('Save Translation')").click()
        change_language_confi_msg = page.get_by_text("Translation saved successfully")
        expect(change_language_confi_msg).to_be_visible(timeout=15000)

        # Category tab
        page.locator("button:has-text('Category')").click()
        page.wait_for_timeout(1000)
        # service tab
        page.locator("button:has-text('Service')").click()
        page.wait_for_timeout(1000)
        # Cookie tab
        page.locator("button:has-text('Cookie')").click()
        page.wait_for_timeout(1000)

        page.locator("button:has-text('Next')").click()

        # banner preview
        page.locator("button:has-text('Banner Preview')").click()
        page.wait_for_timeout(1000)
        page.locator("button:has-text('Details')").click()
        page.wait_for_timeout(1000)
        page.locator("button:has-text('About')").click()
        page.wait_for_timeout(1000)
        # close banner
        cross_btn = page.locator("span:has-text('Close')")
        cross_btn.click()
        # save button
        save_btn = page.locator("button:has-text('Save')")
        save_btn.click()






        page.wait_for_timeout(5000)

def upload_logo(page, file_path: str):
    try:
        page.locator("img[alt='Remove Logo']").click()
        file_input = page.locator("input[type='file']")
        file_input.set_input_files(file_path)
    except Exception as e:
        print(f"Exception while uploading logo: {e}")
        raise


def select_checkbox(page):
    try:
        checkbox = page.locator("button#terms")
        # Wait until visible
        checkbox.wait_for(state="visible")
        if checkbox.get_attribute("aria-checked") != "true":
            checkbox.click()
    except Exception as e:
        print(f"Exception while selecting checkbox: {e}")
        raise






