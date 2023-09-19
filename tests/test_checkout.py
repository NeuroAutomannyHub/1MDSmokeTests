import time
from selenium.webdriver.common.by import By
from seleniumbase import BaseCase
from user_data import *


class TestCheckoutPage(BaseCase):

    def test_checkout_page_cc(self):
        self.open("https://staging.1md.org")
        self.click_link_text("Shop")
        self.click_xpath("//a[@href='/product/probiotics']")
        self.click(By.ID, "pdp-card-ss")
        self.click(By.CLASS_NAME, "pdp-card-add-to-cart-link")
        self.send_keys("name=name", name)
        self.send_keys("name=email", email)
        self.send_keys("name=address[shipping][address_street]", street_address)
        self.send_keys("name=address[shipping][address_city]", city)
        self.select_option_by_value("name=address[shipping][address_state]", "CA")
        self.send_keys("name=address[shipping][address_zip]", zip_code)
        self.send_keys("name=phone", phone_number)
        self.click_xpath("//button[normalize-space()='Ship to This Address']")
        self.click_xpath("//button[normalize-space()='Confirm Delivery Option']")

        time.sleep(3)

    def test_my_computer(self):
        self.open("djwiadjwa")
        self.click("sjdawd")
