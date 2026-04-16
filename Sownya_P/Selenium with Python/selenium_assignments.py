#1. Automate dummy website except dropdown elements.
#https://sqatools.in/dummy-booking-website/
from selenium import webdriver
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome()
driver.get("https://sqatools.in/dummy-booking-website/")
driver.find_element(By.ID, "first_name").send_keys("Sownya")
driver.find_element(By.ID, "last_name").send_keys("P")
driver.find_element(By.ID, "email").send_keys("psownyasree@gmail.com")
driver.find_element(By.ID, "phone").send_keys("7893279076")
driver.find_element(By.ID, "address").send_keys("Hyderabad")
driver.find_element(By.ID, "city").send_keys("Hyderabad")   
driver.find_element(By.ID, "state").send_keys("Telangana")
driver.find_element(By.ID, "zip").send_keys("500032")
driver.find_element(By.ID, "submit").click()




#Take atleast one example of each XPath and use it selenium script from XPATH guide.

# Example 1: Absolute XPath
driver.get("https://www.google.com")
search_box = driver.find_element(By.XPATH, "/html/body/div[1]/div[3
]/form/div[1]/div[1]/div[1]/div/div[2]/input")
search_box.send_keys("Selenium with Python")        

# Example 2: Relative XPath
search_box = driver.find_element(By.XPATH, "//input[@name='q']")
search_box.send_keys("Selenium with Python")
    