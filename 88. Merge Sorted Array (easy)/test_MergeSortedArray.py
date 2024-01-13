import unittest
import MergeSortedArray


class TestSolution(unittest.TestCase):
    def test_merge(self):
        # Test case 1
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        solution = MergeSortedArray.Solution()
        solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

        # Test case 2
        nums1 = [4, 5, 6, 0, 0, 0]
        m = 3
        nums2 = [1, 2, 3]
        n = 3
        solution = MergeSortedArray.Solution()
        solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])

        # Test case 3
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        solution = MergeSortedArray.Solution()
        solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1])


if __name__ == "__main__":
    unittest.main()
