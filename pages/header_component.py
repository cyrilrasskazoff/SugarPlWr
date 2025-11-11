from playwright.sync_api import Page
from pages.locators import HeaderLocators

class HeaderComponent:
    def __init__(self, page: Page):
        self.page = page
        self.logo = page.get_by_role(HeaderLocators.LOGO[1], name=HeaderLocators.LOGO[2])
        self.global_search_input = page.get_by_role(HeaderLocators.GLOBAL_SEARCH_INPUT[1],
                                                    name=HeaderLocators.GLOBAL_SEARCH_INPUT[2])
        self.search_button = page.get_by_role(HeaderLocators.GLOBAL_SEARCH_BUTTON[1],
                                              name=HeaderLocators.GLOBAL_SEARCH_BUTTON[2])
        self.notifications_button = page.get_by_role(HeaderLocators.NOTIFICATIONS_BUTTON[1],
                                                     name=HeaderLocators.NOTIFICATIONS_BUTTON[2])
        self.avatar = page.get_by_role(HeaderLocators.AVATAR[1], name=HeaderLocators.AVATAR[2])
        self.profile_link = page.locator(HeaderLocators.PROFILE_LINK)
        self.change_password_link = page.get_by_role(HeaderLocators.CHANGE_PASSWORD_LINK[1],
                                                     name=HeaderLocators.CHANGE_PASSWORD_LINK[2])
        self.employees_link = page.get_by_role(HeaderLocators.EMPLOYEES_LINK[1], name=HeaderLocators.EMPLOYEES_LINK[2])
        self.mobile_link = page.get_by_role(HeaderLocators.MOBILE_LINK[1], name=HeaderLocators.MOBILE_LINK[2])
        self.shortcuts_link = page.get_by_role(HeaderLocators.SHORTCUTS_LINK[1], name=HeaderLocators.SHORTCUTS_LINK[2])
        self.about_link = page.get_by_role(HeaderLocators.ABOUT_LINK[1], name=HeaderLocators.ABOUT_LINK[2])
        self.log_out_link = page.get_by_role(HeaderLocators.LOG_OUT_LINK[1], name=HeaderLocators.LOG_OUT_LINK[2])

    def expand_dropdown_menu(self):
        self.avatar.click()

    def go_to_profile_page(self):
        self.profile_link.click()

    def go_to_change_password_page(self):
        self.change_password_link.click()

    def go_to_employees_page(self):
        self.employees_link.click()

    def go_to_about_page(self):
        self.about_link.click()

    def log_out(self):
        self.log_out_link.click()

