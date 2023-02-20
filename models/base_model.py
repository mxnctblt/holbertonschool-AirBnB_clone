#!/usr/bin/python3
""" module creating the class BaseModel for others to inherit from  """

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """ define BaseModel

    Attributes:
        id (str): assigns with a unique id when an instance is created
        created_at: assigns with the current datetime when an instance
        is created
        updated_at: assigns with the current datetime when an instance
        is created and it will be updated every time you change your object

    Methods:
        __str__: prints a string representation
        save(self): updates the public instance attribute updated_at
        with the current datetime
        to_dict(self): returns a dictionary containing all keys/values
        of __dict__ of the instance
    """

    def __init__(self):
        """ initialization of BaseModel """
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """ prints: [<class name>] (<self.id>) <self.__dict__> """
        return ('[{}] ({}) {}'.format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance """
        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return d
