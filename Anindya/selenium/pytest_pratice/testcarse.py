import selenium
import time
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://sqatools.in/dummy-booking-website/")

driver.maximize_window()

# driver.implicitly_wait(5)

def test_1():

    wait = WebDriverWait(driver,20,poll_frequency=1)
    wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='fromcituy']"))).send_keys("Anindya")
    # driver.find_element(By.XPATH,"//input[@name='fromcity']").send_keys("Anindya")
    time.sleep(4)

def test2():

    driver.find_element(By.XPATH,"//input[@name='destcity']").send_keys("Abhi")

    time.sleep(4)


test_1()