import unittest
import sys
sys.path.append('../geometric_lib')
import circle


class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = circle.area(5)
        self.assertEqual(res, 78.53981633974483)

    def test_zero_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        res = circle.perimeter(5)
        self.assertEqual(res, 31.41592653589793)


if __name__ == '__main__':
    unittest.main()
