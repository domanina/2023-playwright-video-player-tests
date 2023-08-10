from abc import ABC
from typing import Union

from srvc.pages.base_page import BasePage


class BaseElement(ABC):
    def __init__(self, selector: str, parent: Union[BasePage, "BaseElement"]):
        self.parent = parent
        self.selector = selector

        if isinstance(parent, BasePage):
            self.locator = self.parent.page.locator(self.selector)
        else:
            self.locator = parent.locator.locator(self.selector)

    def _get_page(self):
        return self.parent if isinstance(self.parent, BasePage) else self.parent._get_page()
