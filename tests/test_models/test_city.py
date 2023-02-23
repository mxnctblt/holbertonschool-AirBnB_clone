#!/usr/bin/python3
""" unittests for User """
import os
import models
import unittest
from datetime import datetime
from models.city import City
from models.base_model import BaseModel
from time import sleep


class TestCity(unittest.TestCase):
    """ testing city """

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.city = City()
        cls.city.name = "Antoine"
        cls.city.state_id = "123"

    @classmethod
    def teardown(cls):
        """ at the end of the test cls will tear it down """
        del cls.city

    def tearDown(self):
        """ teardown file.json """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_types(self):
        """ testing the types """
        self.assertEqual(City, type(City()))
        self.assertEqual(datetime, type(City().created_at))
        self.assertEqual(datetime, type(City().updated_at))
        self.assertEqual(str, type(City().id))
        self.assertEqual(str, type(City.name))
        self.assertEqual(str, type(City.state_id))


    def test_city(self):
        """ testing its attributes """
        self.assertTrue('name' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertIn(City(), models.storage.all().values())
        self.assertEqual(self.city.name, 'Antoine')
        self.assertEqual(self.city.state_id, '123')
        self.assertIsNotNone(City.__doc__)
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)
        self.assertEqual('to_dict' in dir(self.city), True)

    def test_str(self):
        """ testing string representation """
        dt = datetime.today()
        dt_repr = repr(dt)
        ct = City()
        ct.id = "123456"
        ct.created_at = ct.updated_at = dt
        ctstr = ct.__str__()
        self.assertIn("[City] (123456)", ctstr)
        self.assertIn("'id': '123456'", ctstr)
        self.assertIn("'created_at': " + dt_repr, ctstr)
        self.assertIn("'updated_at': " + dt_repr, ctstr)

    def test_kwargs(self):
        """ testing instantation with kwargs """
        dt = datetime.today()
        dt_iso = dt.isoformat()
        ct = City(id="123456", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(ct.id, "123456")
        self.assertEqual(ct.created_at, dt)
        self.assertEqual(ct.updated_at, dt)
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
