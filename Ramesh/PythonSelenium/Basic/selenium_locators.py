from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# global variable to hold the driver isinstance
driver = None


def launch_website_and_verify():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://sqatools.in/dummy-booking-website/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    # verify the correct page is loaded.

    assert driver.current_url == "https://sqatools.in/dummy-booking-website/"


def selenium_locators():
    # ID locator
    driver.find_element(By.ID, "fromcity").send_keys("Assam")
    driver.find_element(By.ID, "destcity").send_keys("Guwahati")

    # Name locator
    driver.find_element(By.NAME, "departdate").send_keys("01/01/2026")
    driver.find_element(By.NAME, "returndate").send_keys("03/01/2026")

    # Class Name locator
    heading = driver.find_element(By.CLASS_NAME, "entry-title").text
    print("Heading of the page is :", heading)
    
    
    # link text locator
    driver.find_element(By.LINK_TEXT, "Home").click()
    


    # partial link text locator
    driver.find_element(By.PARTIAL_LINK_TEXT, "String Programs").click()
    time.sleep(5)

# selenium methods to find element 

def selenium_get_elements():
    # get list of elements using find_elements method
    username_fields = driver.find_elements(By.ID, "firstname")
    username_fields[0].send_keys("Ramesh")
    username_fields[1].send_keys("Kumar")
    time.sleep(5)

    # get all links on the page
    list_of_links = driver.find_elements(By.TAG_NAME, "a")
    print("All links on the page:", len(list_of_links))
    for link in list_of_links:
        print("Link Text:", link.text, " - URL:", link.get_attribute("href"))

    





launch_website_and_verify()
# selenium_get_elements()
selenium_locators()