import selenium

from selenium import webdriver

from selenium.webdriver.common.by import By

import time
# import pytest



def test_1(func):
    driver = func
    driver.find_element(By.XPATH,"//input[@name='fromcity']").send_keys("Anindya")
    time.sleep(5)

def test_2(func):
    driver = func

    driver.find_element(By.XPATH,"//input[@name='destcity']").send_keys("QWFGH")
    time.sleep(5)

def test_3(func):
    
    driver = func
    print(driver.current_url)


