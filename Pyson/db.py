import json
import time


DEF_FILE_NAME = 'db.json'
DEF_DATA = {"data": {}}


class SetDB:
    def __init__(self, path: str) -> None:
        self.path = path
        self.data = self.read_db()


    def read_db(self) -> dict:

        try:
            with open(self.path) as f:
                data = json.load(f)
            return data

        except json.decoder.JSONDecodeError:
            with open(self.path, 'w') as f:
                json.dump(DEF_DATA, f)
            return DEF_DATA

        except FileNotFoundError:
            with open(DEF_FILE_NAME, 'x') as f:
                json.dump(DEF_DATA, f)
            return DEF_DATA
    

    def update_db(self, data: dict, indent=None):
        
        with open(self.path, 'w') as f:
            json.dump(data, f, indent=indent)

        return data


    def add_item(self, key, value):

        self.data[key] = value

        self.update_db(self.data)


    def remove_item(self, key):

        del self.data[key]

        self.update_db(self.data)

    
    def search_query(self, key):
        
        return self.data[key]