import allure
import pytest
from assertpy import assert_that

from playwright.sync_api import expect
from config.config import RUN_BROWSER
from consts import consts
from consts.consts import RESTRICTED_COUNTRY_CODES
from tests.helper import fill_content_id, verify_playback_button, \
    reload_button_click, fill_inputs_one_panel, verify_error_message_on_player_window, play_different_environment
from ui.helper import make_failure_screenshot



@allure.label("functional")
class TestFunctional:
    @pytest.mark.parametrize("content_id", consts.COMMON_CONTENTS)
    @allure.title("Check common videos are played")
    def test_check_play_common_video(self, app_page, content_id):
        fill_content_id(page=app_page, content_id=content_id)
        reload_button_click(page=app_page)
        play_different_environment(app_page)
        verify_playback_button(page=app_page)

    @allure.title("Check live channel is played")
    def test_check_play_live_video(self, app_page):
        fill_content_id(page=app_page, content_id="channel_one")
        app_page.one_panel.streaming_type.select_option("live")
        reload_button_click(page=app_page)

    @pytest.mark.parametrize("content_id, right_country_code", [
        ("v_at", "at"),
        ("v_de", "de")
    ])
    @allure.title("Country restrictions - fill correct country codes, video is playable")
    def test_check_play_correct_country_video(self, app_page, content_id, right_country_code):
        fill_content_id(page=app_page, content_id=content_id)
        with allure.step("Fill suitable country code to input and check video is played"):
            fill_inputs_one_panel(page=app_page, country_code=right_country_code)
            reload_button_click(page=app_page)
            verify_playback_button(page=app_page)

    @pytest.mark.parametrize("content_id, wrong_country_code", [
        (content_id, country_code)
        for content_id in ["v_at", "v_de"]
        for country_code in RESTRICTED_COUNTRY_CODES
    ])
    @allure.title("Country restrictions - fill restricted country codes, video is not playable")
    def test_check_play_restricted_country_video(self, app_page, content_id, wrong_country_code):
        fill_content_id(page=app_page, content_id=content_id)
        with allure.step("Fill restricted country code to input and check video is not played"):
            fill_inputs_one_panel(page=app_page, country_code=wrong_country_code)
            reload_button_click(page=app_page)
            verify_error_message_on_player_window(page=app_page)


    @pytest.mark.parametrize("content_id",
                             [
                                 "fsk18",
                                 "fsk6",
                             ])
    @allure.title("Check video with age restriction - correct age and PIN")
    def test_check_play_correct_age_pin_video(self, app_page, content_id):
        fill_content_id(page=app_page, content_id=content_id)
        with allure.step("Prepare and verify video playback with correct age and PIN"):
            fill_inputs_one_panel(app_page,
                                  pin_age="1234",
                                  pin_age_level="5")
            reload_button_click(page=app_page)
            verify_playback_button(page=app_page)
