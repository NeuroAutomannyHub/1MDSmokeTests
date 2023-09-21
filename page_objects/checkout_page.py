from seleniumbase import BaseCase
from tests.user_data import *


class CheckoutPage:
    URL = "https://staging.1md.org/"
    SHOP_PAGE = "Shop"
    PRODUCT_PAGE = "//a[@href='/product/probiotics']"
    SS_SELECTOR = "//div[@class='pricing-area remove-product-image']//div[@id='pdpst2v1']//div[@id='pdp-card-ss']"
    ADD_TO_CART_BUTTON = "//div//a[@class='pdp-card-add-to-cart-link'][""normalize-space()='Add to cart']"
    NAME_INPUT = "//input[@placeholder='Full Name']"
    EMAIL_INPUT = "//input[@placeholder='Email']"
    STREET_ADDRESS_INPUT = "//input[@placeholder='Street Address']"
    CITY_INPUT = "//input[@placeholder='City / Town']"
    STATE_DROPDOWN = "/html//select[@id='address-shipping-address_state']"
    STATE_DROPDOWN_SELECTION = "California"
    ZIP_INPUT = "//input[@placeholder='Zip / Postal Code']"
    PHONE_NUMBER_INPUT = "//input[@placeholder='Phone number']"
    SHIP_TO_THIS_ADDRESS_BUTTON = "//button[normalize-space()='Ship to This Address']"
    CONFIRM_DELIVERY_BUTTON = "//button[normalize-space()='Confirm Delivery Option']"

    def __init__(self, base_case: BaseCase):
        self._base = base_case

    def navigate_to_url(self):
        self._base.open(self.URL)

    def click_shop(self):
        self._base.click_link_text(self.SHOP_PAGE)

    def click_on_product(self):
        self._base.click_xpath(self.PRODUCT_PAGE)

    def click_ss_selector(self):
        self._base.click(self.SS_SELECTOR)

    def add_to_cart_button(self):
        self._base.click_xpath(self.ADD_TO_CART_BUTTON)

    def input_name(self):
        self._base.type(self.NAME_INPUT, name)

    def input_email(self):
        self._base.type(self.EMAIL_INPUT, email)

    def input_street_address(self):
        self._base.type(self.STREET_ADDRESS_INPUT, street_address)

    def input_city(self):
        self._base.type(self.CITY_INPUT, city)

    def select_state_dropdown(self):
        self._base.select_option_by_text(self.STATE_DROPDOWN, self.STATE_DROPDOWN_SELECTION)

    def input_zip(self):
        self._base.type(self.ZIP_INPUT, zip_code)

    def input_phone_number(self):
        self._base.type(self.PHONE_NUMBER_INPUT, phone_number)

    def click_ship_to_this_address_button(self):
        self._base.click_xpath(self.SHIP_TO_THIS_ADDRESS_BUTTON)

    def click_confirm_delivery_button(self):
        self._base.click_xpath(self.CONFIRM_DELIVERY_BUTTON)
