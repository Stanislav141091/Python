import json


class TestData:

    @staticmethod
    def get_test_data():
        filename = '../test_data/test_data.json'
        with open(filename, 'r') as f_obj:
            data_json = f_obj.read()
            data = json.loads(data_json)
            return data

    @staticmethod
    def get_version():
        version = TestData.get_test_data().get("version")
        return version

    @staticmethod
    def get_qty_symbols():
        qty = TestData.get_test_data().get("qty_symbols")
        return qty

    @staticmethod
    def get_log_file_name():
        log = TestData.get_test_data().get("log_file_name")
        return log

    @staticmethod
    def get_screenshot_name():
        screenshot = TestData.get_test_data().get("screenshot_name")
        return screenshot

    @staticmethod
    def get_data():
        data = TestData.get_test_data().get("data")
        return data

    @staticmethod
    def get_test_variant():
        test_data = TestData.get_test_data().get("test_variant")
        return test_data

    @staticmethod
    def get_token_url():
        token_url = TestData.get_test_data().get("get_token")
        return token_url