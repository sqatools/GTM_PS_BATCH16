import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select



class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.log = logging.getLogger(__name__)

    def get_element(self, locator):
        self.log.info(f"getting element with locator : {locator}")
        return self.wait.until(ec.presence_of_element_located(locator))
    
    def click_element(self, locator):
        self.log.info(f"clicking on element with locator : {locator}")
        element = self.get_element(locator)
        element.click()

    def enter_text(self, locator, value):
        self.log.info(f"entering text:{value} in the locator : {locator}")
        element = self.get_element(locator)
        element.send_keys(value)


    def get_element_text(self, locator):
        element = self.get_element(locator)
        return element.text
    

    def get_current_url(self):
        return self.driver.current_url
    

    def get_website_title(self):
        return self.driver.title
    

    def get_elements_list(self, locator):
        return self.wait.until(ec.presence_of_all_elements_located(locator))
    

    def check_element_is_selected(self, locator):
        element = self.get_element(locator)
        return element.is_selected()
    
    def check_element_is_enabled(self, locator):
        element = self.get_element(locator)
        return element.is_enabled()
    
    def check_element_is_displayed(self, locator):
        element = self.get_element(locator)
        return element.is_displayed()
    

    def get_attribute_value(self, locator, attribute):
        element = self.get_element(locator)
        return element.get_attribute(attribute)
    

    def select_dropdown_value(self, locator, value):
        element = self.get_element(locator)
        select_obj = Select(element)
        select_obj.select_by_visible_text(value)


    def refresh_page(self):
        self.driver.refresh()


    def move_forward(self):
        self.driver.forward()


    def move_backword(self):
        self.driver.back()

    

    



