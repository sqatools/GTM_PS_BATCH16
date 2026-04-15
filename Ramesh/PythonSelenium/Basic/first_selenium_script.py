# Istall selenium with given command
# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def launch_website_and_verify():
    driver = webdriver.Chrome()
    driver.get("https://sqatools.in/dummy-booking-website/")
    driver.find_element(By.ID, "fromcity").send_keys("Assam")
    driver.find_element(By.ID, "destcity").send_keys("Guwahati")

    time.sleep(10)
    driver.close()

launch_website_and_verify()