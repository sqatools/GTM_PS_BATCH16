# read write json file
import json

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        print("JSON data:", data)   

    return data


output = read_json(file_path=r"C:\AutomationProject\GTM_PS_BATCH16\Sownya_P\Python programming\File Handling\emp_data.json")

print("Employee Name:", output['employees'][0]['name'])
print("Employee Age:", output['employees'][0]['age'])   


def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)  # indent for pretty printing       

new_data = { "employees": [ "pavan", "sownya", "nithya" ] }
write_json(file_path=r"C:\AutomationProject\GTM_PS_BATCH16\Sownya_P\Python programming\File Handling\new_emp_data.json", data=new_data)
