from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=None

def launch_website_and_verify():
    global driver
    driver=webdriver.Chrome()
    driver.get("https://sqatools.in/dummy-booking-website/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    assert driver.current_url=="https://sqatools.in/dummy-booking-website/" #verify correct page is loaded
   
   #selenium locators-->
def selenium_locators():
  #id locator 
   driver.find_elements(By.ID,"firstname")[0].send_keys("Ekta")
   driver.find_elements(By.ID,"firstname")[1].send_keys("Gund")
   driver.find_element(By.ID,"fromcity").send_keys("Mumbai")
   driver.find_element(By.ID, "destcity").send_keys("Pune")
   #Name locator
   driver.find_element(By.NAME,"departdate").send_keys("15-04-2026")
   driver.find_element(By.NAME,"returndate").send_keys("20-04-2026")
   #class name locator
   heading=driver.find_element(By.CLASS_NAME,"entry-title").text
   print("heading is ",heading)
   time.sleep(30)
   
   

#link text locator
   driver.find_element(By.LINK_TEXT,"Home").click()
#partial link text locator
   driver.find_element(By.PARTIAL_LINK_TEXT,"String Programs").click()
#get all links on page
   links = driver.find_elements(By.TAG_NAME,"a")
   for link in links:
    print("Link text: ",link.text, "URL : ",link.get_attribute("href"))
    print("total links are ",len(links))
  
  

launch_website_and_verify()
selenium_locators()


   

