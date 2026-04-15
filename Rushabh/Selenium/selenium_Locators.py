import selenium
from selenium import webdriver  
from selenium.webdriver.common.by import By
import time     

driver = None
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
def launch_website_and_verify():
    global driver
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)

    print("Current URL:",driver.current_url)
    assert driver.current_url == url , f"Expected URL:{url},but got: {driver.current_url}"

launch_website_and_verify()   

def selenium_locators():
    # By name
    driver.find_element(By.NAME, "username").send_keys("Admin")
   
    driver.find_element(By.NAME,"password").send_keys("admin123")

    #By Xpath normalize space method
    driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
    time.sleep(10)

selenium_locators()