from Base.selenium_base import SeleniumBase

from .Test_page1_locator import Element_locator
from selenium import webdriver

import pytest

class Test_Page_one(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.d1 = Element_locator()

    def enter_multiple_city(self,fromcity,descity):
        self.element_enter_text(self.d1.fromcity,fromcity)
        self.element_enter_text(self.d1.descity,descity)
            

