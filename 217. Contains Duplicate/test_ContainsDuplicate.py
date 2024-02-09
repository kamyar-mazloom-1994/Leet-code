import unittest

import ContainsDuplicate


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(
            ContainsDuplicate.contains_duplicate(self, num=[1, 2, 3, 4, 5, 6]), False
        )
        self.assertEqual(
            ContainsDuplicate.contains_duplicate(self, num=[1, 2, 3, 4, 5, 6, 6]), True
        )


if __name__ == "__main__":
    unittest.main()
