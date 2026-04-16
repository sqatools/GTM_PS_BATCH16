from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://www.facebook.com/")

driver.find_element(By.ID, "_r_9_").sendkeys("ektakharade@gmail.com")
driver.find_element(By.ID, "_r_c").sendkeys("Bapumaza1*")
driver.find_element(By.CLASS_NAME,"x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft").click()
driver.close()