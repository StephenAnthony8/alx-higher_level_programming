#!/usr/bin/python3
"""
    test_instance_common_methods:
    - Module
    - Contains class testing methods shared by Rectangle & Square
"""
from models.rectangle import Rectangle
from models.square import Square
import unittest


class common_methods(unittest.TestCase):
    """
        common_methods:
        - class object
        - Tests methods __str__, update & to_dictionary of Rectangle & Square
    """
    def test_str(self):
        r1 = Rectangle(4, 5, 5, 7)
        s1 = Square(4, 5, 7)

        s1_str = "[{}] ({}) {}/{} - {}".format(s1.__class__.__name__,
                                               s1.id,
                                               s1.x,
                                               s1.y,
                                               s1.size
                                               )
        r1_str = "[{}] ({}) {}/{} - {}/{}".format(r1.__class__.__name__,
                                                  r1.id,
                                                  r1.x,
                                                  r1.y,
                                                  r1.width,
                                                  r1.height,
                                                  )

        self.assertEqual(str(r1), r1_str)
        self.assertEqual(str(s1), s1_str)
        del r1, s1

    def test_update(self):
        """
            test_update:
            - public method
            - Tests update method for Rectangle & Square
        """

        r1 = Rectangle(1, 2)
        s1 = Square(1)

        r_original = [r1.id, r1.width, r1.height, r1.x, r1.y]
        s_original = [s1.id, s1.size, s1.x, s1.y]

        r1.update()
        s1.update()

        r_new = [r1.id, r1.width, r1.height, r1.x, r1.y]
        s_new = [s1.id, s1.size, s1.x, s1.y]

        for i in range(len(r_original)):
            self.assertEqual(r_original[i], r_new[i])
        for i in range(len(s_original)):
            self.assertEqual(s_original[i], s_new[i])

        r_new = [10, 11, 12, 7, 10]
        s_new = [15, 12, 7, 10]

        r1.update(*r_new)
        s1.update(*s_new)
        r_original = [r1.id, r1.width, r1.height, r1.x, r1.y]
        s_original = [s1.id, s1.size, s1.x, s1.y]

        for i in range(len(r_original)):
            self.assertEqual(r_new[i], r_original[i])
        for i in range(len(s_original)):
            self.assertEqual(s_original[i], s_new[i])

        dict_or = {"id": r1.id, "x": r1.x,
                   "y": r1.y, "width": r1.width, "height": r1.height}
        dict_os = {"id": s1.id, "x": s1.x, "y": r1.y, "size": s1.size}

        dict_r = {"id": 7, "x": 13, "y": 14, "width": 15, "height": 16}
        dict_s = {"id": 7, "x": 13, "y": 14, "size": 15}

        r1.update(**dict_r)
        s1.update(**dict_s)

        dict_r_attr = {"id": r1.id, "x": r1.x,
                       "y": r1.y, "width": r1.width, "height": r1.height}
        dict_s_attr = {"id": s1.id, "x": s1.x, "y": r1.y, "size": s1.size}
        for key in dict_s_attr:
            self.assertEqual(dict_s[key], dict_s_attr[key])

        for key in dict_r_attr:
            self.assertEqual(dict_r[key], dict_r_attr[key])

        for key in dict_r_attr:
            self.assertNotEqual(dict_or[key], dict_r_attr[key])

        for key in dict_s_attr:
            self.assertNotEqual(dict_os[key], dict_s_attr[key])

        r_new = [10, 11, 12, 7, 10]
        s_new = [15, 12, 7, 10]

        r1.update(*r_new, **dict_r)
        s1.update(*s_new, **dict_s)

        r_original = [r1.id, r1.width, r1.height, r1.x, r1.y]
        s_original = [s1.id, s1.size, s1.x, s1.y]

        r1.update(10, 11, 12, 7, 10, **dict_r)
        s1.update(15, 12, 7, 10, **dict_s)

        for i in range(len(r_original)):
            self.assertEqual(r_new[i], r_original[i])
        for i in range(len(s_original)):
            self.assertEqual(s_original[i], s_new[i])

        l_args = [1, "3", "4", "5", "3"]
        for i in range(0, 5):
            with self.assertRaises(TypeError):
                r1.update(*l_args)
            l_args[i] = int(l_args[i])

        l_args = [1, "3", "4", "5"]
        for i in range(0, 4):
            with self.assertRaises(TypeError):
                s1.update(*l_args)
            l_args[i] = int(l_args[i])

        v_args = [1, 0, 0, -1, -1]

        for i in range(len(v_args)):
            with self.assertRaises(ValueError):
                r1.update(*v_args)
            v_args[i] += 1
        v_args = [1, 0, -1, -1]

        for i in range(len(v_args)):
            with self.assertRaises(ValueError):
                s1.update(*v_args)

        dict_r = {"x": "13", "y": "14", "width": "15", "height": "16"}
        dict_s = {"x": "13", "y": "14", "size": "15"}
        for i in ["x", "y", "size"]:
            with self.assertRaises(TypeError):
                s1.update(**dict_s)
            dict_s.pop(i)

        for i in ["x", "y", "width", "height"]:
            with self.assertRaises(TypeError):
                r1.update(**dict_r)
            dict_r.pop(i)

        dict_r = {"x": -5, "y": -4, "width": 0, "height": -3}
        dict_s = {"x": -3, "y": -3, "size": -3}
        for i in ["x", "y", "size"]:
            with self.assertRaises(ValueError):
                s1.update(**dict_s)
            dict_s.pop(i)

        for i in ["x", "y", "width", "height"]:
            with self.assertRaises(ValueError):
                r1.update(**dict_r)
            dict_r.pop(i)

    def test_to_dictionary(self):
        """
            test_to_dictionary:
            - public method
            - Tests the implementation of method "to_dictionary"
        """
        r1 = Rectangle(3, 1, 7, 15, 21)
        s1 = Square(5, 8, 9, 31)

        l_inst = [r1, s1]
        for i in l_inst:
            with self.assertRaises(TypeError):
                i.to_dictionary({})
            self.assertTrue(i.to_dictionary(), type(dict))

            if (i == l_inst[0]):
                l_attr = [i.height, i.width, i.x, i.y, i.id]
            else:
                l_attr = [i.size, i.x, i.y, i.id]
            for j in l_attr:
                self.assertTrue(j in i.to_dictionary().values())
