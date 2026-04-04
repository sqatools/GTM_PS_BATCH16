import json

def read_json_file(filepath):
    with open(filepath, "r") as file:
        data = file.read()
        # convert raw data to dict format
        json_data = json.loads(data)
        return json_data
    

data = read_json_file(filepath="users_data.json")
print(data)
print(data["firstname"])

data["email"] = "rahul@gmail.com"
data["designation"] ="software engineer"


def write_json_file(filepath, new_data):
    with open(filepath, "w") as file:
        # convert dict data into json format
        json_data = json.dumps(new_data)
        file.write(json_data)


write_json_file(filepath="users_data.json", new_data=data)