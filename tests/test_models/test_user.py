#!/usr/bin/python3
""" unittests for User """
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestUser(unittest.TestCase):
    """ testing User """
    def test_user(self):
        """ testing its attributes """
        u = User()
        u.email = '5645@holbertonstudents.com'
        u.password = 'helloworld'
        u.first_name = 'Betty'
        u.last_name = 'Holberton'
        self.assertEqual(u.email, '5645@holbertonstudents.com')
        self.assertEqual(u.password, 'helloworld')
        self.assertEqual(u.first_name, 'Betty')
        self.assertEqual(u.last_name, 'Holberton')
        self.assertEqual(str, type(u.email))
        self.assertEqual(str, type(u.password))
        self.assertEqual(str, type(u.first_name))
        self.assertEqual(str, type(u.last_name))


if __name__ == "__main__":
    unittest.main()
