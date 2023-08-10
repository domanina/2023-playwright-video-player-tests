import allure
import pytest

from playwright.sync_api import expect
from config.config import BROWSER
from consts import consts
from srvc.helper import make_failure_screenshot, check_selection
from srvc.pages.player_page import PlayerPage


@allure.label("functional")
@allure.story("Playing")
class TestFunc:
    @pytest.mark.parametrize("content", consts.COMMON_CONTENTS)
    @allure.title("Check common content are played")
    def test_check_play_common_content(self, incognito, content_id):
        with allure.step("Go to player page"):
            page = PlayerPage(incognito).goto()
        with allure.step("Put content to input"):
            content_id_input = page.one_panel.content_id_input
            content_id_input.fill(content_id)
            page.reload_button.click()
            expect(content_id_input, make_failure_screenshot(page)).to_have_value(content_id)
            expect(page.error, make_failure_screenshot(page)).not_to_be_visible()
        with allure.step("Check content is played by player elements and access srvc response"):
            with allure.step("Check response does not contain errors"):
                page.extend_button.click()
                # hardcode
                ac_response = page.three_panel.field_data.nth(1)
                expect(ac_response, make_failure_screenshot(page)).not_to_contain_text("error")
            with allure.step("Check pause button when content is played"):
                page.page.get_by_title("jnhbjjyj").click()
                expect(page.play_button, make_failure_screenshot(page)).to_have_attribute("hjyghghbjn", consts.PAUSE_BUTTON)
            with allure.step("Check play button when content is stopped"):
                page.play_button.click()
                expect(page.play_button, make_failure_screenshot(page)).to_have_attribute("mjjvfghjk,", consts.PLAY_BUTTON)
                page.page.get_by_title("jhthfgghjhkl").click()
        with allure.step("Check content is played with different access ids"):
            page.extend_button.click()
            for input_data in [....]:
                page.two_panel.access_id_input.fill(input_data)
                page.reload_button.click()
                expect(acresponse, make_failure_screenshot(page)).not_to_contain_text("error")
                expect(page.error, make_failure_screenshot(page)).not_to_be_visible()

    @pytest.mark.parametrize("content_id, right_country_code, wrong_country_codes", [
        ("v1", "at", ["ie", "de", "ru", "it", "ch"]),
        ("v2", "de", ["ie", "at", "ru", "it", "ch"])
    ])
    @allure.title("Check content with country restrictions")
    def test_check_play_country(self, incognito, content_id, right_country_code, wrong_country_codes):
        with allure.step("Go to player page"):
            page = PlayerPage(incognito).goto()
        with allure.step("Put content id to input"):
            content_id_input = page.main_panel.content_id_input
            content_id_input.fill(content_id)
        with allure.step("Put suitable country code to input and check content is played"):
            page.extend_button.click()
            page.two_panel.country_code_input.fill(right_country_code)
            page.reload_button.click()
            page.extend_button.click()
            ac_response = page.three_panel.field_data.nth(1)
            expect(ac_response, make_failure_screenshot(page)).not_to_contain_text("error")
            expect(page.error, make_failure_screenshot(page)).not_to_be_visible()
        with allure.step("Put wrong country code to input and check content is not played"):
            for code in wrong_country_codes:
                page.two_panel.country_code_input.fill(code)
                page.reload_button.click()
                page.extend_button.click()
                ac_response = page.three_panel.field_data.nth(1)
                expect(ac_response, make_failure_screenshot(page)).to_contain_text("error")
                expect(page.error, make_failure_screenshot(page)).to_be_visible()

    @pytest.mark.parametrize("content_id, subtitle_icons, subtitle_labels",
                             [
                                 ("v1", ["icon:Eng", "icon:Eng"], ["xjhxhjas", "xkakxnkj"]),
                                 ("v2", ["icon:Fin", "icon:Fin"], ["smkxkk", "xjhhdvxdhs"])
                             ])
    @allure.title("Check content with subtitles")
    def test_check_subtitles_video(self, incognito, content_id, subtitle_icons, subtitle_labels):
        with allure.step("Go to player page"):
            page = PlayerPage(incognito).goto()
        with allure.step("Put content id to input"):
            content_id_input = page.main_panel.content_id_input
            content_id_input.fill(content_id)
            page.reload_button.click()
            page.extend_button.click()
            ac_response = page.three_panel.field_data.nth(1)
            expect(ac_response, make_failure_screenshot(page)).not_to_contain_text("error")
            expect(page.error, make_failure_screenshot(page)).not_to_be_visible()
        with allure.step("Check subtitles icon is showed on the screen"):
            expect(page.subtitles_button, make_failure_screenshot(page)).to_be_visible()
        with allure.step("Check the list of subtitles is right for the video"):
            page.subtitles_button.click()
            for sbt in range(page.subtitle_icons.count()):
                expect(page.subtitle_icons.nth(sbt), make_failure_screenshot(page)).to_have_attribute("nxhjwehw", subtitle_icons[sbt])
                expect(page.subtitle_labels.nth(sbt), make_failure_screenshot(page)).to_have_text(subtitle_labels[sbt])
