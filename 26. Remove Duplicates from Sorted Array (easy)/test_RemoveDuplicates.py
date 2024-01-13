import unittest
import RemoveDuplicates


class MyTestCase(unittest.TestCase):
    def test_remove_duplicates(self):
        self.assertEqual(
            RemoveDuplicates.Solution.remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]),
            5,
        )


if __name__ == "__main__":
    unittest.main()
