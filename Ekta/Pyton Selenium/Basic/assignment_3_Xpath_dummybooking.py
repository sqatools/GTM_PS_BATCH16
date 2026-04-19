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
    #text method 
    element=driver.find_element(By.XPATH,"//td[text()='Kolkata']")
    print("Element is ",element.text)
    element=driver.find_element(By.XPATH,"//td[text()='5000']")
    print("Element is ",element.text)
    #partial text value
    element=driver.find_element(By.XPATH,"//td[contains(text(),'Kolk')]")
    print("Element is ",element.text)
    element=driver.find_element(By.XPATH,"//td[contains(text(),'500')]")
    print("Element is ",element.text)
    #xpath ancestor method
    element=driver.find_element(By.XPATH,"//input[@value='radio_123']/ancestor::li")
    print("Element is ",element.text)
    #text method
    driver.find_element(By.XPATH,"//a[text()='Courses']").click()
    time.sleep(5)
    
    driver.find_element(By.XPATH,"//img[@title='Courses 3']").click()


   
    time.sleep(10)


launch_website_and_verify()
xpath_locators()