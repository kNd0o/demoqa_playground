import pytest
from pages.textbox_page import TextBoxPage
from pages.checkbox_page import CheckBoxPage
from config.data import Data


class BaseTest:
    data: Data
    textbox_page: TextBoxPage
    checkbox_page: CheckBoxPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.textbox_page = TextBoxPage(driver)
        request.cls.checkbox_page = CheckBoxPage(driver)
