import re
import time
from itertools import count

import pytest
from playwright.sync_api import expect, Page

login_test_data = [("dpo.preprod@yopmail.com", "Test@123", "valid")]
#login_test_data = [("dpo.sgt@yopmail.com", "Test@123", "valid")]

# TEST DATA
processing_category_name = "master 1"
processing_activity_name_1 = "act 1"
processing_activity_name_2 = "act 2"
pii_label_name = "phone number"
processing_purpose_name = "purp 1"


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
        pii_label_inventory_btn =page.locator("span:has-text('PII Label Inventory')")
        expect(pii_label_inventory_btn).to_be_visible(timeout=15000)


        pii_label_inventory_btn.click()
        pii_label_inventory_btn.click()

        ucm_title = page.locator("a:has-text('Universal Consent Management')")
        expect(ucm_title).to_be_visible(timeout=15000)

        # click search box
        page.locator("input[placeholder='Search']").fill(pii_label_name)
        page.wait_for_timeout(1000)


        # select pii label
        select_pii_label(page)

        # click yes button
        page.locator("button[role='radio']").nth(0).click()
        save_btn = page.locator("button:has-text('Save')")
        save_btn.click()

        pii_label_update_confi_msg = page.get_by_text("PII label updated successfully")
        expect(pii_label_update_confi_msg).to_be_visible(timeout=15000)

        # add processing category
        page.locator("a:has-text('Processing Category')").nth(1).click()
        page.locator("button:has-text('Add Processing Category')").click()
        name_txt = page.locator("#name")
        name_txt.fill(processing_category_name)
        description_txt = page.locator("#description")
        description_txt.fill("test")
        save_btn.click()
        add_processing_category_confi_msg = page.get_by_text("Processing category added successfully")
        expect(add_processing_category_confi_msg).to_be_visible(timeout=15000)

        # extend pagination
        page_extend(page)

        # select processing category
        select_processing_category_in_table(page)

        # add processing activity under the category name
        name_txt = page.locator("#name")
        name_txt.fill(processing_activity_name_1)
        description_txt = page.locator("#description")
        description_txt.fill("test")
        add_btn = page.locator("button:has-text('Add')")
        add_btn.nth(1).click()
        add_processing_activity_confi_msg_1 = page.get_by_text("Processing activity added successfully")
        expect(add_processing_activity_confi_msg_1).to_be_visible(timeout=15000)

        # add processing activity

        page.locator("a:has-text('Processing Activities')").nth(1).click()
        page.locator("button:has-text('Add Processing Activities')").click()
        name_txt = page.locator("#name")
        name_txt.fill(processing_activity_name_2)

        page.wait_for_timeout(1000)
        select_processing_category_in_list(page)
        page.wait_for_timeout(1000)

        description_txt = page.locator("#description")
        description_txt.fill("test")
        save_btn.click()
        add_processing_activity_confi_msg_2 = page.get_by_text("Processing activities added successfully")
        expect(add_processing_activity_confi_msg_2).to_be_visible(timeout=15000)

        # add processing purpose
        page.locator("a:has-text('Processing Purpose')").nth(1).click()
        page.locator("button:has-text('Add Processing Purpose')").click()
        name_txt = page.locator("#name")
        name_txt.fill(processing_purpose_name)

        select_processing_activity(page)

        description_txt = page.locator("#description")
        description_txt.fill("test")
        # expiry days
        page.locator("input[placeholder='Enter expiry']").clear()
        page.locator("input[placeholder='Enter expiry']").fill("7")

        save_btn.click()
        add_processing_purpose_confi_msg = page.get_by_text("Processing purpose added successfully")
        expect(add_processing_purpose_confi_msg).to_be_visible(timeout=15000)





        page.wait_for_timeout(5000)

def select_pii_label(page):
    try:
        all_pii_label = page.locator("table tbody tr p")
        edit_btn = page.locator("button:has(svg.lucide-pencil)")
        count = all_pii_label.count()
        for i in range(count):
            print("\n pii label count", count)
            text = all_pii_label.nth(i).inner_text().strip()
            if text.lower() == pii_label_name.lower():
                print("\n pii label name", text)
                edit_btn.nth(i).click()
                break
    except Exception as e:
        print(f"Exception while selecting pii label name: {e}")
        raise

def page_extend(page):
    try:
        item_per_page_txt = page.locator(".lucide.lucide-chevron-down.size-4")
        dropdown = page.locator("div[role='option']")
        item_per_page_txt.click()
        dropdown.nth(4).click()
        time.sleep(1)
    except Exception as e:
        print(f"Exception while page extend: {e}")
        raise

def select_processing_category_in_table(page):
    try:
        all_processing_category = page.locator("table tbody tr p")
        plus_btn = page.locator("button:has(svg.lucide-plus)")
        count = all_processing_category.count()
        for i in range(count):
            print("\n processing category count", count)
            text = all_processing_category.nth(i).inner_text().strip()
            if text.lower() == processing_category_name.lower():
                print("\n processing category name", text)
                plus_btn.nth(i).click()
                break
    except Exception as e:
        print(f"Exception while selecting processing category name: {e}")
        raise

def select_processing_category_in_list(page):
    try:
        page.locator("span:has-text('Select')").click()
        dropdown = page.locator("div[role='option']")
        count = dropdown.count()
        for i in range(count):
            print("\n processing category count", count)
            text = dropdown.nth(i).inner_text().strip()
            if text.lower() == processing_category_name.lower():
                print("\n processing category name", text)
                dropdown.nth(i).click()
                break

    except Exception as e:
        print(f"Exception while selecting processing category name: {e}")
        raise

def select_processing_activity(page):
    try:
        page.locator("span:has-text('Select')").click()
        dropdown = page.locator("div[role='option']")
        count = dropdown.count()
        for i in range(count):
            print("\n processing category count", count)
            text = dropdown.nth(i).inner_text().strip()
            if text.lower() == processing_activity_name_1.lower():
                print("\n processing category name", text)
                dropdown.nth(i).click()
                break

    except Exception as e:
        print(f"Exception while selecting processing activity name: {e}")
        raise















