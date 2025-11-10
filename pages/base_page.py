from playwright.sync_api import Page
from pages.locators import CommonLocators
from pages.sidebar_component import SidebarComponent

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.sidebar = SidebarComponent(page)
        self.common_locators = CommonLocators()
    def navigate(self, url):
        self.page.goto(url, timeout=30000)
