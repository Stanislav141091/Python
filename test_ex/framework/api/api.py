import requests, requests.utils
from test_data.test_data import TestData


def get_token():
    url = TestData.get_token_url()
    param = {TestData.get_data(): TestData.get_test_variant()}
    token = requests.post(url, data=param)
    return str(token.text)