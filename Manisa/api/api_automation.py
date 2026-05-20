#Notes
#restful api doesnot store any data doesnot heavy
"""
HTTP Methods:
1. GET : get all information
https://api.restful-api.dev/objects/{id}
Retrieves detailed information for a single object specified by its unique ID.

2. POST: create new entry
3. PUT : update existing entry or create new one
4. PATCH : update specific field of existing entry
5. DELETE : Delete entry from server


status code
1. 100 - 199 #informational
2. 200 - 299 #success
3. 300 - 399 #redirection - further action to be  taken
4. 400 - 499 #client error bad syntax- developer's fault
5. 500 - 599 #server fault
"""
#install requests module
#pip install requests

import requests
import json #create entry by api bcz value needs to be updated in json format required for POST method



def get_all_objects():
    url = "https://api.restful-api.dev/objects/"
    request_data = {}
    headers = {}
    response = requests.request("GET", url = url, headers=headers, data=request_data)
    print(response.content) #string format output
    print(response.json())
    print("status_code-", response.status_code)
    data = response.json()
    print("-----"*60)
    print("getting value from first index from response-",data[0])

get_all_objects()

def get_specific_objects():
    url = "https://api.restful-api.dev/objects/7"
    request_data = {}
    headers = {}
    response = requests.request("GET", url=url, headers=headers, data=request_data)
    print(response.content)
    print(response.json())
    print("get secific data by giving id ", response.status_code)

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

print("="*30)

'''

def create_put_object():
    url = "https://api.restful-api.dev/objects/7"
    update_data = {
        "name": "Apple iphone 15 pro",
        "data": {
            "year": 2024,
            "price": 1050.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "256 gb",
            "color": "midnight blue"
        }
        }
    headers = {"Content-Type" : "application/json"}
    response = requests.request("PUT", url=url, headers=headers, json = update_data))
    print(response.content)
    print(response.json())
    print(response.status_code)

create_put_object()

'''


def delete_objects():
    url = "https://api.restful-api.dev/objects/7"
    request_data = {}
    headers = {}
    response = requests.request("DELETE", url=url, headers=headers, data=request_data)
    
    print(response.json())
    print("delete secific data by giving id ", response.status_code)

delete_objects()


