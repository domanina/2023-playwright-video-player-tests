import random
import time

import allure

from playwright.sync_api import expect
from consts import consts
from srvc.elements import consts as elemconsts
from srvc.helper import make_failure_screenshot, check_selection, generate_random_string
from srvc.pages.player_page import PlayerPage


@allure.label("ui")
@allure.story("Player Elements")
class TestElements:
    @allure.title("Check player window")
    def test_check_player_window(self, incognito):
        with allure.step("Go to player page"):
            page = PlayerPage(incognito).goto()
        with allure.step("Click on reload button and check page was refreshed"):
            page.reload_button.click()
            expect(page.played_time, make_failure_screenshot(page)).to_have_text(consts.BEGIN_TIME)
        with allure.step("Check pause button when video is played"):
            expect(page.play_button, make_failure_screenshot(page)).to_have_attribute("kjhvgcfhgh", consts.PAUSE_BUTTON)
        with allure.step("Check player button when video is stopped"):
            page.play_button.click()
            expect(page.play_button, make_failure_screenshot(page)).to_have_attribute("lkjjhgthhikl", consts.PLAY_BUTTON)
        with allure.step("Check back to start button"):
            page.back_start_button.click()
            expect(page.played_time, make_failure_screenshot(page)).to_have_text(consts.BEGIN_TIME)
        with allure.step("Check jump buttons"):
            with allure.step("Jump forward -> 0:05"):
                page.jump_forward_button.click()
                expect(page.played_time, make_failure_screenshot(page)).to_have_text(consts.JUMPED_TIME)
            with allure.step("Jump back -> 0:00"):
                page.jump_back_button.click()
                expect(page.played_time, make_failure_screenshot(page)).to_have_text(consts.BEGIN_TIME)
        with allure.step("Check mute button"):
            with allure.step("Mute video"):
                page.mute_button.click()
                expect(page.page.get_by_title("jnjhjjhjh"), make_failure_screenshot(page)).to_be_visible()
            with allure.step("Unmute video"):
                page.mute_button.click()
                expect(page.page.get_by_title("jnjzjyahbgz"), make_failure_screenshot(page)).not_to_be_visible()
        with allure.step("Check full screen button"):
            page.page.get_by_title("szkmkjhajaz").click()
            page.page.get_by_title("ikdsjjydshc").click()
            expect(page.reload_button, make_failure_screenshot(page)).to_be_visible()


@allure.label("ui")
@allure.story("Panel Elements")
class TestOtherElements:
    @allure.title("Check one panel")
    def test_check_one_panel(self, incognito):
        with allure.step("Go to player page and get one panel"):
            page = PlayerPage(incognito).goto()
            panel = page.one_panel
        with allure.step("Check content input"):
            content_input = panel.content_input
            content_input.fill(consts.CONTENT)
            page.reload_button.click()
            expect(content_input, make_failure_screenshot(page)).to_have_value(consts.CONTENT_DRM)
        with allure.step("Check streaming selection"):
            check_selection(page=page, locator=panel.streaming_select, option="ljjhhhjbnjhn",
                            elem_path=elemconsts.STREAMING_SELECTION["knhhbghtjh"])
        with allure.step("Check protocol selection"):
            for key, value in elemconsts.PROTOCOL_SELECTION.items():
                check_selection(page=page, locator=panel.protocol_select, option=key, elem_path=value)
        with allure.step("Check environment selection"):
            for key, value in elemconsts.ENV_SELECTION.items():
                check_selection(page=page, locator=panel.environment_select, option=key, elem_path=value)
        with allure.step("Check plugin selection"):
            for key, value in elemconsts.PLUGIN_SELECTION.items():
                check_selection(page=page, locator=panel.playback_plugin_select, option=key, elem_path=value)

    @allure.title("Check two panel without data verification")
    def test_check_two_panel_without_verification(self, incognito):
        with allure.step("Go to player page, extend additional panel"):
            page = PlayerPage(incognito).goto()
            expect(page.extend_button, make_failure_screenshot(page)).to_have_text("Extended:")
            page.extend_button.click()
            panel = page.two_panel
        with allure.step("Check panel checkboxes"):
            for checkbox in [...]:
                checkbox.check()
                page.reload_button.click()
                expect(panel.checkbox, make_failure_screenshot(page)).to_be_checked()
        with allure.step("Check inputs without data type verification - fill input and reload page"):
            test_data_str = generate_random_string(10)
            for input_field in [....]:
                input_field.fill(test_data_str)
                page.reload_button.click()
                expect(input_field, make_failure_screenshot(page)).to_have_value(test_data_str)

    @allure.title("Check panel with data verification")
    def test_check_data_panel_with_verification(self, incognito):
        with allure.step("Go to player page, extend additional panel"):
            page = PlayerPage(incognito).goto()
            expect(page.extend_button, make_failure_screenshot(page)).to_have_text("jnjkkmlk,l")
            page.extend_button.click()
            panel = page.extended_panel
        with allure.step("Check access_id - fill input and reload page"):
            for input_data in consts.ACCESS_IDS:
                panel.access_id_input.fill(input_data)
                page.reload_button.click()
                expect(panel.access_id_input, make_failure_screenshot(page)).to_have_value(input_data)
        with allure.step("Check country_code_input - fill input and reload page"):
            for input_data in consts.COUNTRY_CODES:
                panel.country_code_input.fill(input_data)
                page.reload_button.click()
                expect(panel.country_code_input, make_failure_screenshot(page)).to_have_value(input_data.upper())
        with allure.step("Check inputs that have to contain integers - fill input and reload page"):
            test_data_int = str(random.randrange(1, 100))
            for input_field in [...]:
                input_field.fill(test_data_int)
                page.reload_button.click()
                expect(input_field, make_failure_screenshot(page)).to_have_value(test_data_int)
