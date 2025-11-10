from playwright.sync_api import Page
from pages.locators import SidebarLocators

class SidebarComponent:
    def __init__(self, page: Page):
        self.page = page
        self.hamburger_btn = page.locator(SidebarLocators.HAMBURGER)
        self.account_link = page.locator(SidebarLocators.ACCOUNTS_LINK)

    def expand_sidebar(self):
        self.hamburger_btn.click()

    def go_to_accounts(self):
        self.account_link.click()
