#!/usr/bin/python3
"""
Unit tests for Base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Base(unittest.TestCase):
    
    def setUp(self):
        Base._Base_nb_objects = 0
        self.B1 = Base()
        self.B2 = Base(5)
        self.C1 = Base()
        self.C2 = Base(20)
        self.C3 = Base(None)
        self.E = Base()

    def test_id(self):
        self.assertEqual(self.B1.id, 1)
        self.assertEqual(self.B2.id, 5)
        self.assertEqual(self.C1.id, 2)
        self.assertEqual(self.C2.id, 20)
        self.assertEqual(self.C3.id, 3)

    def test_type(self):
        """ Test type and instance """
        self.assertEqual(type(self.E), Base)
        self.assertTrue(isinstance(self.E, Base))

if __name__ == "__main__":
    unittest.main()
