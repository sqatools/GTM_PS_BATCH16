from selenium.webdriver.common.by import By

class Locators:
    username = (By.NAME, "username")
    password = (By.NAME, "password")

    login = (By.XPATH, "//button[normalize-space()='Login']")
    
    PageHeading = (By.CLASS_NAME, "orangehrm")

