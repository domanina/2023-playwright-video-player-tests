from playwright.sync_api import Page
from config.config import AUTOTEST_KEY
from consts.consts import INT_BASE_URL
from srvc.elements.panel_three import PanelThree
from srvc.elements.panel_two import PanelTwo
from srvc.elements.panel_one import PanelOne
from srvc.pages.base_page import BasePage


class PlayerPage(BasePage):
    URL = INT_BASE_URL + AUTOTEST_KEY
    PANEL_ONE = "xpath=//div[@id='...']//div[@class='...']"
    PANEL_TWO = "xpath=//div[@id='...']//div[@class='...']"
    PANEL_THREE = "//div[@id='...']//div[@class='...']//div[@id='...']"

    def __init__(self, page: Page):
        super().__init__(page)
        self.play_button = self.locator("xpath=//*[@class='djmnwxbewbdxjew']")
        self.mute_button = self.locator("xpath=//*[@hxjhx='xmhwjmsnxjwnx']")
        self.jump_forward_button = self.locator("...")
        self.jump_back_button = self.locator("....")
        self.subtitles_button = self.locator("....")
        self.extend_button = self.locator("....")
        self.played_time = self.locator("....")
        self.error = self.locator("xpath=//*[@class='lizjksuxsjkx']")
        self.one_panel = PanelOne(selector=self.PANEL_ONE, parent=self)
        self.two_panel = PanelTwo(selector=self.PANEL_TWO, parent=self)
        self.three_panel = PanelThree(selector=self.PANEL_THREE, parent=self)
