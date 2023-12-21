#!/usr/bin/python3
"""
    test_stati_methods:
    - Module
    - contains base object static methods tests
"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import json


class test_static(unittest.TestCase):
    """
        test_static:
        - class object
        - tests the static methods in base object
    """

    def test_to_json_string(self):
        """
            test_to_json_string:
            - public method
            - tests the implementation of method 'to_json_string'
        """
        list_d = [
                {"id": 10, "x": 9, "y": 8, "width": 7, "length": 6},
                {"id": 10, "x": 6, "y": 8, "size": 5}
                ]

        self.assertEqual(Base.to_json_string(list_d), json.dumps(list_d))
        self.assertEqual(Rectangle.to_json_string(list_d), json.dumps(list_d))
        self.assertEqual(Square.to_json_string(list_d), json.dumps(list_d))

        b1 = Base()
        s1 = Square(2)
        r1 = Rectangle(2, 2)

        o_list = [s1.to_dictionary(), r1.to_dictionary()]

        self.assertEqual(b1.to_json_string(o_list), json.dumps(o_list))
        self.assertEqual(r1.to_json_string(o_list), json.dumps(o_list))
        self.assertEqual(s1.to_json_string(o_list), json.dumps(o_list))

        for i in [[], None]:
            self.assertEqual(Base.to_json_string(i), json.dumps([]))
            self.assertEqual(type(Base.to_json_string(i)), str)

        with self.assertRaises(TypeError):
            Base.to_json_string(o_list, [r1.to_dictionary])
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_from_json_string(self):
        """
            test_from_json_string:
            - public method
            - tests static method 'from_json_string'
        """
        r1 = Rectangle(3, 3)
        s1 = Square(4)
        b1 = Base()

        l_ist = [r1.to_dictionary(), s1.to_dictionary()]

        j_str = json.dumps(l_ist)

        self.assertEqual(b1.from_json_string(j_str), json.loads(j_str))
        self.assertEqual(r1.from_json_string(j_str), json.loads(j_str))
        self.assertEqual(s1.from_json_string(j_str), json.loads(j_str))

        for i in ["", None]:
            self.assertEqual(r1.from_json_string(i), [])

        with self.assertRaises(TypeError):
            r1.from_json_string()
            s1.from_json_string()
            b1.from_json_string()

    def test_create(self):
        """
            test_create:
            - public method
            - tests the 'create' class method
        """

        r1 = Rectangle(3, 3)
        s1 = Square(4)

        r1_dict = dict(height=15, x=13, y=17)
        s1_dict = dict(size=13, x=14, y=18)

        r1_empty = dict(id=15, width=13)
        s1_empty = dict(id=16)

        for key in r1_dict:
            r1_empty[key] = r1_dict[key]
            new_inst = r1.create(**r1_empty)
            self.assertIsInstance(new_inst, Rectangle)
            del new_inst

        for key in s1_dict:
            s1_empty[key] = s1_dict[key]
            new_inst = s1.create(**s1_empty)
            self.assertIsInstance(new_inst, Square)
            del new_inst
