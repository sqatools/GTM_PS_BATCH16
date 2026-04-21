## install selenium using pip command on terminal
# pip install selenium
# Install selenium with given command
# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login_website():
    driver = webdriver.Chrome()
    driver.get("https://sqatools.in/login-page/")
    driver.find_element(By.ID, "email").send_keys("psownyasree@gmail.com")
    driver.find_element(By.ID, "pass").send_keys("Kaasi@26")
    driver.find_element(By.ID, "loginbutton").click()
    time.sleep(5)
    driver.close()

login_website()



def launch_website_and_verify():
    driver = webdriver.Chrome()
    driver.get("https://sqatools.in/dummy-booking-website/")
    driver.find_element(By.ID, "fromcity").send_keys("Mumbai")
    driver.find_element(By.ID, "destcity").send_keys("Pune")
    #time.sleep(5)
    driver.close()

launch_website_and_verify()

