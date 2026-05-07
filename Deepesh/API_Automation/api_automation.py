"""
HTTP Methods:
1. GET : get all information
2. POST: create new entry
3. PUT : update existing entry or create new one
4. PATCH : update specific field of existing entry
5. DELETE : Delete entry from server


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
    print(response.content)
    print(response.json())
    print(response.status_code)
    data = response.json()
    print("#"*50)
    print(data[0])

#get_all_objects()


def get_specific_objects():
    url = "https://api.restful-api.dev/objects/7"
    request_data = {}
    headers = {}
    response = requests.request("GET", url=url, headers=headers, data=request_data)
    print(response.content)
    print(response.json())
    print(response.status_code)


get_specific_objects()


def create_new_object():
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

create_new_object()
