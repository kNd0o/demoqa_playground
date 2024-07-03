import allure
import pytest
from base.base_test import BaseTest


@allure.feature('Checkbox test')
class TestCheckBox(BaseTest):
    @allure.title('Full collapse/expand check')
    def test_checkbox_collapse_expand(self, driver):
        self.checkbox_page.open()
        self.checkbox_page.wait_to_open()
        self.checkbox_page.is_tree_collapsed()
        self.checkbox_page.expand_tree()
        self.checkbox_page.debug_sleep()
        self.checkbox_page.is_tree_expanded()
        self.checkbox_page.collapse_tree()

    @allure.title('Checking home checks all inner elements')
    def test_home_check_selects_all(self):
        self.checkbox_page.check_home_node()
        self.checkbox_page.check_selected_elements(self.data.CHECKBOX_ALL_ELEMENTS)
