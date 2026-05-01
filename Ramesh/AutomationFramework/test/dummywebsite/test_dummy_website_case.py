import pytest
import time
from page_objects.dummy_page.dummy_page_class import DummyPage


@pytest.mark.usefixtures("get_driver_class")
class TestDummyWebsite:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.dp = DummyPage(self.driver)


    def test_enter_source_dest_city(self):
        self.dp.enter_source_anddestination("Mumbai", "Pune")
        # import pdb; pdb.set_trace()
        time.sleep(10)