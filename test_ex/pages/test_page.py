from framework.elements.label import Label
from framework.base_page import BasePage
import logging
from framework.utils.log_conf_util import Loger


class TestPage(BasePage):

    __project_name = Label("//h4[contains(text(),'Project name')]//following-sibling::p", "Project name")
    __test_name = Label("//h4[contains(text(),'Test name')]//following-sibling::p", "Test name")
    __test_method = Label("//h4[contains(text(),'Test method name')]//following-sibling::p", "Test method")
    __start_time = Label("//h4[contains(text(),'Time info')]//following-sibling::p[1]", "Start time")
    __end_time = Label("//h4[contains(text(),'Time info')]//following-sibling::p[2]", "End time")
    __environment = Label("//h4[contains(text(),'Environment')]//following-sibling::p", "Environment")
    __browser = Label("//h4[contains(text(),'Browser')]//following-sibling::p", "Browser")
    __image = Label("//img[@class='thumbnail']", "Image")
    __logs = Label("//div[contains(text(),'Logs')]//following-sibling::table//td", "Logs")
    __uniq_elem = "//div[contains(text(),'Common info')]"

    def __init__(self):
        super().__init__(locator=TestPage.__uniq_elem)

    def get_project_name(self):
        Loger.info(f"Get project name")
        project_name = self.__project_name.get_text_from_element()
        return project_name

    def get_test_name(self):
        Loger.info(f"Get test name")
        test_name = self.__test_name.get_text_from_element()
        return test_name

    def get_test_method(self):
        Loger.info(f"Get test method")
        method_name = self.__test_method.get_text_from_element()
        return method_name

    def get_start_time(self):
        Loger.info(f"Get start time")
        start_time = self.__start_time.get_text_from_element()
        return start_time

    def get_end_time(self):
        Loger.info(f"Get end time")
        end_time = self.__end_time.get_text_from_element()
        return end_time

    def get_environment(self):
        Loger.info(f"Get environment")
        environment = self.__environment.get_text_from_element()
        return environment

    def get_browser(self):
        Loger.info(f"Get browser")
        browser = self.__browser.get_text_from_element()
        return browser

    def get_logs(self):
        Loger.info(f"Get logs")
        logs = self.__logs.get_text_from_element()
        return logs

    def get_image_src(self):
        Loger.info(f"Get image")
        image = self.__image.get_the_attribute_value("src")
        return image