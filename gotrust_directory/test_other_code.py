from itertools import count

import pytest
from playwright.sync_api import Page, expect
import re


def test_coll_login(page:Page):
    page.goto("https://sandbox.gotrust.tech/home")
    assessment_name = "DPIA 111"

    # ASSIGNEE LOGIN
    # locators
    txt_email_address = page.locator("#username")
    txt_email_address.fill("assignee.sgt@yopmail.com")

    txt_password = page.locator("#password")
    txt_password.fill("Test@123")
    btn_login_button = page.locator("button[type='submit']")
    btn_login_button.click()

    dpia_btn = page.locator("a span:has-text('DPIA')")
    expect(dpia_btn).to_be_visible(timeout=15000)

    # Click dpia button
    dpia_btn.click()
    dpia_btn.click()

    dpia_title = page.locator("h1:has-text('Data Protection Impact Assessment')")
    expect(dpia_title).to_be_visible(timeout=15000)

    # # assessment name
    card = page.locator(
        "div.rounded-lg",
        has=page.locator(f"h3 span:has-text('{assessment_name}')")
    )
    card.locator("button:has-text('Start'), button:has-text('Continue')").first.click()

    # assessment questions and answers
    page.wait_for_timeout(2000)
    give_assessment_and_submit_for_review(page)  # this is function

    # Logout assignee
    # locators
    txt_my_account = page.locator(".hidden.text-left")  # click on account
    txt_my_account.click()
    btn_sign_out = page.get_by_role("menuitem", name="Sign out")  # click on signout button
    btn_sign_out.click()
    # btn_confirm_sign_out = page.locator("#kc-logout")  # click on confi signout button
    # btn_confirm_sign_out.click()
    signin_title = page.locator("#kc-page-title")
    expect(signin_title).to_be_visible(timeout=10000)

    # REVIEWER 1 ACCOUNT LOGIN
    # locators
    txt_email_address = page.locator("#username")
    txt_email_address.fill("braj.reviewer.sgt@yopmail.com")

    txt_password = page.locator("#password")
    txt_password.fill("123")
    btn_login_button = page.locator("button[type='submit']")
    btn_login_button.click()

    dpia_btn = page.locator("a span:has-text('DPIA')")
    expect(dpia_btn).to_be_visible(timeout=15000)

    # Click dpia button
    dpia_btn.click()
    dpia_btn.click()

    # # assessment name
    card = page.locator(
        "div.rounded-lg",
        has=page.locator(f"h3 span:has-text('{assessment_name}')")
    )
    card.locator("button:has-text('Review')").first.click()

    # assessment questions and answers
    page.wait_for_timeout(2000)
    assessment_review_and_change_request(page)  # this is function

    # Logout reviewer
    # locators
    txt_my_account = page.locator(".hidden.text-left")  # click on account
    txt_my_account.click()
    btn_sign_out = page.get_by_role("menuitem", name="Sign out")  # click on signout button
    btn_sign_out.click()
    # btn_confirm_sign_out = page.locator("#kc-logout")  # click on confi signout button
    # btn_confirm_sign_out.click()
    signin_title = page.locator("#kc-page-title")
    expect(signin_title).to_be_visible(timeout=10000)

    # ASSIGNEE LOGIN
    # locators
    txt_email_address = page.locator("#username")
    txt_email_address.fill("assignee.sgt@yopmail.com")

    txt_password = page.locator("#password")
    txt_password.fill("Test@123")
    btn_login_button = page.locator("button[type='submit']")
    btn_login_button.click()

    dpia_btn = page.locator("a span:has-text('DPIA')")
    expect(dpia_btn).to_be_visible(timeout=15000)

    # Click dpia button
    dpia_btn.click()
    dpia_btn.click()

    dpia_title = page.locator("h1:has-text('Data Protection Impact Assessment')")
    expect(dpia_title).to_be_visible(timeout=15000)

    # # assessment name
    card = page.locator(
        "div.rounded-lg",
        has=page.locator(f"h3 span:has-text('{assessment_name}')")
    )
    card.locator("button:has-text('Edit')").first.click()

    # assessment questions and answers
    page.wait_for_timeout(2000)
    give_assessment_and_submit_for_review(page)  # this is function

    # Logout assignee
    # locators
    txt_my_account = page.locator(".hidden.text-left")  # click on account
    txt_my_account.click()
    btn_sign_out = page.get_by_role("menuitem", name="Sign out")  # click on signout button
    btn_sign_out.click()
    # btn_confirm_sign_out = page.locator("#kc-logout")  # click on confi signout button
    # btn_confirm_sign_out.click()
    signin_title = page.locator("#kc-page-title")
    expect(signin_title).to_be_visible(timeout=10000)


    # REVIEWER 1 ACCOUNT LOGIN
    # locators
    txt_email_address = page.locator("#username")
    txt_email_address.fill("braj.reviewer.sgt@yopmail.com")

    txt_password = page.locator("#password")
    txt_password.fill("123")
    btn_login_button = page.locator("button[type='submit']")
    btn_login_button.click()

    dpia_btn = page.locator("a span:has-text('DPIA')")
    expect(dpia_btn).to_be_visible(timeout=15000)

    # Click dpia button
    dpia_btn.click()
    dpia_btn.click()

    # # assessment name
    card = page.locator(
        "div.rounded-lg",
        has=page.locator(f"h3 span:has-text('{assessment_name}')")
    )
    card.locator("button:has-text('Review')").first.click()

    # assessment questions and answers
    page.wait_for_timeout(2000)
    assessment_review_and_submit(page)  # this is function




    page.wait_for_timeout(3000)

