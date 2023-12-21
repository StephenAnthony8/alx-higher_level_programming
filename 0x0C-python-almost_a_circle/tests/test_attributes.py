#!/usr/bin/python3
"""
   test_cases
   - Module
   - Class 'Test_Init_Attr'
   - Contains class testing attributes and initialization
"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest


class Test_init_attr(unittest.TestCase):
    """
        Test_objects
        - Class object
        - Test class running unit tests on Base, Rectangle & Square classes
        - Inherits from unittest.TestCase
    """
    def test_initialize(self):
        """
            test_initialize:
            - Public method
            - Runs initialization test cases on the object instances
        """
        # Rectangle
        with self.assertRaises(TypeError):
            r1 = Rectangle()

        with self.assertRaises(TypeError):
            s1 = Square()

        with self.assertRaises(TypeError):
            b1 = Base(None, 1)

        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, 1, 1, 1)

        with self.assertRaises(TypeError):
            s1 = Square(1, 1, 1, 1, 1)

    def test_initialize_args(self):
        """
            test_initialize_args:
            - Public method
            - Runs initialization with args test cases on the object instances
        """
        r1 = s1 = None
        with self.assertRaises(TypeError):
            r1 = Rectangle("wrong", 1)

        with self.assertRaises(TypeError):
            r1 = Rectangle(1, "1")

        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, "3", 3)

        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, '4')

        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, -1, 3)

        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, 0, -3)

        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 1)

        with self.assertRaises(ValueError):
            r1 = Rectangle(2, 0)

        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 1)

        with self.assertRaises(ValueError):
            r1 = Rectangle(2, -1)

        # Square
        with self.assertRaises(TypeError):
            s1 = Square("1")

        with self.assertRaises(TypeError):
            s1 = Square(2, "3", 3)

        with self.assertRaises(TypeError):
            s1 = Square(2, 3, '4')

        with self.assertRaises(ValueError):
            s1 = Square(0)

        with self.assertRaises(ValueError):
            s1 = Square(-1)

        with self.assertRaises(ValueError):
            s1 = Square(2, -3, 3)

        with self.assertRaises(ValueError):
            s1 = Square(2, 3, -3)

        r1 = Rectangle(1, 2, 3, 4, 5)
        s1 = Square(1, 2, 3, 4)
        self.assertTrue(r1, type(Rectangle))
        self.assertIsInstance(r1, Rectangle)

        self.assertTrue(s1, type(Square))
        self.assertIsInstance(s1, Square)

        del r1
        del s1

    def test_get(self):
        """
            test_set_get:
            - public method
            - Tests the instance / class attributes & getters
        """
        b1 = Base()
        r1 = Rectangle(1, 1)
        s1 = Square(1)

        self.assertEqual(b1.id, 1)
        self.assertEqual(r1.id, 2)
        self.assertEqual(s1.id, 3)

        b1.id = 10
        r1.id = 20
        s1.id = 30

        self.assertEqual(b1.id, 10)
        self.assertEqual(r1.id, 20)
        self.assertEqual(s1.id, 30)

        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        del b1, r1, s1

    def test_sets(self):
        """
            test_sets:
            - public method
            - Tests the setters of instance attributes
        """
        r1 = Rectangle(1, 1)
        s1 = Square(1)

        old_width = r1.width
        old_height = r1.height
        old_x = r1.x
        old_y = r1.y

        s_old_size = s1.size
        s_old_x = s1.x
        s_old_y = s1.y

        self.assertNotEqual(r1.id, s1.id)
        self.assertEqual(r1.id, (s1.id - 1))

        r1.width = 10
        r1.height = 15
        r1.x = 5
        r1.y = 6

        s1.size = 10
        s1.x = 5
        s1.y = 6

        self.assertNotEqual(old_width, r1.width)
        self.assertNotEqual(old_height, r1.height)
        self.assertNotEqual(old_x, r1.x)
        self.assertNotEqual(old_y, r1.y)
        self.assertNotEqual(s_old_size, s1.size)
        self.assertNotEqual(s_old_x, s1.x)
        self.assertNotEqual(s_old_y, s1.y)

        for i in [-3, 0]:
            with self.assertRaises(ValueError):
                r1.width = i

            with self.assertRaises(ValueError):
                r1.height = i

            with self.assertRaises(ValueError):
                s1.size = i
            if (i == 0):
                continue

            with self.assertRaises(ValueError):
                r1.x = i

            with self.assertRaises(ValueError):
                r1.y = i

            with self.assertRaises(ValueError):
                s1.x = i

            with self.assertRaises(ValueError):
                s1.y = i

        for i in [None, "10", 4.5, [5, 2], (7, 0), {}]:
            with self.assertRaises(TypeError):
                r1.width = i

            with self.assertRaises(TypeError):
                r1.height = i

            with self.assertRaises(TypeError):
                s1.size = i
            if (i == 0):
                continue

            with self.assertRaises(TypeError):
                r1.x = i

            with self.assertRaises(TypeError):
                r1.y = i

            with self.assertRaises(TypeError):
                s1.x = i

            with self.assertRaises(TypeError):
                s1.y = i

        del r1, s1


if __name__ == "__main__":
    unittest.main()
