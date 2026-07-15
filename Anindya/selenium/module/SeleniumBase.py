import selenium
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec

import time

from selenium.webdriver.support.select import Select
import pytest


class SeleniumBase:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)

    def get_element(self,locator):
        return self.wait.until(ec.presence_of_element_located(locator))
    
    def element_click(self,locator):
        element = self.get_element(locator)
        element.click()

    def element_enter_text(self,locator,value):
        element = self.get_element(locator)
        element.send_keys(value)

    def read_text(self,locator):
        element = self.get_element(locator)
        return element.text

    def get_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def element_enabled(self,locator):
        element = self.get_element(locator)
        return element.is_enabled()

    def element_displayed(self,locator):
        element = self.get_element(locator)
        return element.is_displayed()

    def element_selected(self,locator):
        element = self.get_element(locator) 
        return element.is_selected()
    
    def element_dropdown(self,locator,value):
        element = self.get_element(locator)
        element_obj = Select(element)
        element_obj.select_by_visible_text(value)

    def page_forward(self):
        return self.driver.forward()

    def page_refresh(self):
        return self.driver.refresh()

    def page_back(self):
        return self.driver.back()

    def get_element_list(self,locator):
        return self.wait.until(ec.presence_of_all_elements_located(locator))
    


       
    
   


