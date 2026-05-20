#date -14th april

from email.mime import text
from os import link

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = None

def launch_website_and_verify():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://sqatools.in/dummy-booking-website/")
    driver.maximize_window()
    driver.implicitly_wait(15)
    
     # verify the correct page is loaded.
    assert driver.current_url == "https://sqatools.in/dummy-booking-website/"

#selenium locators - 7 locators

"""
ID: ByType = "id"
XPATH: ByType = "xpath"
LINK_TEXT: ByType = "link text"
PARTIAL_LINK_TEXT: ByType = "partial link text"
NAME: ByType = "name"
TAG_NAME: ByType = "tag name"
CLASS_NAME: ByType = "class name"
CSS_SELECTOR: ByType = "css selector"
"""

   
def selenium_locators():
    # ID locator
    driver.find_element(By.ID, "fromcity").send_keys("Mumbai")
    driver.find_element(By.ID, "destcity").send_keys("Pune")

    # Name locator
    driver.find_element(By.NAME, "departdate").send_keys("10/10/2023")
    driver.find_element(By.NAME, "returndate").send_keys("15/10/2023")

    # Class Name locator
    heading = driver.find_element(By.CLASS_NAME, "entry-title").text
    print("Heading of the page is:", heading)
    time.sleep(5)

    # link text locator
    driver.find_element(By.LINK_TEXT, "Home").click()
    time.sleep(5)

    # partial link text locator
    driver.find_element(By.PARTIAL_LINK_TEXT, "Basic Programs").click()
    time.sleep(10)

launch_website_and_verify()
#selenium_locators()

# selenium methods to find multiple elements:
def selenium_get_elements():
    # get list of elements using find_elements method
    username_fields = driver.find_elements(By.ID, "firstname")
    username_fields[0].send_keys("manisa")
    username_fields[1].send_keys("sarangi")
    time.sleep(5)

    #dob_fields = driver.find_elements(By.ID, "Date of Birth")
    dob_field = driver.find_element(By.XPATH, "//span[contains(text(), 'Date of birth')]/following::input[1]")
    dob_field.send_keys("01/01/1990")
    time.sleep(5)
    
    #sex_fields = driver.find_elements(By.ID, "female") - radio button
    sex = driver.find_element(By.ID, 'female')
    sex.click()
    # Click the text "male" using xpath
    #driver.find_element(By.XPATH, "//span[text()='male']").click()//wrong xpath

    #traveldetails - radio button one way / two way
    traveldetails = driver.find_element(By.ID, "oneway").click()

    element=driver.find_element(By.XPATH,"//td[text()='Hyderabad']")
    print("element highlighted ",element.text)
    

    time.sleep(5)

    #get all the links on the page
    #list_of_links = driver.find_elements(By.TAG_NAME, "a")
    #print("Total number of links on the page:", len(list_of_links))
    #for link in list_of_links:
    #    print(link.text)
    #    #print("Link Text:", link.text, " - URL:", link.get_attribute("href"))

selenium_get_elements()



