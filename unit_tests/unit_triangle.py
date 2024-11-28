import unittest
import math
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'py_files')))
from triangle import area, perimeter

class TriangleAreaTestCases(unittest.TestCase):
    def test_triangle_int_first(self):
        self.assertEqual(area(10, 15), 10 * 15 / 2)

    def test_triangle_int_second(self):
    	self.assertEqual(perimeter(30000, 40000, 50000), 30000 + 40000 + 50000)


    def test_triangle_string_first(self):
        with self.assertRaises(TypeError):
            area("90", 100)

    def test_triangle_string_second(self):
        with self.assertRaises(TypeError):
            area("XYZ1", "ABC2")

    def test_triangle_bool_first(self):
        with self.assertRaises(TypeError):
            area(True, False)

    def test_triangle_bool_second(self):
        with self.assertRaises(TypeError):
            area(False, False)

    def test_triangle_negative_int_first(self):
        with self.assertRaises(ValueError):
            area(-10, 100)

    def test_triangle_negative_int_second(self):
        with self.assertRaises(ValueError):
            area(-98765, -158)

    def test_triangle_zero_int(self):
        with self.assertRaises(ValueError):
            area(0, 6)

class TrianglePerimeterTestCases(unittest.TestCase):
    def test_triangle_int_first(self):
        self.assertEqual(perimeter(15, 20, 25), 15 + 20 + 25)

    def test_triangle_int_second(self):
        self.assertEqual(perimeter(12345, 67890, 98765), 12345 + 67890 + 98765)

    def test_triangle_string_first(self):
        with self.assertRaises(TypeError):
            perimeter("90", "35", "15")

    def test_triangle_string_second(self):
        with self.assertRaises(TypeError):
            perimeter("XYZ1", "ABC2", "M3118")

    def test_triangle_bool_first(self):
        with self.assertRaises(TypeError):
            perimeter(True, True, True)

    def test_triangle_bool_second(self):
        with self.assertRaises(TypeError):
            perimeter(False, False, False)

    def test_triangle_negative_int_first(self):
        with self.assertRaises(ValueError):
            perimeter(-10, 158, 29)

    def test_triangle_negative_int_second(self):
        with self.assertRaises(ValueError):
            perimeter(-98765, -15, -25)

    def test_triangle_zero_int(self):
        with self.assertRaises(ValueError):
            perimeter(0, 19, 10)

if __name__ == '__main__':
    unittest.main()