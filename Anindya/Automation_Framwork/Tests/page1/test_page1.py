from selenium import webdriver

from selenium.webdriver.common.by import By

import pytest

import time

from PageObjectModel.Page_1.test_page1_class import Test_Page_one

@pytest.mark.usefixtures("get_driver")
class Test_Page_New:
    
    @pytest.fixture(scope="function",autouse=True)
    def setup(self):
        self.t1 = Test_Page_one(self.driver)

    def test_case_one(self):
        self.t1.enter_multiple_city("MUmbai","Bangalore")
        time.sleep(10)

