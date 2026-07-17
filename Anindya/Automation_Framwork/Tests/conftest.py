from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

import pytest

headless = True

@pytest.fixture(scope="class",autouse=True)
def get_driver(request):
    opt = Options()
    opt.add_argument("--headless")
    driver = webdriver.Chrome(options=opt)
    driver.get("https://sqatools.in/dummy-booking-website/")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()
    