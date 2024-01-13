import unittest
import SearchInsertPosition


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(
            SearchInsertPosition.Solution.search_insert([1, 2, 3, 4], 2), 1
        )
        self.assertEqual(
            SearchInsertPosition.Solution.search_insert([1, 2, 3, 5], 6), 4
        )
        self.assertEqual(
            SearchInsertPosition.Solution.search_insert([1, 2, 3, 7], 6), 3
        )


if __name__ == "__main__":
    unittest.main()
