import logging
from selenium.webdriver.common.by import By
from framework.drivers.driver import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from configuration.configuration import Configuration
from framework.utils.log_conf_util import Loger


class BaseElement:

    def __init__(self, locator, name_of_elements):
        self.locator = locator
        self.name_of_element = name_of_elements

    def find_element(self):
        Loger.info(f"Finding element {self.name_of_element}")
        path_locator = (By.XPATH, self.locator)
        return WebDriverWait(Driver.get_instance(), Configuration.get_time()).until(
            EC.element_to_be_clickable(path_locator))

    def find_elements(self):
        Loger.info(f"Finding elements {self.name_of_element}")
        path_locator = (By.XPATH, self.locator)
        return WebDriverWait(Driver.get_instance(), Configuration.get_time()).until(
            EC.presence_of_all_elements_located(path_locator))

    def click_on_the_element(self):
        Loger.info(f"Clicking on the {self.name_of_element}")
        self.find_element().click()

    def get_text_from_element(self):
        Loger.info(f"Got a text from {self.name_of_element}")
        return BaseElement.find_element(self).text

    def element_is_displayed(self):
        Loger.info(f"{self.name_of_element} is displayed")
        return BaseElement.find_element(self).is_displayed()

    def get_the_attribute_value(self, attribute):
        Loger.info(f"Getting the {attribute} from {self.name_of_element}")
        return BaseElement.find_element(self).get_attribute(attribute)

    def get_list_of_elements(self):
        Loger.info(f"Getting list of elements from {self.name_of_element}")
        return self.find_elements()

    def get_quantity_of_elements(self):
        Loger.info(f"Getting quantity of elements from {self.name_of_element}")
        return len(self.find_elements())