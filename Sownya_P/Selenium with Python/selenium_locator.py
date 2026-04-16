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
