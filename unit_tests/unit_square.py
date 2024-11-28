import unittest
import math
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'py_files')))
from square import area, perimeter

class SquareAreaTestCases(unittest.TestCase):
    def test_square_int_first(self):
        self.assertEqual(area(10), 10 * 10)

    def test_square_int_second(self):
        self.assertEqual(area(12345), 12345 * 12345)

    def test_square_string_first(self):
        with self.assertRaises(TypeError):
            area("90")

    def test_square_string_second(self):
        with self.assertRaises(TypeError):
            area("XYZ1")

    def test_square_bool_first(self):
        with self.assertRaises(TypeError):
            area(True)

    def test_square_bool_second(self):
        with self.assertRaises(TypeError):
            area(False)

    def test_square_negative_int_first(self):
        with self.assertRaises(ValueError):
            area(-10)

    def test_square_negative_int_second(self):
        with self.assertRaises(ValueError):
            area(-98765)

    def test_square_zero_int(self):
        with self.assertRaises(ValueError):
            area(0)

class SquarePerimeterTestCases(unittest.TestCase):
    def test_square_int_first(self):
        self.assertEqual(perimeter(15), 4 * 15)

    def test_square_int_second(self):
        self.assertEqual(perimeter(12345), 4 * 12345)

    def test_square_string_first(self):
        with self.assertRaises(TypeError):
            perimeter("90")

    def test_square_string_second(self):
        with self.assertRaises(TypeError):
            perimeter("XYZ1")

    def test_square_bool_first(self):
        with self.assertRaises(TypeError):
            perimeter(True)

    def test_square_bool_second(self):
        with self.assertRaises(TypeError):
            perimeter(False)

    def test_square_negative_int_first(self):
        with self.assertRaises(ValueError):
            perimeter(-10)

    def test_square_negative_int_second(self):
        with self.assertRaises(ValueError):
            perimeter(-98765)

    def test_square_zero_int(self):
        with self.assertRaises(ValueError):
            perimeter(0)

if __name__ == '__main__':
    unittest.main()