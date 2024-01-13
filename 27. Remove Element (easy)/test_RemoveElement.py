import unittest
import RemoveElement


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(
            RemoveElement.Solution.remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2), 5
        )  # add assertion here


if __name__ == "__main__":
    unittest.main()
