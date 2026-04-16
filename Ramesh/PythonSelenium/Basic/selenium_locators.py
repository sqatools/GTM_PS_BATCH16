from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# global variable to hold the driver isinstance
driver = None
url = "https://sqatools.in/dummy-booking-website/"


def launch_website_and_verify(url):
    global driver
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    # verify the correct page is loaded.

    print("Current URL : ", driver.current_url)
    assert driver.current_url == url, f"Expected URL: {url}, but got: {driver.current_url}"


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

    


def xpath_locators(url):
    launch_website_and_verify(url=url)
    # XPATH locator
    driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    dashboard_heading = driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
    print("Heading of the page is : ", dashboard_heading)
    assert dashboard_heading == "Dashboard", f"Expected heading : Dashboard, but got : {dashboard_heading}"
    time.sleep(5)

    # navigate to admin page
    driver.find_element(By.XPATH, "//span[text()='Admin']/parent::a").click()
    assert driver.find_element(By.XPATH, "//h6[text()='User Management']").is_displayed()
    print("Admin page is displayed successfully!")
    
    add_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Add']")
    if add_btn.is_enabled():
        add_btn.click()
        assert driver.find_element(By.XPATH, "//h6[text()='Add User']").is_displayed()
        print("Add User form is displayed successfully!")


    
    driver.find_element(By.XPATH, "//label[text()='User Role']//ancestor::div[contains(@class,'oxd-input-field')]//div[text()='-- Select --']").click()
    driver.find_element(By.XPATH, "//div[@role='option']//span[text()='Admin']").click()
    time.sleep(5)



# launch_website_and_verify(url=url)

# selenium_get_elements()

# selenium_locators()

url2 = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
xpath_locators(url=url2)