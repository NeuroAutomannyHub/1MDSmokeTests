import time

from page_objects.checkout_page import *


class TestCheckoutPage(BaseCase):
    def test_checkout_page_cc(self):
        checkout = CheckoutPage(self)

        checkout.navigate_to_url()
        checkout.click_shop()
        checkout.click_on_product()
        checkout.ss_selector()
        checkout.add_to_cart_button()
        checkout.input_name()
        checkout.input_email()
        checkout.input_street_address()
        checkout.input_city()
        checkout.select_state_dropdown()
        checkout.input_zip()
        checkout.input_phone_number()
        checkout.click_ship_to_this_address_button()
        checkout.click_confirm_delivery_button()
