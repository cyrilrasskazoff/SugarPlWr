from playwright.sync_api import Page, expect, Response, Request
import pytest
from pages.login_page import LoginPage
from pages.base_page import BasePage


@pytest.fixture
def navigate(page, url = 'https://kr-plwr-252.msqa.sugarcrm.com/'):
    return BasePage(page).navigate(url)


def pytest_addoption(parser):
    parser.addoption('--user_name', action='store', default="admin",
                     help="Choose user: admin, will, jim, sarah, etc...")
    parser.addoption('--password', action='store', default="Q2k4g8K6AzG2R~R",
                     help="set password: default admin, will, jim, sarah, etc...")

@pytest.fixture
def login_success(navigate, page, request):
    """
    при запуске теста без укзания параметра '--user_name' автоматически выберется admin.
    в противном случае нужно явно указать '--user_name': pytest -s -v <test_file_path> --user_name=will
    """
    user_name = request.config.getoption("user_name")
    password = request.config.getoption("password")
    if user_name == "will":
        password = "will"
    if user_name == "jim":
        password = "jim"
    if user_name == "sarah":
        password = "sarah"
    return LoginPage(page).login_success(username=user_name, password=password)



@pytest.fixture
def login_failure(navigate, page):
    return LoginPage(page).login_failure(username="invalid", password="invalid")
