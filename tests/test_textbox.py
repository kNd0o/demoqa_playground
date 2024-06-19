import allure
import pytest

from base.base_test import BaseTest


@allure.feature('Textbox test')
class TestTextBox(BaseTest):
    @allure.title('Textbox')
    def test_textbox(self):
        self.textbox_page.open()
        self.textbox_page.wait_to_open()
        self.textbox_page.enter_fullname(self.data.FULL_NAME)
        self.textbox_page.enter_email(self.data.EMAIL)
        self.textbox_page.enter_current_address(self.data.CURR_ADDRESS)
        self.textbox_page.enter_permanent_address(self.data.PERMA_ADDRESS)
        self.textbox_page.click_submit()
        self.textbox_page.check_fullname_output(self.data.FULL_NAME)
        self.textbox_page.check_email_output(self.data.EMAIL)
        self.textbox_page.check_curraddress_output(self.data.CURR_ADDRESS)
        self.textbox_page.check_permaddress_output(self.data.PERMA_ADDRESS)
