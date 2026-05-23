import re
import time
from itertools import count

import pytest
from playwright.sync_api import expect, Page

login_test_data = [("dpo.preprod@yopmail.com", "Test@123", "valid")]
#login_test_data = [("dpo.sgt@yopmail.com", "Test@123", "valid")]

# TEST DATA
consent_template_name = "temp n5"
legal_entity_name = "b2"
processing_purpose_name = "bhh"
pii_label_name = "phone number"
source_name = "Form"
file_path = "uploads/appvin-logo.png"



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
        page.locator("span:has-text('UCM Lab')").click()
        consent_collection_builder_btn =page.locator("span:has-text('Consent Collection Builder')")

        expect(consent_collection_builder_btn).to_be_visible(timeout=15000)


        consent_collection_builder_btn.click()
        consent_collection_builder_btn.click()

        ucm_title = page.locator("a:has-text('Universal Consent Management')")
        expect(ucm_title).to_be_visible(timeout=15000)

        # click Create Consent Collection Template button
        page.locator("button:has-text('Create Consent Collection Template')").click()
        page.wait_for_timeout(1000)

        # step 1
        page.locator("input[placeholder='Enter Template Name']").fill(consent_template_name)

        # select legal entity
        select_legal_entity(page, legal_entity_name)

        # select owner
        select_txt = page.locator("span:has-text('Select')")
        select_txt.nth(0).click()
        dropdown = page.locator("div[role='option']")
        dropdown.nth(1).click()

        # select unique data identifier
        select_txt = page.get_by_label("Unique Data Identifier Type").or_(page.locator("span:has-text('Select')"))
        select_txt.first.click()
        select_pii_label(page, pii_label_name)
        # continue button
        continue_btn = page.locator("button:has-text('Continue')")
        continue_btn.click()

        record_create_confirmation_msg = page.get_by_text("Record Created Successfully")
        expect(record_create_confirmation_msg).to_be_visible(timeout=15000)

        # step 2
        add_processing_purpose_btn = page.locator("button:has-text('Add Processing Purpose')")
        add_processing_purpose_btn.click()
        # select processing purpose

        select_processing_purpose(page,processing_purpose_name)
        add_btn = page.locator("button:has-text('Add')")
        add_btn.nth(1).click()
        # select pii label
        select_txt = page.locator("span:has-text('Select')")
        select_txt.nth(0).click()
        select_pii_label(page, pii_label_name)
        save_btn = page.locator("button:has-text('Save')")
        save_btn.nth(1).click()
        time.sleep(3)
        save_btn.nth(0).click()
        record_create_confirmation_msg = page.get_by_text("Record Created Successfully")
        expect(record_create_confirmation_msg).to_be_visible(timeout=15000)

        # continue step 3
        continue_btn.click()
        # exist button
        exist_btn = page.locator("button:has-text('Existing')")
        exist_btn.click()

        # select privacy notice
        privacy_notice_name = " privacy notice 3"
        select_privacy_notice(page, privacy_notice_name)
        continue_btn.click()

        # step - 4
        # select source
        select_source(page, source_name)
        input_field_txt = page.locator("input[type='text']")
        input_field_txt.nth(1).fill("consent form title 1")
        input_field_txt.nth(2).fill("consent form description 1")

        next_btn = page.locator("button:has-text('Next')")
        next_btn.click()
        record_create_confirmation_msg = page.get_by_text("Record Created Successfully")
        expect(record_create_confirmation_msg).to_be_visible(timeout=15000)

        # USER INPUT TAB
        # customization
        page.locator("button:has-text('Customize Form - Desktop')").click()

        # upload logo
        upload_logo(page, file_path)
        page.wait_for_timeout(1000)

        logo_upload_confi_msg = page.locator("img[alt='Uploaded Logo']")
        expect(logo_upload_confi_msg).to_have_attribute("src", re.compile(r"https://storage-pp.gotrust.tech/gt-logo-bucket/uploads"))
        print("\nupload successfully")

        # reset button
        reset_btn = page.locator("button:has-text('Reset')")
        reset_btn.click()
        time.sleep(1)
        reset_confirmation = page.locator("img[src='/assets/svg/gotrustTitle_light.DIPQ8Yl4.svg']")
        expect(reset_confirmation.nth(0)).to_be_visible(timeout=15000)

        # again upload logo
        upload_logo(page, file_path)
        page.wait_for_timeout(1000)

        logo_upload_confi_msg = page.locator("img[alt='Uploaded Logo']")
        expect(logo_upload_confi_msg).to_have_attribute("src", re.compile(
            r"https://storage-pp.gotrust.tech/gt-logo-bucket/uploads"))
        print("\nupload successfully")



        # mobile view
        switch_btn = page.locator("button[role='switch']")
        switch_btn.nth(0).click()
        # mobile view customization
        upload_logo(page, file_path)
        logo_upload_confi_msg = page.locator("img[alt='Uploaded Logo']")
        expect(logo_upload_confi_msg).to_have_attribute("src", re.compile(r"https://storage-pp.gotrust.tech/gt-logo-bucket/uploads"))
        print("\nupload successfully")

        # reset button
        reset_btn = page.locator("button:has-text('Reset')")
        reset_btn.click()
        reset_confirmation = page.locator("img[src='/assets/svg/gotrustTitle_light.DIPQ8Yl4.svg']")
        expect(reset_confirmation.nth(0)).to_be_visible(timeout=15000)

        # again upload logo in mobile view
        upload_logo(page, file_path)
        page.wait_for_timeout(1000)

        logo_upload_confi_msg = page.locator("img[alt='Uploaded Logo']")
        expect(logo_upload_confi_msg).to_have_attribute("src", re.compile(
            r"https://storage-pp.gotrust.tech/gt-logo-bucket/uploads"))
        print("\nupload successfully")

        continue_btn.click()





        page.wait_for_timeout(5000)

