from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=None
def launch_website_and_verify():
    global driver
    driver=webdriver.Chrome()
    driver.get("https://sqatools.in/dummy-booking-website/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    

def xpath_locators():
    element=driver.find_element(By.XPATH,"//td[text()='Kolkata']")
    print("Element is ",element.text)
   
    time.sleep(10)


launch_website_and_verify()
xpath_locators()