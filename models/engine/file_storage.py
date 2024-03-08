import json
from models.base_model import BaseModel

class FileStorage:
      """
    A class for serializing and deserializing instances to/from a JSON file.
        """
      
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, "w") as file:
        json.dump(self.__objects, file)

    def reload(self):
        