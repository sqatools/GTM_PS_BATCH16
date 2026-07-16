from selenium import webdriver

from selenium.webdriver.common.by import By

import pytest


@pytest.fixture(scope="class",autouse=True)
def get_driver(request):
    driver = webdriver.Chrome()
    driver.get("https://sqatools.in/dummy-booking-website/")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()
    