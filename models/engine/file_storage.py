#!/usr/bin/python3
import json

class FileStorage:
    __file_path = "objects.json"
    __objects = []

    def all(self):
        return __objects

    def new(self, obj):
        __objects.append(obj)

    def save(self):
        with open(__file_path,'w') as f:
            json.dump(__objects,f)

    def reload(self):
        if __file_path:
            with open(__file_path,'r') as f:
                __objects = json.loads(f)
