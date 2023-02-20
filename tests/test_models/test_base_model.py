#!/usr/bin/python3
""" unittests for BaseModel """

import unittest
from models.base_model import BaseModel


Class TestBaseModel(unittest.Testcase):
	""" testing BaseModel """

	def test_id(self):
		""" testing the public instance attribute id """
		bm1 = BaseModel()
		self.assertTrue(type(bm1.id) == str)
		bm2 = BaseModel()
		self.assertTrue(bm1.id != bm2.id)
