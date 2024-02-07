import unittest

import RomanToInteger


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(RomanToInteger.Solution.roman_to_int("MCMXCIV"), 1994)
        self.assertEqual(RomanToInteger.Solution.roman_to_int("LVIII"), 58)


if __name__ == "__main__":
    unittest.main()
