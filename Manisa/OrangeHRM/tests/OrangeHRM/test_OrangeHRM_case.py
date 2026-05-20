from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.mark.usefixtures("get_driver_class")
class TestOrangeHRM:
    def test_enter_username_password(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(10)

    def test_get_heading(self):
        heading = self.driver.find_element(By.CLASS_NAME, "orangehrm-login-form").text
        print("Heading of the page is:", heading)

    def test_login(self):
        login_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
        if login_button.is_displayed():
            print("login button is enabled")
        else:
            print("login button is not enabled")

'''def test_get_heading(get_driver):
    driver = get_driver
    heading = driver.find_element(By.CLASS_NAME, "entry-title").text
    print("Heading of the page is:", heading)'''
    
