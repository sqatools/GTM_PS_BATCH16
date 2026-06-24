import selenium

from selenium import webdriver

from selenium.webdriver.common.by import By

import time

driver = None
def launch():
    global driver 

    driver = webdriver.Chrome()
    driver.get("https://sqatools.in/dummy-booking-website/")

    driver.maximize_window()

    assert driver.current_url == "https://sqatools.in/dummy-booking-website/"
    print(driver.title)

def locator():
    # ID locator
    # driver.find_element(By.ID,"fromcity").send_keys("Mumbai")
    # driver.find_element(By.ID,"destcity").send_keys('Chennai')

    # Xpath locator

    # driver.find_element(By.XPATH,"//*[@name='fromcity']").send_keys("Anindya")
    a = driver.find_element(By.XPATH,"//h2[text()='Passenger Details']").text
    print(a)
    driver.find_element(By.XPATH,"//input[contains(@name,'mcity')]").send_keys("Abhijit")

    

    b = driver.find_element(By.XPATH,"//h2[contains(text(),'Delivery Option')]").text
    print(b)
    

    c = driver.find_element(By.XPATH,"//span[text()='Dummy return ticket – $300 ']/parent::li").text
    print(c)

    d = driver.find_element(By.XPATH,"//span[text()='Dummy ticket for visa application – $200 ']/ancestor::div[@align='left']").text
    print(d)

    driver.find_element(By.XPATH,"//input[@name='fromcity']/following::input[@id='billing_name']").send_keys("Anindya")

    driver.find_element(By.XPATH,"//input[@name='fromcity']/preceding::input[@id='male']").click()
    time.sleep(5)

    w =driver.find_element(By.XPATH,"//td[text()='Kolkata']/following-sibling::td[text()='5000']").text
    print(w) 
    g = driver.find_element(By.XPATH,"//td[text()='Kolkata']/preceding-sibling::td[text()='6004']").text
    print(g)
    driver.find_element(By.XPATH,"//td[text()='Kolkata']/preceding-sibling::td/input[@value='checkbox']").click()
    time.sleep(5)
    driver.close()


    # # Name locator
    # driver.find_element(By.NAME,"departdate").send_keys("10/10/2026")
    # driver.find_element(By.NAME,"returndate").send_keys("23/10/2026")

    # # class locator
    # b = driver.find_element(By.CLASS_NAME,"entry-title").text
    # print(b)

    
   
    # link text

    # driver.find_element(By.ID,"menu-menu_main").driver.find_element(By.LINK_TEXT,"Home").click()

    # time.sleep(15)

    # driver.find_element(By.XPATH,"//div[text()='Close']").click()

    # # time.sleep(15)

    # # partiAL link text

    # driver.find_element(By.PARTIAL_LINK_TEXT,"String Programs").click()
    # time.sleep(5)
    # driver.close()

# def multiple_element():
#         w = driver.find_elements(By.ID,"firstname")
#         print("The value is w is ", len(w))
#         w[0].send_keys("This")
#         w[1].send_keys("That")

#         time.sleep(2)

#         v = driver.find_elements(By.TAG_NAME,"a")
#         print("Total lenght of link",len(v))

#         for item in v :
#             print("link text is", item.text, "and the url is ", item.get_attribute("href"))

#         time.sleep(10)
#         driver.close()    





launch()
locator()


# multiple_element()