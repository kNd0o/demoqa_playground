import pytest
from pages.textbox_page import TextBoxPage
from config.data import Data


class BaseTest:
    data: Data
    textbox_page: TextBoxPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.textbox_page = TextBoxPage(driver)
