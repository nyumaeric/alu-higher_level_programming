#!/usr/bin/python3
"""Moduel containing unit tests for the Rectangle class"""

import unittest
import json
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests all of the atributes and methods of the Rectangle class"""

    # setUp & tearDown

    @classmethod
    def setUpClass(cls):
        """Funcion executes before the testing begins"""
        cls.r1 = Rectangle(10, 2)
        cls.r2 = Rectangle(2, 10)
        cls.r3 = Rectangle(15, 10, 5)
        cls.r4 = Rectangle(6, 8, 2, 4)
        cls.r5 = Rectangle(10, 2, 3, 5, 12)

    @classmethod
    def tearDownClass(cls):
        """Function executes when the testing has ended"""
        del cls.r1
        del cls.r2
        del cls.r3
        del cls.r4
        del cls.r5

    # Method tests

    # Magic method tests

    def test_values(self):
        """Tests for the init, getter, setter, dict,
        and str methods of Rectangle"""

        self.assertEqual(self.r1.__dict__, {'_Rectangle__width': 10,
                                            '_Rectangle__height': 2,
                                            'id': 3, '_Rectangle__x': 0,
                                            '_Rectangle__y': 0})
        self.assertEqual(Rectangle.to_dictionary(self.r1),
                         {'height': 2, 'width': 10, 'id': 3, 'y': 0, 'x': 0})
        self.assertEqual(self.r1.id, 3)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(Rectangle.to_dictionary(self.r2),
                         {'y': 0, 'id': 4, 'height': 10, 'width': 2, 'x': 0})
        self.assertEqual(Rectangle.__str__(self.r2),
                         "[Rectangle] (4) 0/0 - 2/10")
        self.assertEqual(self.r2.id, 4)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r2.height, 10)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(Rectangle.to_dictionary(self.r3),
                         {'y': 0, 'id': 5, 'height': 10, 'width': 15, 'x': 5})
        self.assertEqual(Rectangle.__str__(self.r3),
                         "[Rectangle] (5) 5/0 - 15/10")
        self.assertEqual(self.r3.id, 5)
        self.assertEqual(self.r3.width, 15)
        self.assertEqual(self.r3.height, 10)
        self.assertEqual(self.r3.x, 5)
        self.assertEqual(self.r3.y, 0)
        self.assertEqual(Rectangle.to_dictionary(self.r4),
                         {'y': 4, 'id': 6, 'height': 8, 'width': 6, 'x': 2})
        self.assertEqual(Rectangle.__str__(self.r4),
                         "[Rectangle] (6) 2/4 - 6/8")
        self.assertEqual(self.r4.id, 6)
        self.assertEqual(self.r4.width, 6)
        self.assertEqual(self.r4.height, 8)
        self.assertEqual(self.r4.x, 2)
        self.assertEqual(self.r4.y, 4)
        self.assertEqual(Rectangle.to_dictionary(self.r5),
                         {'y': 5, 'id': 12, 'height': 2, 'width': 10, 'x': 3})
        self.assertEqual(Rectangle.__str__(self.r5),
                         "[Rectangle] (12) 3/5 - 10/2")
        self.assertEqual(self.r5.id, 12)
        self.assertEqual(self.r5.width, 10)
        self.assertEqual(self.r5.height, 2)
        self.assertEqual(self.r5.x, 3)
        self.assertEqual(self.r5.y, 5)
        # self.assertEqual(self.r1._Base__nb_objects, 6)

    # Test for exceptions

    def test_exceptions(self):
        """Function that runs tests for execptions that should occur
        when using the Rectangle class"""

        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle("Cool", 1)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle(2.5, 1)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle(True, 1)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle(7j, 1)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle([4], 1)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle((2, 7), 1)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle({"hat": 4}, 1)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(2, 6.5)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(2, False)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(2, 6j)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(2, [4, 1])
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(2, {"Milk": 1})
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(2, (3, 9))
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(1, 2, 3.5, 4)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(1, 2, True, 4)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(1, 2, 3j, 4)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(1, 2, "3", 4)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(1, 2, [3], 4)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(1, 2, {"My": 3}, 4)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(1, 2, (3, 3), 4)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(1, 2, 3, 4.2)
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(1, 2, 3, False)
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(1, 2, 3, 4j)
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(1, 2, 3, "4")
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(1, 2, 3, [4])
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(1, 2, 3, {"its": 4})
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(1, 2, 3, (4, 4))
        with self.assertRaises(ValueError,  msg="width must be > 0"):
            Rectangle(0, 9)
        with self.assertRaises(ValueError,  msg="width must be > 0"):
            Rectangle(-4, 9)
        with self.assertRaises(ValueError,  msg="height must be > 0"):
            Rectangle(3, 0)
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(3, -2)
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            Rectangle(1, 1, -8, 9)
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            Rectangle(1, 1, 8, -9)

    # Static & class method tests

    def test_to_json_string(self):
        # Tests of the to_json_string method of Rectangle
        list_input = [{'x': 0, 'height': 2, 'width': 10, 'id': 1, 'y': 0},
                      {'x': 0, 'height': 10, 'width': 2, 'id': 2, 'y': 0},
                      {'x': 5, 'height': 10, 'width': 15, 'id': 3, 'y': 0},
                      {'x': 2, 'height': 8, 'width': 6, 'id': None, 'y': 4},
                      {'x': 3, 'height': 2, 'width': 10, 'id': 12, 'y': 5}]
        self.assertEqual(Rectangle.to_json_string(list_input),
                         json.dumps(list_input))
        self.assertEqual(Rectangle.to_json_string([]), "[]")
        self.assertEqual(Rectangle.to_json_string(None), "[]")

    def test_from_json_string(self):
        # Tests of the from_json_string method of rectangle
        str_input = '[{"x": 0, "height": 2, "width": 10, "id": 1, "y": 0}, \
        {"x": 0, "height": 10, "width": 2, "id": 2, "y": 0}, \
        {"x": 5, "height": 10, "width": 15, "id": 3, "y": 0}, \
        {"x": 2, "height": 8, "width": 6, "id": null, "y": 4}, \
        {"x": 3, "height": 2, "width": 10, "id": 12, "y": 5}]'
        dict_list = Rectangle.from_json_string(str_input)
        self.assertDictEqual(dict_list[0],
                             {'x': 0, 'height': 2, 'width': 10,
                              'id': 1, 'y': 0},)
        self.assertDictEqual(dict_list[1],
                             {'x': 0, 'height': 10, 'width': 2,
                              'id': 2, 'y': 0})
        self.assertDictEqual(dict_list[2],
                             {'x': 5, 'height': 10, 'width': 15,
                              'id': 3, 'y': 0})
        self.assertDictEqual(dict_list[3],
                             {'x': 2, 'height': 8, 'width': 6,
                              'id': None, 'y': 4})
        self.assertDictEqual(dict_list[4],
                             {'x': 3, 'height': 2, 'width': 10,
                              'id': 12, 'y': 5})
        self.assertEqual(Rectangle.from_json_string(''), [])
        self.assertEqual(Rectangle.from_json_string(None), [])

    def test_file(self):
        # Tests for the save_to_file method of Rectangle
        pass

    def test_create(self):
        # Tests for the create method of Base
        self.dict_1 = self.r1.__dict__
        self.dict_2 = self.r5.__dict__
        self.r6 = Rectangle.create(**self.dict_1)
        self.r7 = Rectangle.create(**self.dict_2)
        self.assertEqual(self.r6.__dict__, self.dict_1)
        self.assertEqual(self.r7.__dict__, self.dict_2)
        # self.assertEqual(self.r1._Base__nb_objects, 6)
