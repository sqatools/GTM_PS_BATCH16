from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def get_element(self, locator):
        return self.wait.until(ec.presence_of_element_located(locator))
    
    def click_element(self, locator):
        element = self.get_element(locator)
        element.click()

    def enter_text(self, locator, value):
        element = self.get_element(locator)
        element.send_keys(value)


    def get_element_text(self, locator):
        element = self.get_element(locator)
        return element.text


