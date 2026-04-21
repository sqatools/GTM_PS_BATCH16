from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_enter_username(get_driver):
    driver = get_driver
    driver.find_element(By.ID, "fromcity").send_keys("Mumbai")
    driver.find_element(By.ID, "destcity").send_keys("Pune")

def test_enter_dates(get_driver):
    driver = get_driver
    driver.find_element(By.NAME, "departdate").send_keys("10/10/2023")
    driver.find_element(By.NAME, "returndate").send_keys("15/10/2023")

def test_get_heading(get_driver):
    driver = get_driver
    heading = driver.find_element(By.CLASS_NAME, "entry-title").text
    print("Heading of the page is:", heading)

