# pytest test_sandbox.py::test_login -v --browser chromium --headed --slowmo 2000
from playwright.sync_api import Playwright, sync_playwright, expect
import re

def test_run(playwright: Playwright) -> None:
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    browser = playwright.firefox.launch(headless=False, slow_mo=500)
    # Следующие три строки отвечают за запуск браузера и создание в нем контекста
    context = browser.new_context()  # new_context() - создает изолированный сеанс браузера
    page = context.new_page()   # new_page()  - открывает новую страницу(tab) в браузере
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()  # С помощью метода get_by_placeholder("What needs to be
    # done?")  playwright находит в DOM дереве веб-элемент  c  атрибутом тега placeholder и значением атрибута
    # What needs to be done?
    page.get_by_role("textbox", name="What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_text("Mark all as complete").click()

    # ---------------------
    context.close()
    browser.close()


def test_admin_login(page, username="admin", password = "Q2k4g8K6AzG2R~R"):
    page.goto("https://kr-plwr-252.msqa.sugarcrm.com/")
    page.get_by_placeholder("User Name").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Log In").click()
    expect(page.get_by_text("Loading...")).not_to_be_visible(timeout=50000)
    current_url = page.url
    home_page = re.search(r'#Home(/|$)', current_url)
    if not home_page:
        expect(page.locator('//span[text()="Setup your user information"]')).to_be_visible()
        page.get_by_role("button", name="Next").click()
        page.get_by_role("button", name="Next").click()
        page.get_by_role("button", name="Start Sugar").click()
    expect(page).to_have_url(re.compile(r".*#Home.*"))
