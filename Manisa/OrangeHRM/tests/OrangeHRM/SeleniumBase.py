from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        print("SeleniumBase initialized with driver:", driver)

    def get_element(self, locator):
        print(f"Locating element with locator: {locator}")
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
    

    def get_current_url(self):
        return self.driver.current_url

    def get_elements_list(self, locator):
        return self.wait.until(ec.presence_of_all_elements_located(locator))
    
    def get_website_title(self):
        return self.driver.title
    
    def check_element_is_enabled(self, locator):
        element = self.get_element(locator)
        return element.is_enabled()
