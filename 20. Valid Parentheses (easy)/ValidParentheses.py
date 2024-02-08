"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""


def is_valid(s: str) -> bool:
    if len(s) % 2 == 1:
        return False
    else:
        hashmap = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for char in s:
            if char in hashmap:
                stack.append(char)
            elif char == hashmap[stack[-1]]:
                stack.pop()
            else:
                return False
        return True
