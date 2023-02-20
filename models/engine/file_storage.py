#!/usr/bin/python3
"""
This module contain the file storage
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    File storage class with 2 attributes :
    __filepath and __objects
    """
    __file_path = 'objects.json'
    __objects = {}

def all(self):
    """
    returns the dictionary __objects
    """
    return self.__objects

def new(self, obj):
    """
    sets in __objects the obj with key <obj class name>.id
    """
    key = obj.__class__.__name__ + '.' + obj.id
    self.__objects[key] = obj

def save(self):
    """
    serializes __objects to the JSON file (path: __file_path)
    """
    json_dict = {}
    for i, j in self.__objects.items():
        json_dict[i] = j.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(json_dict))

def reload(self):
    """deserializes the JSON file to __objects (only if the 
    JSON file (__file_path) exists ; otherwise, do nothing. 
    If the file doesn’t exist, no exception should be raised)
    """
    if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                json_dict = json.loads(f.read())
                for i, j in json_dict.items():
                    self.__objects[i] = eval(j['__class__'])(**j)
