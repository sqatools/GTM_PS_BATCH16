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


    def test_enter_source_dest_city(self, request):
        # self.dp.enter_source_anddestination("Mumbai", "Pune")
        # self.dp.log(f"Test Name :{request.node.name}")
        self.dp.enter_source_and_destination(self.user_data["fromCity"], self.user_data["destcity"])
        # import pdb; pdb.set_trace()
        # time.sleep(10)


    def test_select_no_passenger(self):
        self.dp.select_number_of_passengers(value=self.user_data["no_of_passanger"])

    def test_select_gender(self):
        self.dp.select_gender(gender=self.user_data["gender_name"])

    def test_select_country(self):
        self.dp.select_country(country_name=self.user_data["country_name"])