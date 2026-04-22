from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://sqatools.in/dummy-booking-website/")
driver.maximize_window()


def test_enter_username():
    driver.find_element(By.ID, "fromcity").send_keys("Assam")
    driver.find_element(By.ID, "destcity").send_keys("Guwahati")

def test_enter_dates():
    driver.find_element(By.NAME, "departdate").send_keys("01/01/2026")
    driver.find_element(By.NAME, "returndate").send_keys("03/01/2026")
    
def test_get_heading():
    heading = driver.find_element(By.CLASS_NAME, "entry-title").text
    print("Heading of the page is :", heading)