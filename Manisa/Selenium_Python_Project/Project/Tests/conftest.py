import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def get_driver_class(request):
    print("============launching browser============")
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    #driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
    print("=============closing browser=============")
    #driver.close()

