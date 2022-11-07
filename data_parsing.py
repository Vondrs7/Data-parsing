import json

class ReadData:

    # method for open, read and close json file
    # loaded to "data" variable
    def read_json(self):
        with open("sample-data.json","r") as file:
            x = file.read()
            data = json.loads(x)
            return data

    # "flattening" json data
    def data_flattening(self, x):
        flattened_data = {}
        def flattening( y, name="" ):
            if type(y) is dict:
                for z in y:
                    flattening(y[z], name + z + "_")        
            elif type(y) is list:
                n = 0
                for z in y:
                    flattening(z, name + str(n) + "_")
                    n += 1
            else:
                flattened_data[name[:-1]] = x
        flattening(x)
        return flattened_data        


if __name__ == '__main__':
    
    read_data = ReadData()
    data = read_data.read_json()
    data = read_data.data_flattening(data)

