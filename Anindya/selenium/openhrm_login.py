import selenium

from selenium import webdriver

from selenium.webdriver.common.by import By

import time

driver = None

def load_url():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(10)
    print(driver.title)
    assert driver.title == "OrangeHRM", f'The title is "OrangeHRM" but we got {driver.title}'


def login():
    driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
    f = driver.find_element(By.XPATH,"//h6[text()='Dashboard']").text
    print(f)

    assert f == "Dashboard", f'not working'

    driver.find_element(By.XPATH,"//span[text()='Admin']/parent::a").click()

    assert driver.find_element(By.XPATH, "//h6[text()='User Management']").is_displayed()
    print("User Management displayed successfully")
    
    b = driver.find_element(By.XPATH,"//button[normalize-space()='Add']")

    if b.is_enabled():
        b.click()
        assert driver.find_element(By.XPATH,"//h6[text()='Add User']").text == "Add User"
        print("yes working fine")


    driver.find_element(By.XPATH,"//label[text()='User Role']/ancestor::div[@class='oxd-input-group oxd-input-field-bottom-space']//div[text()='-- Select --']").click()  
    driver.find_element(By.XPATH,"//div[@role='option']/span[text()='ESS']").click()

    time.sleep(10)

    

load_url()
login()