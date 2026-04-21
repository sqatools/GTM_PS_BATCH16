from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# global variable to hold the driver instance
driver = None 

def launch_website_and_verify(url):
    global driver
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    # verify the correct page is loaded.
    print("Current URL:", driver.current_url)
    assert driver.current_url == url, f"Expected URL: {url}, but got: {driver.current_url}"


def xpath_locators(url):
    launch_website_and_verify(url=url)
    # XPATH locator
    driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    dashboard_heading = driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
    print("Heading of the page is:", dashboard_heading)
    assert dashboard_heading == "Dashboard", f"Expected heading: Dashboard, but got: {dashboard_heading}"
    time.sleep(5)

    # navigate to admin page
    driver.find_element(By.XPATH, "//span[text()='Admin']/parent::a").click()
    assert driver.find_element(By.XPATH, "//h6[text()='User Management']").is_displayed()
    print("Admin page is displayed successfully!")
    
    add_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Add']")
    if add_btn.is_enabled():
        add_btn.click()
        assert driver.find_element(By.XPATH, "//h6[text()='Add User']").is_displayed()
        print("Add User form is displayed successfully!")

    driver.find_element(By.XPATH, "//label[text()='User Role']//ancestor::div[contains(@class,'oxd-input-field')]//div[text()='-- Select --']").click()
    driver.find_element(By.XPATH, "//div[@role='option']//span[text()='Admin']").click()
    time.sleep(5)


    

'''def xpath_locators_rpa(url):
    launch_website_and_verify(url=url)
    # XPATH locator
    driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelCompanyName']").send_keys("Admin")
    driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelFirstName']").send_keys("Rahul")
    driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelPhone']").send_keys("1234567890")
    time.sleep(5)'''
    

url2 = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login" 
xpath_locators(url=url2)