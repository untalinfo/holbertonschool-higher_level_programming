#!/usr/bin/python3
"""
Unit tests for Rectangle class
"""
import unittest
import pep8
import sys
import io
from models import base
from models.base import Base
from models.rectangle import Rectangle


class TestDocsB(unittest.TestCase):
    """ check for documentation """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(base.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(Base.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Base):
            self.assertTrue(len(func.__doc__) > 0)

class Test_Rectangle(unittest.TestCase):
    
    def test_pep8_conformance_rectangle(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                        "Found code style errors (and warnings).")

    def setUp(self):
        Base._Base_nb_objects = 0
        
    def test_subclass(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_parameters(self):
        Base._Base_nb_objects = 0
        r1 = Rectangle(10, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 10)