def assessment_review_and_change_request(page, max_attempts=3):
    submit_btn = page.locator("button:has-text('Submit')")
    submit_msg = page.get_by_text("review submitted successfully!")

    attempt = 1

    while attempt <= max_attempts:
        change_request_review(page)
        submit_btn.wait_for(state="visible", timeout=15000)
        submit_btn.click()
        try:
            expect(submit_msg).to_be_visible(timeout=5000)
            print("Review submitted successfully")
            break
        except:
            print("Submit failed — retrying...")
            attempt += 1


def change_request_review(page):
    while True:
        yes_buttons = page.locator("button[role='radio'][value='true']")
        no_buttons = page.locator("button[role='radio'][value='false']")
        save_review_btn = page.locator("button:has-text('Save Review')")

        yes_btn_count = yes_buttons.count()

        for i in range(yes_btn_count):
            yes_buttons.nth(i).click()
            save_review_btn.nth(i).click()
            page.wait_for_timeout(1000)

        # Check navigation
        next_btn = page.locator("button:has-text('Next')")
        submit_btn = page.locator("button:has-text('Submit')")

        if submit_btn.is_visible():
            # No buttons
            no_btn_count = no_buttons.count()
            for i in range(no_btn_count):
                no_buttons.nth(i).click()
                save_review_btn.nth(i).click()
                page.wait_for_timeout(1000)
            break  # ✅ reached last page

        if next_btn.is_visible():
            next_btn.click()
            page.wait_for_timeout(1000)
        else:
            break


def assessment_review_and_submit(page, max_attempts=3):
    submit_btn = page.locator("button:has-text('Submit')")
    submit_msg = page.get_by_text("review submitted successfully!")

    attempt = 1

    while attempt <= max_attempts:
        complete_review(page)
        submit_btn.wait_for(state="visible", timeout=15000)
        submit_btn.click()
        try:
            expect(submit_msg).to_be_visible(timeout=5000)
            print("Review submitted successfully")
            break
        except:
            print("Submit failed — retrying...")
            attempt += 1


def complete_review(page):
    while True:
        yes_buttons = page.locator("button[role='radio'][value='true']")
        no_buttons = page.locator("button[role='radio'][value='false']")
        save_review_btn = page.locator("button:has-text('Save Review')")

        yes_btn_count = yes_buttons.count()

        for i in range(yes_btn_count):
            yes_buttons.nth(i).click()
            save_review_btn.nth(i).click()
            page.wait_for_timeout(1000)

        # Check navigation
        next_btn = page.locator("button:has-text('Next')")
        submit_btn = page.locator("button:has-text('Submit')")

        if submit_btn.is_visible():
            break

        if next_btn.is_visible():
            next_btn.click()
            page.wait_for_timeout(1000)
        else:
            break



def give_assessment_and_submit_for_review(page, max_attempts=3):
    submit_for_review_btn = page.locator("button:has-text('Submit')")
    submit_for_Review_msg = page.get_by_text("assessment submitted successfully!")

    attempt = 1

    while attempt <= max_attempts:
        complete_assessment(page)  # this is function
        submit_for_review_btn.wait_for(state="visible", timeout=15000)
        submit_for_review_btn.click()
        try:
            expect(submit_for_Review_msg).to_be_visible(timeout=5000)
            print("Submit for review submitted successfully")
            break
        except:
            print("Submit for review failed — retrying...")
            attempt += 1

def complete_assessment(page):
    while True:
        yes_buttons = page.locator("button[role='radio'][value='0']")
        likelihood = page.locator("label:has-text('Likelihood') + button")
        impact = page.locator("label:has-text('Impact') + button")
        dropdown = page.locator("div[role='option']")
        count = yes_buttons.count()

        for i in range(count):
            yes_buttons.nth(i).click()
            likelihood.nth(i).click()
            dropdown.nth(2).click()
            impact.nth(i).click()
            dropdown.nth(2).click()

        # Navigation handling (same pattern as your review function)
        next_btn = page.locator("button:has-text('Next')")
        submit_btn = page.locator("button:has-text('Submit for Review')")

        if submit_btn.is_visible():
            break  # ✅ last page reached

        if next_btn.is_visible():
            next_btn.click()
            page.wait_for_timeout(1000)
        else:
            break



