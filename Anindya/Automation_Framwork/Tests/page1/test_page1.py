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
    # @pytest.mark.f2
    def test_case_one(self):
        # self.t1.enter_multiple_city("MUmbai","Bangalore")
        # import pdb; pdb.set_trace()
        self.t1.enter_multiple_city(self.userr_data["fromcity"],self.userr_data["descity"])
        time.sleep(10)


    def test_case_two(self):
        self.t1.select_gender(self.userr_data["gender"])  
        time.sleep(5)  

    def test_case_three(self):
        self.t1.select_passenger(self.userr_data["passenger"])    
        time.sleep(5)

    def test_case_four(self):
        self.t1.select_country(self.userr_data["country"])
        time.sleep(5)
        

    def test_case_five(self):
        self.t1.select_first_name_last_name(self.userr_data["firstname"],self.userr_data["lastname"])
        time.sleep(5)

    def test_case_six(self):
        self.t1.select_all_details(self.userr_data["billing_name"],self.userr_data["billing_phone"],self.userr_data["email"],self.userr_data["address"],self.userr_data["postcode"],self.userr_data["prefeture"])    
        time.sleep(5)