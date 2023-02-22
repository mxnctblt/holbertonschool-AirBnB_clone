#!/usr/bin/python3
"""
module testing amenity
"""
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.amen = Amenity()
        cls.amen.name = "jacuzzi"

    @classmethod
    def tearDownClass(cls):
        del cls.amen
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_subclass(self):
        self.assertTrue(issubclass(self.amen.__class__, BaseModel), True)

    def test_functions(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_attr(self):
        self.assertTrue('id' in self.amen.__dict__)
        self.assertTrue('created_at' in self.amen.__dict__)
        self.assertTrue('updated_at' in self.amen.__dict__)
        self.assertTrue('name' in self.amen.__dict__)

    def test_strings(self):
        self.assertEqual(type(self.amen.name), str)

    def test_save(self):
        self.amen.save()
        self.assertNotEqual(self.amen.created_at, self.amen.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.amen), True)


if __name__ == "__main__":
    unittest.main()
