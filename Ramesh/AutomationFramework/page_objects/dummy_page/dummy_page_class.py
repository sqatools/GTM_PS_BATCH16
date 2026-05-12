from base.selenium_base import SeleniumBase
from .dummy_page_locator import DummyLocators

class DummyPage(SeleniumBase):
    def __init__(self, driver):
      super().__init__(driver)
      self.dl = DummyLocators()

    def enter_source_and_destination(self, fromcity, destcity):
       self.log.info("Execute Method : enter_source_and_destination")
       self.enter_text(self.dl.fromCityField, fromcity)
       self.enter_text(self.dl.DestCityField, destcity)

    def select_gender(self, gender):
        if gender.lower() == "male":
          self.click_element(self.dl.male_radio_btn)
        elif gender.lower() == "female":
          self.click_element(self.dl.female_radio_btn)


    def select_number_of_passengers(self, value):
      self.select_dropdown_value(self.dl.passenger_dropdown, value)


    def select_country(self, country_name):
       self.select_dropdown_value(self.dl.contry_dropdown, country_name)
           


    