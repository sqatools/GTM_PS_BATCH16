## install selenium using pip command on terminal
# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

def launch_website_verify():
    driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH
    driver.get("https://www.google.com")
    
    # Verify the title of the page
    assert "Google" in driver.title, "Title does not contain 'Google'"
    
    # Verify the presence of the search box
    search_box = driver.find_element(By.NAME, "q")
    assert search_box is not None, "Search box not found"
    
    print("Website launched and verified successfully!")
    
    driver.quit()