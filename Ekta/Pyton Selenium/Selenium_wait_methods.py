# Install selenium with given command
# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def launch_website_with_implicit_wait_and_verify():
    driver = webdriver.Chrome()
    driver.get("https://sqatools.in/dummy-booking-website/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "fromcity").send_keys("Kolhapur")
    driver.find_element(By.ID, "destcity").send_keys("Mumbai")
    time.sleep(5)
   
#launch_website_with_implicit_wait_and_verify()

def launch_website_with_explicit_wait_and_verify():
    driver = webdriver.Chrome()
    wait=WebDriverWait(driver,20,poll_frequency=1)
    driver.get("https://sqatools.in/dummy-booking-website/")
    driver.maximize_window()
    wait.until(ec.presence_of_element_located((By.ID,"fromcity"))).send_keys("Kolhapur")
    wait.until(ec.presence_of_element_located((By.ID,"destcity"))).send_keys("Mumbai")
    #driver.find_element(By.ID, "fromcity").send_keys("Kolhapur")
    #driver.find_element(By.ID, "destcity").send_keys("Mumbai")
   # time.sleep(5)
    driver.close()

launch_website_with_explicit_wait_and_verify()