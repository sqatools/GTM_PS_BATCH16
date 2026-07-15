import selenium
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec

import time

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
            
    
   


