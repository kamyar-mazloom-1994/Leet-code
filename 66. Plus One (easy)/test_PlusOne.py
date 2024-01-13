import unittest
import PlusOne


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(PlusOne.Solution.plus_one([9, 9, 9]), [1, 0, 0, 0])
        self.assertEqual(PlusOne.Solution.plus_one([1, 2, 3]), [1, 2, 4])
        self.assertEqual(PlusOne.Solution.plus_one([9, 0, 9]), [9, 1, 0])


if __name__ == "__main__":
    unittest.main()
