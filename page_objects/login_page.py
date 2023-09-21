from seleniumbase import BaseCase
from tests.user_data import *


class LoginPage:
    URL = "https://staging.1md.org/account/login"
    EMAIL_FIELD = "name=email"
    PASSWORD_FIELD = "name=password"
    LOGIN_BUTTON = ".cta"
    LOGOUT_BUTTON = "//a[@class='g_id_signout']"
    LOGO_IMAGE = "//img[@alt='1MD Nutrition™']"
    INCORRECT_LOGIN = "Log-in incorrect, please try again"
    WELCOME_QA = "//em[normalize-space()='Welcome, QA']"
    NEGATIVE_EMAIL = "negativeemail@gmail.com"
    NEGATIVE_PASSWORD = "negativepassword"

    def __init__(self, base_case: BaseCase):
        self._base = base_case

    def navigate_to(self):
        self._base.open(self.URL)

    def enter_email(self):
        self._base.type(self.EMAIL_FIELD, email)

    def enter_password(self):
        self._base.type(self.PASSWORD_FIELD, password)

    def click_login_button(self):
        self._base.click(self.LOGIN_BUTTON)

    def logout(self):
        self._base.click(self.LOGOUT_BUTTON)

    def text_visible(self):
        assert self._base.is_element_visible(self.WELCOME_QA)

    def logo_visible(self):
        assert self._base.is_element_visible(self.LOGO_IMAGE)

    def incorrect_login_text_visible(self):
        assert self._base.is_text_visible(self.INCORRECT_LOGIN)

    def input_negative_email(self):
        self._base.type(self.EMAIL_FIELD, self.NEGATIVE_EMAIL)

    def input_negative_password(self):
        self._base.type(self.PASSWORD_FIELD, self.NEGATIVE_PASSWORD)
