from base.base_api import BaseAPI
from api_data.api_session_data import *

class RestFullAPI(BaseAPI):

    def get_all_objects(self):
        response = self.get_method(url=common_url)
        return response
    
    def get_one_object_details(self, object_id):
        new_url = f"{common_url}/{object_id}"
        response = self.get_method(url=new_url)
        return response
    

    