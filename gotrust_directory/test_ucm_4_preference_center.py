import re
import time
from itertools import count

import pytest
from openpyxl.writer.excel import save_workbook
from playwright.sync_api import expect, Page

login_test_data = [("dpo.preprod@yopmail.com", "Test@123", "valid")]
# login_test_data = [("dpo.sgt@yopmail.com", "Test@123", "valid")]

# TEST DATA
consent_template_name = "temp n5"
pii_label_name = "phone number"
#processing_purpose_name = "bhh"
privacy_notice_name = " privacy notice 3"  # unique
file_path = "uploads/appvin-logo.png"
preference_center_title = "preference center title 3"


@pytest.mark.parametrize("email,password,validity", login_test_data)
def test_ccm_1(email, password, validity, page: Page):
    page.goto("https://preprod.gotrust.tech/home")
    # page.goto("https://sandbox.gotrust.tech/home")

    # Login
    page.locator("#username").fill(email)
    page.locator("#password").fill(password)
    page.locator("button[type='submit']:has-text('Sign In'), input[type='submit'][value='Sign In']").click()

    if validity == "valid":
        # Wait for dashboard load
        page.locator("span:has-text('UCM Lab')").click()
        consent_collection_builder_btn = page.locator("span:has-text('Consent Collection Builder')")

        expect(consent_collection_builder_btn).to_be_visible(timeout=15000)

        consent_collection_builder_btn.click()
        consent_collection_builder_btn.click()

        ucm_title = page.locator("a:has-text('Universal Consent Management')")
        expect(ucm_title).to_be_visible(timeout=15000)

        # extend page
        page_extend(page)

        # select template name
        select_consent_template_name(page, consent_template_name)
        consent_template_title = page.get_by_text("Create Consent Collection Template")
        expect(consent_template_title).to_be_visible(timeout=15000)

        # select unique data identifier
        time.sleep(3)
        select_txt = page.get_by_label("Unique Data Identifier Type").or_(page.locator("span:has-text('Select')"))
        select_txt.first.click()
        select_pii_label(page, pii_label_name)


        # continue button
        continue_btn = page.locator("button:has-text('Continue')")
        continue_btn.click()
        continue_btn.click()

        # exist button
        time.sleep(1)
        exist_btn = page.locator("button:has-text('Existing')")
        if exist_btn.is_visible():
            exist_btn.click()
            # select privacy notice
            select_privacy_notice(page, privacy_notice_name)
        continue_btn.click()
        continue_btn.click()

        # step - 5 => Preference Center =================
        time.sleep(1)
        # input_field_txt = page.locator("input[type='text']")
        # new_btn = page.locator("button:has-text('New')")
        # next_btn = page.locator("button:has-text('Next')")
        #
        # if new_btn.is_visible():
        #     new_btn.click()
        #     input_field_txt.nth(1).fill(preference_center_title)
        #     time.sleep(3)
        #     next_btn.click()

        # upload logo in the preference center
        upload_logo(page, file_path)
        logo_upload_confi_msg = page.locator("img[alt='Uploaded Logo']")
        expect(logo_upload_confi_msg).to_have_attribute("src", re.compile(
            r"https://storage-pp.gotrust.tech/gt-logo-bucket/uploads"))
        print("\nupload successfully")

        # reset button
        reset_btn = page.locator("button:has-text('Reset')")
        reset_btn.click()
        reset_confirmation = page.locator("img[src='/assets/svg/gotrustTitle_light.DIPQ8Yl4.svg']")
        expect(reset_confirmation.nth(0)).to_be_visible(timeout=15000)

        # full screen button
        full_screen_btn = page.locator("button:has-text('View on full screen')")
        expect(full_screen_btn).to_be_visible(timeout=15000)
        full_screen_btn.click()
        cross_btn = page.locator("span:has-text('Close')")
        cross_btn.click()
        expect(full_screen_btn).to_be_visible(timeout=15000)

        # agin upload logo
        upload_logo(page, file_path)
        logo_upload_confi_msg = page.locator("img[alt='Uploaded Logo']")
        expect(logo_upload_confi_msg).to_have_attribute("src", re.compile(
            r"https://storage-pp.gotrust.tech/gt-logo-bucket/uploads"))
        print("\nupload successfully")



        # mobile view under the user input tab
        switch_btn = page.locator("button[role='switch']")
        switch_btn.nth(0).click()
        # mobile view customization
        upload_logo(page, file_path)
        logo_upload_confi_msg = page.locator("img[alt='Uploaded Logo']")
        expect(logo_upload_confi_msg).to_have_attribute("src", re.compile(
            r"https://storage-pp.gotrust.tech/gt-logo-bucket/uploads"))
        print("\nupload successfully")

        # reset button
        reset_btn = page.locator("button:has-text('Reset')")
        reset_btn.click()
        reset_confirmation = page.locator("img[src='/assets/svg/gotrustTitle_light.DIPQ8Yl4.svg']")
        expect(reset_confirmation.nth(0)).to_be_visible(timeout=15000)

        # full screen button
        full_screen_btn = page.locator("button:has-text('View on full screen')")
        expect(full_screen_btn).to_be_visible(timeout=15000)
        full_screen_btn.click()
        cross_btn = page.locator("span:has-text('Close')")
        cross_btn.click()
        expect(full_screen_btn).to_be_visible(timeout=15000)

        # again upload logo in mobile view
        upload_logo(page, file_path)
        page.wait_for_timeout(1000)
        logo_upload_confi_msg = page.locator("img[alt='Uploaded Logo']")
        expect(logo_upload_confi_msg).to_have_attribute("src", re.compile(
            r"https://storage-pp.gotrust.tech/gt-logo-bucket/uploads"))
        print("\nupload successfully")
        time.sleep(1)

        # VERIFY INPUT TAB under the mobile view
        verify_input_tab = page.locator("button:has-text('Verify Input')")
        verify_input_tab.nth(0).click()
        # upload logo
        upload_logo(page, file_path)
        logo_upload_confi_msg = page.locator("img[alt='Uploaded Logo']")
        expect(logo_upload_confi_msg).to_have_attribute("src", re.compile(
            r"https://storage-pp.gotrust.tech/gt-logo-bucket/uploads"))
        print("\nupload successfully")
        # reset button
        reset_btn = page.locator("button:has-text('Reset')")
        reset_btn.click()
        reset_confirmation = page.locator("img[src='/assets/svg/gotrustTitle_light.DIPQ8Yl4.svg']")
        expect(reset_confirmation.nth(0)).to_be_visible(timeout=15000)
        # full screen button
        full_screen_btn = page.locator("button:has-text('View on full screen')")
        expect(full_screen_btn).to_be_visible(timeout=15000)
        full_screen_btn.click()
        cross_btn = page.locator("span:has-text('Close')")
        cross_btn.click()
        expect(full_screen_btn).to_be_visible(timeout=15000)

        # upload logo again
        upload_logo(page, file_path)
        # otp section
        swap_button_order =  page.locator("button:has-text('Swap Button Order')")
        swap_button_order.click()
        time.sleep(1)
        swap_button_order.click()

        # laptop view under the VERIFY INPUT TAB
        switch_btn.nth(0).click()
        # upload logo
        upload_logo(page, file_path)
        logo_upload_confi_msg = page.locator("img[alt='Uploaded Logo']")
        expect(logo_upload_confi_msg).to_have_attribute("src", re.compile(
            r"https://storage-pp.gotrust.tech/gt-logo-bucket/uploads"))
        print("\nupload successfully")
        # reset button
        reset_btn = page.locator("button:has-text('Reset')")
        reset_btn.click()
        reset_confirmation = page.locator("img[src='/assets/svg/gotrustTitle_light.DIPQ8Yl4.svg']")
        expect(reset_confirmation.nth(0)).to_be_visible(timeout=15000)

        # full screen button
        full_screen_btn = page.locator("button:has-text('View on full screen')")
        expect(full_screen_btn).to_be_visible(timeout=15000)
        full_screen_btn.click()
        cross_btn = page.locator("span:has-text('Close')")
        cross_btn.click()
        expect(full_screen_btn).to_be_visible(timeout=15000)
        # upload logo again
        upload_logo(page, file_path)
        # otp section
        swap_button_order = page.locator("button:has-text('Swap Button Order')")
        swap_button_order.click()
        time.sleep(1)
        swap_button_order.click()
        time.sleep(1)

        # preference center tab under the laptop view ==================
        preference_center_tab = page.locator("button:has-text('Preference Center')")
        preference_center_tab.nth(1).click()
        # upload logo
        upload_logo(page, file_path)
        logo_upload_confi_msg = page.locator("img[alt='Uploaded Logo']")
        expect(logo_upload_confi_msg).to_have_attribute("src", re.compile(
            r"https://storage-pp.gotrust.tech/gt-logo-bucket/uploads"))
        print("\nupload successfully")
        # reset button
        reset_btn = page.locator("button:has-text('Reset')")
        reset_btn.click()
        reset_confirmation = page.locator("img[src='/assets/svg/gotrustTitle_light.DIPQ8Yl4.svg']")
        expect(reset_confirmation.nth(0)).to_be_visible(timeout=15000)

        # # full screen button
        # full_screen_btn = page.locator("button:has-text('View on full screen')")
        # expect(full_screen_btn).to_be_visible(timeout=15000)
        # full_screen_btn.click()
        # cross_btn = page.locator("span:has-text('Close')")
        # time.sleep(1)
        # cross_btn.click()
        # expect(full_screen_btn).to_be_visible(timeout=15000)

        # upload logo again
        upload_logo(page, file_path)

        # consent preference tab under the preference center tab
        consent_preference_tab = page.locator("button:has-text('Consent Preferences')")
        consent_preference_tab.nth(1).click()
        # dsr tab
        dsr_tab = page.locator("button:has-text('DSR')")
        dsr_tab.click()
        # consent flow tab
        consent_flow_tab = page.locator("button:has-text('Consent Flow')")
        consent_flow_tab.click()

        # mobile view under the PREFERENCE CENTER
        switch_btn.nth(0).click()
        # upload logo
        upload_logo(page, file_path)
        logo_upload_confi_msg = page.locator("img[alt='Uploaded Logo']")
        expect(logo_upload_confi_msg).to_have_attribute("src", re.compile(
            r"https://storage-pp.gotrust.tech/gt-logo-bucket/uploads"))
        print("\nupload successfully")
        # reset button
        reset_btn = page.locator("button:has-text('Reset')")
        reset_btn.click()
        reset_confirmation = page.locator("img[src='/assets/svg/gotrustTitle_light.DIPQ8Yl4.svg']")
        expect(reset_confirmation.nth(0)).to_be_visible(timeout=15000)

        # # full screen button
        # full_screen_btn = page.locator("button:has-text('View on full screen')")
        # expect(full_screen_btn).to_be_visible(timeout=15000)
        # full_screen_btn.click()
        # cross_btn = page.locator("span:has-text('Close')")
        # cross_btn.click()
        # expect(full_screen_btn).to_be_visible(timeout=15000)

        # upload logo again
        upload_logo(page, file_path)
        # consent preference tab under the preference center tab
        consent_preference_tab = page.locator("button:has-text('Consent Preferences')")
        consent_preference_tab.nth(1).click()
        # dsr tab
        dsr_tab = page.locator("button:has-text('DSR')")
        dsr_tab.click()
        # consent flow tab
        consent_flow_tab = page.locator("button:has-text('Consent Flow')")
        consent_flow_tab.click()

        continue_btn.click()
        # step - 6 Language
        change_language(page)
        time.sleep(1)
        get_change_language_confi_msg(page)
        expect(get_change_language_confi_msg(page)).to_be_visible(timeout=15000)

        continue_btn.click()
        # step - 7 Code Snippets
        mobile_consent_sdk_tab = page.locator("button:has-text('Mobile Consent SDK')")
        mobile_consent_sdk_tab.click()
        time.sleep(1)
        web_preference_center_tab = page.locator("button:has-text('Web Preference Center')")
        web_preference_center_tab.click()
        time.sleep(1)
        mobile_preference_sdk_tab = page.locator("button:has-text('Mobile Preference SDK')")
        mobile_preference_sdk_tab.click()
        time.sleep(1)
        # download button
        download_btn = page.locator("button:has-text('Download Guide')")
        download_btn.click()
        time.sleep(1)
        download_title_txt = page.locator("h2:has-text('Download Integration Guide')")
        expect(download_title_txt).to_be_visible(timeout=15000)

        cross_btn = page.locator("button:has(svg.lucide-x)")
        cross_btn.click()




        continue_btn.click()
        # step - 8 Workflow
        save_btn = page.locator("button:has-text('Save')")
        save_btn.click()
        ucm_title = page.locator("a:has-text('Universal Consent Management')")
        expect(ucm_title).to_be_visible(timeout=15000)
        print("\nPreference center customization successfully")









        page.wait_for_timeout(5000)


