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
