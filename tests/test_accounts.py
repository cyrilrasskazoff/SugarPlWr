import pytest
from pages.accounts_page import AccountsPage
from pages.home_page import HomePage



def test_navigate_to_accounts_page(login_success, page):
    home_page = HomePage(page)
    accounts_page = AccountsPage(page)
    home_page.assert_home_page()
    home_page.sidebar.expand_sidebar()
    home_page.sidebar.go_to_accounts()
    accounts_page.assert_accounts_page()


