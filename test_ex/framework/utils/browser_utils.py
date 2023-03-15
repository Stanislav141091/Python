from configuration.configuration import Configuration
from selenium.webdriver.common.action_chains import ActionChains
from framework.drivers.driver import Driver
from framework.api.api import get_token


class BrowserUtils:

    def __init__(self):
        self.url = "http://" + Configuration.get_login() + ":" + Configuration.get_password() + "@" \
                   + Configuration.get_url()
        self.script_closepopup = ("$('#addProject').modal('hide')")

    def go_to_site(self):
        return Driver.get_instance().get(self.url)

    def upload_cookies(self):
        token = get_token()
        Driver.get_instance().add_cookie({'name': 'token', 'value': token})

    def refresh_page(self):
        return Driver.get_instance().refresh()

    def click_by_coordinate(self, x, y):
        ActionChains(Driver.get_instance()).reset_actions()
        ActionChains(Driver.get_instance()).move_by_offset(x, y).click().perform()

    def create_screenshot(self, file_name):
        Driver.get_instance().save_screenshot(file_name)

    def closepopup(self):
        Driver.get_instance().execute_script(self.script_closepopup)