import requests
import json

def get_specific_objects():
    url = "https://api.restful-api.dev/objects/Apple MacBook Pro 16"
    request_data = {}
    headers = {}
    response = requests.request("GET", url=url, headers=headers, data=request_data)
    #print(response.content)
    print(response.json())
    print(response.status_code)


get_specific_objects()
