from srvc.elements.base_element import BaseElement


class PanelThree(BaseElement):

    def __init__(self, selector: str, parent):
        super().__init__(selector, parent)
        self.field_names = self.locator.locator("xpath=//*[@class='lzjkahzjha']")
        self.field_data = self.locator.locator("xpath=//*[@class='jhbgbvgfvhj']")
