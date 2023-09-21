def test_login_page_positive(self):
    self.open("https://staging.1md.org")
    self.click_link_text('Login')
    self.assert_text_visible("Login")
    self.send_keys("name=email", email)
    self.send_keys("name=password", password)
    self.click(".cta")
    self.assert_text("Your Subscription Box")
    self.click_link_text("log-out")
    self.assert_element_visible(By.XPATH, "//img[@alt='1MD Nutrition™']")
    self.tearDown()


def test_login_page_negative(self):
    self.open("https://staging.1md.org")
    self.click_link_text('Login')
    self.assert_text_visible("Login")
    self.send_keys("name=email", "wrongemail@gmail.com")
    self.send_keys("name=password", "wrontpassword")
    self.click(".cta")
    self.assert_text_visible("Log-in incorrect, please try again")