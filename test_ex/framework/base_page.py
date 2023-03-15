from framework.elements.label import Label


class BasePage:

    def __init__(self, locator):
        self.__uniq_element_home_page = Label(locator, "Element")

    def check_uniq_element_home_page(self):
        self.__uniq_element_home_page.element_is_displayed()