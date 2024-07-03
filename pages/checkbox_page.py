import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


# desktop documents>workspace+office downloads


class CheckBoxPage(BasePage):
    PAGE_URL = Links.CHECKBOX_URL
    EXPAND_ALL_BTN = (By.CSS_SELECTOR, '.rct-option-expand-all')
    COLLAPSE_ALL_BTN = (By.CSS_SELECTOR, '.rct-option-collapse-all')
    HOME_CHECKBOX = (By.XPATH, '//*[@id="tree-node"]/ol/li/span/label')
    HOME_TOGGLE = (By.XPATH, '//*[@id="tree-node"]/ol/li/span/button')
    DESKTOP_CHECKBOX = (By.ID, 'tree-node-desktop')
    DESKTOP_TOGGLE = (
        By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[1]/span/button')
    DOCUMENTS_CHECKBOX = (By.ID, 'tree-node-documents')
    DOCUMENTS_TOGGLE = (
        By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[2]/span/button')
    WORKSPACE_CHECKBOX = (By.ID, 'tree-node-workspace')
    OFFICE_CHECKBOX = (By.ID, 'tree-node-office')
    DOWNLOADS_CHECKBOX = (By.ID, 'tree-node-downloads')
    REACT_CHECKBOX = (By.ID, 'tree-node-react')
    SELECTED_ELEMENT = (By.CSS_SELECTOR, '.text-success')

    @allure.step('Click expand tree button')
    def expand_tree(self):
        self.wait.until(ec.element_to_be_clickable(
            self.EXPAND_ALL_BTN)).click()

    @allure.step('Click collapse tree button')
    def collapse_tree(self):
        self.wait.until(ec.element_to_be_clickable(
            self.COLLAPSE_ALL_BTN)).click()

    @allure.step('Check home node')
    def check_home_node(self):
        self.wait.until(ec.element_to_be_clickable(self.HOME_CHECKBOX)).click()

    @allure.step('Toggle Home node')
    def toggle_home_node(self):
        self.wait.until(ec.element_to_be_clickable(self.HOME_TOGGLE)).click()

    @allure.step('Check if first depth element is visible')
    def is_tree_collapsed(self):
        assert not self.is_element_present(*self.DESKTOP_CHECKBOX), 'First depth element is visible'

    @allure.step('Check if last depth element is visible')
    def is_tree_expanded(self):
        assert self.is_element_present(*self.REACT_CHECKBOX), 'Last depth element is not visible'

    @allure.step('Extract selected elements list')
    def extract_selected_elements(self):
        elements_selected = self.driver.find_elements(*self.SELECTED_ELEMENT)
        return [elem.text for elem in elements_selected]

    @allure.step('Check selected elements')
    def check_selected_elements(self, lst):
        assert lst == self.extract_selected_elements(), 'Lists of elements dont match'