def upload_logo(page, file_path: str):
    try:
        time.sleep(1)
        page.locator("img[alt='Remove Logo'], button:has(svg.lucide-x):nth-child(2)").click()
        time.sleep(3)
        file_input = page.locator("input[type='file']")
        file_input.set_input_files(file_path)
    except Exception as e:
        print(f"Exception while uploading logo: {e}")
        raise


def select_source(page, source_name):
    try:
        select_txt = page.locator("span:has-text('Select')")
        select_txt.nth(0).click()
        page.wait_for_selector("[role='option']")
        dropdown = page.locator("div[role='option']")
        option = dropdown.filter(has_text=source_name)

        if option.is_visible():
            option.click()
        else:
            print(f" {source_name} is not found")

    except Exception as e:
        print(f"Exception while selecting source name: {e}")
        raise

def select_privacy_notice(page, privacy_notice_name):
    try:
        select_txt = page.locator("span:has-text('Select')")
        select_txt.nth(0).click()
        page.wait_for_selector("[role='option']")
        dropdown = page.locator("div[role='option']")
        option = dropdown.filter(has_text=privacy_notice_name)

        if option.is_visible():
            option.click()
        else:
            print(f" {privacy_notice_name} is not found")

    except Exception as e:
        print(f"Exception while selecting privacy notice name: {e}")
        raise


def select_processing_purpose(page, processing_purpose_name):
    try:
        select_txt = page.locator("span:has-text('Select')")
        select_txt.nth(0).click()
        page.wait_for_selector("[role='option']")
        dropdown = page.locator("div[role='option']")
        option = dropdown.filter(has_text=processing_purpose_name)

        if option.is_visible():
            option.click()
        else:
            print(f" {processing_purpose_name} is not found")

    except Exception as e:
        print(f"Exception while selecting processing purpose name: {e}")
        raise


def select_pii_label(page: Page, pii_label_name:str):
    try:
        page.wait_for_selector("[role='option']")
        dropdown = page.locator("div[role='option']")
        option = dropdown.filter(has_text=pii_label_name)

        if option.is_visible():
            option.click()
        else:
            print(f" {pii_label_name} is not found")

    except Exception as e:
        print(f"Exception while selecting pii label name: {e}")
        raise


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




