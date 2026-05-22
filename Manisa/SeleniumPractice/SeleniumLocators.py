from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


driver = None #global variable
url = "https://sqatools.in/dummy-booking-website/"

def launch_website_and_verify(url):
    global driver
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)

#This tells Python, "Inside this function, when I use the word 'driver',
#I am talking about the global variable I created at the top of the script, not a new local one."
    assert driver.current_url == "https://sqatools.in/dummy-booking-website/"
    print(f"expected url is {url} url opened is {driver.current_url}")

launch_website_and_verify(url= url)

def selenium_locators():
     
     #By.CLASS_NAME header
     heading = driver.find_element(By.CLASS_NAME, "entry-title").text
     print("header-", heading)

     element = driver.find_element(By.XPATH, "//span[contains(text(), 'Dummy ticket for visa application')]")
     print(element.text)
     
     visa_radio = driver.find_element(By.XPATH, "//input[@value='radio_123']")
     #driver.execute_script("arguments[0].click();", visa_radio)
     visa_radio.click()
     time.sleep(2)

     visa_radio = driver.find_element(By.XPATH, "//input[@value='radio_345']")
   
     visa_radio.click()
     time.sleep(2)

     visa_radio = driver.find_element(By.XPATH, "//input[@value='radio_678']")
     #driver.execute_script("arguments[0].click();", visa_radio)
     visa_radio.click()
     time.sleep(2)

     


     #multiple fields with same is/ indexing
     user_name = driver.find_elements(By.ID, "firstname")
     user_name[0].send_keys("Manisa")
     user_name[1].send_keys("Sarangi")
     time.sleep(2)

     dobfield = driver.find_element(By.XPATH, "//span[contains(text(), 'Date of birth')]/following::input[1]")
     dobfield.send_keys("01/01/1990")
     time.sleep(5)
     
     driver.find_element(By.ID, "male").click()
     time.sleep(3)

     driver.find_element(By.XPATH, "//input[@id = 'female']").click()
     time.sleep(3)

     #Number of Additional Passangers
     passenger_dropdown = driver.find_element(By.ID, "admorepass")
     #= driver.find_element(By.ID, "admorepass")
     select_obj = Select(passenger_dropdown)
     select_obj.select_by_visible_text("Add 1 more passenger (100%)")
     time.sleep(2)

     driver.find_element(By.ID, "roundtrip").click()
     time.sleep(5)

    

    #By.ID locator fromcity and destcity
     driver.find_element(By.ID, "fromcity").send_keys("mumbai")
     driver.find_element(By.ID, "destcity").send_keys("kolkata")
     time.sleep(3)

     #By.NAME departure date return date
     driver.find_element(By.NAME, "departdate").send_keys("10-10-2023")
     driver.find_element(By.NAME, "returndate").send_keys("11-11-2023")
     time.sleep(3)

     driver.find_element(By.NAME, "visadate").send_keys("12-12-2023")
     time.sleep(5)

     #driver.find_element(By.XPATH, "//span[contains(text(), 'Both')]/preceding-sibling::input[1]")
     driver.find_element(By.XPATH, "//span[contains(text(), 'Both')]/preceding-sibling::input[1]").click()
     female_radio = driver.find_elements(By.ID, "female")
     female_radio[1].click
     time.sleep(5)

     country_option = driver.find_element(By.ID, "billing_country")
     select_option = Select(country_option)
     select_option.select_by_visible_text("India")
     time.sleep(5)




     # get all links on the page
     list_of_links = driver.find_elements(By.TAG_NAME, "a")
     print("------------------------All links on the page:", len(list_of_links))

     # get all links on the page
     list_of_links = driver.find_elements(By.TAG_NAME, "a")
     print("All links on the page:", len(list_of_links))
     for link in list_of_links:
        print("Link Text:", link.text, " - URL:", link.get_attribute("href"))

     #partial link text locator
     driver.find_element(By.PARTIAL_LINK_TEXT, "Home").click()
     driver.find_element(By.PARTIAL_LINK_TEXT, "Selenium").click()

     
selenium_locators()



