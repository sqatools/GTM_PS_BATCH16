from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# global variable to hold the driver instance
driver = None 
url = "https://sqatools.in/dummy-booking-website/"

def launch_website_and_verify():
    global driver
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    # verify the correct page is loaded.
    print("Current URL:", driver.current_url)
    assert driver.current_url == url, f"Expected URL: {url}, but got: {driver.current_url}"

# selenium locators
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

    # link text locator
    driver.find_element(By.LINK_TEXT, "Home").click()
    time.sleep(5)

    # partial link text locator
    driver.find_element(By.PARTIAL_LINK_TEXT, "String Programs").click()
    time.sleep(5)

# selenium methods to find elements:

def selenium_get_elements():
    # get list of elements using find_elements method
    username_fields = driver.find_elements(By.ID, "firstname")
    username_fields[0].send_keys("Rahul")
    username_fields[1].send_keys("Kumar")
    time.sleep(5)

    # get all links on the page
    list_of_links = driver.find_elements(By.TAG_NAME, "a")
    print("All links on the page:", len(list_of_links))
    for link in list_of_links:
        print("Link Text:", link.text, " - URL:", link.get_attribute("href"))
    
launch_website_and_verify()
selenium_get_elements()


#selenium_locators()

