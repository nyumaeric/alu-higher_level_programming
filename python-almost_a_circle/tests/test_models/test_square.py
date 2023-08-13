#!/usr/bin/python3
"""Moduel containing unit tests for the Rectangle class"""

import unittest
import json
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Tests all of the atributes and methods of the Rectangle class"""

    # setUp & tearDown

    @classmethod
    def setUpClass(cls):
        """Funcion executes before the testing begins"""
        cls.s1 = Square(10)
        cls.s2 = Square(2)
        cls.s3 = Square(10, 5)
        cls.s4 = Square(6, 2, 4)
        cls.s5 = Square(2, 3, 5, 20)

    @classmethod
    def tearDownClass(cls):
        """Function executes when the testing has ended"""
        del cls.s1
        del cls.s2
        del cls.s3
        del cls.s4
        del cls.s5

    # Method tests

    # Magic method tests

    def test_values(self):
        """Tests for the init, getter, setter, dict,
        and str methods of Square"""

        self.assertDictEqual(Square.to_dictionary(self.s1),
                             {'size': 10, 'id': 9, 'y': 0, 'x': 0})
        self.assertEqual(self.s1.id, 9)
        self.assertEqual(self.s1.width, 10)
        self.assertEqual(self.s1.height, 10)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)
        self.assertDictEqual(Square.to_dictionary(self.s2),
                             {'y': 0, 'id': 10, 'size': 2, 'x': 0})
        self.assertEqual(Square.__str__(self.s2),
                         "[Square] (10) 0/0 - 2")
        self.assertEqual(self.s2.id, 10)
        self.assertEqual(self.s2.width, 2)
        self.assertEqual(self.s2.height, 2)
        self.assertEqual(self.s2.x, 0)
        self.assertEqual(self.s2.y, 0)
        self.assertDictEqual(Square.to_dictionary(self.s3),
                             {'y': 0, 'id': 11, 'size': 10, 'x': 5})
        self.assertEqual(Square.__str__(self.s3),
                         "[Square] (11) 5/0 - 10")
        self.assertEqual(self.s3.id, 11)
        self.assertEqual(self.s3.width, 10)
        self.assertEqual(self.s3.height, 10)
        self.assertEqual(self.s3.x, 5)
        self.assertEqual(self.s3.y, 0)
        self.assertDictEqual(Square.to_dictionary(self.s4),
                             {'y': 4, 'id': 12, 'size': 6, 'x': 2})
        self.assertEqual(Square.__str__(self.s4),
                         "[Square] (12) 2/4 - 6")
        self.assertEqual(self.s4.id, 12)
        self.assertEqual(self.s4.width, 6)
        self.assertEqual(self.s4.height, 6)
        self.assertEqual(self.s4.x, 2)
        self.assertEqual(self.s4.y, 4)
        self.assertDictEqual(Square.to_dictionary(self.s5),
                             {'y': 5, 'id': 20, 'size': 2, 'x': 3})
        self.assertEqual(Square.__str__(self.s5),
                         "[Square] (20) 3/5 - 2")
        self.assertEqual(self.s5.id, 20)
        self.assertEqual(self.s5.width, 2)
        self.assertEqual(self.s5.height, 2)
        self.assertEqual(self.s5.x, 3)
        self.assertEqual(self.s5.y, 5)
        # self.assertEqual(self.s1._Base__nb_objects, 6)

    # Test for exceptions

    def test_exceptions(self):
        """Function that runs tests for execptions that should occur
        when using the Square class"""

        with self.assertRaises(TypeError, msg="size must be an integer"):
            Square(6.5)
        with self.assertRaises(TypeError, msg="size must be an integer"):
            Square(False)
        with self.assertRaises(TypeError, msg="size must be an integer"):
            Square(6j)
        with self.assertRaises(TypeError, msg="size must be an integer"):
            Square([4, 1])
        with self.assertRaises(TypeError, msg="size must be an integer"):
            Square({"Milk": 1})
        with self.assertRaises(TypeError, msg="size must be an integer"):
            Square((3, 9))
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(2, 3.5, 4)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(2, True, 4)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(2, 3j, 4)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(2, "3", 4)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(2, [3], 4)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(2, {"My": 3}, 4)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(2, (3, 3), 4)
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(2, 3, 4.2)
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(2, 3, False)
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(2, 3, 4j)
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(2, 3, "4")
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(2, 3, [4])
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(2, 3, {"its": 4})
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(2, 3, (4, 4))
        with self.assertRaises(ValueError, msg="size must be > 0"):
            Square(0)
        with self.assertRaises(ValueError, msg="size must be > 0"):
            Square(-2)
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            Square(1, -8, 9)
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            Square(1, 8, -9)

    # Static & class method tests

    def test_to_json_string(self):
        # Tests of the to_json_string method of Square
        list_input = [{'x': 0, 'height': 10, 'width': 10, 'id': 1, 'y': 0},
                      {'x': 0, 'height': 2, 'width': 2, 'id': 2, 'y': 0},
                      {'x': 5, 'height': 15, 'width': 15, 'id': 3, 'y': 0},
                      {'x': 2, 'height': 6, 'width': 6, 'id': None, 'y': 4},
                      {'x': 3, 'height': 10, 'width': 10, 'id': 12, 'y': 5}]
        self.assertEqual(Square.to_json_string(list_input),
                         json.dumps(list_input))
        self.assertEqual(Square.to_json_string([]), "[]")
        self.assertEqual(Square.to_json_string(None), "[]")

    def test_from_json_string(self):
        # Tests of the from_json_string method of rectangle
        str_input = '[{"x": 0, "height": 10, "width": 10, "id": 1, "y": 0}, \
        {"x": 0, "height": 2, "width": 2, "id": 2, "y": 0}, \
        {"x": 5, "height": 15, "width": 15, "id": 3, "y": 0}, \
        {"x": 2, "height": 6, "width": 6, "id": null, "y": 4}, \
        {"x": 3, "height": 10, "width": 10, "id": 12, "y": 5}]'
        dict_list = Square.from_json_string(str_input)
        self.assertDictEqual(dict_list[0],
                             {'x': 0, 'height': 10, 'width': 10,
                              'id': 1, 'y': 0},)
        self.assertDictEqual(dict_list[1],
                             {'x': 0, 'height': 2, 'width': 2,
                              'id': 2, 'y': 0})
        self.assertDictEqual(dict_list[2],
                             {'x': 5, 'height': 15, 'width': 15,
                              'id': 3, 'y': 0})
        self.assertDictEqual(dict_list[3],
                             {'x': 2, 'height': 6, 'width': 6,
                              'id': None, 'y': 4})
        self.assertDictEqual(dict_list[4],
                             {'x': 3, 'height': 10, 'width': 10,
                              'id': 12, 'y': 5})
        self.assertEqual(Square.from_json_string(''), [])
        self.assertEqual(Square.from_json_string(None), [])

    def test_file(self):
        # Tests for the save_to_file method of Rectangle
        pass

    def test_create(self):
        # Tests for the create method of Base
        self.dict_1 = self.s1.__dict__
        self.dict_2 = self.s5.__dict__
        self.s6 = Square.create(**self.dict_1)
        self.s7 = Square.create(**self.dict_2)
        self.assertEqual(self.s6.__dict__, self.dict_1)
        self.assertEqual(self.s7.__dict__, self.dict_2)
        # self.assertEqual(self.s1._Base__nb_objects, 6)
