from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
# Import your DummyPage class so you can use it
from DummyWebsite.page.dummybookingwebsite import DummyPage

@pytest.mark.usefixtures("get_driver_class")
class TestDummyWebsite:

    
    # initialize page objects
    @pytest.fixture(autouse=True)
    def setup_class(self):
        # self.driver comes from your 'get_driver_class' fixture
        self.dummy_page = DummyPage(self.driver)

    def test_verify_login_successful(self):
    #verification
    # Calling your page helper method inside an assert block
        expected_url = "https://sqatools.in/dummy-booking-website/"
        assert self.dummy_page.verify_login_successful(expected_url) == True, "Login verification failed: Current URL does not match dashboard!"
    
    def test_enter_source_and_destination(self):
        self.dummy_page.enter_source_and_destination(fromcity="Mumbai", destcity="Pune")
        time.sleep(2)
        #self.driver.find_element(By.ID, "destcity").send_keys("Pune")

    def test_enter_dates(self):
        self.dummy_page.enter_dates(departdate="10/10/2023", returndate="15/10/2023")
        #self.driver.find_element(By.NAME, "departdate").send_keys("10/10/2023")
        #self.driver.find_element(By.NAME, "returndate").send_keys("15/10/2023")

    def test_select_gender(self):
        self.dummy_page.select_gender(gender="Female")

  

