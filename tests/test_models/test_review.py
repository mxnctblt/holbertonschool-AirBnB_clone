#!/usr/bin/python3
""" unittests for User """
import os
import models
import unittest
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel
from time import sleep


class TestReview(unittest.TestCase):
    """ testing review """

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.review = Review()
        cls.review.text = "Antoine"
        cls.review.place_id = "123"
        cls.review.user_id = "456"

    @classmethod
    def teardown(cls):
        """ at the end of the test cls will tear it down """
        del cls.review

    def tearDown(self):
        """ teardown file.json """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_types(self):
        """ testing the types """
        self.assertEqual(Review, type(Review()))
        self.assertEqual(datetime, type(Review().created_at))
        self.assertEqual(datetime, type(Review().updated_at))
        self.assertEqual(str, type(Review().id))
        self.assertEqual(str, type(Review.text))
        self.assertEqual(str, type(Review.user_id))
        self.assertEqual(str, type(Review.place_id))


    def test_state(self):
        """ testing its attributes """
        self.assertTrue('text' in self.review.__dict__)
        self.assertTrue('user_id' in self.review.__dict__)
        self.assertTrue('place_id' in self.review.__dict__)
        self.assertTrue('id' in self.review.__dict__)
        self.assertTrue('created_at' in self.review.__dict__)
        self.assertTrue('updated_at' in self.review.__dict__)
        self.assertIn(Review(), models.storage.all().values())
        self.assertEqual(self.review.text, 'Antoine')
        self.assertEqual(self.review.place_id, '123')
        self.assertEqual(self.review.user_id, '456')
        self.assertIsNotNone(Review.__doc__)
        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)
        self.assertEqual('to_dict' in dir(self.review), True)

    def test_str(self):
        """ testing string representation """
        dt = datetime.today()
        dt_repr = repr(dt)
        st = Review()
        st.id = "123456"
        st.created_at = st.updated_at = dt
        ststr = st.__str__()
        self.assertIn("[Review] (123456)", ststr)
        self.assertIn("'id': '123456'", ststr)
        self.assertIn("'created_at': " + dt_repr, ststr)
        self.assertIn("'updated_at': " + dt_repr, ststr)

    def test_kwargs(self):
        """ testing instantation with kwargs """
        dt = datetime.today()
        dt_iso = dt.isoformat()
        st = Review(id="123456", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(st.id, "123456")
        self.assertEqual(st.created_at, dt)
        self.assertEqual(st.updated_at, dt)
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
