import unittest
from lab_4_2 import calc_function


class MyTestCase(unittest.TestCase):
    def test_something(self):
        expected = 1.59576912161
        actual = calc_function(1, 1, 0.25)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
