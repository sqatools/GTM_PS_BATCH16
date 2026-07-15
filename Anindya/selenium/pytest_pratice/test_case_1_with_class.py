import selenium

from selenium import webdriver

from selenium.webdriver.common.by import By

import pytest

@pytest.mark.usefixtures("get_class")
class Test_Anindya:
    def test_1(self):
        self.driver.find_element(By.XPATH,"(//input[@name='firstname'])[1]").send_keys("Anindya")

    def test_2(self):
        self.driver.find_element(By.XPATH,"(//input[@name='firstname'])[2]").send_keys("Paul")

    def test_3(self):
        self.driver.find_element(By.XPATH,"(//input[@name='fromcity'])").send_keys("Cooch Behar")     