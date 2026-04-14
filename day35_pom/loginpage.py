from playwright.sync_api import Page

class LoginPage:
    def __init__(self,page:Page):
        self.page = page
        self.login_link = self.page.locator("#login2")
        self.user_input = self.page.locator("#loginusername")
        self.password_input = self.page.locator("#loginpassword")
        self.login_button = self.page.locator("button[onclick='logIn()']")

    # Action methods
    def click_login_button(self):
        self.login_link.click()

    def enter_username(self,username):
        self.user_input.fill("")  # clear the inputbox
        self.user_input.fill(username)

    def enter_password(self,password):
        self.password_input.fill("")   # clear the password
        self.password_input.fill(password)

    def click_login_button(self):
        self.login_button.click()

    def perform_login(self,username,password):
        self.login_link.click()
        self.user_input.fill("")  # clear the inputbox
        self.user_input.fill(username)
        self.password_input.fill("")  # clear the password
        self.password_input.fill(password)
        self.login_button.click() 
