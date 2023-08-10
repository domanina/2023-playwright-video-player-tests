import random
import string
import time
import allure

from typing import Optional
from playwright.sync_api import Page, Locator, expect
from srvc.pages.player_page import PlayerPage


def generate_random_string(length: int) -> str:
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def check_selection(page: PlayerPage, locator: Locator, option: str, elem_path: str):
    with allure.step("Find element with selection"):
        locator.select_option(option)
    with allure.step("Reload page to be sure the selected option is saved"):
        page.reload_button.click()
        expect(locator.locator(elem_path), make_failure_screenshot(page)).to_have_attribute("selected", "selected")


def make_failure_screenshot(page: Page):
    allure.attach(page.page.screenshot(type="png"), name="allure-report/failure",
                  attachment_type=allure.attachment_type.PNG)
