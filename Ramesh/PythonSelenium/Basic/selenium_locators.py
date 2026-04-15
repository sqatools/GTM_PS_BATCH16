from selenium import webdriver
from selenium.webdriver.common.by import By

# global variable to hold the driver isinstance
driver = None


def launch_website_and_verify():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://sqatools.in/dummy-booking-website/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    # verify the correct page is loaded.

    assert driver.current_url == "https://sqatools.in/dummy-booking-website/"


def selenium_locators():
    # ID locator
    driver.find_element(By.ID, "form_first_name_7").send_keys("Ramesh")
    driver.find_element(By.ID, "form_email_7").send_keys("ramesh@123.com")

    # Name locator
