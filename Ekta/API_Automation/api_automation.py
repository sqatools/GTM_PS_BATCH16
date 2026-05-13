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
    requests.get("https://api.restful-api.dev/objects")
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
    new_id=response.json()["id"]
    return new_id
   
   
    
new_id=create_new_object()
print("ID of newly created object is-->",new_id)


def update_existing_object(new_id):
    url=f"https://api.restful-api.dev/objects/{new_id}"
    requests_data={
  "name": "Google Pixel 6 Pro",
  "data": {
    "year": 2030,
    "price": "3500 USD 2030 model",
    "CPU model": "Intel Core i9 2030 model",
    "Hard disk size": "1 TB 2030 model"
  }
}      
    headers={"Content-Type": "application/json"}
    response=requests.request("PUT",url=url,headers=headers,data=json.dumps(requests_data))
    print("Updating existing details with PUT method --> It update all details ")
    print(response.json()) # converting raw data into Json format so we can read it in dictionary format and perform operations on it.
    print(response.status_code)


update_existing_object(new_id)


def delete_existing_object(new_id):
    # You must append the specific ID of the object you want to delete
    url = f"https://api.restful-api.dev/objects/{new_id}"
    
 
    headers = {"Content-Type": "application/json"}
    
   
    response = requests.request("DELETE", url=url, headers=headers)
    
    print(response.json())     # converting raw data into Json format
    print(response.status_code) # variable which holds the status code (usually 200 or 204)


#delete_existing_object(new_id)



def get_specific_objects(new_id):
    url = f"https://api.restful-api.dev/objects/{new_id}"
    request_data = {}
    headers = {}
    response = requests.request("GET", url=url, headers=headers, data=request_data)
    print(response.content)
    print(response.json())
    print(response.status_code)


#get_specific_objects(new_id)


def update_existing_object(new_id):
    url=f"https://api.restful-api.dev/objects/{new_id}"
    requests_data={
  "name": "Apple MacBook Pro 16",
  "data": {
    "year": 2050,
    "price": "3500 USD",
    "CPU model": "Intel Core i9",
    "Hard disk size": "1 TB"
  }
}      
    headers={"Content-Type": "application/json"}
    response=requests.request("PATCH",url=url,headers=headers,data=json.dumps(requests_data))
    print("Updating existing details with PATCH method --> It update only the specified fields ")
    print(response.json()) # converting raw data into Json format so we can read it in dictionary format and perform operations on it.
    print(response.status_code)


update_existing_object(new_id)



