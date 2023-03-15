from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from configuration.configuration import Configuration


class Driver:

    __instance = None

    @staticmethod
    def get_instance():
        if Driver.__instance is None:
            if Configuration.get_browser() == "Chrome":
                Driver.__instance = Driver.get_driver_chrome()
            elif Configuration.get_browser() == "Firefox":
                Driver.__instance = Driver.get_driver_firefox()
        return Driver.__instance

    @staticmethod
    def get_browser(browser):
        if browser == 'Chrome':
            return

    @staticmethod
    def get_driver_chrome():
        options = webdriver.ChromeOptions()
        if Configuration.get_screen_size():
            options.add_argument("--start-maximized")
        if Configuration.get_incognito_mod():
            options.add_argument("--incognito")
        driver = webdriver.Chrome((ChromeDriverManager().install()), chrome_options=options)
        return driver

    @staticmethod
    def get_driver_firefox():
        options = webdriver.FirefoxOptions()
        if Configuration.get_screen_size():
            options.add_argument("--start-maximized")
        if Configuration.get_incognito_mod():
            options.add_argument("--incognito")
        driver = webdriver.Firefox((GeckoDriverManager.install()), firefox_profile=options)
        return driver

    @staticmethod
    def reset_instance():
        Driver.get_instance().quit()
        if Driver.__instance is not None:
            Driver.__instance = None
            return Driver.__instance