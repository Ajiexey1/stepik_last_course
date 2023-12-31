from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert '/login/' in self.browser.current_url, "it's not login link"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        # регистрация нового пользователя
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION_INPUT)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION_INPUT)
        input_password.send_keys(password)
        input_password_twice = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION_INPUT_TWICE)
        input_password_twice.send_keys(password)
        input_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        input_button.click()
