import json

class Utils:
    def read_json_data(self,file_name):
        with open(file_name,'r') as f :
            data = f.read()
        return json.loads(data)
        