"""
Write a function that reverses a string.
The input string is given as an array of characters s.

You must do this by modifying the input array
in-place with O(1) extra memory.

>>> reverseString(["h","e","l","l","o"])
['o', 'l', 'l', 'e', 'h']

>>> reverseString(["H","a","n","n","a","h"])
['h', 'a', 'n', 'n', 'a', 'H']

"""

import doctest
from typing import List


def reverseString(s: List[str]) -> None:
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    left_pointer = 0
    right_pointer = len(s) - 1
    while left_pointer < right_pointer:
        s[left_pointer], s[right_pointer] = s[right_pointer], s[left_pointer]
        left_pointer += 1
        right_pointer -= 1

    return s


doctest.testmod()
