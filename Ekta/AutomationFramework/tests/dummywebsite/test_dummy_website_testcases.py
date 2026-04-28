import pytest
import time
from page_objects.dummyPage.dummy_page_class import DummyPage


@pytest.mark.usefixtures("get_driver_class")
class TestDummyWebsite:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.dp = DummyPage(self.driver)


    def test_enter_source_dest_city(self):
        self.dp.enter_source_and_destination("Mumbai", "Pune")
        #time.sleep(10)

    def test_enter_depart_return_dates(self):
        self.dp.enter_depart_and_return_dates("01/08/2026", "01/09/2026")
        time.sleep(10)

    def test_get_page_heading(self):
        heading = self.dp.get_page_heading()
        print("Heading of the page is:", heading)       
        