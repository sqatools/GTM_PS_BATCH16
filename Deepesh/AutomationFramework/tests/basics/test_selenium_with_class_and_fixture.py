from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.mark.usefixtures("get_driver_class")
class TestDummyWebsite:
    
    def test_enter_username(self):
        self.driver.find_element(By.ID, "fromcity").send_keys("Mumbai")
        self.driver.find_element(By.ID, "destcity").send_keys("Pune")

    def test_enter_dates(self):
        self.driver.find_element(By.NAME, "departdate").send_keys("10/10/2023")
        self.driver.find_element(By.NAME, "returndate").send_keys("15/10/2023")

    def test_get_heading(self):
        heading = self.driver.find_element(By.CLASS_NAME, "entry-title").text
        print("Heading of the page is:", heading)

