from framework.elements.base_elements import BaseElement


class Label(BaseElement):

    def __init__(self, locator, name_of_element):
        super().__init__(locator, name_of_element)