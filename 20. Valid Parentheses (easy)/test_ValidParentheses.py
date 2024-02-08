import unittest

import ValidParentheses


class MyTestCase(unittest.TestCase):
    def test_true(self):
        self.assertEqual(ValidParentheses.is_valid("()"), True)
        self.assertEqual(ValidParentheses.is_valid("[[([])]]"), True)
        self.assertEqual(ValidParentheses.is_valid("()[]{}"), True)

    def test_odd(self):
        self.assertEqual(ValidParentheses.is_valid("([{}]"), False)

    def test_false(self):
        self.assertEqual(ValidParentheses.is_valid("([{})]"), False)
        self.assertEqual(ValidParentheses.is_valid("(("), False)
        self.assertEqual(ValidParentheses.is_valid(")["), False)


if __name__ == "__main__":
    unittest.main()
