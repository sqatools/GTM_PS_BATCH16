import pytest
import time
from page_objects.dummyPage.dummy_page_class import DummyPage


@pytest.mark.usefixtures("get_driver_class")
class TestDummyWebsite:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.dp = DummyPage(self.driver)


    def test_enter_source_dest_city(self):
        self.dp.enter_source_and_destination("Bangalore", "Kolhapur")
        #time.sleep(10)

    def test_enter_depart_return_dates(self):
        self.dp.enter_depart_and_return_dates("01/08/2026", "01/09/2026")
        #time.sleep(10)

    def test_get_page_heading(self):
        heading = self.dp.get_page_heading()
        print("Heading of the page is:", heading)     

    def test_select_female_radio_btn(self):
        self.dp.select_male_radio_btn() 
    
    #def test_select_passenger_count(self):
       # self.dp.select_passenger_count("4")

    def test_select_country(self):
        self.dp.select_country("India")
        