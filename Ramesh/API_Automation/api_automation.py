"""
HTTP Methods:
1. GET : get all information
2. POST : create new entry
3. PUT : update existing entry or create new one
4. PATCH : update specific field of existing entry
5. DELETE : Delete entryvfrom server


status code
1. 100 - 199
2. 200 - 299
3. 300 - 399
4. 400 - 499
5. 500 - 599
"""

# install requests modules using below command
# -> pip install requests.


import requests
import json


def get_all_objects():
    url = "https://api.restful-api.dev/objects"
    request_data = {}
    headers = {}
    response = requests.request("GET", url=url, headers=headers, data=request_data)
    print(response.json())
    print(response.status_code)

# get_all_objects()


def get_specific_objects():
    url = "https://api.restful-api.dev/objects/7"
    request_data = {}
    headers = {}
    response = requests.request("GET", url=url, headers=headers, data=request_data)
    print(response.json())
    print(response.status_code)


# get_specific_objects()


def create_new_objects():
    url = "https://api.restful-api.dev/objects"
    request_data = {
            "name": "Apple MacBook Pro 200",
            "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
        }
    headers = {"Content-Type" : "application/json"}
    response = requests.request("POST", url=url, headers=headers, data=json.dumps(request_data))
    print(response.content)
    print(response.json())
    print(response.status_code)
    new_id = response.json()['id']
    return new_id

new_id = create_new_objects()
print("New ID: :", new_id)


def delete_entry(new_id): 
    url = f"https://api.restful-api.dev/objects/{new_id}"
    response = requests.request("DELETE", url)
    print(response.json())
    print(response.status_code)


# delete_entry(new_id)
# get_specific_objects(new_id)



def update_new_object(new_id):
    url = f"https://api.restful-api.dev/objects/{new_id}"
    request_data = {
            "name": "Apple MacBook Pro 250",
            "data": {
            "year": 200,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
        }
    headers = {"Content-Type" : "application/json"}
    response = requests.request("PUT", url=url, headers=headers, data=json.dumps(request_data))
    print(response.content)
    print(response.json())
    print(response.status_code)


def patch_new_object(new_id):
    url = f"https://api.restful-api.dev/objects/{new_id}"
    request_data = {
            "data": {
                "price": 5000.99,
                }
        }
    headers = {"Content-Type" : "application/json"}
    response = requests.request("PATCH", url=url, headers=headers, data=json.dumps(request_data))
    print(response.content)
    print(response.json())
    print(response.status_code)

# print("*"*50)
# obj_id = create_new_objects()
# print("*"*50)
# update_new_object(obj_id)
# print("*"*50)
# # get_specific_objects(new_id)
# print("*"*50)
# patch_new_object(new_id)

def Authentication_Base_Api():
    