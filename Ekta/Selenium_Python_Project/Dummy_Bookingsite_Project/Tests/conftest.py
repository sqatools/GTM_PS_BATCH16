import pytest # we can use pytest features like fixtures, markers, and assertions in this file
from selenium import webdriver


@pytest.fixture(scope="session")
def get_driver_class():
    print("Launching Browser for entire test session")
    driver = webdriver.Chrome()
    driver.get("https://sqatools.in/dummy-booking-website/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver 
    print("Closing Browser for entire test session")
    driver.quit() 