#!/usr/bin/python3
"""
This is the base class that all other classes will inherit from
Below are the importations required
"""
import uuid
import datetime
from __init__ import storage


class BaseModel():
    """All methods and attributes required by all child classes are defined within the base class"""
    def __init__(self, *args, **kwargs):
        """This is a method that is called when a new base class instance is created"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            new(storage)
        """If statement to check if its a new instance, if it is call new(obj)"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Returns a string representation of the object created with all the attributes"""
        return ("{} {} {}".format(self.name, self.id, self.__dict__))

    def save(self):
        """Method to save information to a file"""
        save(storage)
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the object with keys and values of __dict__ instance"""
        obj_dict = dict(self.__dict__)
        obj_dict["__class__"] = type(self).__name__
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return obj_dict

test_model = BaseModel()
test_model.name = "Test"
test_model.my_number = 89
print(test_model)
test_model_json = test_model.to_dict()
print(test_model_json)

