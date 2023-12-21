#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
"""
    6-max_integer_test - module testing 6-max_integer
"""


class Test_Max_Integer(unittest.TestCase):
    """
        Test_Max_Integer - tests the function max_integer
        @unittest.TestCase: import argument for test cases
    """

    def test_correct_list(self):
        """ tests a correct list """
        list_1 = [1, 2, 3, 4]
        self.assertEqual(max_integer(list_1), 4)

    def test_empty_list(self):
        """ tests an empty list """
        list_2 = []
        self.assertEqual(max_integer(list_2), None)

    def test_no_args(self):
        """ tests no args """
        self.assertEqual(max_integer(), None)

    def test_mixed_list(self):
        """ tests list with mixed int values """
        list_3 = [7, 2, 4, 6]
        self.assertEqual(max_integer(list_3), 7)

    def test_same_index(self):
        """ tests list with same int values"""
        list_4 = [7, 10, 10, 9, 7]
        self.assertEqual(max_integer(list_4), 10)

    def test_type_error(self):
        """ tests Exception output type with wrong arg"""
        list_5 = [1, "yeet", 2, 3]
        self.assertRaises(TypeError, max_integer(list_5[1]))
        # self.assertRaises(TypeError, max_integer(list_5))
