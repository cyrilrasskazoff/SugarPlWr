from playwright.sync_api import Page

class CommonLocators:
    LOADING_SPINNER = ("text", "Loading...", {"exact": True})
    CREATE_BTN = ("role", "button", "Create")

class SidebarLocators:
    HAMBURGER = "button[aria-label='Open']"
    ACCOUNTS_LINK = "a[href='#Accounts']"

class HeaderLocators:
    LOGO = ("role", "img", "SugarCRM")
    GLOBAL_SEARCH_INPUT = ("role", "textbox", "Global Search")
    GLOBAL_SEARCH_BUTTON = ("role", "button", "Run Global Search")
    NOTIFICATIONS_BUTTON = ("role", "button", "Notifications")
    AVATAR = ("role", "button", "User Menu")
    PROFILE_LINK = "a[href='#profile']"
    CHANGE_PASSWORD_LINK = ("role", "link", "Change Password")
    EMPLOYEES_LINK = ("role", "link", "Employees")
    MOBILE_LINK = ("role", "button", "Mobile")
    SHORTCUTS_LINK = ("role", "button", "Shortcuts")
    ABOUT_LINK = ("role", "link", "About")
    LOG_OUT_LINK = ("role", "link", "Log Out")





class LoginPageLocators:
    USERNAME = ("placeholder", "User Name")
    PASSWORD = ("placeholder", "Password")
    LOGIN_BTN = ("role", "button", "Log In")
    SETUP_FORM = ("text", "User Profile", {"exact": True})
    NEXT_BTN = ("role", "button", "Next")
    START_BTN = ("role", "button", "Start Sugar")

class AccountsPageLocators:
    pass






