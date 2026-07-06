from DummyWebsite.base.base import SeleniumBase
from .locators import DummyLocators
import time
from selenium.webdriver.common.by import By


class DummyPage(SeleniumBase):
    def __init__(self, driver):
      super().__init__(driver)
  

    def verify_login_successful(self, expected_url, time_out=10):
        actual_url = self.get_current_url()
        if actual_url == expected_url:
            self.log.info("Login successful, URL matched")
            return True
        else:
            self.log.error(f"Login failed, expected URL: {expected_url}, but got: {actual_url}")
            return False

    def enter_source_and_destination(self, fromcity, destcity):
       self.enter_text(DummyLocators.fromCityField, fromcity)
       self.enter_text(DummyLocators.DestCityField, destcity)

    def enter_dates(self, departdate, returndate):
        self.enter_text(DummyLocators.departDate, departdate)
        self.enter_text(DummyLocators.returnDate, returndate)

    def select_gender(self, gender):
        if gender.lower() == "male":
          self.click_element(DummyLocators.male_radio_btn)
        elif gender.lower() == "female":
          self.click_element(DummyLocators.female_radio_btn)


    def select_number_of_passengers(self, value):
      self.select_dropdown_value(DummyLocators.passenger_dropdown, value)


    def select_country(self, country_name):
       self.select_dropdown_value(DummyLocators.contry_dropdown, country_name)
           