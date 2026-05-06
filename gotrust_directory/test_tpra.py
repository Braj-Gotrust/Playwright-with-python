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
        tpra_btn =page.locator("a span:has-text('TPRA')").nth(0)
        expect(tpra_btn).to_be_visible(timeout=15000)

        # Click ropa registry button
        tpra_btn.click()
        tpra_btn.click()

        tpra_title = page.locator("h1:has-text('Third Party Risk Assessment')")
        expect(tpra_title).to_be_visible(timeout=15000)

        vendor_name = "vendor 8"
        vendor_email = "vendor.8@yopmail.com"


        # click ADD vendor button
        page.locator("button:has-text('Add Vendor')").click()

        # form title
        form_title = page.locator("h2:has-text('Add Vendor')")
        expect(form_title).to_be_visible()

        # input fields
        page.get_by_placeholder("Enter vendor name").fill(vendor_name)
        page.get_by_placeholder("Enter email").nth(0).fill(vendor_email)
        page.get_by_placeholder("Enter address").fill("Noida")
        page.get_by_placeholder("Enter admin name").fill("vendor 1 admin name")
        page.get_by_placeholder("Enter phone number").fill("9876543210")

        # select legal entity
        page.locator("span:has-text('Select legal entities')").click()

        dropdowns = page.locator("div[role='group'] span")
        close = page.locator("div[role='option']:has-text('Close')")
        #dropdowns.nth(1).click()

        count = dropdowns.count()
        print("\nTOtal number of legal entity : ",count)

        found = False

        for i in range(count):
            dropdown_text = dropdowns.nth(i).inner_text()
            if dropdown_text == "Appvin 4":
                dropdowns.nth(i).click()
                close.click()
                found = True
                break
        if not found:
            dropdowns.nth(1).click()
            close.click()

        # save and continue button
        page.locator("button:has-text('Save and continue')").click()
        vendor_add_confi_msg = page.get_by_text("Vendor added successfully")
        expect(vendor_add_confi_msg).to_be_visible(timeout=10000)


        # this locator to wait until vendor table properly load
        page.locator("tbody tr").first.wait_for(state="visible", timeout=15000)
        vendor_name_list = page.locator("tbody tr td:first-child span")
        count_vendor = vendor_name_list.count()
        print("\nTotal number of vendor : ", count_vendor)
        for i in range(count_vendor):
            text = vendor_name_list.nth(i).inner_text()
            if vendor_name in text:
                vendor_name_list.nth(i).click()
                break

        page.locator("button:has-text('Start Vendor Assessment')").click()
        page.get_by_placeholder("Description").fill("test")

        # select legal entity
        page.locator("span:has-text('Select legal entity')").click()
        dropdowns = page.locator("div[role='option'] span span")
        count = dropdowns.count()
        print("\nTOtal number of legal entity : ", count)
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
        page.locator("div[role='option'] span").nth(1).click()
        close = page.locator("div[role='option']:has-text('Close')")
        close.click()


        # select SPOC
        page.locator("span:has-text('Select Internal SPOC')").click()
        spoc_list = page.locator("div[role='option'] span:nth-child(2)")
        count = spoc_list.count()
        for i in range(count):
            time.sleep(1)
            text = spoc_list.nth(i).inner_text()
            if "Braj Reviewer 2" in text:
                spoc_list.nth(i).click()
                break

        # select-  type of vendor
        page.get_by_label("Types of Vendor").click()
        page.locator("div[role='option'] span:nth-child(2)").nth(2).click()
        # select intake template
        page.locator("span:has-text('Select Intake Template')").click()
        page.locator("span:has-text('Intake Assessment(Default)')").click()

        # select assessment due date
        page.get_by_label("Assessment Due Date").nth(0).click()
        page.locator("button[name='next-month']").click()
        page.get_by_role("gridcell", name="15").click()

        # select Vendor Risk Assessment Due Date
        page.get_by_label("Vendor Risk Assessment Due Date").click()
        time.sleep(3)
        page.locator("button[name='next-month']").click()
        time.sleep(3)
        page.get_by_role("gridcell", name="10").click()


        # click assignee
        page.locator("span:has-text('Select assignee name')").click()
        # select assignee
        assignee_list = page.locator("div[role='option'] span:nth-child(2)")
        # assignee_list.nth(1).click()
        count = assignee_list.count()
        print("\nTotal number of Assignee : ", count)
        for i in range(count):
            text = assignee_list.nth(i).inner_text()
            if "keshav sharma" in text:
                assignee_list.nth(i).click()
                print("\nSelected index number:", i)
                break

        # select reviewer
        page.locator("span:has-text('Select reviewer name')").click()
        reviewer_list = page.locator("div[role='option'] span:nth-child(2)")
        count = reviewer_list.count()
        print("\nTotal number of reviewer : ", count)
        for i in range(count):
            text = reviewer_list.nth(i).inner_text()
            if "Braj Reviewer 1" in text:
                reviewer_list.nth(i).click()
                time.sleep(3)
                break

        # save and continue button - start vendor assessment
        page.locator("button:has-text('Save and continue')").click()
        vendor_assessment_confi_msg = page.get_by_text("Assessment created successfully")
        expect(vendor_assessment_confi_msg).to_be_visible(timeout=10000)

        # this locator to wait until vendor assessment table properly load
        page.locator("tbody tr").first.wait_for(state="visible", timeout=15000)
        vendor_assess = page.locator("tbody tr td:first-child")
        vendor_assess.nth(0).click()

        # save and next
        page.locator("button:has-text('Save and Next')").click()


        # add collaborator
        page.locator("button:has-text('Add Collaborator')").click()
        # popup collaborator
        collaborator_popup = page.locator("h2:has-text('Assign Collaborators')")
        expect(collaborator_popup).to_be_visible(timeout=15000)
        # click collaborator dropdown
        page.locator("button:has-text('Select collaborators')").click()
        # select collaborator
        collaborator_list = page.locator("div[role='group'] span")
        close = page.locator("div[role='option']:has-text('Close')")
        count = collaborator_list.count()
        print("\nTotal number of collaborator : ", count)
        for i in range(count):
            text = collaborator_list.nth(i).inner_text()
            if "samarth" in text:
                collaborator_list.nth(i).click()
                close.click()
                break

        # click collaborator submit button
        page.locator("//button[normalize-space()='Submit']").click()

        # collaborator add confirmation message
        collab_add_confi_msg = page.get_by_text("Collaborator added successfully!")
        expect(collab_add_confi_msg).to_be_visible(timeout=10000)



        # Logout dpo
        # locators
        txt_my_account = page.locator(".hidden.text-left")  # click on account
        txt_my_account.click()
        btn_sign_out = page.get_by_role("menuitem", name="Sign out")  # click on signout button
        btn_sign_out.click()
        btn_confirm_sign_out = page.locator("#kc-logout")  # click on confi signout button
        btn_confirm_sign_out.click()
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

        # Wait for dashboard load
        tpra_btn = page.locator("a span:has-text('TPRA')").nth(0)
        expect(tpra_btn).to_be_visible(timeout=15000)

        # Click ropa registry button
        tpra_btn.click()
        tpra_btn.click()

        tpra_title = page.locator("h1:has-text('Third Party Risk Assessment')")
        expect(tpra_title).to_be_visible(timeout=15000)

        # this locator to wait until vendor table properly load
        page.locator("tbody tr").first.wait_for(state="visible", timeout=15000)
        vendor_name_list = page.locator("tbody tr td:first-child span")
        count_vendor = vendor_name_list.count()
        print("\nTotal number of vendor : ", count_vendor)
        for i in range(count_vendor):
            text = vendor_name_list.nth(i).inner_text()
            if vendor_name in text:
                vendor_name_list.nth(i).click()
                break

        # this locator to wait until vendor assessment table properly load
        page.locator("tbody tr").first.wait_for(state="visible", timeout=15000)
        vendor_assess = page.locator("tbody tr td:first-child")
        vendor_assess.nth(0).click()

        # Giving the answers of the assessment
        # 1 question
        questions = page.locator("button[role='combobox']")
        questions.nth(0).click()
        answers = page.locator("div[role='option']")
        answers.nth(1).click()  # no

        # 2 question
        questions.nth(1).click()
        answers.nth(0).click()  # yes

        # 3 question
        questions.nth(2).click()
        answers.nth(0).click()  # yes

        # 4 question
        questions.nth(3).click()
        answers.nth(1).click()  # no

        # 5 question
        questions.nth(4).click()
        answers.nth(0).click()  # yes

        # 6 question
        questions.nth(5).click()
        answers.nth(1).click()  # no

        # 7 question
        questions.nth(6).click()
        answers.nth(0).click()  # yes

        # 8 question
        questions.nth(7).click()
        answers.nth(1).click()  # no

        # save button
        page.locator("button:has-text('Save')").click()
        save_msg = page.get_by_text("Saved successfully").first
        expect(save_msg).to_be_visible(timeout=15000)

        # Logout collaborator
        # locators
        txt_my_account = page.locator(".hidden.text-left")  # click on account
        txt_my_account.click()
        btn_sign_out = page.get_by_role("menuitem", name="Sign out")  # click on signout button
        btn_sign_out.click()
        btn_confirm_sign_out = page.locator("#kc-logout")  # click on confi signout button
        btn_confirm_sign_out.click()
        signin_title = page.locator("#kc-page-title")
        expect(signin_title).to_be_visible(timeout=10000)



        # ASSIGNEE ACCOUNT LOGIN
        # locators
        txt_email_address = page.locator("#username")
        txt_email_address.fill("assignee.sgt@yopmail.com")

        txt_password = page.locator("#password")
        txt_password.fill("Test@123")
        btn_login_button = page.locator("button[type='submit']")
        btn_login_button.click()

        # Wait for dashboard load
        tpra_btn = page.locator("a span:has-text('TPRA')").nth(0)
        expect(tpra_btn).to_be_visible(timeout=15000)

        # Click ropa registry button
        tpra_btn.click()
        tpra_btn.click()

        tpra_title = page.locator("h1:has-text('Third Party Risk Assessment')")
        expect(tpra_title).to_be_visible(timeout=15000)

        # this locator to wait until vendor table properly load
        page.locator("tbody tr").first.wait_for(state="visible", timeout=15000)
        vendor_name_list = page.locator("tbody tr td:first-child span")
        count_vendor = vendor_name_list.count()
        print("\nTotal number of vendor : ", count_vendor)
        for i in range(count_vendor):
            text = vendor_name_list.nth(i).inner_text()
            if vendor_name in text:
                vendor_name_list.nth(i).click()
                break

        # this locator to wait until vendor assessment table properly load
        page.locator("tbody tr").first.wait_for(state="visible", timeout=15000)
        vendor_assess = page.locator("tbody tr td:first-child")
        vendor_assess.nth(0).click()  # list name of vendor assessment

        # save and submit for review
        page.locator("button:has-text('Save')").click()
        page.locator("button:has-text('Submit for Review')").click()
        submit_for_Review_msg = page.get_by_text("Assessment submitted successfully")
        expect(submit_for_Review_msg).to_be_visible(timeout=15000)

        # ASSIGNEE SIGN OUT
        # locators
        txt_my_account = page.locator(".hidden.text-left")  # click on account
        txt_my_account.click()
        btn_sign_out = page.get_by_role("menuitem", name="Sign out")  # click on signout button
        btn_sign_out.click()
        btn_confirm_sign_out = page.locator("#kc-logout")  # click on confi signout button
        btn_confirm_sign_out.click()
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

        # Wait for dashboard load
        tpra_btn = page.locator("a span:has-text('TPRA')").nth(0)
        expect(tpra_btn).to_be_visible(timeout=15000)

        # Click ropa registry button
        tpra_btn.click()
        tpra_btn.click()

        tpra_title = page.locator("h1:has-text('Third Party Risk Assessment')")
        expect(tpra_title).to_be_visible(timeout=15000)

        # this locator to wait until vendor table properly load
        page.locator("tbody tr").first.wait_for(state="visible", timeout=15000)
        vendor_name_list = page.locator("tbody tr td:first-child span")
        count_vendor = vendor_name_list.count()
        print("\nTotal number of vendor : ", count_vendor)
        for i in range(count_vendor):
            text = vendor_name_list.nth(i).inner_text()
            if vendor_name in text:
                vendor_name_list.nth(i).click()
                break

        # this locator to wait until vendor assessment table properly load
        page.locator("tbody tr").first.wait_for(state="visible", timeout=15000)
        vendor_assess = page.locator("tbody tr td:first-child")
        vendor_assess.nth(0).click()  # list name of vendor assessment
        page.wait_for_timeout(3000)

        # click all yes button like review all answers
        all_yes_button = page.locator("label:has-text('Yes')")
        count_yes_btn = all_yes_button.count()
        print("\nTotal number of yes button : ", count_yes_btn)
        for i in range(count_yes_btn):
            all_yes_button.nth(i).click()
        page.locator("button:has-text('Save')").click()
        save_review_msg = page.get_by_text(re.compile(r"Review saved successfully|Success!"))
        expect(save_review_msg.first).to_be_visible(timeout=15000)

        # REVIEWER SIGN OUT
        # locators
        txt_my_account = page.locator(".hidden.text-left")  # click on account
        txt_my_account.click()
        btn_sign_out = page.get_by_role("menuitem", name="Sign out")  # click on signout button
        btn_sign_out.click()
        btn_confirm_sign_out = page.locator("#kc-logout")  # click on confi signout button
        btn_confirm_sign_out.click()
        signin_title = page.locator("#kc-page-title")
        expect(signin_title).to_be_visible(timeout=10000)

        # DPO LOGIN
        # locators
        txt_email_address = page.locator("#username")
        txt_email_address.fill("dpo.sgt@yopmail.com")

        txt_password = page.locator("#password")
        txt_password.fill("Test@123")
        btn_login_button = page.locator("button[type='submit']")
        btn_login_button.click()

        # Wait for dashboard load
        tpra_btn = page.locator("a span:has-text('TPRA')").nth(0)
        expect(tpra_btn).to_be_visible(timeout=15000)

        # Click ropa registry button
        tpra_btn.click()
        tpra_btn.click()

        tpra_title = page.locator("h1:has-text('Third Party Risk Assessment')")
        expect(tpra_title).to_be_visible(timeout=15000)

        # this locator to wait until vendor table properly load
        page.locator("tbody tr").first.wait_for(state="visible", timeout=15000)
        vendor_name_list = page.locator("tbody tr td:first-child span")
        count_vendor = vendor_name_list.count()
        print("\nTotal number of vendor : ", count_vendor)
        for i in range(count_vendor):
            text = vendor_name_list.nth(i).inner_text()
            if vendor_name in text:
                vendor_name_list.nth(i).click()
                break

        # this locator to wait until vendor assessment table properly load
        page.locator("tbody tr").first.wait_for(state="visible", timeout=15000)
        vendor_assess = page.locator("tbody tr td:first-child")
        vendor_assess.nth(0).click()  # list name of vendor assessment

        # Save and submit button
        page.locator("button:has-text('Save')").click()
        page.locator("button:has-text('Submit')").click()
        submit_dpo_msg = page.get_by_text("Assessment reviewed successfully")
        expect(submit_dpo_msg).to_be_visible(timeout=15000)

        # DD popup modal
        dd_popup_modal = page.locator("button:has-text('Proceed to Due Diligence')")
        expect(dd_popup_modal).to_be_visible(timeout=15000)
        dd_popup_modal.click()

        # select default dd template
        page.get_by_label("DUE Diligence ( Default )").click()
        page.locator("button:has-text('Continue')").click()

        # DPO SIGN OUT
        # locators
        txt_my_account = page.locator(".hidden.text-left")  # click on account
        txt_my_account.click()
        btn_sign_out = page.get_by_role("menuitem", name="Sign out")  # click on signout button
        btn_sign_out.click()
        btn_confirm_sign_out = page.locator("#kc-logout")  # click on confi signout button
        btn_confirm_sign_out.click()
        signin_title = page.locator("#kc-page-title")
        expect(signin_title).to_be_visible(timeout=10000)



        page.wait_for_timeout(5000)


    else:
        # Invalid login validation
        expect(page.locator("div[aria-live='polite']")).to_be_visible(timeout=5000)




