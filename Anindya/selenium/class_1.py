from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def func():
    driver = webdriver.Chrome()
    driver.get("https://sqatools.in/dummy-booking-website/")

    driver.maximize_window()

    driver.find_element(By.ID,"fromcity").send_keys("bangalore")
    driver.find_element(By.ID,"destcity").send_keys("Mumbai")
    time.sleep(3)

    driver.close()

func()
    