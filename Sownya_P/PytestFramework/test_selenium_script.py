import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://sqatools.in/automation-practice-page/")
driver.maximize_window()

def test_username():
    driver.find_element(By.ID, "username").send_keys("sownya")  
    driver.find_element(By.ID, "password").send_keys("Test")