import re

import pytest
from playwright.sync_api import expect, Page

login_test_data = [("dpo.sgt@yopmail.com", "Test@123", "valid")]


@pytest.mark.parametrize("email,password,validity", login_test_data)
def test_login_data_driven(email, password, validity, page: Page):
    page.goto("https://sandbox.gotrust.tech/home")

    # Login
    page.get_by_role("textbox", name="Username or email").fill(email)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Sign In").click()

    if validity == "valid":
        # Wait for dashboard load
        ropa_registry_btn =page.locator("a span:has-text('Ropa Registry')")
        expect(ropa_registry_btn).to_be_visible(timeout=15000)
        print("\nROPA TEXT : ",ropa_registry_btn.inner_text())

        # Click ropa registry button
        ropa_registry_btn.click()
        ropa_registry_btn.click()

        ropa_title = page.locator("h1:has-text('ROPA Registry')")
        expect(ropa_title).to_be_visible(timeout=15000)

        # click processing activity button
        page.locator("button:has-text('Processing Activity')").click()

        # form title
        form_title = page.locator("form h3:has-text('Processing Activity Information')")
        expect(form_title).to_be_visible()


        # input fields
        ropa_name = "ROPA 337"
        page.get_by_placeholder("e.g., Customer Registration").fill(ropa_name)
        page.get_by_placeholder("Short explanation...").fill("ROPA 302 description")

        # select legal entity
        page.locator("span:has-text('Select legal entity')").nth(0).click()

        dropdowns = page.locator("div[role='presentation'] span span")
        #dropdowns.nth(1).click()

        count = dropdowns.count()
        print("\nTOtal number of element : ",count)

        for i in range(count):
            dropdown_text = dropdowns.nth(i).inner_text()
            if dropdown_text == "Appvin 4":
                dropdowns.nth(i).click()
                break


        # select department
        page.locator("span:has-text('Select department')").click()
        page.locator("div[role='option'] span span").nth(0).click()


        # select due date
        due_date = page.locator("div.mt-2 button[aria-haspopup='dialog']")
        is_future = True
        month_year = "May 2026"
        date = "25"
        due_date.click()
        calender_haeder = page.locator("div[aria-live='polite']")
        expect(calender_haeder).to_be_visible(timeout=15000)
        select_date(page, month_year, date, is_future)
        print("selected date ======> : ", due_date.inner_text())
        expect(due_date).to_be_visible(timeout=15000)

        # click assignee
        page.locator("span:has-text('Select assignee')").click()
        # select assignee
        assignee_list = page.locator("div[role='option'] span span")
        #assignee_list.nth(1).click()
        count = assignee_list.count()
        print("\nTotal number of Assignee : ",count)
        for i in range(count):
            text = assignee_list.nth(i).inner_text()
            if "keshav sharma" in text:
                assignee_list.nth(i).click()
                print("\nSelected index number:",i)
                break


        # click yes button
        page.locator("label:has-text('Yes')").click()
        # level 2 reviewer title
        level_2_reviewer_title = page.locator("label:has-text('Do you want to add more level of reviewer?')")
        expect(level_2_reviewer_title).to_be_visible(timeout=15000)
        # level 1 reviewer
        page.locator("span:has-text('Select reviewers for Level 1...')").click()
        # select level 1 reviewer
        level_1_reviewer_list = page.locator("div[role='group'] span")
        close = page.locator("div[role='option']:has-text('Close')")
        count = level_1_reviewer_list.count()
        print("\nTotal number of level 1 reviewer : ", count)
        for i in range(count):
            text = level_1_reviewer_list.nth(i).inner_text()
            if "Braj Reviewer 1" in text:
                level_1_reviewer_list.nth(i).click()
                close.click()
                break

        # click second yes button
        page.locator("label:has-text('Yes')").nth(1).click()
        level_3_reviewer_title = page.locator("label:has-text('Do you want to add more level of reviewer?')").nth(1)
        expect(level_3_reviewer_title).to_be_visible(timeout=15000)
        # level 2 reviewer
        page.locator("span:has-text('Select reviewers for Level 2...')").click()
        # select level 2 reviewer
        level_2_reviewer_list = page.locator("div[role='group'] span")
        close = page.locator("div[role='option']:has-text('Close')")
        count = level_2_reviewer_list.count()
        print("\nTotal number of level 2 reviewer : ", count)
        for i in range(count):
            text = level_2_reviewer_list.nth(i).inner_text()
            if "Braj Reviewer 2" in text:
                level_2_reviewer_list.nth(i).click()
                close.click()
                break


        # click create ropa button
        page.locator("button:has-text('Create ROPA')").click()
        ropa_title = page.locator("h3:has-text('Create Processing Activity')")
        expect(ropa_title).to_be_visible(timeout=15000)

        # add collaborator
        page.locator("button:has-text('Add Collaborator')").click()
        # popup collaborator
        collaborator_popup = page.locator("h3:has-text('Assign Collaborators')")
        expect(collaborator_popup).to_be_visible(timeout=15000)
        # click collaborator dropdown
        page.locator("span:has-text('Select collaborators')").click()
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
        collab_add_confi_msg = page.get_by_text("Collaborators added")
        expect(collab_add_confi_msg).to_be_visible(timeout=10000)

        # click organizaion role
        page.locator("span[style='pointer-events: none;'] span:has-text('Select organizational role')").click()

        # select organization role
        page.locator("span:has-text('Fiduciary')").nth(0).click()

        # click update button
        page.locator("button:has-text('Update')").click()

        # Roles and Contacts update confirmation message
        update_msg = page.get_by_text("ROPA updated successfully")
        expect(update_msg).to_be_visible(timeout=15000)

        # click on data principal tagging
        page.locator("span:has-text('Data Principal Tagging')").click()

        # click on data principal category
        page.locator("span[style='pointer-events: none;'] span:has-text('Select Data Principal Category')").click()

        # select data principal category
        dropdown = page.locator("div[role='option'] span:nth-child(2)")
        #dropdown.nth(0).click()
        expect(dropdown.first).to_be_visible(timeout=10000)
        dropdown.first.scroll_into_view_if_needed()
        dropdown.first.click(force=True)


        # click data principal
        page.locator("span:has-text('Select Data Principal')").click()

        # select data principal
        data_principal_list = page.locator("div[role='group'] span")
        data_principal_list.nth(0).click()

        # data principal close
        page.locator("div[role='option']:has-text('Close')").click()
        # click on countries
        page.locator("span:has-text('Select Country')").click()

        # select country
        page.locator("span:has-text('India')").nth(1).click()
        # close countries dropdown
        page.locator("div[role='option']:has-text('Close')").click()

        # data principal update
        page.locator("button:has-text('Update')").click()
        # data principal update confirmation message
        update_msg = page.get_by_text("Data Principal updated successfull")
        expect(update_msg).to_be_visible(timeout=10000)


        # click on PII tagging
        page.locator("span:has-text('PII Tagging')").click()
        # click pii type
        page.locator("span span:has-text('Select PII type')").click()
        # select pii type
        page.locator("span span:has-text('EMAIL ADDRESS')").click()
        # click on department collecting data
        page.locator("button[role='combobox'] span span:has-text('Select Department')").click()
        # select department collecting data
        dropdown = page.locator("div[role='option'] span:nth-child(2)")
        dropdown.nth(0).click()

        # click on department processing data
        page.locator("span span:has-text('Select Department')").click()
        # select department processing data
        dropdown = page.locator("div[role='option'] span")
        dropdown.nth(1).click()
        # close
        page.locator("div[role='option']:has-text('Close')").click()

        # input fields
        # click on source of personal data
        page.get_by_placeholder("e.g., User provided, Third-party, Public records").fill("Third-party")
        page.get_by_placeholder("e.g., Web form, API, CSV upload").fill("Web form")
        page.get_by_placeholder("Describe why this personal data is being processed...").fill("test description")

        # PII tagging update button
        page.locator("button:has-text('Update')").click()
        # data principal update confirmation message
        update_msg = page.get_by_text("Personal Data Updated Successfully")
        expect(update_msg).to_be_visible(timeout=10000)



        # Logout dpo
        # locators
        txt_my_account = page.locator(".hidden.text-left") # click on account
        txt_my_account.click()
        btn_sign_out = page.get_by_role("menuitem", name="Sign out") # click on signout button
        btn_sign_out.click()
        btn_confirm_sign_out = page.locator("#kc-logout") # click on confi signout button
        btn_confirm_sign_out.click()
        signin_title = page.locator("#kc-page-title")
        expect(signin_title).to_be_visible(timeout=10000)

        # COLLABORATOR ACCOUNT LOGIN
        # locators
        txt_email_address = page.locator("#username")
        txt_email_address.fill("samarth.collab@yopmail.com")

        txt_password = page.locator("#password")
        txt_password.fill("123")
        btn_login_button = page.locator("button[type='submit']")
        btn_login_button.click()
        txt_error_message = page.locator("div[aria-live='polite']")

        # Wait for dashboard load
        ropa_registry_btn = page.locator("a span:has-text('Ropa Registry')")
        expect(ropa_registry_btn).to_be_visible(timeout=15000)
        # Click ropa registry button
        ropa_registry_btn.click()
        ropa_registry_btn.click()

        ropa_title = page.locator("h1:has-text('ROPA Registry')")
        expect(ropa_title).to_be_visible(timeout=15000)

        # ROPA NAME COUNT
        all_ropa_name = page.locator(".cursor-pointer.break-words.text-sm")
        count = all_ropa_name.count()
        three_dot = page.locator("button:has(svg.lucide-ellipsis)")
        print("\nTotal count number of ropa : ", count)
        for i in range(count):
            text = all_ropa_name.nth(i).inner_text().strip()
            if text == ropa_name:
                three_dot.nth(i).click()
                # click on ropa edit button
                page.get_by_role("menuitem", name="Edit").click()
                break

        # edit ropa title is visible
        edit_ropa_page_title = page.locator("h3:has-text('Create Processing Activity')")
        expect(edit_ropa_page_title).to_be_visible(timeout=20000)

        # click on legal basis tab
        page.locator("span:has-text('Legal Basis')").click()
        # click legal basis for india button
        page.locator("span:has-text('Legal Basis for India')").click()
        # select
        checkbox_label = page.locator("label:has-text('Personal data voluntarily provided')")
        checkbox = checkbox_label.locator("button[role='checkbox']")
        # check state
        state = checkbox.get_attribute("aria-checked")

        if state == "false":
            checkbox_label.click()

        # select first yes button
        page.locator(".inline-flex.items-center.gap-2 span:has-text('Yes')").nth(0).click()
        # critical modal open
        critical_modal = page.locator("h2:has-text('Set sensitivity to CRITICAL?')")
        # criticality success message
        if critical_modal.is_visible(timeout=5000):
            expect(critical_modal).to_be_visible(timeout=15000)
            # click make critical button
            page.locator("button:has-text('Make Critical')").click()
            critical_msg = page.get_by_text("Sensitivity set to CRITICAL")
            expect(critical_msg).to_be_visible(timeout=10000)

        # select second yes button
        page.locator(".inline-flex.items-center.gap-2 span:has-text('Yes')").nth(1).click()
        # select third yes button
        page.locator(".inline-flex.items-center.gap-2 span:has-text('Yes')").nth(2).click()

        # legal basis update button
        page.locator("button:has-text('Update')").click()
        # legal basis update confirmation message
        update_msg = page.get_by_text("Legal Basis updated successfully.")
        expect(update_msg).to_be_visible(timeout=10000)

        # click on submit button
        page.locator("button:has-text('Submit')").click()
        collab_submit_msg = page.get_by_text("Submitted as collaborator")
        expect(collab_submit_msg).to_be_visible(timeout=10000)

        # Collaborator logout
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
        ropa_registry_btn = page.locator("a span:has-text('Ropa Registry')")
        expect(ropa_registry_btn).to_be_visible(timeout=15000)
        # Click ropa registry button
        ropa_registry_btn.click()
        ropa_registry_btn.click()

        ropa_title = page.locator("h1:has-text('ROPA Registry')")
        expect(ropa_title).to_be_visible(timeout=15000)

        # ROPA NAME COUNT
        all_ropa_name = page.locator(".cursor-pointer.break-words.text-sm")
        count = all_ropa_name.count()
        three_dot = page.locator("button:has(svg.lucide-ellipsis)")
        print("\nTotal count number of ropa : ", count)
        for i in range(count):
            text = all_ropa_name.nth(i).inner_text().strip()
            if text == ropa_name:
                three_dot.nth(i).click()
                # click on ropa edit button
                page.get_by_role("menuitem", name="Edit").click()
                break

        # edit ropa title is visible
        edit_ropa_page_title = page.locator("h3:has-text('Create Processing Activity')")
        expect(edit_ropa_page_title).to_be_visible(timeout=20000)

        # click on submit for review button
        page.locator("button:has-text('Submit for Review')").click()
        assignee_submit_msg = page.get_by_text("Processing activity submitted for review.")
        expect(assignee_submit_msg).to_be_visible(timeout=20000)

        # Assignee logout
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
        ropa_registry_btn = page.locator("a span:has-text('Ropa Registry')")
        expect(ropa_registry_btn).to_be_visible(timeout=15000)
        # Click ropa registry button
        ropa_registry_btn.click()
        ropa_registry_btn.click()

        ropa_title = page.locator("h1:has-text('ROPA Registry')")
        expect(ropa_title).to_be_visible(timeout=15000)

        # ROPA NAME COUNT
        all_ropa_name = page.locator(".cursor-pointer.break-words.text-sm")
        count = all_ropa_name.count()
        three_dot = page.locator("button:has(svg.lucide-ellipsis)")
        print("\nTotal count number of ropa : ", count)
        for i in range(count):
            text = all_ropa_name.nth(i).inner_text().strip()
            if text == ropa_name:
                three_dot.nth(i).click()
                # click on ropa edit button
                page.get_by_role("menuitem", name="Edit").click()
                break

        # edit ropa title is visible
        edit_ropa_page_title = page.locator("h3:has-text('Create Processing Activity')")
        expect(edit_ropa_page_title).to_be_visible(timeout=15000)

        # click on submit for review button
        page.locator("button:has-text('Acknowledge')").click()
        page.get_by_placeholder("Comment (required)").fill("Done")
        page.locator("button:has-text('Submit')").click()
        reviewer_1_submit_msg = page.get_by_text("Reviewer action submitted")
        expect(reviewer_1_submit_msg).to_be_visible(timeout=10000)

        # reviewer 1 logout
        # locators
        txt_my_account = page.locator(".hidden.text-left")  # click on account
        txt_my_account.click()
        btn_sign_out = page.get_by_role("menuitem", name="Sign out")  # click on signout button
        btn_sign_out.click()
        btn_confirm_sign_out = page.locator("#kc-logout")  # click on confi signout button
        btn_confirm_sign_out.click()
        signin_title = page.locator("#kc-page-title")
        expect(signin_title).to_be_visible(timeout=10000)





        # REVIEWER 2 ACCOUNT LOGIN
        # locators
        txt_email_address = page.locator("#username")
        txt_email_address.fill("braj.reviewer2.sgt@yopmail.com")

        txt_password = page.locator("#password")
        txt_password.fill("Braj@123")
        btn_login_button = page.locator("button[type='submit']")
        btn_login_button.click()

        # Wait for dashboard load
        ropa_registry_btn = page.locator("a span:has-text('Ropa Registry')")
        expect(ropa_registry_btn).to_be_visible(timeout=15000)
        # Click ropa registry button
        ropa_registry_btn.click()
        ropa_registry_btn.click()

        ropa_title = page.locator("h1:has-text('ROPA Registry')")
        expect(ropa_title).to_be_visible(timeout=15000)

        # ROPA NAME COUNT
        all_ropa_name = page.locator(".cursor-pointer.break-words.text-sm")
        count = all_ropa_name.count()
        three_dot = page.locator("button:has(svg.lucide-ellipsis)")
        print("\nTotal count number of ropa : ", count)
        for i in range(count):
            text = all_ropa_name.nth(i).inner_text().strip()
            if text == ropa_name:
                three_dot.nth(i).click()
                # click on ropa edit button
                page.get_by_role("menuitem", name="Edit").click()
                break

        # edit ropa title is visible
        edit_ropa_page_title = page.locator("h3:has-text('Create Processing Activity')")
        expect(edit_ropa_page_title).to_be_visible(timeout=15000)

        # click on submit for review button
        page.locator("button:has-text('Acknowledge')").click()
        page.get_by_placeholder("Comment (required)").fill("Done")
        page.locator("button:has-text('Submit')").click()
        reviewer_2_submit_msg = page.get_by_text("Reviewer action submitted")
        expect(reviewer_2_submit_msg).to_be_visible(timeout=10000)

        # ROPA status is visible
        all_ropa_name = page.locator(".cursor-pointer.break-words.text-sm")
        count = all_ropa_name.count()
        ropa_status = page.locator("td:has-text('ACTIVE')")
        print("\nTotal count number of ropa : ", count)
        for i in range(count):
            text = all_ropa_name.nth(i).inner_text().strip()
            if text == ropa_name:
                expect(ropa_status.nth(i)).to_be_visible(timeout=15000)
                break






        page.wait_for_timeout(5000)


    else:
        # Invalid login validation
        expect(page.locator("div[aria-live='polite']")).to_be_visible(timeout=5000)




def select_date(page, target_month_year, target_date, is_future):
    # selecting month and year from the date picker
    while True:
        current_month_year = page.locator("div[aria-live='polite']").text_content().strip()

        if current_month_year == target_month_year:
            break
        if is_future == True:
            page.locator("button[name='next-month']").click() # for future date
        else:
            page.locator("button[name='previous-month']").click()  # for past date

    all_dates = page.locator(".rdp-tbody td").all()
    # selecting date from the date picker
    for date in all_dates:
        date_text = date.inner_text()
        if date_text == target_date:
            date.click()
            break

