#!/usr/bin/python3
"""Test Review"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class Testreview(unittest.TestCase):
    """
    Unittests for the Review class.
    """

    def test_class(self):
        """
        Tests to check if class is named correctly.
        """
        rev1 = Review()
        self.assertEqual(rev1.__class__.__name__, "Review")

    def test_father(self):
        """
        Tests to check if lass inherits from BaseModel.
        """
        rev1 = Review()
        self.assertTrue(issubclass(rev1.__class__, BaseModel))

    def test_none(self):
        bm1 = BaseModel(None)
        self.assertNotIn(None, bm1.__dict__)

if __name__ == "__main__":
    unittest.main()
