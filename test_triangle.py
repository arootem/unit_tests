import unittest
import sys
sys.path.append('../geometric_lib')
import triangle


class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = triangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = triangle.area(10, 5)
        self.assertEqual(res, 25.0)

    def test_perimeter(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_zero_perimeter(self):
        res = triangle.perimeter(10, 0, 5)
        self.assertEqual(res, 15)


if __name__ == '__main__':
    unittest.main()
