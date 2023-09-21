from page_objects.login_page import *


class TestLoginPage(BaseCase):
    def test_login_page_positive(self):
        login = LoginPage(self)

        login.navigate_to()
        login.enter_email()
        login.enter_password()
        login.click_login_button()
        login.text_visible()
        login.logo_visible()
        login.logout()

    def test_login_page_negative(self):
        login = LoginPage(self)

        login.navigate_to()
        login.input_negative_email()
        login.input_negative_password()
        login.click_login_button()
        login.incorrect_login_text_visible()
