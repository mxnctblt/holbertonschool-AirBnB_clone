#!/usr/bin/python3
""" unittests for User """
import os
import models
import unittest
from datetime import datetime
from models.state import State
from models.base_model import BaseModel
from time import sleep


class TestState(unittest.TestCase):
    """ testing state """

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.state = State()
        cls.state.name = "Antoine"

    @classmethod
    def teardown(cls):
        """ at the end of the test cls will tear it down """
        del cls.state

    def tearDown(self):
        """ teardown file.json """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_types(self):
        """ testing the types """
        self.assertEqual(State, type(State()))
        self.assertEqual(datetime, type(State().created_at))
        self.assertEqual(datetime, type(State().updated_at))
        self.assertEqual(str, type(State().id))
        self.assertEqual(str, type(State.name))


    def test_state(self):
        """ testing its attributes """
        self.assertTrue('name' in self.state.__dict__)
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertIn(State(), models.storage.all().values())
        self.assertEqual(self.state.name, 'Antoine')
        self.assertIsNotNone(State.__doc__)
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)
        self.assertEqual('to_dict' in dir(self.state), True)

    def test_str(self):
        """ testing string representation """
        dt = datetime.today()
        dt_repr = repr(dt)
        st = State()
        st.id = "123456"
        st.created_at = st.updated_at = dt
        ststr = st.__str__()
        self.assertIn("[State] (123456)", ststr)
        self.assertIn("'id': '123456'", ststr)
        self.assertIn("'created_at': " + dt_repr, ststr)
        self.assertIn("'updated_at': " + dt_repr, ststr)

    def test_kwargs(self):
        """ testing instantation with kwargs """
        dt = datetime.today()
        dt_iso = dt.isoformat()
        st = State(id="123456", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(st.id, "123456")
        self.assertEqual(st.created_at, dt)
        self.assertEqual(st.updated_at, dt)
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
