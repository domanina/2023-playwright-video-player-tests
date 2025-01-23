import allure
from assertpy import assert_that
from playwright.sync_api import expect

from consts import consts
from ui.helper import make_failure_screenshot


@allure.step("Reload button click")
def reload_button_click(page: PlayerPage):
    page.reload_button.click()


@allure.step("Fill CID input")
def fill_content_id(page: PlayerPage, content_id: str):
    content_id_input = page.main_panel.content_id_input
    expect(content_id_input, make_failure_screenshot(page)).to_be_visible()
    content_id_input.fill(content_id)


@allure.step("Fill inputs in extended panel")
def fill_inputs_one_panel(page: PlayerPage, **inputs):
    with allure.step("Click to extend additional panel"):
        page.extend_button.click()
    for field_name, value in inputs.items():
        if isinstance(value, bool):
            with allure.step(f"Check  box: {field_name}"):
                checkbox_locator = getattr(page.extended_panel, f"{field_name}", None)
                if checkbox_locator is None:
                    raise ValueError(f"Checkbox field '{field_name}' not found in panel")
                expect(checkbox_locator, make_failure_screenshot(page)).to_be_visible()
                checkbox_state = checkbox_locator.is_checked()
                if checkbox_state != value:
                    checkbox_locator.click()
        else:
            with allure.step(f"Fill input: {field_name}"):
                input_locator = getattr(page.extended_panel, f"{field_name}", None)
                if input_locator is None:
                    raise ValueError(f"Input field '{field_name}' not found in panel")
                expect(input_locator, make_failure_screenshot(page)).to_be_visible()
                input_locator.fill(value)


@allure.step("Verify playback button state")
def verify_playback_button(page: PlayerPage):
    play_button_handler = page.get_shadow_element(page.play_button)
    test_value = play_button_handler.evaluate('(element) => element.getAttribute("test-test")')
    assert_that(test_value, "Playback button state").is_equal_to(consts.PAUSE_BUTTON)
    play_button_handler.click()


@allure.step("Verify error message is displayed on player window")
def verify_error_message_on_player_window(page: PlayerPage):
    error_label_handler = page.get_shadow_element(page.error)
    assert_that(error_label_handler.text_content(), "Error on the player window").is_equal_to("Error")


@allure.step("Verify dropdown selection")
def verify_dropdown_selection(page: PlayerPage, locator, options_map, dropdown_name):
    for option, elem_path in options_map.items():
        with allure.step(f"Verify {dropdown_name} selection -> {option}"):
            locator.select_option(option)
            page.reload_button.click()
            expect(locator.locator(elem_path), make_failure_screenshot(page)).to_have_attribute("selected", "selected")


@allure.step("Play content in different environments")
def play_different_environment(page: PlayerPage, options):
    for option in options:
        page.one_panel.environment.select_option(option)
        reload_button_click(page)