def change_language(page):
    try:
        consent_form_tab = page.locator("button:has-text('Consent Form')")
        preference_form_tab = page.locator("button:has-text('Preference Form')")
        language_btn_txt = page.locator("button[role='combobox']:nth-child(1)")
        save_translation_txt = page.locator("button:has-text('Save Translation')")

        consent_form_tab.nth(0).click()
        time.sleep(2)
        preference_form_tab.nth(0).click()
        time.sleep(2)
        language_btn_txt.click()
        dropdown = page.locator("div[role='option']")
        dropdown.filter(has_text="Hindi").click()
        save_translation_txt.click()
    except Exception as e:
        print(f" Exception while change language : {e}")
        raise

def get_change_language_confi_msg(page):
    try:
        change_language_confi_msg = page.get_by_text("Translations saved successfully")
        return change_language_confi_msg
    except Exception as e:
        print(f" Exception while getting change language confirmation successful message : {e}")
        return None

def upload_logo(page, file_path: str):
    try:
        time.sleep(2)
        page.locator("img[alt='Remove Logo'], button:has(svg.lucide-x):nth-child(2)").click()
        time.sleep(3)
        file_input = page.locator("input[type='file']")
        file_input.set_input_files(file_path)
    except Exception as e:
        print(f"Exception while uploading logo: {e}")
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


def select_consent_template_name(page, consent_template_name):
    try:
        all_consent_template_name = page.locator("table tbody tr td:first-child div")
        count = all_consent_template_name.count()
        print("\ntotal count template name : ",count)
        for i in range(count):
            text = all_consent_template_name.nth(i).inner_text().strip()
            if text.lower() == consent_template_name.lower():
                print("\template name : ", text)
                all_consent_template_name.nth(i).click()
                break
    except Exception as e:
        print(f"Exception while page extend: {e}")
        raise

def page_extend(page):
    try:
        item_per_page_txt = page.locator(".lucide.lucide-chevron-down.size-4")
        dropdown = page.locator("div[role='option']")
        item_per_page_txt.nth(1).click()
        dropdown.nth(4).click()
        time.sleep(1)
    except Exception as e:
        print(f"Exception while page extend: {e}")
        raise


