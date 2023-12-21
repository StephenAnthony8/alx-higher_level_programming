#!/usr/bin/python3
"""
    test_Rectangle_functions:
    - Module
    - Contains class testing functions with similar operations
"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import sys
from io import StringIO


class Test_Rectangle_Functs(unittest.TestCase):
    """
        Test_similar_Functs:
        - Class
        - Tests methods found in the Rectangle classes
    """

    def test_area(self):
        """
            test_area:
            - public method
            - Test area method for Rectangle & Square objects
        """
        r1 = Rectangle(4, 5)
        s1 = Square(4)

        self.assertEqual(s1.area(), 16)
        self.assertEqual(r1.area(), 20)

        with self.assertRaises(TypeError):
            r1.area(5, 3)

        with self.assertRaises(TypeError):
            s1.area(4)
        del r1, s1

    def test_display(self):
        """
            test_display:
            - public method
            - Test display method for both Square & Rectangle objects
        """

        r1 = Rectangle(4, 5)
        s1 = Square(4)
        r2 = Rectangle(5, 2, 2, 1)
        s2 = Square(4, 2, 1)

        r1_out = "####\n####\n####\n####\n####\n"
        s1_out = "####\n####\n####\n####\n"
        r2_out = "\n  #####\n  #####\n"
        s2_out = "\n  ####\n  ####\n  ####\n  ####\n"

        l_inst = [r1, r2, s1, s2]
        l_outp = [r1_out, r2_out, s1_out, s2_out]

        for i in range(len(l_inst)):
            capt_out = StringIO()
            sys.stdout = capt_out

            l_inst[i].display()

            sys.stdout = sys.__stdout__

            output = capt_out.getvalue()
            self.assertEqual(output, l_outp[i])
        del r1, r2, s1, s2
