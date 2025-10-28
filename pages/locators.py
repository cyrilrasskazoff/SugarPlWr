from playwright.sync_api import Page
from typing import Tuple

class CommonLocators:
    LOADING_SPINNER = ("text", "Loading...", {"exact": True})


class LoginPageLocators:
    USERNAME = ("placeholder", "User Name")
    PASSWORD = ("placeholder", "Password")
    LOGIN_BTN = ("role", "button", {"name": "Log In"})
    SETUP_FORM = '//span[text()="Setup your user information"]'
    NEXT_BTN = ("role", "button", {"name": "Next"})
    START_BTN = ("role", "button", {"name": "Start Sugar"})




