#!/usr/bin/python3
"""
Unitesting for review
"""
import unittest
import os
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.Test1 = Review()
        cls.Test1.place_id = "Test"
        cls.Test1.user_id = "Test2"
        cls.Test1.text = "Test3"

    @classmethod
    def tearDownClass(cls):
        del cls.Test1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_is_sub(self):
        self.assertTrue(issubclass(self.Test1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(Review.__doc__)

    def test_has_attr(self):
        self.assertTrue('id' in self.Test1.__dict__)
        self.assertTrue('created_at' in self.Test1.__dict__)
        self.assertTrue('updated_at' in self.Test1.__dict__)
        self.assertTrue('place_id' in self.Test1.__dict__)
        self.assertTrue('text' in self.Test1.__dict__)
        self.assertTrue('user_id' in self.Test1.__dict__)

    def test_strings(self):
        self.assertEqual(type(self.Test1.text), str)
        self.assertEqual(type(self.Test1.place_id), str)
        self.assertEqual(type(self.Test1.user_id), str)

    def test_save(self):
        self.Mitali.save()
        self.assertNotEqual(self.Test1.created_at, self.Test1.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.Test1), True)


if __name__ == "__main__":
    unittest.main()
