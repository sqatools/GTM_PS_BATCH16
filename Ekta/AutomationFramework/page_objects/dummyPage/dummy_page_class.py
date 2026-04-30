from base.selenium_base import SeleniumBase
from .dummy_page_locator import DummyLocators

class DummyPage(SeleniumBase): # WE NEED TO INHERIT THE SELENIUM BASE CLASS TO ACCESS ALL THE METHODS OF SELENIUM BASE
    def __init__(self, driver): #parent and child class constructor
      super().__init__(driver)
      self.dl = DummyLocators()

    def enter_source_and_destination(self, fromcity, destcity):
       self.enter_text(self.dl.fromCityField, fromcity)
       self.enter_text(self.dl.DestCityField, destcity)

    def enter_depart_and_return_dates(self, departdate, returndate):
        self.enter_text(self.dl.DepartDate, departdate)
        self.enter_text(self.dl.ReturnDate, returndate)

    def get_page_heading(self):
        return self.get_element_text(self.dl.PageHeading)

    def select_male_radio_btn(self):
        self.click_element(self.dl.male_radio_btn)          

    def select_passenger_count(self, count):
        self.select_dropdown_value(self.dl.passenger_dropdown, count)       
    
    def select_country(self, country_name):
        self.select_dropdown_value(self.dl.contry_dropdown, country_name)   

    
