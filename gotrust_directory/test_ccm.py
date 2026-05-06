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
        ccm_btn =page.locator("a span:has-text('Cookie Consent')").nth(0)
        expect(ccm_btn).to_be_visible(timeout=15000)

        # Click ccm button
        ccm_btn.click()
        ccm_btn.click()

        ccm_title = page.locator("h1:has-text('Cookie Consent Management')")
        expect(ccm_title).to_be_visible(timeout=15000)

        #page.wait_for_timeout(3000)
        # click banner builder tab
        page.locator("button:has-text('Banner Builder')").click()

        # domain details
        domain_name = "HDFC BANK"
        domain_url = "https://www.hdfc.bank.in/"
        cookie_policy_link = "https://www.hdfc.bank.in/privacy-policy"

        category_name = "category 4"
        category_description = "test"

        service_name = "service 4"
        service_description = "test"

        cookie_key_name = "key 4"
        cookie_key_description = "test"


        # banner builder create button
        create_btn =  page.locator("button:has-text('Create')")
        create_btn.click()

        page.wait_for_timeout(1000)

        page.get_by_label("Domain Name").fill(domain_name)
        page.get_by_label("Domain URL").fill(domain_url)
        page.get_by_label("Cookie Policy Link").fill(cookie_policy_link)

        # consent framework
        page.get_by_label("Consent Framework").click()
        page.locator("span:has-text('General Data Protection Regulation (GDPR)')").click()
        page.locator("span:has-text('Digital Personal Data Protection Act, 2023 (DPDPA)')").click()
        close = page.locator("div[role='option']:has-text('Close')")
        close.click()

        # next button
        page.locator("button:has-text('Next')").click()
        create_domain_confi_msg = page.get_by_text("Domain details updated successfully")
        expect(create_domain_confi_msg).to_be_visible(timeout=15000)

        # auto scan
        page.locator("button[role='switch']").click()
        page.locator("span:has-text('Select Frequency')").click()
        dropdown = page.locator("div[role='option']")
        dropdown.nth(2).click()

        # scan now button
        page.locator("button:has-text('Scan Now')").click()

        # next button
        page.locator("button:has-text('Next')").click()

        # category and service tab
        page.locator("button:has-text('Category & Service')").click()

        # add category button
        page.locator("button:has-text('Add Category')").click()
        page.get_by_label("Category Name ").fill(category_name)
        page.get_by_label("Description ").fill(category_description)

        # create button
        create_btn.click()
        add_category_confi_msg = page.get_by_text("Category saved successfully")
        expect(add_category_confi_msg).to_be_visible(timeout=15000)

        # # Items per page
        # page.locator(".lucide.lucide-chevron-down.size-4").click()
        # dropdown = page.locator("div[role='option']")
        # dropdown.nth(4).click()
        #
        # page.wait_for_timeout(1000)
        #
        # # select domain name
        # all_domain_name = page.locator("tbody td:nth-child(1)")
        # domain_count = all_domain_name.count()
        # for i in range(domain_count):
        #     text = all_domain_name.nth(i).inner_text()
        #     if text == domain_name:
        #         all_domain_name.nth(i).click()
        #         break
        # # select domain name confirmation
        # select_domain_name_confi = page.locator("p:has-text('Cookie Configuration')")
        # expect(select_domain_name_confi).to_be_visible(timeout=15000)
        #
        # # next button
        # page.wait_for_timeout(3000)
        # page.locator("button:has-text('Next')").click()
        # page.wait_for_timeout(1000)
        # # next button
        # page.locator("button:has-text('Next')").click()
        # page.wait_for_timeout(3000)
        #






        page.wait_for_timeout(1000)
        # select category name
        all_category_name = page.locator("tbody td:nth-child(1)")

        plus_btn = page.locator("button:has(svg.lucide-circle-plus)")
        category_count = all_category_name.count()
        for i in range(category_count):
            text = all_category_name.nth(i).inner_text().strip()
            if text.lower() == category_name.lower():
                plus_btn.nth(i).click()
                break

        # select category name confirmation
        select_category_name_confi = page.locator("h2:has-text('Add Service')")
        expect(select_category_name_confi).to_be_visible(timeout=15000)

        # add service
        page.locator("#name").fill(service_name)
        page.locator("#description").fill(service_description)
        page.wait_for_timeout(1000)
        create_btn = page.locator("button:has-text('Create')")
        create_btn.click()

        add_service_confi_msg = page.get_by_text("Service saved successfully")
        expect(add_service_confi_msg).to_be_visible(timeout=15000)
        page.wait_for_timeout(3000)



        # unique cookies tab
        page.locator("button:has-text('Unique Cookies')").click()
        page.locator("p:has-text('Add Cookies')").click()

        # add cookies key
        page.locator("#cookie_key").fill(cookie_key_name)
        page.locator("#description").fill(cookie_key_description)
        page.locator("#path").fill("/")

        # select cookie category
        # select dropdown value
        dropdown = page.locator("#category_id")
        options = page.locator("#category_id option")
        count = options.count()
        for i in range(count):
            text = options.nth(i).inner_text().strip()
            if text.lower() == category_name.lower():
                value = options.nth(i).get_attribute("value")
                dropdown.select_option(value=value)
                break

        # select cookie service
        # select dropdown value
        dropdown = page.locator("#cookie_service_id")
        options = page.locator("#cookie_service_id option")
        count = options.count()
        for i in range(count):
            text = options.nth(i).inner_text().strip()
            if text.lower() == service_name.lower():
                value = options.nth(i).get_attribute("value")
                dropdown.select_option(value=value)
                break

        # # select cookie type
        page.locator("#cookie_type").select_option(value="first-party")

        # # select cookie regulation
        page.locator("#regulation_id").select_option(value="121")

        # click session
        page.locator("input[value='session']").click()
        # fill domain
        page.locator("#scanned_cookie_domain").fill("braj/test.com")

        # create button
        create_btn = page.locator("button:has-text('Create')")
        create_btn.click()
        add_cookie_confi_msg = page.get_by_text("Cookie created successfully")
        expect(add_cookie_confi_msg).to_be_visible(timeout=15000)
        page.wait_for_timeout(3000)



        # select compliance tab
        page.locator("button:has-text('Compliance')").click()
        page.locator("span:has-text('Add Audit Observation')").nth(0).click()
        page.locator("#description").fill("observation")
        save_btn = page.locator("button:has-text('Save')")
        save_btn.click()
        add_observation_confi_msg = page.get_by_text("Observation added successfully")
        expect(add_observation_confi_msg).to_be_visible(timeout=15000)

        # add duty
        # click observation
        page.locator("button[aria-haspopup='dialog']").nth(0).click()
        page.locator("button:has-text('Add duty')").click()
        # fill duty details
        page.get_by_placeholder("Duty Title").fill("duty")
        page.locator("span:has-text('Select Assignee')").click()
        page.locator("div[role='group'] span").nth(1).click()
        close_btn = page.locator("div[role='option']:has-text('Close')")
        close_btn.click()
        # select due data
        page.locator("button:has-text('Pick a date')").click()
        page.locator("button[name='next-month']").click()
        page.get_by_role("gridcell", name="15").click()

        page.get_by_label("Entity").click()
        dropdown = page.locator("div[role='option']")
        dropdown.nth(1).click()

        page.get_by_placeholder("Enter your standards here...").fill("standards")
        page.get_by_placeholder("Enter your comments here...").fill("comments")

        add_btn = page.locator("button.gotrust-button:has-text('Add')")
        add_btn.click()
        add_duty_confi_msg = page.get_by_text("Duty is created successfully")
        expect(add_duty_confi_msg).to_be_visible(timeout=15000)

        page.wait_for_timeout(3000)

        # add action
        # click observation
        page.locator("button[aria-haspopup='dialog']").nth(0).click()
        # click add action
        page.locator("button:has-text('Add action')").click()
        # fill action details
        page.get_by_placeholder("Category").fill("category")
        page.get_by_placeholder("Description").fill("test")
        page.get_by_label("Entity").click()
        dropdown = page.locator("div[role='option']")
        dropdown.nth(1).click()
        # select due data
        page.locator("button:has-text('Pick a date')").nth(0).click()
        page.locator("button[name='next-month']").click()
        page.get_by_role("gridcell", name="15").click()

        page.get_by_label("Assigned by").click()
        dropdown.nth(1).click()
        page.get_by_label("Assigned To").click()
        dropdown.nth(1).click()

        # select due data
        page.locator("button:has-text('Pick a date')").click()
        page.locator("button[name='next-month']").click()
        page.get_by_role("gridcell", name="15").click()

        page.wait_for_timeout(2000)

        # select due data
        page.locator("button:has-text('Pick a date')").click()
        page.locator("button[name='next-month']").click()
        page.get_by_role("gridcell", name="15").click()

        add_btn = page.locator("button.gotrust-button:has-text('Add')")
        add_btn.click()
        add_action_confi_msg = page.get_by_text("Action Added Successfully")
        expect(add_action_confi_msg).to_be_visible(timeout=15000)




        # select compliance tab
        page.locator("button:has-text('Recommendations')").click()







        page.wait_for_timeout(5000)

























