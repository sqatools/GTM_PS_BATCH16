import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .Seleniumbase import seleniumbase
import pytest
from .locators import DummyLocators

@pytest.mark.usefixtures("get_driver_class")
class TestDummyWebsite:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.sb=seleniumbase(self.driver)
        self.dl=DummyLocators()
        print("Test setup initiated")

    def test_enter_username(self):
       # self.driver.find_element(By.ID, "fromcity").send_keys("Gadhinglaj")
       #self.driver.find_element(By.ID, "destcity").send_keys("Kohapur")
       self.sb.enter_text(self.dl.fromCityField,"Gadhinglaj")
       self.sb.enter_text(self.dl.DestCityField,"Kolhapur")

    def test_enter_dates(self):
        #self.driver.find_element(By.NAME, "departdate").send_keys("01/05/2026")
        #self.driver.find_element(By.NAME, "returndate").send_keys("01/06/2026")

        self.sb.enter_text(self.dl.DepartDate,"01/05/2026")
        self.sb.enter_text(self.dl.ReturnDate,"01/06/2026")




    def test_get_heading(self):
        #heading = self.driver.find_element(By.CLASS_NAME, "entry-title").text
        #print("Heading of the page is:", heading)
        heading_text=self.sb.get_element_text(self.dl.PageHeading)
        print("Heading of the page is:", heading_text)