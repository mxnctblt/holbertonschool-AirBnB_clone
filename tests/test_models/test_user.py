#!/usr/bin/python3
""" unittests for User """
import os
import models
import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel
from time import sleep


class TestUser(unittest.TestCase):
    """ testing User """

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Betty"
        cls.user.last_name = "Holberton"
        cls.user.email = "5645@holbertonstudents.com"
        cls.user.password = "helloworld"

    @classmethod
    def teardown(cls):
        """ at the end of the test cls will tear it down """
        del cls.user

    def tearDown(self):
        """ teardown file.json """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_types(self):
        """ testing the types """
        self.assertEqual(User, type(User()))
        self.assertEqual(datetime, type(User().created_at))
        self.assertEqual(datetime, type(User().updated_at))
        self.assertEqual(str, type(User().id))
        self.assertEqual(str, type(User.email))
        self.assertEqual(str, type(User.password))
        self.assertEqual(str, type(User.first_name))
        self.assertEqual(str, type(User.last_name))

    def test_user(self):
        """ testing its attributes """
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)
        self.assertIn(User(), models.storage.all().values())
        self.assertEqual(self.user.email, '5645@holbertonstudents.com')
        self.assertEqual(self.user.password, 'helloworld')
        self.assertEqual(self.user.first_name, 'Betty')
        self.assertEqual(self.user.last_name, 'Holberton')
        self.assertIsNotNone(User.__doc__)
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)
        self.assertEqual('to_dict' in dir(self.user), True)

    def test_users(self):
        """ testing with 2 users """
        u1 = User()
        sleep(0.05)
        u2 = User()
        self.assertNotEqual(u1.id, u2.id)
        self.assertLess(u1.created_at, u2.created_at)
        self.assertLess(u1.updated_at, u2.updated_at)
        u3 = User(None)
        self.assertNotIn(None, u3.__dict__.values())

    def test_str(self):
        """ testing string representation """
        dt = datetime.today()
        dt_repr = repr(dt)
        us = User()
        us.id = "123456"
        us.created_at = us.updated_at = dt
        usstr = us.__str__()
        self.assertIn("[User] (123456)", usstr)
        self.assertIn("'id': '123456'", usstr)
        self.assertIn("'created_at': " + dt_repr, usstr)
        self.assertIn("'updated_at': " + dt_repr, usstr)

    def test_kwargs(self):
        """ testing instantation with kwargs """
        dt = datetime.today()
        dt_iso = dt.isoformat()
        us = User(id="123456", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(us.id, "123456")
        self.assertEqual(us.created_at, dt)
        self.assertEqual(us.updated_at, dt)
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
