from base.selenium_base import SeleniumBase
from .dummy_page_locator import DummyLocators

class DummyPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.dl = DummyLocators()
    
    def enter_source_anddestination(self, fromcity, destcity):
        self.enter_text(self.dl.fromCityField, fromcity)
        self.enter_text(self.dl.DestCityField, destcity)