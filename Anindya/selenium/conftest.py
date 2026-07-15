import selenium

from selenium import webdriver

from selenium.webdriver.common.by import By

import time

import pytest

# @pytest.fixture(scope="function")
# def func():
#     # global driver                  no need
#     driver = webdriver.Chrome()
#     driver.get("https://sqatools.in/dummy-booking-website/")
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#     yield driver
#     driver.close()


# @pytest.fixture(scope="function")
# def next():
#     print("test started")
#     yield
#     print("test ended")


@pytest.fixture(scope="function",autouse = True)
def get_driver(request):
    driver = webdriver.Chrome()
    driver.get("https://sqatools.in/dummy-booking-website/")
    driver.maximize_window()
    driver.implicitly_wait(5)

    request.cls.driver = driver
    yield driver
    driver.close()
