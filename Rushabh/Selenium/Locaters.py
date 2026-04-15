import selenium 
from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

driver = None
url = "https://sqatools.in/dummy-booking-website/"
def launch_website_and_verify():
    global driver
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)

def selenium_locators():
    # By name
    driver.find_element(By.XPATH,//input[@id='firstname']).send_keys("Viaan")
    
    driver.find_element(By.XPATH,(//input[@id='firstname'])[2]).send_keys("Kumar")
    time.sleep(10)

launch_website_and_verify()
selenium_locators()