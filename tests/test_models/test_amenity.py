#!/usr/bin/python3
""" unittests for User """
import os
import models
import unittest
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
from time import sleep


class TestAmenity(unittest.TestCase):
    """ testing amenity """

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.amen = Amenity()
        cls.amen.name = "Antoine"

    @classmethod
    def teardown(cls):
        """ at the end of the test cls will tear it down """
        del cls.amen

    def tearDown(self):
        """ teardown file.json """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_types(self):
        """ testing the types """
        self.assertEqual(Amenity, type(Amenity()))
        self.assertEqual(datetime, type(Amenity().created_at))
        self.assertEqual(datetime, type(Amenity().updated_at))
        self.assertEqual(str, type(Amenity().id))
        self.assertEqual(str, type(Amenity.name))


    def test_state(self):
        """ testing its attributes """
        self.assertTrue('name' in self.amen.__dict__)
        self.assertTrue('id' in self.amen.__dict__)
        self.assertTrue('created_at' in self.amen.__dict__)
        self.assertTrue('updated_at' in self.amen.__dict__)
        self.assertIn(Amenity(), models.storage.all().values())
        self.assertEqual(self.amen.name, 'Antoine')
        self.assertIsNotNone(Amenity.__doc__)
        self.assertTrue(issubclass(self.amen.__class__, BaseModel), True)
        self.amen.save()
        self.assertNotEqual(self.amen.created_at, self.amen.updated_at)
        self.assertEqual('to_dict' in dir(self.amen), True)

    def test_str(self):
        """ testing string representation """
        dt = datetime.today()
        dt_repr = repr(dt)
        st = Amenity()
        st.id = "123456"
        st.created_at = st.updated_at = dt
        ststr = st.__str__()
        self.assertIn("[Amenity] (123456)", ststr)
        self.assertIn("'id': '123456'", ststr)
        self.assertIn("'created_at': " + dt_repr, ststr)
        self.assertIn("'updated_at': " + dt_repr, ststr)

    def test_kwargs(self):
        """ testing instantation with kwargs """
        dt = datetime.today()
        dt_iso = dt.isoformat()
        st = Amenity(id="123456", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(st.id, "123456")
        self.assertEqual(st.created_at, dt)
        self.assertEqual(st.updated_at, dt)
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
