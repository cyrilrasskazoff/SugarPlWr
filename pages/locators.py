from playwright.sync_api import Page

class CommonLocators:
    LOADING_SPINNER = ("text", "Loading...", {"exact": True})
    CREATE_BTN = ("role", "button", "Create")

class SidebarLocators:
    HAMBURGER = "button[aria-label='Open']"
    ACCOUNTS_LINK = "a[href='#Accounts']"



class LoginPageLocators:
    USERNAME = ("placeholder", "User Name")
    PASSWORD = ("placeholder", "Password")
    LOGIN_BTN = ("role", "button", "Log In")
    SETUP_FORM = ("text", "User Profile", {"exact": True})
    NEXT_BTN = ("role", "button", "Next")
    START_BTN = ("role", "button", "Start Sugar")

class AccountsPageLocators:
    pass






