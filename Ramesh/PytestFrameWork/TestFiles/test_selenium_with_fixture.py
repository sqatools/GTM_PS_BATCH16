from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_enter_username(get_driver):
    driver = get_driver
    driver.find_element(By.ID, "fromcity").send_keys("Assam")
    driver.find_element(By.ID, "destcity").send_keys("Guwahati")


def test_enter_dates(get_driver):
    driver = get_driver
    driver.find_element(By.NAME, "departdate").send_keys("01/01/2026")
    driver.find_element(By.NAME, "returndate").send_keys("03/01/2026")


def test_get_heading(get_driver):
    driver = get_driver
    heading = driver.find_element(By.CLASS_NAME, "entry-title").text
    print("Heading of the page is :", heading)