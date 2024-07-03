import allure
import pytest
from base.base_test import BaseTest


@allure.feature('Checkbox test')
class TestCheckBox(BaseTest):
    @allure.title('Checkbox')
    def test_checkbox_collapse_expand(self):
        self.checkbox_page.open()
        self.checkbox_page.wait_to_open()
        self.checkbox_page.expand_tree()
        self.checkbox_page.debug_sleep(3)
        self.checkbox_page.check_home_node()
        self.checkbox_page.debug_sleep(3)
        self.checkbox_page.toggle_home_node()
        self.checkbox_page.debug_sleep(3)
        self.checkbox_page.collapse_tree()
        self.checkbox_page.debug_sleep(3)
