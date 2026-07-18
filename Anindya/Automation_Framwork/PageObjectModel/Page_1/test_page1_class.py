from Base.selenium_base import SeleniumBase

from .Test_page1_locator import Element_locator
from selenium import webdriver

import pytest

class Test_Page_one(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.d1 = Element_locator()

    def enter_multiple_city(self,fromcity,descity):
        self.log.info("This function name is enter_multiple_city")
        self.element_enter_text(self.d1.fromcity,fromcity)
        self.element_enter_text(self.d1.descity,descity)

    def select_gender(self,gender):
        if gender.lower() == "male":
            self.element_click(self.d1.male_radio)   
        elif gender.lower() == "female":
            self.element_click(self.d1.female_radio)

    def select_passenger(self,value):
        self.element_dropdown(self.d1.drop_down_1,value)

    def select_country(self,value1):
        self.element_dropdown(self.d1.drop_down_2,value1)


    def select_first_name_last_name(self,firstname,lastname):
        self.element_enter_text(self.d1.first_name,firstname)
        self.element_enter_text(self.d1.last_name,lastname)


    def select_all_details(self,billing_name,billing_phone,email,address,postcode,prefeture):
        self.element_enter_text(self.d1.billing_name,billing_name)
        self.element_enter_text(self.d1.billing_phone,billing_phone)
        self.element_enter_text(self.d1.email,email)
        self.element_enter_text(self.d1.address,address)
        self.element_enter_text(self.d1.postcode,postcode)
        self.element_enter_text(self.d1.prefeture,prefeture)
                          
            

