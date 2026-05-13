from api_pages.restful_api_page import RestFullAPI
import pytest

class TestRestFullAPI:
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):   
        self.obj = RestFullAPI()

    def test_get_all_objects_and_verify(self):
        response = self.obj.get_all_objects()
        assert len(response.json()) == 13
        assert response.status_code == 200

  

