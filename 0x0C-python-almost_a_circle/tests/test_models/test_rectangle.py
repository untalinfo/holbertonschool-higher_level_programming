#!/usr/bin/python3
"""
Unit tests for Rectangle class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    
    def setUp(self):
        Base._Base_nb_objects = 0
        
    def test_subclass(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_parameters(self):
        r1 = Rectangle(10, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 9)
