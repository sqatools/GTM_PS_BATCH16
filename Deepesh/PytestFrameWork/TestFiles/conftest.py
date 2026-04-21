from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture(scope="session")
def get_driver():
    print("Launching Browser")
    driver = webdriver.Chrome()
    driver.get("https://sqatools.in/dummy-booking-website/")
    driver.maximize_window()
    yield driver


@pytest.fixture(scope="function")
def setup():
    print("\n---Test setup initiate--")
    yield
    print("\n---Test Teardown initiate--")
