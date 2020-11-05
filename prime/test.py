import unittest

import prime


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, prime.is_prime(2))
        self.assertEqual(False, prime.is_prime(10))
        self.assertEqual(True, prime.is_prime(3))
        self.assertEqual(True, prime.is_prime(97))


if __name__ == '__main__':
    unittest.main()
