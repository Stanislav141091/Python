from framework.base_page import BasePage
from framework.elements.button import Button
from framework.elements.textfield import TextField
from framework.elements.label import Label
import logging
from framework.utils.log_conf_util import Loger


class ProjectPage(BasePage):

    __home_button = Button("//a[contains(text(),'Home')]", "Home button")
    __add_button = Button("//button[contains(text(),'+Add')]", "Add button")
    __test_name_field = TextField("//input[contains(@name,'testName')]", "Test name field")
    __test_method_field = TextField("//input[contains(@name,'testMethod')]", "Test method field")
    __start_time_field = TextField("//input[contains(@name,'startTime')]", "Start time field")
    __end_time_field = TextField("//input[contains(@name,'endTime')]", "End time field")
    __environment_field = TextField("//input[contains(@name,'environment')]", "Environment field")
    __browser_field = TextField("//input[contains(@name,'browser')]", "Browser field")
    __save_test_button = Button("//button[contains(text(),'Save')]", "Save test button")
    __log_field = TextField("//textarea[@id='log']", "Log field")
    __upload_file = TextField("//input[@id='attachment']", "Upload field")
    __success_alert = Label("//div[contains(@class,'alert-success')]", "Success alert")
    __created_test = ("//a[contains(text(),'")
    __uniq_elem = "//div[@class='panel-heading']"

    def __init__(self):
        super().__init__(locator=ProjectPage.__uniq_elem)

    def click_home_button(self):
        Loger.info(f"Click home button")
        self.__home_button.click_on_the_element()

    def click_add_button(self):
        Loger.info(f"Click add button")
        self.__add_button.click_on_the_element()

    def fill_test_name_field(self, test_name):
        Loger.info(f"Input {test_name} in field")
        self.__test_name_field.send_value(test_name)

    def fill_test_method_field(self, test_method):
        Loger.info(f"Input {test_method} in field")
        self.__test_method_field.send_value(test_method)

    def fill_start_time_field(self, start_time):
        Loger.info(f"Input {start_time} in field")
        self.__start_time_field.send_value(start_time)

    def fill_end_time_field(self, end_time):
        Loger.info(f"Input {end_time} in field")
        self.__end_time_field.send_value(end_time)

    def fill_environment_field(self, environment):
        Loger.info(f"Input {environment} in field")
        self.__environment_field.send_value(environment)

    def fill_browser_field(self, browser):
        Loger.info(f"Input {browser} in field")
        self.__browser_field.send_value(browser)

    def fill_log_field(self,log):
        Loger.info(f"Input {log} in field")
        self.__log_field.send_value(log)

    def add_attach(self, file_path):
        Loger.info(f"Add attach")
        self.__upload_file.send_value(file_path)

    def click_save_test_button(self):
        Loger.info(f"Click save button")
        self.__save_test_button.click_on_the_element()

    def check_alert(self):
        Loger.info(f"Check alert")
        text = self.__success_alert.get_text_from_element()
        return text

    def check_added_test(self, test_name):
        Loger.info(f"Check {test_name} in field")
        added_test = self.__created_test + test_name + "')]"
        test = Button(added_test, "Check added test")
        get_name = test.get_text_from_element()
        return get_name

    def click_created_test(self,test_name):
        Loger.info(f"Click {test_name}")
        created_test = self.__created_test + test_name + "')]"
        test = Button(created_test, "Click test")
        test.click_on_the_element()

    def alert(self, test_name):
        Loger.info(f"Check alert")
        return f"Test {test_name} saved"