import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from SeleniumBase import SeleniumBase
from locators import Locators


'''@pytest.fixture(scope="session", autouse=True)
def get_driver():
    print("Launching Browser")
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver'''

'''@pytest.fixture(scope="class")
def get_driver_class(request):
    print("Launching Browser")
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield

@pytest.fixture(scope="session")
def get_driver():
    print("Launching Browser")
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/")
    driver.maximize_window()
    yield driver


pytest.fixture(scope="function", autouse=True)
def setup():
    print("---Test setup initiate--")
    yield
    print("---Test Teardown initiate--")



@pytest.fixture(scope="class")
def get_driver_class(request):
    print("Launching Browser")
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver'''


@pytest.fixture(scope="class", autouse=True)
def get_driver_class(request):
    print("\n--- Launching Browser (Class Scope) ---")
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/")
    driver.maximize_window()
    time.sleep(20)
    driver.implicitly_wait(10)
    
    # This attaches the driver directly to the Test Class as 'self.driver'
    if request.cls is not None:
        request.cls.driver = driver
        request.cls.sb = SeleniumBase(driver)
        request.cls.ol = Locators()
        
    yield driver
    
    print("\n--- Closing Browser ---")
    driver.quit()

@pytest.fixture(scope="function", autouse=True)
def setup_teardown_log():
    print("\n--- Test setup initiate --")
    yield
    print("\n--- Test Teardown initiate --")