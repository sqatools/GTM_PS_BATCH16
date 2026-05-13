import pytest
import time
from page_objects.dummy_page.dummy_page_class import DummyPage



#This tells Pytest to go find the get_driver_class fixture you wrote in your conftest.py.
@pytest.mark.usefixtures("get_driver_class")
class TestDummyWebsite:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.dp = DummyPage(self.driver)

        '''Because that fixture was scoped to "class", the browser opens once when this class starts. 
        It also attaches the driver to self.driver, making it available to everything inside this class.'''


    def test_enter_source_dest_city(self):
        self.dp.enter_source_and_destination("Mumbai", "Pune")
        time.sleep(10)