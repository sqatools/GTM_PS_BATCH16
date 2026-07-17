from selenium import webdriver

from selenium.webdriver.common.by import By

import pytest

import time

from PageObjectModel.Page_1.test_page1_class import Test_Page_one

from Utilities.utils import Utils

@pytest.mark.usefixtures("get_driver")
class Test_Page_New:
    
    @pytest.fixture(scope="function",autouse=True)
    def setup(self):
        self.t1 = Test_Page_one(self.driver)
        self.util = Utils()
        self.userr_data = self.util.read_json_data("PageObjectModel/Page_1/user_data.json")

    def test_case_one(self):
        # self.t1.enter_multiple_city("MUmbai","Bangalore")
        import pdb; pdb.set_trace()
        self.t1.enter_multiple_city(self.userr_data["fromcity"],self.userr_data["descity"])
        time.sleep(10)

