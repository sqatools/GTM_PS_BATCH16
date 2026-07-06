
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()

driver.get("https://sqatools.in/automation-practice-page/")
driver.maximize_window()

print("Title of page is ",driver.title)
print("Current URL is ",driver.current_url)
#driver.title()
driver.find_element(By.ID,"username").send_keys("Ekta")
driver.find_element(By.ID,"password").send_keys("123")
driver.find_element(By.ID,"address").send_keys("Pune, Maharashtra ,India-416502")
driver.find_element(By.ID,"female").click()
var=(driver.find_element(By.ID,"selenium"))
var.click()
assert var.is_selected()==True
#driver.find_element(By.ID,"Python").click()
driver.find_element(By.ID,"skills").click()

dd_demo=driver.find_element(By.ID,"skills")
dd_multi=Select(dd_demo)
dd_multi.select_by_index(1)
dd_multi.select_by_value
dd_multi.select_by_visible_text("API Testing")

dd_multi.select_by_index(0)
dd_multi.select_by_visible_text("Playwright")

time.sleep(8)
