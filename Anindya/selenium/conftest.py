import selenium

from selenium import webdriver

from selenium.webdriver.common.by import By

import pytest


@pytest.fixture(scope="function",autouse=True)
def func():
    # global driver
    driver = webdriver.Chrome()
    driver.get("https://sqatools.in/dummy-booking-website/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.close()
