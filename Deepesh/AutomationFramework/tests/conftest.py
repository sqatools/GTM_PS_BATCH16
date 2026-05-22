import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

headless = False


@pytest.fixture(scope="class")
def get_driver_class(request):
    print("Launching Browser")
    opt = Options()
    if headless:
        opt.add_argument("--headless")
    driver = webdriver.Chrome(options=opt)
    driver.get("https://sqatools.in/dummy-booking-website/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
    driver.quit()