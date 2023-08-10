import allure
import pytest
from playwright.sync_api import sync_playwright

from config.config import HEADLESS_MODE, BROWSER


@allure.title("Open browser incognito")
@pytest.fixture(scope="function")
def incognito():
    with sync_playwright() as playwright:
        headless = False if HEADLESS_MODE else True
        if BROWSER == "webkit":
            browser = playwright.webkit.launch(headless=headless)
        elif BROWSER == "chromium":
            browser = playwright.chromium.launch(headless=headless, channel="chrome-canary")
        elif BROWSER == "firefox":
            browser = playwright.firefox.launch(headless=headless)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()
