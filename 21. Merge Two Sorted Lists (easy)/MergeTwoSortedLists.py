"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""
from typing import List


def merge_sorted_lists(list1: List, list2: List) -> List:
    sorted_list = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            sorted_list.append(list1[i])
            i += 1
        else:
            sorted_list.append(list2[j])
            j += 1

    while i < len(list1):
        sorted_list.append(list1[i])
        i += 1

    while j < len(list2):
        sorted_list.append(list2[j])
        j += 1

    return sorted_list


merge_sorted_lists([1, 2, 3], [1, 2, 5])
