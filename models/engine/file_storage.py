#!/usr/bin/python3
import json
import os
from models.user import User 
from models import get_storage


class FileStorage:
    """
    A class for serializing and deserializing instances to/from a JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects
    pass

    def new(self, obj):
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj
    def reload(self):
        from models import storage
        storage = get_storage()
        
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
            for k, v in objs.items():
                cls = v['__class__']
                if cls in storage.classes:
                    self.__objects[k] = storage.classes[cls](**v)

