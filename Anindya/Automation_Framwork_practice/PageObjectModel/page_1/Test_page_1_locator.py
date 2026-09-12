import selenium

from selenium import webdriver

from selenium.webdriver.common.by import By

class Element_Locator:
    user_name = (By.XPATH,"//input[@name='username']")
    password = (By.XPATH,"//input[@name='password']")
    address = (By.XPATH,"//textarea[@name='address']")
    gender = (By.XPATH,"//input[@value='male']")
    check_box = (By.XPATH,"//input[@value='Python']")
    country_name = (By.XPATH,"//select[@id = 'country']")
    

