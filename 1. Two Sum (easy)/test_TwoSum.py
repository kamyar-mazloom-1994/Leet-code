import unittest
import TwoSum


class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(TwoSum.Solution.two_sum([2, 7, 11, 15], 9), [1, 0])
        self.assertEqual(TwoSum.Solution.two_sum([-10, 7, 11, 15], 1), [2, 0])
        self.assertEqual(TwoSum.Solution.two_sum([2, 1, 9, 0], 9), [3, 2])
