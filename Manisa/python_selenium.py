#install selennium with given command
#pip install selenium

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def launch_website_and_verify():
    driver = webdriver.Chrome()
    driver.get("https://sqatools.in/dummy-booking-website")
    driver.find_element(By.ID, "fromcity").send_keys("Mumbai")
    driver.find_element(By.ID, "destcity").send_keys("Pune")
    time.sleep(15)
    driver.close()

launch_website_and_verify()

