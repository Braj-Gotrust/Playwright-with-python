import pytest
from playwright.sync_api import Playwright,expect,Page

# login_test_data=[("braj.dpo@yopmail.com","121","valid"),
#                  ("braj.dpo@yopmail.com","121323","invalid"),
#                  ("braj.dp@yopmail.com","1217667","invalid"),
#                  ("","","invalid")]

login_test_data=[("braj.dpo@yopmail.com","121","valid")]

@pytest.mark.parametrize("email,password,validity",login_test_data)
def test_login_data_driven(email,password,validity,page: Page):
    page.goto("https://preprod.gotrust.tech/home")
    page.wait_for_timeout(1000)
    page.locator("#username").fill(email)
    page.wait_for_timeout(1000)
    page.locator("#password").fill(password)
    page.wait_for_timeout(1000)
    page.locator("button[type='submit']").click()
    page.wait_for_timeout(3000)
    if validity=="valid":
        notification = page.locator("#radix-_r_3d_")
        expect(notification).to_be_visible(timeout=3000)
    else:
        error_msg=page.locator("div[aria-live='polite']")
        expect(error_msg).to_be_visible(timeout=3000)
        #expect(page).to_have_url("https://preprod.gotrust.tech/home")


    # my_account.click()
    # page.wait_for_timeout(1000)
    #page.get_by_role("menuitem", name="Organization").click()

    # sign_out = page.get_by_role("menuitem", name="Sign out")
    # sign_out.click()
    # page.wait_for_timeout(1000)
    # confirm_sign_out = page.locator("#kc-logout")
    # confirm_sign_out.click()

    page.wait_for_timeout(5000)




def get_my_account_page_name(self):
    try:
        return self.my_account.text_content().strip()
    except Exception as e:
        print(f"Error returning My Account page name: {e}")
        return None







