#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__": 
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())            
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    def save(self):
        self.updated_at = datetime.utcnow()
        storage.save()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def to_dict(self):
        dict_ = self.__dict__.copy()
        dict_['__class__'] = self.__class__.__name__
        dict_['created_at'] = dict_['created_at'].isoformat()
        dict_['updated_at'] = dict_['updated_at'].isoformat()
        return dict_