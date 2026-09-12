from Base.selenium_base import SeleniumBase

from .Test_page_1_locator import Element_Locator

from selenium import webdriver

import pytest

class Test_page_One(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.d1 = Element_Locator()

    def enter_multiple_values(self,username,password,address):
        self.element_enter_text(self.d1.user_name,username)
        self.element_enter_text(self.d1.password,password)
        self.element_enter_text(self.d1.address,address)

    def element_checkbox_radio(self):
        self.click_element(self.d1.gender)      
        self.click_element(self.d1.check_box)

    def country_func(self,value):
        self.drop_down_selection(self.d1.country_name,value)
              