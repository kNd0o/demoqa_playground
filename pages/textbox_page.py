import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class TextBoxPage(BasePage):
    PAGE_URL = Links.TEXTBOX_URL
    FULLNAME_FIELD = (By.ID, 'userName')
    EMAIL_FIELD = (By.ID, 'userEmail')
    CURR_ADDRESS_FIELD = (By.ID, 'currentAddress')
    PERMA_ADDRESS_FIELD = (By.ID, 'permanentAddress')
    BTN_SUBMIT = (By.ID, 'submit')
    OUTPUT_NAME = (By.ID, 'name')
    OUTPUT_EMAIL = (By.ID, 'email')
    OUTPUT_CURRADDRESS = (By.CSS_SELECTOR, '.border #currentAddress')
    OUTPUT_PERMADDRESS = (By.CSS_SELECTOR, '.border #permanentAddress')

    @allure.step('Enter fullname')
    def enter_fullname(self, fullname):
        self.wait.until(ec.element_to_be_clickable(
            self.FULLNAME_FIELD)).send_keys(fullname)

    @allure.step('Enter email')
    def enter_email(self, email):
        self.wait.until(ec.element_to_be_clickable(
            self.EMAIL_FIELD)).send_keys(email)

    @allure.step('Enter current address')
    def enter_current_address(self, current_address):
        self.wait.until(ec.element_to_be_clickable(
            self.CURR_ADDRESS_FIELD)).send_keys(current_address)

    @allure.step('Enter permanent address')
    def enter_permanent_address(self, permanent_address):
        self.wait.until(ec.element_to_be_clickable(
            self.PERMA_ADDRESS_FIELD)).send_keys(permanent_address)

    @allure.step('Click submit button')
    def click_submit(self):
        self.wait.until(ec.element_to_be_clickable(self.BTN_SUBMIT)).click()

    @allure.step('Check fullname output')
    def check_fullname_output(self, input_name):
        if self.is_element_present(*self.OUTPUT_NAME):
            text = self.driver.find_element(
                *self.OUTPUT_NAME).text.split(':')[1]
            assert text == input_name, f'Input text: {input_name} doesnt match output: {text}'

    @allure.step('Check email output')
    def check_email_output(self, input_email):
        if self.is_element_present(*self.OUTPUT_EMAIL):
            text = self.driver.find_element(
                *self.OUTPUT_EMAIL).text.split(':')[1]
            assert text == input_email, f'Input text: {input_email} doesnt match output {text}'

    @allure.step('Check current address output')
    def check_curraddress_output(self, input_curr_address):
        if self.is_element_present(*self.OUTPUT_CURRADDRESS):
            text = self.driver.find_element(
                *self.OUTPUT_CURRADDRESS).text.split(':')[1]
            assert text == input_curr_address, f'Input text {input_curr_address} doesnt match {text}'

    @allure.step('Check permanent address output')
    def check_permaddress_output(self, input_perm_address):
        if self.is_element_present(*self.OUTPUT_PERMADDRESS):
            text = self.driver.find_element(
                *self.OUTPUT_PERMADDRESS).text.split(':')[1]
            assert text == input_perm_address, f'Input text {input_perm_address} doesnt match {text}'

    # def fill_textbox_form(self, fullname, email, current_address, permanent_address):
    #     self.enter_fullname(fullname)
    #     self.enter_email(email)
    #     self.enter_current_address(current_address)
    #     self.enter_permanent_address(permanent_address)
