import selenium

from selenium import webdriver

from selenium.webdriver.common.by import By

from PageObjectModel.page_1.Test_page_1_class import Test_page_One

import time

import pytest


@pytest.mark.usefixtures("get_driver")
class Test_One:

    @pytest.fixture(scope="function",autouse=True)
    def setup(self):
        self.obj_1 = Test_page_One(self.driver)

    def test_case_one(self):
        self.obj_1.enter_multiple_values("Anindya","Anindya@123","Neheru Nagar Colony")
        time.sleep(7)

    def test_case_two(self):
        self.obj_1.element_checkbox_radio()
        time.sleep(7)

    def test_case_three(self):
        self.obj_1.country_func("usa")   
        time.sleep(10) 




