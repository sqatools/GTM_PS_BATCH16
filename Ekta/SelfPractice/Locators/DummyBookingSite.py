from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select



driver=webdriver.Chrome()
driver.get("https://sqatools.in/dummy-booking-website/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@value='radio_558']").click()
driver.find_element(By.ID,"firstname").send_keys("Ekta")
driver.find_element(By.ID,"birthday").send_keys("01-04-1994")
driver.find_element(By.ID,"female").click()
time.sleep(3)
#dropdown_element = 

# Pass it to the Select class wrapper
dropdown = Select(driver.find_element(By.ID, "admorepass"))
dropdown.select_by_visible_text("Add 2 more passenger (200%)")
#select by index
#select by value

time.sleep(5)
