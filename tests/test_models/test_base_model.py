#!/usr/bin/python3
""" unittests for BaseModel """

import os
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from time import sleep


class TestBaseModel(unittest.TestCase):
    """ testing BaseModel """

    def test_attributes(self):
        """ testing the public instance attributes """
        # testing the type
        self.assertEqual(BaseModel, type(BaseModel()))
        self.assertEqual(str, type(BaseModel().id))
        self.assertEqual(datetime, type(BaseModel().created_at))
        self.assertEqual(datetime, type(BaseModel().updated_at))
        # testing the id
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)
        # testing created_at
        self.assertLess(bm1.created_at, bm2.created_at)
        # testing updated_at
        self.assertLess(bm1.updated_at, bm2.updated_at)
        # testing __str__
        dt = datetime.utcnow()
        bm3 = BaseModel()
        bm3.id = "abcdef"
        bm3.created_at = bm3.updated_at = dt
        self.assertIn("[BaseModel] (abcdef)", bm3.__str__())
        self.assertIn("'id': 'abcdef'", bm3.__str__())
        self.assertIn("'created_at': " + repr(dt), bm3.__str__())
        self.assertIn("'updated_at': " + repr(dt), bm3.__str__())
        # testing args is not used
        bm4 = BaseModel(None)
        self.assertNotIn(None, bm4.__dict__)
        # testing kwargs
        dtiso = dt.isoformat()
        bm5 = BaseModel(id="abcdef", created_at=dtiso, updated_at=dtiso)
        self.assertEqual(bm5.id, "abcdef")
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)
        bm6 = BaseModel("1234", id="5678", created_at=dtiso, updated_at=dtiso)
        self.assertEqual(bm6.id, "5678")

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save(self):
        """ testing the public instance method save() """
        # testing with arg
        bm1 = BaseModel()
        with self.assertRaises(TypeError):
            bm1.save(None)
        # testing with one save
        bm2 = BaseModel()
        sleep(0.05)
        up1 = bm2.updated_at
        bm2.save()
        self.assertLess(up1, bm2.updated_at)
        # testing with two save
        up2 = bm2.updated_at
        bm2.save()
        self.assertLess(up2, bm2.updated_at)
        self.assertIn(BaseModel(), models.storage.all().values())
        # testing save updated_at
        bm3 = BaseModel()
        bm3.save()
        with open("file.json", "r") as f:
            self.assertIn("BaseModel." + bm3.id, f.read())

    def test_to_dict(self):
        """ testing the public instance method to_dict() """
        # testing the type
        bm1 = BaseModel()
        self.assertTrue(dict, type(bm1.to_dict()))
        # testing the content
        self.assertIn("id", bm1.to_dict())
        self.assertIn("created_at", bm1.to_dict())
        self.assertIn("updated_at", bm1.to_dict())
        self.assertIn("__class__", bm1.to_dict())
        # testing adding attributes
        bm1.name = "Betty"
        bm1.cohort = 19
        self.assertIn("name", bm1.to_dict())
        self.assertIn("cohort", bm1.to_dict())
        # testing datetime attributes type
        d1 = bm1.to_dict()
        self.assertEqual(str, type(d1["created_at"]))
        self.assertEqual(str, type(d1["updated_at"]))
        # testing the output
        dt = datetime.utcnow()
        bm2 = BaseModel()
        bm2.id = "123"
        bm2.created_at = bm2.updated_at = dt
        d2 = {
            'id': '123',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm2.to_dict(), d2)
        # testing with arg
        bm3 = BaseModel()
        with self.assertRaises(TypeError):
            bm3.to_dict(None)
        # testing to_dict() != __dict__
        bm4 = BaseModel()
        self.assertTrue(bm4.to_dict() != bm4.__dict__)

if __name__ == "__main__":
    unittest.main()
