import unittest

import euclid


class ExtendedEuclidTestCase(unittest.TestCase):
    def test_something(self):
        gcd, x, y = euclid.egcd(30, 50)
        self.assertEqual(gcd, 10)  # a * x + b * y = gcd(a, b)
        self.assertEqual(x, 2)
        self.assertEqual(y, -1)


if __name__ == '__main__':
    unittest.main()
