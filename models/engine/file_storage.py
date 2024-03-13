#!/usr/bin/python3
import json
import os



class FileStorage:
    
    """
    A class for serializing and deserializing instances to/from a JSON file.
    """

    __file_path = "file.json"
    __objects = {}
    _instance = None

    def __init__(self):
        self._data = []
        self._index = 0

    def save(self):
        with open(self.__file_path, 'w') as f:
            objs = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(objs, f)

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._data):
            result = self._data[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def all(self):
        return FileStorage.__objects
    pass

    def new(self, obj):
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj
    def reload(self):
        from models.user import User
        from models.base_model import BaseModel
        from models import storage
        
        if os.path.getsize(self.__file_path) > 0:
            with open(self.__file_path, "r") as f:
                try:
                    objs = json.load(f)
                except json.JSONDecodeError:
                    print("JSON file is not properly formatted")
        else:
            print("JSON file is empty")

