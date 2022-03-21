from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_form()
        self.should_be_register_form()
        self.should_be_login_url()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "no login word in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), 'no email entry field in login form'
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), 'no password entry field in login form'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), \
            'no email entry field in registration form'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_1),\
            'no password entry field in registration form'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_2),\
            'no password repeated entry field in registration form'
        assert True

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON).click()
