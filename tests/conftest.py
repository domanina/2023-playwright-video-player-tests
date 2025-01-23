import allure
import pytest
from playwright.sync_api import sync_playwright

from config.config import RUN_BROWSER
from  srvc.pages.player_page import PlayerPage


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        headless = not os.getenv("HEADFULL_MODE_ONLY_LOCAL_RUN", False)
        if RUN_BROWSER == "webkit":
            browser = playwright.webkit.launch(headless=headless)
        elif RUN_BROWSER == "chromium":
            browser = playwright.chromium.launch(headless=headless)
        elif RUN_BROWSER == "firefox":
            browser = playwright.firefox.launch(headless=headless)
        yield browser
        browser.close()


@allure.title("Create browser context")
@pytest.fixture(scope="function")
def new_context(browser):
    context = browser.new_context()
    yield context
    context.close()


@allure.title("Open browser page")
@pytest.fixture(scope="function")
def default_page(new_context):
    page = new_context.new_page()
    yield page



@allure.title("Navigate to the app page")
@pytest.fixture(scope="function")
def app_page():
    page = PlayerPage(default_page).goto()
    return page
