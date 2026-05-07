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
    url="https://api.restful-api.dev/objects"
    requests_data={}      
    headers={}   
    response=requests.request("GET",url=url,headers=headers,data=requests_data)
    #print(response.content)    # normal string content 
    print(response.json()) # converting raw data into Json format so we can read it in dictionary format and perform operations on it.
    print(response.status_code) # its variable which hold the status code.
    data=response.json()
    print("*"*60)
    print(data[12])

#get_all_objects()  


def get_specific_objects():
    url = "https://api.restful-api.dev/objects/7"
    request_data = {}
    headers = {}
    response = requests.request("GET", url=url, headers=headers, data=request_data)
    print(response.content)
    print(response.json())
    print(response.status_code)


#get_specific_objects()


def create_new_object():
    url="https://api.restful-api.dev/objects"
    requests_data={
  "name": "Apple MacBook Pro 16",
  "data": {
    "year": 2026,
    "price": "3500 USD",
    "CPU model": "Intel Core i9",
    "Hard disk size": "1 TB"
  }
}      
    headers={"Content-Type": "application/json"}
    response=requests.request("POST",url=url,headers=headers,data=json.dumps(requests_data))
    print(response.content)    # normal string content 
    print(response.json()) # converting raw data into Json format so we can read it in dictionary format and perform operations on it.
    print(response.status_code) # its variable which hold the status code.
    
#create_new_object()

def update_existing_object():
    url="https://api.restful-api.dev/objects/1"
    requests_data={
  "name": "Google Pixel 6 Pro",
  "data": {
    "year": 2025,
    "price": "3500 USD 2025 model",
    "CPU model": "Intel Core i9 2025 model",
    "Hard disk size": "1 TB 2025 model"
  }
}      
    headers={"Content-Type": "application/json"}
    response=requests.request("PUT",url=url,headers=headers,data=json.dumps(requests_data))
    print(response.content)    # normal string content 
    print(response.json()) # converting raw data into Json format so we can read it in dictionary format and perform operations on it.
    print(response.status_code)


update_existing_object()
