import pytest
import time
from page_objects.dummy_page.dummy_page_class import DummyPage
from utilities.utils import Utils


@pytest.mark.usefixtures("get_driver_class")
class TestDummyWebsite:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.dp = DummyPage(self.driver)

        # create object of util class
        self.util = Utils()
        self.user_data = self.util.read_json_data("page_objects/dummy_page/user_data.json")


    def test_enter_source_dest_city(self):
        #self.dp.enter_source_and_destination("Mumbai", "Pune")
        self.dp.enter_source_and_destination(self.user_data["fromCity"], self.user_data["destcity"])
        time.sleep(10)

        
        