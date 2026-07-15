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

    def test_eneblaed_selected(self):
        assert self.s1.element_enabled(self.d1.male_radio), 'Button not enabled'
        assert self.s1.element_displayed(self.d1.male_radio), "Button not displayed"

        assert not self.s1.element_selected(self.d1.male_radio),'button is selected'
        self.s1.element_click(self.d1.male_radio)
        assert self.s1.element_selected(self.d1.male_radio), "Button is not selected"

    def test_verify_url_and_title(self):
        current_url = self.s1.get_url()
        print("The current url is ", current_url)
        assert "dummy" in current_url, "Not presengt"
        title = self.s1.get_title()
        print("The title is ", title)
        assert "Dummy" in title, "Title not matched"

    def drop_down(self):
        value = "Add 2 more passenger (200%)"
        self.s1.element_dropdown(self.d1.drop_down_1,value)
        value2 = "India"    
        self.s1.element_dropdown(self.d1.drop_down_2,value2)

        





