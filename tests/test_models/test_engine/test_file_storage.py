#!/usr/bin/python3
""" unittests for FileStorage """
import os
import json
import models
import unittest
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from time import sleep


class TestFileStorage(unittest.TestCase):
    """ testing FileStorage """

    def test_type(self):
        """ testing the types """
        self.assertEqual(type(FileStorage()), FileStorage)
        with self.assertRaises(TypeError):
            FileStorage(None)
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))
        self.assertEqual(type(models.storage), FileStorage)

    def test_all(self):
        """ testing all """
        s1 = FileStorage()
        self.assertEqual(dict, type(s1.all()))
        self.assertIsNotNone(s1.all())
        self.assertIs(s1.all(), s1._FileStorage__objects)
        with self.assertRaises(TypeError):
            models.storage.all(None)

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
        FileStorage._FileStorage__objects = {}

    def test_new(self):
        """ testing new """
        # for BaseModel
        bm = BaseModel()
        models.storage.new(bm)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        # for User
        user = User()
        models.storage.new(user)
        self.assertIn("User." + user.id, models.storage.all().keys())
        self.assertIn(user, models.storage.all().values())
        # for State
        state = State()
        models.storage.new(state)
        self.assertIn("State." + state.id, models.storage.all().keys())
        self.assertIn(state, models.storage.all().values())
        # for Place
        place = Place()
        models.storage.new(place)
        self.assertIn("Place." + place.id, models.storage.all().keys())
        self.assertIn(place, models.storage.all().values())
        # for City
        city = City()
        models.storage.new(city)
        self.assertIn("City." + city.id, models.storage.all().keys())
        self.assertIn(city, models.storage.all().values())
        # for Amenity
        amenity = Amenity()
        models.storage.new(amenity)
        self.assertIn("Amenity." + amenity.id, models.storage.all().keys())
        self.assertIn(amenity, models.storage.all().values())
        # for Review
        review = Review()
        models.storage.new(review)
        self.assertIn("Review." + review.id, models.storage.all().keys())
        self.assertIn(review, models.storage.all().values())
        # with args & None
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        """ testing save """
        # for BaseModel
        bm = BaseModel()
        models.storage.new(bm)
        # for User
        user = User()
        models.storage.new(user)
        # for State
        state = State()
        models.storage.new(state)
        # for Place
        place = Place()
        models.storage.new(place)
        # for City
        city = City()
        models.storage.new(city)
        # for Amenity
        amenity = Amenity()
        models.storage.new(amenity)
        # for Review
        review = Review()
        models.storage.new(review)
        # save then assert
        models.storage.save()
        test = ""
        with open("file.json", "r") as f:
            test = f.read()
            self.assertIn("BaseModel." + bm.id, test)
            self.assertIn("User." + user.id, test)
            self.assertIn("State." + state.id, test)
            self.assertIn("Place." + place.id, test)
            self.assertIn("City." + city.id, test)
            self.assertIn("Amenity." + amenity.id, test)
            self.assertIn("Review." + review.id, test)
        # test with arg
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        """ testing reload """
        # for BaseModel
        bm = BaseModel()
        models.storage.new(bm)
        # for User
        user = User()
        models.storage.new(user)
        # for State
        state = State()
        models.storage.new(state)
        # for Place
        place = Place()
        models.storage.new(place)
        # for City
        city = City()
        models.storage.new(city)
        # for Amenity
        amenity = Amenity()
        models.storage.new(amenity)
        # for Review
        review = Review()
        models.storage.new(review)
        # save & reload then assert
        models.storage.save()
        models.storage.reload()
        obj = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, obj)
        self.assertIn("User." + user.id, obj)
        self.assertIn("State." + state.id, obj)
        self.assertIn("Place." + place.id, obj)
        self.assertIn("City." + city.id, obj)
        self.assertIn("Amenity." + amenity.id, obj)
        self.assertIn("Review." + review.id, obj)
        # test with arg
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
