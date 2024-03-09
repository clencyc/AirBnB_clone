#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel

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
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj
    pass

    def save(self):
        new = {key: value for key, value in self.__objects.items()}

        with open(self.__file_path, "w") as f:
            json.dump(new, f)
    pass

    def reload(self):

        try:
            with open(self.__file_path, "r") as fileread:
                self.__objects.update(json.load(fileread))
        except Exception:
            pass

