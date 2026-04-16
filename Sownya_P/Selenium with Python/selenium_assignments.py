#1. Automate dummy website except dropdown elements.
#https://sqatools.in/dummy-booking-website/
from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

global driver
driver = None
url = "https://sqatools.in/dummy-booking-website/"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(10)
driver.find_element(By.ID, "firstname").send_keys("sownya")
driver.find_element(By.ID, "birthday").send_keys("29/03/1995")
time.sleep(20)
driver.close()



#Practice program 2:
#https://sqatools.in/automation-practice-page/


import time
from selenium import webdriver
from selenium.webdriver.common.by import By 
# Initialize the Chrome driver
driver=webdriver.Chrome()
# Set implicit wait time
driver.implicitly_wait(5)
# Maximize the browser window
driver.maximize_window()
# Navigate to the URL
driver.get("https://sqatools.in/automation-practice-page/")
driver.find_element(By.ID, "username").send_keys("sownya")
driver.find_element(By.ID, "password").send_keys("Test")   
Address= driver.find_element(By.NAME, "address")
Address.clear()
Address.send_keys("Hyderabad")
time.sleep(2)
Radio_option= driver.find_element(By.NAME , "gender")
Radio_option.click()
Checkbox= driver.find_element(By.ID, "selenium")
Checkbox.click()
Choosecountry= driver.find_element(By.NAME, "country")
Choosecountry.click()
Choosecountry.send_keys("UK")
Mult_Select= driver.find_element(By.ID, "skills")
Mult_Select.click()
Mult_Select.send_keys("Selenium") 
Mult_Select.send_keys("API Testing")

driver.close()
#3. Take atleast one example of each XPath and use it selenium script from XPATH guide.

import time 
from selenium import webdriver
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(10)

username_field = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
username_field.send_keys("Admin")
password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
password_field.send_keys("admin123")
login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
login_button.click()
time.sleep(5)

driver.quit()

