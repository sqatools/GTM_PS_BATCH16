from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = None #global variable
url = "https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp"

def launch_website_and_verify_hiddenelement(url):
    global driver
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)

    elem = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
    print(elem)
    time.sleep(5)

    driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()
    time.sleep(2)
    elem = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
    print(elem)
    time.sleep(5)



launch_website_and_verify_hiddenelement(url=url)