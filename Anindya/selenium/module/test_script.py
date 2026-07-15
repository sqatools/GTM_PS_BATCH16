import selenium

from selenium import webdriver

from selenium.webdriver.common.by import By

import pytest

import time

from .locators import Element_locator
from .SeleniumBase import SeleniumBase


@pytest.mark.usefixtures("get_driver")
class Test_script:

    @pytest.fixture(scope="function",autouse=True)
    def setup(self):
        self.s1 = SeleniumBase(self.driver)
        self.d1 = Element_locator()

    def test_1(self):
        self.s1.element_enter_text(self.d1.fromcity,"Mumbai")
        self.s1.element_enter_text(self.d1.descity,"Kolkata")
        self.s1.element_enter_text(self.d1.drpart_date,"28/10/1993")
        self.s1.element_enter_text(self.d1.return_date,"12/11/2026")

    def test2(self):

        print(self.s1.read_text(self.d1.text_field))

    def test3(self):
        self.s1.element_click(self.d1.click_field)



