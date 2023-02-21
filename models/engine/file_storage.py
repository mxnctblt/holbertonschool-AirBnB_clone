#!/usr/bin/python3
""" module FileStorage """
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """ serializes instances to a JSON file and deserializes JSON file
    to instances

    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): empty but will store all objects by <class name>.id

    Methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to __objects (only if the JSON
            file (__file_path) exists ; otherwise, do nothing. If the file
            doesn’t exist, no exception should be raised)
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            jdict = {key: f.to_dict() for key, f in self.__objects.items()}
            json.dump(jdict, f)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the
        JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, encoding='utf-8') as f:
                jdict = json.load(f)
                for k, v in jdict.items():
                    f = eval(v['__class__'])(**v)
                    self.__objects[k] = f

        except FileNotFoundError:
            return
