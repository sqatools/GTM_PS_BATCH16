from selenium import webdriver
from selenium.webdriver.common.by import By
from .SeleniumBase import SeleniumBase
from .locators import DummyLocators
import time
import pytest


@pytest.mark.usefixtures("get_driver_class")
class TestDummyWebsite:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.sb = SeleniumBase(self.driver)
        self.dl = DummyLocators()

    def test_enter_username(self):
        
        # self.driver.find_element(By.ID, "fromcity").send_keys("Assam")
        self.sb.enter_text(self.dl.fromCityField, "Mumbai")

        # self.driver.find_element(By.ID, "destcity").send_keys("Guwahati")
        self.sb.enter_text(self.dl.DestCityField, "Pune")


    def test_enter_dates(self):
        
        # self.driver.find_element(By.NAME, "departdate").send_keys("01/01/2026")
        # self.driver.find_element(By.NAME, "returndate").send_keys("03/01/2026")
        self.sb.enter_text(self.dl.DepartDate, "10/10/2023")
        self.sb.enter_text(self.dl.ReturnDate, "15/10/2023")
        


    def test_get_heading(self):
        
        # heading = self.driver.find_element(By.CLASS_NAME, "entry-title").text
        heading_text = self.sb.get_element_text(self.dl.PageHeading)
        print("Heading of the page is:", heading_text)
        # assert heading_text == "Dummy Booking Website"