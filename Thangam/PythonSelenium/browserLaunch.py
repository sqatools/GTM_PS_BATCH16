from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def launch_website_and_verify():
    driver = webdriver.Chrome()
    driver.get("https://sqatools.in/dummy-booking-website/")
    driver.find_element(By.ID, "firstname").send_keys("Thangam")
    driver.find_element(By.ID, "destcity").send_keys("Fremont")
    #driver.find_element(By.ID,"")
    time.sleep(5)
    driver.close()

launch_website_and_verify()
