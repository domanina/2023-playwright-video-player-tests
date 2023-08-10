from srvc.elements.base_element import BaseElement


class PanelTwo(BaseElement):

    def __init__(self, selector: str, parent):
        super().__init__(selector, parent)
        self.token_input = self.locator.locator("xpath=//input[@name='kuhhtfghjhk']")
        self.pin_input = self.locator.locator("xpath=//input[@name='lkkjhggfvghjk']")
        self.country_code_input = self.locator.locator("xpath=//input[@name='bgewdewghdujew']")
        self.access_id_input = self.locator.locator("xpath=//input[@name='djnjwhgdweghdj']")
        self.timestamp_input = self.locator.locator("xpath=//input[@name='ckdgcdghchwj']")
