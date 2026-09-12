import selenium

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import time

import pytest


class SeleniumBase:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)

    def get_element(self,locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self,locator):
        element = self.get_element(locator)
        element.click()
            
