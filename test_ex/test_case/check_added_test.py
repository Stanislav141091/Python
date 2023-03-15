from framework.utils.browser_utils import BrowserUtils
from pages.main_page import MainPage
from pages.nexage_project_page import NexagePage
from pages.project_page import ProjectPage
from pages.test_page import TestPage
from framework.utils.get_random_string import get_random_string
from framework.utils.time_util import get_current_time
from framework.utils.encode_util import Encode
from framework.utils.get_text_from_file import get_text_from_file
from test_data.test_data import TestData
import os


def test_check_added_test(close):
    browser_utils = BrowserUtils()
    main_page = MainPage()
    nexage = NexagePage()
    project_page = ProjectPage()
    test_page = TestPage()
    qty_symbols = TestData.get_qty_symbols()
    browser_utils.go_to_site()
    browser_utils.upload_cookies()
    browser_utils.refresh_page()
    version = TestData.get_version()
    assert main_page.get_version() == version, 'Version: 3 is displayed'
    main_page.click_nexage_project()
    list = nexage.get_list_started_time()
    assert nexage.compare_list_of_elements(list), 'Sort by start time is corrected'
    nexage.click_home_button()
    main_page.click_add_button()
    project = get_random_string(qty_symbols)
    main_page.input_project_name(project)
    main_page.click_save_project_button()
    assert main_page.check_alert() == main_page.saved_alert(project), 'Alert is displayed'
    browser_utils.closepopup()
    browser_utils.refresh_page()
    assert main_page.check_created_project(project) == project, 'Added project is displayed'
    main_page.click_new_project(project)
    project_page.click_add_button()
    test_name = get_random_string(qty_symbols)
    project_page.fill_test_name_field(test_name)
    test_method = get_random_string(qty_symbols)
    project_page.fill_test_method_field(test_method)
    start_time = get_current_time()
    project_page.fill_start_time_field(start_time)
    end_time = get_current_time()
    project_page.fill_end_time_field(end_time)
    environment = get_random_string(qty_symbols)
    project_page.fill_environment_field(environment)
    browser = get_random_string(qty_symbols)
    project_page.fill_browser_field(browser)
    log_file = TestData.get_log_file_name()
    log = get_text_from_file(log_file)
    project_page.fill_log_field(log)
    file_name = TestData.get_screenshot_name()
    browser_utils.create_screenshot(file_name)
    path = os.path.abspath(file_name)
    project_page.add_attach(path)
    project_page.click_save_test_button()
    assert project_page.check_alert() == project_page.alert(test_name), 'Alert is displayed'
    browser_utils.click_by_coordinate(100, 350)
    assert project_page.check_added_test(test_name) == test_name, 'Created test is displayed'
    project_page.click_created_test(test_name)
    assert project == test_page.get_project_name(), "Project name is matched"
    assert test_name == test_page.get_test_name(), "Test name is matched"
    assert test_method == test_page.get_test_method(), "Test method is matched"
    assert log in test_page.get_logs(), "Logs is matched"
    assert start_time in test_page.get_start_time(), "Start time is matched"
    assert end_time in test_page.get_end_time(), "End time is matched"
    assert environment == test_page.get_environment(), "Environment is matched"
    assert browser == test_page.get_browser(), "Browser is matched"
    assert Encode.encode_file(file_name) in test_page.get_image_src(), "File is matched"