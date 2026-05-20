import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#A fixture is a function that runs before (and optionally after) your tests to set up the environment.

@pytest.fixture(scope= "class") #scope="class": This is a key setting. It tells Pytest to run this fixture only once per test class.
def get_driver_class(request):
    print("Launching Browser")
    driver = webdriver.Chrome() #initializes the Chrome browser session
    driver.get("https://sqatools.in/dummy-booking-website/") #directs the browser to your specific target URL.
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver #regression testing ????
    yield driver

'''The yield statement is where the "setup" ends and the "teardown" begins.

When Pytest hits yield, it pauses the fixture and goes off to run your test cases.

Current Gap: Right now, your code stops at yield. Usually, you would add driver.quit() after the yield to ensure the browser closes automatically once the tests are finished.'''