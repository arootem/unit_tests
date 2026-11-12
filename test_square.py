import unittest
import sys
sys.path.append('../geometric_lib')
import square


class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = square.area(10)
        self.assertEqual(res, 100)

    def test_zero_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        res = square.perimeter(10)
        self.assertEqual(res, 40)


if __name__ == '__main__':
    unittest.main()
