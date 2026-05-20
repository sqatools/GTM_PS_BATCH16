# Install selenium with given command
# pip install selenium

from selenium import webdriver #imports the main webdriver module from the Selenium library
from selenium.webdriver.common.by import By #tell Python how to find specific elements on a webpage
from selenium.webdriver.common.keys import Keys
import time

def launch_website_and_verify():
    driver = webdriver.Chrome() #direct Selenium to start up an instance of the Google Chrome browser.
    driver.get("https://sqatools.in/dummy-booking-website/")
    driver.find_element(By.ID, "fromcity").send_keys("mumbai")
    time.sleep(2)
    from_city_input = driver.find_element(By.ID, "fromcity")
    var = from_city_input.get_attribute("value")
    print(var)
    #print(from_city_input.text)
    from_city_input.clear()
    
    driver.find_element(By.ID, "fromcity").send_keys("kolkata")
    driver.find_element(By.ID, "destcity").send_keys("mumbai")
    time.sleep(10)
    driver.close


launch_website_and_verify()