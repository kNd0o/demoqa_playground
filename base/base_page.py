import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        with allure.step(f'Open {self.PAGE_URL} page'):
            self.driver.get(self.PAGE_URL)

    def wait_to_open(self):
        with allure.step(f'Page {self.PAGE_URL} is opened'):
            self.wait.until(ec.url_to_be(self.PAGE_URL))

    def get_current_url(self):
        return self.driver.current_url

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.JPG
        )

    def is_element_present(self, by, locator):
        try:
            self.driver.find_element(by, locator)
        except NoSuchElementException:
            return False
        return True

    def debug_sleep(self, sec=1):
        time.sleep(sec)

    def wait_implicitly(self, sec=1):
        self.driver.implicitly_wait(sec)
