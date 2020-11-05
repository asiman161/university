import unittest

import fast_pow


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(125, fast_pow.fast_pow(5, 3))
        self.assertEqual(30517578125, fast_pow.fast_pow(5, 15))
        self.assertEqual(68122318582951682301, fast_pow.fast_pow(21, 15))


if __name__ == '__main__':
    unittest.main()
