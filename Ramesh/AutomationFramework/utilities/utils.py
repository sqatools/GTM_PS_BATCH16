import json

class Utils:
    def read_json_data(self, filename):
        with open(filename, "r") as file:
            data = file.read()
        return json.loads(data)
