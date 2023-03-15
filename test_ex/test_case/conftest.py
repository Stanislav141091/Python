import pytest
from framework.drivers.driver import Driver


@pytest.fixture(scope="session")
def close():
    Driver.get_instance()
    yield
    Driver.reset_instance()