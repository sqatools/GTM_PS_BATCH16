from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=None
def launch_website_and_verify():
    global driver
    driver=webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(10)
    assert driver.current_url=="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

def xpath_locators():
    driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH,"//input[@type='password']").send_keys("admin123")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    #driver.find_element(By.XPATH,"//p[text()='Apply Leave']").click()
    driver.find_element(By.XPATH,"")
    time.sleep(10)


launch_website_and_verify()
xpath_locators()