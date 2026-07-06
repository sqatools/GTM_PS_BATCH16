import pytest # we can use pytest features like fixtures, markers, and assertions in this file
from selenium import webdriver


@pytest.fixture(scope="class")
def get_driver_class(request):
    print("Launching Browser")
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver # its like pause 
    driver.quit() #closes all browser after test execution is completed.It destroy the driver object and close all associated windows. It is used when you want to end the entire browser session after the test execution is completed.Destroy driver session also closes all browser windows opened during that session.  
    #driver.close() #closes the current active browser window. If there is only one browser window open, it will close that window but the driver session will still be active. It is used when you want to close only the current browser window after the test execution is completed, but keep the driver session alive for further use.