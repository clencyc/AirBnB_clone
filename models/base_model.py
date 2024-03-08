#!/usr/bin/python3

import uuid
import models
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":  # Don't set __class__ as an attribute
                    if key == "created_at" or key == "updated_at":
            # Convert string to datetime object
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()

        def save(self):
            self.updated_at = datetime.utcnow()
        
        def __str__(self):
            return f"[ {self.__class__.__name__}] ({self.id}) {self.__dict__}"
        
        def to_dict(self):
            dict_ = self.__dict__.copy()
            dict_['__class__'] = self.created_at.isoformat()
            dict_['created_at'] = self.created_at.isoformat()
            dict_['updated_at'] = self.updated_at.isoformat()
            return dict_
if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My first model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
