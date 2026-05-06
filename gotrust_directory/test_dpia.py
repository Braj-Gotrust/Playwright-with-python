import re
import time

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
        dpia_btn =page.locator("a span:has-text('DPIA')")
        expect(dpia_btn).to_be_visible(timeout=15000)

        # Click dpia button
        dpia_btn.click()
        dpia_btn.click()

        dpia_title = page.locator("h1:has-text('Data Protection Impact Assessment')")
        expect(dpia_title).to_be_visible(timeout=15000)

        assessment_name = "DPIA 112"
        assessment_description = "TEST"


        # click ADD vendor button
        page.locator("button:has-text('New Assessment')").click()

        # form title
        form_title = page.locator("h2:has-text('Create New DPIA')")
        expect(form_title).to_be_visible()

        # input fields
        page.get_by_label("Assessment Name").fill(assessment_name)
        page.get_by_label("Description").fill(assessment_description)

        # select due data
        page.locator("button:has-text('Pick a date')").click()
        page.locator("button[name='next-month']").click()
        page.get_by_role("gridcell", name="15").click()

        # select legal entity
        page.locator("span:has-text('Select legal entity')").nth(0).click()

        dropdowns = page.locator("div[role='option'] span:last-child")
        #dropdowns.nth(1).click()

        count = dropdowns.count()
        print("\nTOtal number of legal entity : ",count)

        found = False

        for i in range(count):
            dropdown_text = dropdowns.nth(i).inner_text()
            if dropdown_text == "Appvin 4":
                dropdowns.nth(i).click()
                found = True
                break
        if not found:
            dropdowns.nth(0).click()

        # select department
        page.locator("span:has-text('Select departments')").click()
        page.locator("div[role='option'] span").nth(0).click()
        close = page.locator("div[role='option']:has-text('Close')")
        close.click()

        # select assignee
        assignee_name = "keshav sharma"
        # click assignee dropdown
        page.locator("span:has-text('Select responsible person')").click()

        # wait for dropdown options
        page.wait_for_selector("[role='option']")
        # select assignee
        page.get_by_role("option", name=assignee_name).click()

        # select reviewer
        reviewer_name = "Braj Reviewer 1"
        # click assignee dropdown
        page.locator("span:has-text('Select reviewer person')").click()
        # wait for dropdown options
        page.wait_for_selector("[role='option']")
        # select assignee
        page.get_by_role("option", name=reviewer_name).click()

        # save button
        page.locator("button:has-text('Save')").click()
        save_msg = page.get_by_text("Assessment created Successfully.")
        expect(save_msg).to_be_visible(timeout=15000)
        # create assessment button
        page.locator("button:has-text('Create Assessment')").click()
        create_assessment_msg = page.get_by_text("Assessment card created successfully")
        expect(create_assessment_msg).to_be_visible(timeout=15000)


        # # assessment name
        card = page.locator(
            "div.rounded-lg",
            has=page.locator(f"h3 span:has-text('{assessment_name}')")
        )
        card.locator("button:has-text('Start'), button:has-text('Continue')").first.click()

        # add collaborator
        collaborator_name = "samarth"
        page.locator("button:has-text('Add Collaborator')").click()
        page.get_by_placeholder("Type name or email to search users...").first.fill(collaborator_name)
        page.wait_for_selector("div.text-sm.font-medium")
        page.locator("div.text-sm.font-medium").filter(has_text=collaborator_name).click()
        # click on plus button
        page.locator("button:has(svg.lucide-plus)").first.click()
        # collaborator add confirmation message
        collab_add_confi_msg = page.get_by_text("Collaborator added successfully")
        expect(collab_add_confi_msg).to_be_visible(timeout=10000)
        close = page.locator("button:has-text('Close')").first
        close.click()

        # Logout dpo
        # locators
        txt_my_account = page.locator(".hidden.text-left")  # click on account
        txt_my_account.click()
        btn_sign_out = page.get_by_role("menuitem", name="Sign out")  # click on signout button
        btn_sign_out.click()
        # btn_confirm_sign_out = page.locator("#kc-logout")  # click on confi signout button
        # btn_confirm_sign_out.click()
        signin_title = page.locator("#kc-page-title")
        expect(signin_title).to_be_visible(timeout=10000)


        # COLLABORATOR LOGIN
        # locators
        txt_email_address = page.locator("#username")
        txt_email_address.fill("samarth.collab@yopmail.com")
        txt_password = page.locator("#password")
        txt_password.fill("123")
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
        yes_buttons = page.locator("button[role='radio'][value='0']")
        no_buttons = page.locator("button[role='radio'][value='1']")
        not_buttons = page.locator("button[role='radio'][value='2']")

        # questions
        likelihood = page.locator("label:has-text('Likelihood') + button")
        dropdown = page.locator("div[role='option']")
        impact = page.locator("label:has-text('Impact') + button")

        yes_count = yes_buttons.count()
        for i in range(yes_count):
            yes_buttons.nth(i).click()
            likelihood.nth(i).click()
            dropdown.nth(2).click()
            impact.nth(i).click()
            dropdown.nth(2).click()

        submit_for_review_btn = page.locator("button:has-text('Submit for Review')")
        submit_for_review_btn.click()

        # Logout collaborator
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


        page.wait_for_timeout(5000)

    else:
        # Invalid login validation
        expect(page.locator("div[aria-live='polite']")).to_be_visible(timeout=5000)


def give_assessment_and_submit_for_review(page, max_attempts=3):
    submit_for_review_btn = page.locator("button:has-text('Submit for Review')")
    submit_for_Review_msg = page.get_by_text("DPIA assessment submitted successfully!")

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
    submit_msg = page.get_by_text("DPIA review submitted successfully!")

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
        save_review_btn = page.locator("button:has-text('Save Review')")

        count = yes_buttons.count()

        for i in range(count):
            yes_buttons.nth(i).click()
            save_review_btn.nth(i).click()
            page.wait_for_timeout(1000)

        # Check navigation
        next_btn = page.locator("button:has-text('Next')")
        submit_btn = page.locator("button:has-text('Submit')")

        if submit_btn.is_visible():
            break   # ✅ reached last page

        if next_btn.is_visible():
            next_btn.click()
            page.wait_for_timeout(1000)
        else:
            break