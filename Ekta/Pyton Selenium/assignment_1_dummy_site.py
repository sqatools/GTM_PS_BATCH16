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
    assert driver.current_url=="https://sqatools.in/dummy-booking-website/"

def selenium_locators():
    driver.find_element(By.XPATH,"(//input[@id='firstname'])[1]").send_keys("Ekta")
    driver.find_element(By.XPATH,"(//input[@id='firstname'])[2]").send_keys("Gund")
    time.sleep(30)

launch_website_and_verify()
selenium_locators()