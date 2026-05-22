import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("https://sqatools.in/automation-practice-page/")
driver.maximize_window()

# 1. Get the absolute path first
absolute_path = os.path.abspath("sample.text")
print("Absolute path is :", absolute_path)

# 2. Direct Selenium to the file input element
file_input = driver.find_element(By.ID, "fileUpload")

# 3. DO NOT CLICK. Just send the path directly to the element.
file_input.send_keys(absolute_path)
time.sleep(5)
driver.quit()