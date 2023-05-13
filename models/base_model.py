#!/usr/bin/python3
"""
This is the base class that all other classes will inherit from
Below are the importations required
"""
import uuid
import datetime
from models import storage


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
        return ("[{}] ({}) <{}>".format(type(self)__.name__, self.id, self.__dict__))

    def save(self):
        """Method to save information to a file"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the object with keys and values of __dict__ instance"""
        obj_dict = dict(self.__dict__)
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return obj_dict
