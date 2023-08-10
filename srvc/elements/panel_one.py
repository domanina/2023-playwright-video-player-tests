from srvc.elements.base_element import BaseElement


class PanelOne(BaseElement):

    def __init__(self, selector: str, parent):
        super().__init__(selector, parent)
        self.content_id_input = self.locator.locator("xpath=//input[@name='jhhfggfh']")
        self.user_agent_input = self.locator.locator("xpath=//input[@id='mhhtgfrgf']")
        self.streaming_select = self.locator.locator("xpath=....")
        self.environment_select = self.locator.locator("xpath=...")
        self.protocol_select = self.locator.locator("xpath=...")
        self.playback_plugin_select = self.locator.locator("xpath=...")
