#!/usr/bin/python3
""" module creating the class BaseModel for others to inherit from  """

from datetime import datetime
import uuid
import models


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

    def __init__(self, *args, **kwargs):
        """ initialization of BaseModel """
        time = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, time)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)
    def __str__(self):
        """ prints: [<class name>] (<self.id>) <self.__dict__> """
        return ('[{}] ({}) {}'.format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance """
        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return d
