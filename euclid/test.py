import unittest

import euclid


class ExtendedEuclidTestCase(unittest.TestCase):
    def test_something(self):
        gcd, x, y = euclid.egcd(30, 50)
        self.assertEqual(gcd, 10)  # a * x + b * y = gcd(a, b)
        self.assertEqual(x, 2)
        self.assertEqual(y, -1)

        gcd, x, y = euclid.egcd(150, 15)
        self.assertEqual(gcd, 15)
        self.assertEqual(x, 0)
        self.assertEqual(y, 1)

        gcd, x, y = euclid.egcd(652, 12)
        self.assertEqual(gcd, 4)
        self.assertEqual(x, 1)
        self.assertEqual(y, -54)

        gcd, x, y = euclid.egcd(66, 114)
        self.assertEqual(gcd, 6)
        self.assertEqual(x, 7)
        self.assertEqual(y, -4)


if __name__ == '__main__':
    unittest.main()
