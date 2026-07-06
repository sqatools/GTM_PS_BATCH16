import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def get_driver_class(request):
    print("Launching Browser")
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
    driver.quit() 
    

   

