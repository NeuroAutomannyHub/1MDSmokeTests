import time

from selenium.webdriver.common.by import By
from seleniumbase import BaseCase


class TestCase(BaseCase):

    def test_apple_page(self):
        self.open("https://apple.com")
        self.click(By.XPATH, "//a[@aria-label='Store']//span[@class='globalnav-link-text-container']")
        self.click_xpath("//a[@class='rf-productnav-card-title'][normalize-space()='Mac']")
        self.click_xpath("//a[normalize-space()='Wallet']")
        time.sleep(3)