#!/usr/bin/python3
"""Moduel containing unit tests for the Base class"""


import unittest
from models.base import Base
import pep8

class TestBase(unittest.TestCase):
    """Tests all of the atributes and methods of the Base class"""

    # setUp & tearDown

    @classmethod
    def setUpClass(cls):
        """Funcion executes before the testing begins"""
        cls.b1 = Base()
        cls.b2 = Base(12)
        cls.b3 = Base()
        cls.b4 = Base(0)
        cls.b5 = Base(-5)

    @classmethod
    def tearDownClass(cls):
        """Function executes when the testing has ended"""
        del cls.b1
        del cls.b2
        del cls.b3
        del cls.b4
        del cls.b5

    # Argument Errors

    def test_arguments(self):
        """Tests for invalid Number of arguments for methods in Base"""
        self.assertRaises(Exception, Base.__init__, 1, 5)

    # Method tests

    # Magic method tests

    def test_init(self):
        # Tests for the __init__ method of Base
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 12)
        self.assertEqual(self.b3.id, 2)
        self.assertEqual(self.b4.id, 0)
        self.assertEqual(self.b5.id, -5)
        self.assertEqual(self.b1._Base__nb_objects, 2)
        self.assertEqual(self.b4._Base__nb_objects, 2)

    # Static method tests

    def test_to_json_string(self):
        # Tests of the to_json_string method of Base
        list_input = [{'id': 789}, {'id': 6}, {'id': None}, {'id': -16}]
        self.assertEqual(Base.to_json_string(list_input),
                         '[{"id": 789}, {"id": 6}, {"id": null}, {"id": -16}]')

    def test_from_json_string(self):
        # Tests of the from_json_string method of Base
        str_input = '[{"id": 789}, {"id": 6}, {"id": null}, {"id": -16}]'
        self.assertEqual(Base.from_json_string(str_input),
                         [{'id': 789}, {'id': 6}, {'id': None}, {'id': -16}])

    # Class methods

    def test_save_to_file(self):
        # Tests for the save_to_file method of Base
        pass

    def test_load_from_file(self):
        # Tests for the laod_from_file method of Base
        pass

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
