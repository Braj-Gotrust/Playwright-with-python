import re
import time

from playwright.sync_api import Page,expect

# 1) page.get_by_alt_text() -> located only images
# 2) page.get_by_text()
# 3) page.get_by_role()
# 4) page.get_by_label()
# 5) page.get_by_placeholder()
# 6) page.get_by_title()
# 7) page.get_by_test_id()


def test_verify_pwlocator(page: Page):
    page.goto("https://demo.nopcommerce.com/")
    #time.sleep(5)  # second
    page.wait_for_timeout(2000) # millisecond
    # 1) page.get_by_alt_text()
    logo=page.get_by_alt_text("nopCommerce demo store")
    expect(logo).to_be_visible()

    # 2) page.get_by_text()
    txt=page.get_by_text("Welcome to our store")
    expect(txt).to_be_visible()  # full text
    expect(page.get_by_text("Welcome to")).to_be_visible() # partial text
    expect(page.get_by_text(re.compile(".*Welcome.*"))).to_be_visible() # regular expression

    # 3) page.get_by_role("heading", name="Welcome to our stor")
    txt2=page.get_by_role("heading",name="Welcome to our stor")
    expect(txt2).to_be_visible()

    # page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    # page.wait_for_timeout(5000)
    # heading=page.get_by_role("heading",name="Register")
    # expect(heading).to_be_visible()

    # # 4) page.get_by_label()
    # page.get_by_label("First name:").fill("John")
    # page.get_by_label("Last name:").fill("Dev")
    # page.get_by_label("Email:").fill("abc@gmail.com")

    # 5) page.get_by_placeholder()
    page.get_by_placeholder("Search store").fill("Apple MacBook Pro")
    page.wait_for_timeout(2000)

    # # 6) page.get_by_title()
    # page.goto("https://demo.nopcommerce.com/")
    # title=page.get_by_title("Show products in category Electronics")
    # expect(title).to_have_text("Electronics")
    # page.wait_for_timeout(2000)


# 7) page.get_by_test_id()
    testid=page.get_by_test_id("profile-name")
    expect(testid).to_have_text("John Deo")




