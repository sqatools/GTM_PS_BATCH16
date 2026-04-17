import selenium 
from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

driver = None
url = "https://sqatools.in/dummy-booking-website/"
def launch_website_and_verify():
    global driver
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)

def selenium_locators():
    # By name
    driver.find_element(By.XPATH,"(//input[@id='firstname'])[1]").send_keys("Viaan")
    
    driver.find_element(By.XPATH,"(//input[@id='firstname'])[2]").send_keys("Dahake")
    time.sleep(10)

    driver.find_element(By.ID,"fromcity").send_keys("Mumbai")
    driver.find_element(By.ID, "destcity").send_keys("Pune")
    time.sleep(10)

    driver.find_element(By.NAME,"departdate").send_keys("15-04-2026")
    driver.find_element(By.NAME,"returndate").send_keys("20-04-2026")
    time.sleep(10)              

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