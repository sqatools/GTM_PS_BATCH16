from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



class seleniumbase:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,15)

    def get_element(self,locator):
        return self.wait.until(ec.presence_of_element_located(locator))


    def click_element(self,locator):
        self.get_element(locator).click()

    def enter_text(self,locator,value):
        self.get_element(locator).send_keys(value)

    def get_element_text(self,locator):
        return self.get_element(locator).text   