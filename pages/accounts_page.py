from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import re


class AccountsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def assert_accounts_page(self):
        expect(self.page).to_have_url(re.compile(r".*#Accounts.*"))
