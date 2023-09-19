import os
from dotenv import load_dotenv

load_dotenv()
name = os.getenv("NAME")
email = os.getenv("LOGINEMAIL")
street_address = os.getenv("STREETADDRESS")
city = os.getenv("CITY")
zip_code = os.getenv("ZIPNUMBER")
phone_number = os.getenv("PHONENUMBER")
card_number = os.getenv("CCNUMBER")
exp_date = os.getenv("EXPDATE")
cvv = os.getenv("CVV")
billing_zip = os.getenv("BILLINGZIP")
password = os.getenv("PASSWORD")