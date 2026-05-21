from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()

driver.get("https://sqatools.in/automation-practice-page/")
driver.maximize_window()

drop_down_element=driver.find_element(By.ID,"skills") #location dropdown element 
select=Select(drop_down_element) #Wrap it in the Selenium Select class
print("Check if user able to select multiple options from drop-down-->",select.is_multiple)
#select by visible text 
time.sleep(2)
select.select_by_visible_text("API Testing")
#select by index
select.select_by_index(0)

select.select_by_visible_text("Playwright")

time.sleep(5)

#select.deselect_by_index(0)
select.deselect_all()
time.sleep(3)
#select by value --> show this site for example https://the-internet.herokuapp.com/dropdown




