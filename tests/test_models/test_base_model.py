#!/usr/bin/python3
"""Unittest for BaseModel()
"""
import unittest
from models.base_model import BaseModel
from uuid import uuid4
from datetime import datetime, date



class TestsBaseModel(unittest.TestCase):


    def test_instancia(self):
        """ test of instance"""
        my_object = BaseModel()
        self.assertEqual(str(type(my_object)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(my_object, BaseModel)
        self.assertTrue(issubclass(type(my_object), BaseModel))
   
    def test_attributes(self):
        """ verify attributes """
        my_object = BaseModel()
        my_object2 = BaseModel()
        my_object.name = "Holbiland"
        my_object.my_number = 29
        self.assertFalse(my_object.id == my_object2.id)
        self.assertTrue(date.today() == my_object.created_at.date())
        self.assertTrue(date.today() == my_object.updated_at.date())
    
    def test_dictionary(self):
        my_object = BaseModel()
        self.assertEqual(type(my_object.__dict__), dict)

if __name__ == '__main__':
    unittest.main()
