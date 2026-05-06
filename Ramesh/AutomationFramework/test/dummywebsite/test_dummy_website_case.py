import pytest
import time
from page_objects.dummy_page.dummy_page_class import DummyPage
from utilities.utils import Utils


@pytest.mark.usefixtures("get_driver_class")
class TestDummyWebsite:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.dp = DummyPage(self.driver)

        self.util = Utils()
        self.user_data = self.util.read_json_data("page_objects/dummy_page/user_data.json")


    def test_enter_source_dest_city(self):
        # self.dp.enter_source_anddestination("Mumbai", "Pune")
        self.dp.enter_source_anddestination(self.user_data["fromCity"], self.user_data["destcity"])
        # import pdb; pdb.set_trace()
        time.sleep(10)


    