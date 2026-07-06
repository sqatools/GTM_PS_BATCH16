import selenium
import time
from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://sqatools.in/dummy-booking-website/")

driver.maximize_window()

driver.implicitly_wait(5)

def test_1():
    driver.find_element(By.XPATH,"//input[@name='fromcity']").send_keys("Anindya")
    time.sleep(4)

def test2():

    driver.find_element(By.XPATH,"//input[@name='destcity']").send_keys("Abhi")

    time.sleep(4)