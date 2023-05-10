#!/usr/bin/python3
import uuid
import datetime

class BaseModel():
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):

       return ("{} {} {}".format(self.name, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """self.__class__ = self"""
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return self.__dict__

test_model = BaseModel()
test_model.name = "Test"
test_model.my_number = 89
print(test_model)
test_model_json = test_model.to_dict()
print(test_model_json)

