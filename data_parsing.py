import json

class ReadData:

    # method for open, read and close json file
    # loaded to "data" variable
    def read_json(self):
        with open("sample-data.json","r") as file:
            x = file.read()
            data = json.loads(x)
            return data


if __name__ == '__main__':
    
    read_data = ReadData()
    data = read_data.read_json()
