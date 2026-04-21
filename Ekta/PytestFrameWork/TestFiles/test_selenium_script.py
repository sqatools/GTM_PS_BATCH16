from selenium import webdriver
from selenium.webdriver.common.by import By
#below three lines of code is friction part. i.e prerequisites.
driver=webdriver.Chrome()
driver.get("https://sqatools.in/dummy-booking-website/")
driver.maximize_window()

def test_enter_username():
    driver.find_element(By.ID, "fromcity").send_keys("Mumbai")
    driver.find_element(By.ID, "destcity").send_keys("Pune")

def test_enter_dates():
    driver.find_element(By.NAME, "departdate").send_keys("10/10/2023")
    driver.find_element(By.NAME, "returndate").send_keys("15/10/2023")


def test_get_heading():
    heading = driver.find_element(By.CLASS_NAME, "entry-title").text
    print("Heading of the page is:", heading)