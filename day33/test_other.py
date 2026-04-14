
from playwright.sync_api import Page, expect


def test_coll_login(page:Page):
    page.goto("https://sandbox.gotrust.tech/home")

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
        if text == "ROPA 325":
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
        if text == "ROPA 325":
            expect(ropa_status.nth(i)).to_be_visible(timeout=15000)
            break












    page.wait_for_timeout(5000)



