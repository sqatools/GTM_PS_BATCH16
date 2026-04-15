# Istall selenium with given command
# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def launch_website_and_verify():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/")
    driver.find_element(By.ID, "form_first_name_7").send_keys("Ramesh")
    driver.find_element(By.ID, "form_email_7").send_keys("ramesh@123.com")

    time.sleep(10)
    driver.close()

launch_website_and_verify()