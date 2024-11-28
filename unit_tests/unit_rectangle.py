import unittest
import math
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'py_files')))
from rectangle import area, perimeter

class RectangleAreaTestCases(unittest.TestCase):
    def test_rectangle_int_first(self):
        self.assertEqual(area(10, 20), 10 * 20)

    def test_rectangle_int_second(self):
        self.assertEqual(area(12345, 67890), 12345 * 67890)

    def test_rectangle_string_first(self):
        with self.assertRaises(TypeError):
            area("90", "100")

    def test_rectangle_string_second(self):
        with self.assertRaises(TypeError):
            area("90", 20)

    def test_rectangle_bool_first(self):
        with self.assertRaises(TypeError):
            area(True, True)

    def test_rectangle_bool_second(self):
        with self.assertRaises(TypeError):
            area(False, False)

    def test_rectangle_negative_int_first(self):
        with self.assertRaises(ValueError):
            area(-10, 8)

    def test_rectangle_negative_int_second(self):
        with self.assertRaises(ValueError):
            area(-98765, -15)

    def test_rectangle_zero_int(self):
        with self.assertRaises(ValueError):
            area(0, 6)

class RectanglePerimeterTestCases(unittest.TestCase):
    def test_rectangle_int_first(self):
        self.assertEqual(perimeter(10, 20), 2 * (10 + 20))

    def test_rectangle_int_second(self):
        self.assertEqual(perimeter(12345, 67890), 2 * (12345 + 67890))

    def test_rectangle_string_first(self):
        with self.assertRaises(TypeError):
            perimeter("35", "100")

    def test_rectangle_string_second(self):
        with self.assertRaises(TypeError):
            perimeter("35", 20)

    def test_rectangle_bool_first(self):
        with self.assertRaises(TypeError):
            perimeter(True, True)

    def test_rectangle_bool_second(self):
        with self.assertRaises(TypeError):
            perimeter(False, False)

    def test_rectangle_negative_int_first(self):
        with self.assertRaises(ValueError):
            perimeter(-10, 8)

    def test_rectangle_negative_int_second(self):
        with self.assertRaises(ValueError):
            perimeter(-98765, -15)

    def test_rectangle_zero_int(self):
        with self.assertRaises(ValueError):
            perimeter(0, 6)

if __name__ == '__main__':
    unittest.main()