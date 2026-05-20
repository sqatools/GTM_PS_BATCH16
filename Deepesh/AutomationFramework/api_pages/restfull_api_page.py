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
    

    def create_new_object(self):
        response = self.post_method(url=common_url, header=headers, request_body=post_request_data)
        return response
    

    def update_new_object(self):
        response = self.post_method(url=common_url, header=headers, request_body=post_request_data)
        user_id = response.json()["id"]
        updated_url = f"{common_url}/{user_id}"
        response = self.put_method(url=updated_url, header=headers, request_body=post_request_data)
        return response

    def get_All_users(self):
        response = self.get_method(get_all_users_url, header=go_rest_headers)
        return response
    


        

