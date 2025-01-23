import random
import allure

from playwright.sync_api import expect
from consts import consts
from ui.helper import make_failure_screenshot, generate_random_string


@allure.label("ui")
@allure.story("Panels Elements")
class TestUIElements:

    @allure.title("Check content ID input on the first panel")
    def test_content_id_main_panel(self, app_page):
        content_id_input = app_page.main_panel.content_id_input
        content_id_input.fill(consts.CONTENT_DRM)
        reload_button_click(page=app_page)
        expect(content_id_input, make_failure_screenshot(app_page)).to_have_value(consts.CONTENT_DRM)

    @allure.title("Check oasis debug checkbox on the first panel")
    def test_oasis_checkbox_main_panel(self, app_page):
        debug_mode_checkbox = app_page.one_panel.checkbox
        expect(debug_mode_checkbox, make_failure_screenshot(app_page)).to_be_visible()

        debug_mode_checkbox.check()
        reload_button_click(page=app_page)
        expect(debug_mode_checkbox, make_failure_screenshot(app_page)).to_be_checked()

    @allure.title("Check live environment selection")
    def test_live_environment_main_panel(self, app_page):
        verify_dropdown_selection(
            app_page,
            app_page.one_panel.environment_select,
            "live",
            "Live environment"
        )


    @allure.title("Check second panel exist and extendable")
    def test_check_second_panel_exist(self, app_page):
        expect(app_page.extend_button, make_failure_screenshot(app_page)).to_have_text("Extended:")
        app_page.extend_button.click()
        expect(app_page.extend_button, make_failure_screenshot(app_page)).to_have_attribute("aria-expanded", "true")
