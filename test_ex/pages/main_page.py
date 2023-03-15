from framework.base_page import BasePage
from framework.elements.label import Label
from framework.elements.button import Button
from framework.elements.textfield import TextField
from framework.elements.modal_window import ModalWindow
from framework.elements.list_of_elements import Elements
from framework.utils.log_conf_util import Loger


class MainPage(BasePage):

    __version = Label("//p[contains(@class,'footer-text')]//span", "Version")
    __nexage_project = Button("//a[contains(text(),'Nexage')]","Nexage project button")
    __add_button = Button("//button[contains(text(),'+Add')]", "Add button")
    __project_name = TextField("//input[@class='form-control']", "Project name")
    __save_project = Button("//button[contains(text(),'Save')]", "Save project button")
    __add_new_project_form = ModalWindow("//div[@class='modal-content']", "Add new project form")
    __alert_success = Label("//div[contains(@class,'alert-success')]", "Success aller")
    __list_of_project = Elements("//a[@class='list-group-item']", "List of projects")
    __uniq_element = "//div[contains(text(),'Available project')]"

    def __init__(self):
        super().__init__(locator=MainPage.__uniq_element)

    def get_version(self):
        Loger.info(f"Get the version")
        version = self.__version.get_text_from_element()
        return version

    def click_nexage_project(self):
        Loger.info(f"Click the Nexage project")
        self.__nexage_project.click_on_the_element()

    def click_add_button(self):
        Loger.info(f"Click the add button")
        self.__add_button.click_on_the_element()

    def input_project_name(self, project):
        Loger.info(f"Input the {project} name")
        self.__add_new_project_form.element_is_displayed()
        self.__project_name.click_on_the_element()
        self.__project_name.send_value(project)

    def click_save_project_button(self):
        Loger.info(f"Click the save button")
        self.__save_project.click_on_the_element()

    def check_alert(self):
        Loger.info(f"Check alert")
        text = self.__alert_success.get_text_from_element()
        return text

    def check_created_project(self, project):
        Loger.info(f"Check created {project}")
        new_project = "//a[contains(text(),'{0}')]".format(project)
        check_project = Button(new_project, "Get text")
        text = check_project.get_text_from_element()
        return text

    def click_new_project(self, project):
        Loger.info(f"Click the {project}")
        new_project = f"//a[contains(text(),'{project}')]"
        click_project = Button(new_project, "Click button")
        click_project.click_on_the_element()

    def saved_alert(self, project):
        Loger.info(f"Check saved alert")
        return f"Project {project} saved"