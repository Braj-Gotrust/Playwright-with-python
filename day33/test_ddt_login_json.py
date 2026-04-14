import pytest
from playwright.sync_api import Playwright,expect,Page
import json

# Read json file

file=open("testdata/data.json","r")
login_data=json.load(file)

@pytest.mark.parametrize("email,password,validity",[(data["email"],data["password"],data["validity"]) for data in login_data])
def test_login_data_driven(email,password,validity,page: Page):
    page.goto("https://preprod.gotrust.tech/home")
    page.wait_for_timeout(1000)
    page.locator("#username").fill(email)
    page.wait_for_timeout(1000)
    page.locator("#password").fill(password)
    page.wait_for_timeout(1000)
    page.locator("button[type='submit']").click()
    page.wait_for_timeout(5000)
    if validity=="valid":
        notification = page.locator("#radix-_r_3d_")
        expect(notification).to_be_visible(timeout=3000)
    else:
        error_msg=page.locator("div[aria-live='polite']")
        expect(error_msg).to_be_visible(timeout=3000)
        #expect(page).to_have_url("https://preprod.gotrust.tech/home")


