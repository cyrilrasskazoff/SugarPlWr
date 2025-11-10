import pytest

from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.mark.smoke
@pytest.mark.parametrize('username, password', [
    ('admin', 'Q2k4g8K6AzG2R~R'),
    ('testtwelve', 'will')
])
def test_login_success_param(navigate, page, username, password):
    login_page = LoginPage(navigate)
    home_page = HomePage(navigate)
    login_page.login_success(username, password)
    home_page.assert_home_page()



def test_login_success(login_success, page):
    home_page = HomePage(page)
    home_page.assert_home_page()



def test_login_failure(login_failure, page):
    login_page = LoginPage(page)
    login_page.assert_error_message()







