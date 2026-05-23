import re
import pytest
from playwright.sync_api import expect, Page

login_test_data = [("braj.dpo@yopmail.com", "Test@123", "valid")]

@pytest.mark.parametrize("email,password,validity", login_test_data)
def test_login_data_driven(email, password, validity, page: Page):
    page.goto("https://preprod.gotrust.tech/home")

    # Login
    page.locator("#username").fill(email)
    page.locator("#password").fill(password)
    page.locator("button:has-text('Sign In')").click()

    if validity == "valid":
        # Wait for dashboard load
        profile_btn =page.locator("button>span:has-text('Profile Configuration')")
        # profile_btn = page.get_by_role("button", name="Profile Configuration")
        expect(profile_btn).to_be_visible(timeout=15000)

        # Open profile dropdown
        profile_btn.click()
        # Click Organization Structure (use text for reliability)
        page.locator("text=Organization Structure").first.click()

        # Wait for UI change (SPA → no URL change)
        expect(page.locator("text=Organization")).to_be_visible(timeout=10000)

        page.locator("text=Organization Structure").first.click()
        # Click Structure tab
        page.get_by_role("tab", name="Structure").click()

        # Optional validation
        expect(page.get_by_role("tab", name="Structure")).to_be_visible()

        page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()

        page.get_by_role("combobox").click()

        page.get_by_role("option", name="Legal Entity").click()

        # ✅ USE PLACEHOLDER / LABEL (NOT ID)
        page.get_by_placeholder("Enter Legal Entity name").fill("aaa test 6")
        page.get_by_placeholder("description").fill("test1")
        page.get_by_placeholder("Full company address").fill("noida1")

        # Country dropdown
        page.locator("button span:has-text('Select a country')").click()
        page.locator("span:has-text('India (IN)')").click()

        page.locator("span:has-text('Select options')").click()
        page.locator("span:has-text('(Select All)')").click()
        page.locator("div[data-value='Close']").click()
        page.locator("span:has-text('Select region')").click()
        page.locator("span:has-text('APAC')").click()
        page.locator("span:has-text('Select regulations')").click()
        page.locator("span:has-text('(Select All)')").click()
        page.locator("div[data-value='Close']").click()
        # select dop
        page.locator("//span[normalize-space()='Select']").click()
        page.get_by_role("presentation").nth(1).click()

        # Click submit
        page.locator("button:has-text('Create Legal Entity')").click()

        # Handle Continue
        if page.locator("button:has-text('Continue')").is_visible():
            page.locator("button:has-text('Continue')").click()

        # successful message
        success_msg = page.locator("text=Legal entity created")
        expect(success_msg).to_be_visible(timeout=10000)
        # LEGAL ENTITY CREATED SUCCESSFULLY



        # div.border-blue-200 button:has(svg.lucide-plus)

        legal_entities = page.locator("div.border-blue-200 h3")
        plus_btn = page.locator("div.border-blue-200 button:has(svg.lucide-plus)")
        plus_btn_title = page.locator(".text-center h2")
        count = legal_entities.count()
        print("\nTotal legal entities: ",count)

        for i in range (count):
            text = legal_entities.nth(i).inner_text()
            if text == "aaa test 5":
                #legal_entities.nth(i)
                plus_btn.nth(i).click()
                expect(plus_btn_title).to_be_visible()

                page.locator("div span:has-text('Select type')").click()

                # select business unit option
                page.locator("div span:has-text('Business Unit')").click()
                page.get_by_placeholder("Enter Business Unit name").fill("business unit 1")
                page.get_by_placeholder("Brief description").fill("test")

                # click create business unit button
                page.locator("button:has-text('Create Business Unit')").click()

                # confirmation message
                confirm_msg = page.get_by_text("Business unit created successfully", exact=False)
                expect(confirm_msg).to_be_visible(timeout=10000)
                # BUSINESS UNIT CREATED SUCCESSFULLY

                # select department option
                plus_btn.nth(i).click()
                page.locator("div span:has-text('Select type')").click()
                page.locator("div span:has-text('Department')").click()
                page.get_by_placeholder("Enter Department name").fill("department 1")
                page.get_by_placeholder("Brief description").fill("test")

                # click create department button
                page.locator("button:has-text('Create Department')").click()

                # confirmation message
                confirm_msg = page.get_by_text("Department created successfully!", exact=False)
                expect(confirm_msg).to_be_visible(timeout=10000)
                # DEPARTMENT CREATED SUCCESSFULLY

                # select product option
                plus_btn.nth(i).click()
                page.locator("div span:has-text('Select type')").click()
                page.locator("div span:has-text('Product')").click()
                page.get_by_placeholder("Enter Product name").fill("product 1")
                page.get_by_placeholder("Brief description").fill("test")

                # click create product button
                page.locator("button:has-text('Create Product')").click()

                # confirmation message
                confirm_msg = page.get_by_text("Product created successfully!", exact=False)
                expect(confirm_msg).to_be_visible(timeout=10000)
                # PRODUCT CREATED SUCCESSFULLY

                # select service option
                plus_btn.nth(i).click()
                page.locator("div span:has-text('Select type')").click()
                page.locator("div span:has-text('Service')").click()
                page.get_by_placeholder("Enter Service name").fill("service 1")
                page.get_by_placeholder("Brief description").fill("service description")

                # click create service button
                page.locator("button:has-text('Create Service')").click()

                # confirmation message
                confirm_msg = page.get_by_text("Service created successfully!", exact=False)
                expect(confirm_msg).to_be_visible(timeout=10000)
                # PRODUCT CREATED SUCCESSFULLY

                # select business process option
                plus_btn.nth(i).click()
                page.locator("div span:has-text('Select type')").click()
                page.locator("div span:has-text('Business Process')").click()
                page.get_by_placeholder("Enter Business Process name").fill("business process 1")
                page.get_by_placeholder("Brief description").fill("business process 1 description")

                # click create service button
                page.locator("button:has-text('Create Business Process')").click()

                # confirmation message
                confirm_msg = page.get_by_text("Business process created successfully!", exact=False)
                expect(confirm_msg).to_be_visible(timeout=10000)
                # BUSINESS PROCESS CREATED SUCCESSFULLY

                break

    else:
        # Invalid login validation
        expect(page.locator("div[aria-live='polite']")).to_be_visible(timeout=5000)