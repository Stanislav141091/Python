import logging
from framework.elements.base_elements import BaseElement
from framework.utils.log_conf_util import Loger


class TextField(BaseElement):
    log = Loger.custom_logger(loglevel=logging.INFO)

    def __init__(self, locator, name_of_element):
        super().__init__(locator, name_of_element)

    def send_value(self, value):
        self.log.info(f"Sent {value} in the {self.name_of_element}")
        self.find_element().send_keys(value)

    def clean_field(self):
        self.log.info(f"{self.name_of_element} is clined")
        self.find_element().clear()