import requests
import logging


class BaseAPI:
    def __init__(self):
        self.log = logging.getLogger(__name__)

    def get_method(self, url, header=None, request_body=None):
        header = header if header else {}
        request_body = request_body if request_body else {}
        response = requests.request("GET", url, headers=header, data=request_body)
        self.log.info("Method Name : GET")
        self.log.info(f"URL :{url}")
        self.log.info(f"Headers : {header}")
        self.log.info(f"Request body : {request_body}")
        self.log.info(f"response : {response.json()}")
        self.log.info(f"status code : {response.status_code}")
        return response
    

    def post_method(self, url, header=None, request_body=None):
        header = header if header else {}
        request_body = request_body if request_body else {}
        response = requests.request("POST", url, headers=header, data=request_body)
        self.log.info("Method Name : POST")
        self.log.info(f"URL :{url}")
        self.log.info(f"Headers : {header}")
        self.log.info(f"Request body : {request_body}")
        self.log.info(f"response : {response.json()}")
        self.log.info(f"status code : {response.status_code}")
        return response
    
    def put_method(self, url, header=None, request_body=None):
        header = header if header else {}
        request_body = request_body if request_body else {}
        response = requests.request("PUT", url, headers=header, data=request_body)
        self.log.info("Method Name : PUT")
        self.log.info(f"URL :{url}")
        self.log.info(f"Headers : {header}")
        self.log.info(f"Request body : {request_body}")
        self.log.info(f"response : {response.json()}")
        self.log.info(f"status code : {response.status_code}")
        return response
    
    def patch_method(self, url, header=None, request_body=None):
        header = header if header else {}
        request_body = request_body if request_body else {}
        response = requests.request("GET", url, headers=header, data=request_body)
        self.log.info("Method Name : GET")
        self.log.info(f"URL :{url}")
        self.log.info(f"Headers : {header}")
        self.log.info(f"Request body : {request_body}")
        self.log.info(f"response : {response.json()}")
        self.log.info(f"status code : {response.status_code}")
        return response
    

    def delete_method(self, url, header=None, request_body=None):
        header = header if header else {}
        request_body = request_body if request_body else {}
        response = requests.request("GET", url, headers=header, data=request_body)
        self.log.info("Method Name : GET")
        self.log.info(f"URL :{url}")
        self.log.info(f"Headers : {header}")
        self.log.info(f"Request body : {request_body}")
        self.log.info(f"response : {response.json()}")
        self.log.info(f"status code : {response.status_code}")
        return response