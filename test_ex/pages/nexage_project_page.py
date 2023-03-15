from framework.base_page import BasePage
from framework.elements.button import Button
from framework.elements.list_of_elements import Elements
from datetime import datetime
from framework.utils.log_conf_util import Loger


class NexagePage(BasePage):

    __home_button = Button("//a[contains(text(),'Home')]", "Home button")
    __table = Elements("//table[@class='table']//tr", "List of elements")
    __test = ("//table[@class='table']//tr", "")
    __start_time = ("//td[4]")
    __list_of_start_time = Elements("//table[@class='table']//tr//td[4]", "Started time")
    __uniq_elem = "//li[contains(text(),'Nexage')]"

    def __init__(self):
        super().__init__(locator=NexagePage.__uniq_elem)

    def click_home_button(self):
        Loger.info(f"Click home button")
        self.__home_button.click_on_the_element()

    def get_list_started_time(self):
        list = self.__list_of_start_time.get_list_of_elements()
        Loger.info(f"Get list of element {list}")
        return list

    def compare_list_of_elements(self, list_of_element):
        Loger.info(f"Check {list_of_element}")
        date_format = "%Y-%m-%d %H:%M:%S.%f"
        qty_elements = len(list_of_element)
        Loger.info(f"Elements {qty_elements}")
        x = 0
        while x == qty_elements - 1:
            first_data = list_of_element[x].text
            Loger.info(f"Elements {first_data}")
            first_time = datetime.strptime(first_data, date_format)
            x += 1
            second_data = list_of_element[x].text
            Loger.info(f"Elements {second_data}")
            second_time = datetime.strptime(second_data, date_format)
            result = first_time > second_time
            if result != True:
                return False
        return True