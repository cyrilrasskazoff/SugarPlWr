from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from pages.locators import CommonLocators
import re


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.common_locators = CommonLocators()
        self.user_name = page.get_by_placeholder("User Name")
        self.password = page.get_by_placeholder("Password")
        self.login_btn  = page.get_by_role("button", name="Log In")
        self.user_profile = page.get_by_text("User Profile")
        self.next_btn = page.get_by_role("button", name="Next")
        self.user_locale_settings = page.get_by_text("User Locale Settings")
        self.setup_complete = page.get_by_text("Setup Complete")
        self.start_btn = page.get_by_role("button", name="Start Sugar")
        # self.error_alert = page.locator(".alert-wrapper")
        self.error_alert = page.get_by_text("Invalid Credentials:")



    def login_success(self, username: str, password: str):
        """Perfoms login/signup to the app: idm-disabled
        combines locators.py and get_by_* locators within page class
        """
        with (self.page.expect_response(lambda r: "/me" in r.url and r.request.method == "PUT") as
              response_info):
            self.user_name.fill(username)
            self.password.fill(password)
            self.login_btn.click()
            self.page.get_by_text(self.common_locators.LOADING_SPINNER[1]).wait_for(state="hidden", timeout=20000)
            home_page = re.search(r'#Home(/|$)', self.page.url)
            if not home_page:
                response = response_info.value
                self.user_profile.wait_for(state="visible")
                self.next_btn.click()
                if response.status == 200:
                    self.user_locale_settings.wait_for(state="visible")
                    self.next_btn.click()
                    self.setup_complete.wait_for(state="visible")
                    self.start_btn.click()
        # self.page.pause()

    def assert_error_message(self):
        expect(self.error_alert).to_be_visible()

    # def get_error_message(self):
    #     # return self.error_alert.inner_text()
    #     expect(self.error_alert).inner_text()


    def login_failure(self, username: str, password: str):
        """shows error message in case invalid credentials have been provided"""
        self.user_name.fill(username)
        self.password.fill(password)
        self.login_btn.click()




