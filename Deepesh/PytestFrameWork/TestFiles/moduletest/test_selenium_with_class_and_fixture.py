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
        #self.driver.find_element(By.ID, "fromcity").send_keys("Mumbai")
        self.sb.enter_text(self.dl.fromCityField, "Mumbai")
        #self.driver.find_element(By.ID, "destcity").send_keys("Pune")
        self.sb.enter_text(self.dl.DestCityField, "Pune")

    def test_enter_dates(self):
        #self.driver.find_element(By.NAME, "departdate").send_keys("10/10/2023")
        #self.driver.find_element(By.NAME, "returndate").send_keys("15/10/2023")
        self.sb.enter_text(self.dl.DepartDate, "10/10/2023")
        self.sb.enter_text(self.dl.ReturnDate, "15/10/2023")

    def test_get_heading(self):
        # heading = self.driver.find_element(By.CLASS_NAME, "entry-title").text
        heading_text = self.sb.get_element_text(self.dl.PageHeading)
        print("Heading of the page is:", heading_text)
        assert heading_text == "Dummy Booking Website"

    
    def test_select_gender_and_verify(self):
        # check element is displayed
        assert self.sb.check_element_is_displayed(self.dl.male_radio_btn), "Element is not available"
        # check element is enable to perform operation
        assert self.sb.check_element_is_enabled(self.dl.male_radio_btn), "Element is not enabled to perform operation"
        # check radio btn is not selected before click
        assert not self.sb.check_element_is_selected(self.dl.male_radio_btn)
        # select the radio button
        self.sb.click_element(self.dl.male_radio_btn)
        # check radio btn is selected after click
        assert self.sb.check_element_is_selected(self.dl.male_radio_btn)


    def test_verify_url_and_title(self):
        current_url = self.sb.get_current_url()
        print("current_url:", current_url)
        assert "dummy-booking-website" in current_url
        title = self.sb.get_website_title()
        print("title:", title)
        assert "Dummy Booking Website" in title

    def test_select_no_of_passengers(self):
        value = "Add 3 more passenger (200%)"
        self.sb.select_dropdown_value(self.dl.passenger_dropdown, value)
        count_name = "India"
        self.sb.select_dropdown_value(self.dl.contry_dropdown, count_name)