import selenium

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.select import Select

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

    def element_enter_text(self,locator,value):
        element = self.get_element(locator)
        element.send_keys(value)

    def drop_down_selection(self,locator,value):
        element = self.get_element(locator)
        select =  Select(element)
        select.select_by_value(value)
                   
