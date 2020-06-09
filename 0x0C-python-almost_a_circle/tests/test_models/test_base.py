#!/usr/bin/python3
"""
Unit tests for Base class
"""
import unittest
import pep8
import sys
import io
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

class Test_Base(unittest.TestCase):
    """
    Class test on the base class
    """
    def test_pep8_conformance_base(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                        "Found code style errors (and warnings).")

    def setUp(self):
        """
        Method to set the start point
        """
        Base._Base_nb_objects = 0
        self.B1 = Base()
        self.B2 = Base(5)
        self.C1 = Base()
        self.C2 = Base(20)
        self.C3 = Base(None)
        self.E = Base(-3)

    def test_id(self):
        """
        Testing id
        """
        self.assertEqual(self.B1.id, 1)
        self.assertEqual(self.B2.id, 5)
        self.assertEqual(self.C1.id, 2)
        self.assertEqual(self.C2.id, 20)
        self.assertEqual(self.C3.id, 3)
        self.assertEqual(self.E.id, -3)

    def test_type(self):
        """
        Test type and instance
        """
        self.assertEqual(type(self.E), Base)
        self.assertTrue(isinstance(self.E, Base))

if __name__ == "__main__":
    unittest.main()
