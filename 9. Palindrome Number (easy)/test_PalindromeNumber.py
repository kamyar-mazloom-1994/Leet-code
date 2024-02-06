import unittest

import PalindromeNumber


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(PalindromeNumber.Solution.is_palindrome(121), True)
        self.assertEqual(PalindromeNumber.Solution.is_palindrome(1201), False)


if __name__ == "__main__":
    unittest.main()
