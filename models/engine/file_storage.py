#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    __file_path = 'objects.json'
    __objects = {}

    def all(self):
        return FileStorage._objects

    def new(self, obj):
        FileStorage.__objects.append(obj)

    def save(self):
        with open(FileStorage.__file_path,'w') as f:
            json.dump(FileStorage.__objects,f)

    def reload(self):
        if len(FileStorage.__file_path) > 0:
            with open(FileStorage.__file_path,'r') as f:
               FileStorage.__objects = json.loads(f)
